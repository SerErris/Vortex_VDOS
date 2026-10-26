# VDOS 2.11-X — what the ROM does

Analysis of the Vortex X-module ROM **VDOS 2.11-X** (`roms/vdos211x.rom`, upper ROM 5 of a
CPC 464 with AMSDOS in ROM 7). State: 2026-10-24.

The commented source is `project/vdos211x.asm`. It is generated from `project/annotations.txt`
and reassembles byte-identically to the ROM (`source_verify`: 0 differences). This document
explains what the source shows: how the ROM is built, what each part does, what was seen in the
emulator and what is still open. The work log is in
[project-annotation-progress.md](project-annotation-progress.md).

**Status words used below:**

| Status | Meaning |
|---|---|
| **observed** | seen in CPC X-Ray: breakpoint, trace or memory |
| **read** | understood from the code but not run |
| **open** | not understood yet |

"Manual" means the VDOS 2.0 manual (`research/Vortex_X-Laufwerke_Manual_formatiert.md`).
"Research" means the earlier hand disassembly (`research/vdos211x.asm`).

---

## 1. How the document is structured

VDOS works in **two environments**, which never run at the same time:

- **BASIC (the "VDOS part"):** the CPC firmware and BASIC run. VDOS replaces AMSDOS's disc
  handling (the CAS jumpblock), adds RSX commands and a turnkey start.
- **CP/M:** `|CPM,1` starts Vortex's own 44K CP/M 2.2 from disc. The CP/M BDOS and CCP come
  from the disc, and the ROM provides the **BIOS**.

Under both runs the same layered code:

```
 BASIC environment                        CP/M environment
 -----------------                        ----------------
 BASIC / programs                         CP/M programs, CCP, BDOS (from disc)
   |  CAS jumpblock, RSX commands            |  BIOS jumpblock (&AC00), extended jumpblock (&BE80)
 [1] firmware interface (CAS, RSX)       [5] CP/M BIOS functions + BIOS entry handler
   |                                         |
 [2] DOS: files, headers, catalog            |
   |  internal BDOS (FCB functions)          |
   |  DOS indirections (&BE8F)               |
   +------------------+----------------------+
                      |
                [3] disc BIOS: SELDSK/SETTRK/READ/WRITE, sector functions (hidden RSX &81-&89)
                      |
                [4] hardware: uPD765 FDC, motor port, timing
```

So the chapters follow the layers. Chapters 2-4 are mainly the BASIC environment, chapter 5 is
the shared disc BIOS, and chapter 6 is CP/M. Chapter 7 is the RAM map, sorted by environment. A
routine that both environments use (e.g. `bios_settrk`) is described once, in its layer.

**Reference meaning: VDOS overrides AMSDOS.** Where a variable, parameter block, BIOS function
or CAS entry is defined by AMSDOS (firmware manual) and by VDOS, this document and the source
use the **VDOS definition**. AMSDOS is not used while VDOS is present. AMSDOS's meaning is named
only as background, where outside code written for AMSDOS (the Amstrad CP/M boot sector, BASIC
or CP/M programs) passes or expects it (example: byte 6 of the SETUP DISC block, 6.6).

In the annotations the environment is expressed with **groups** for RAM names: `vdos`, `basic`
and `cpm`. A **context** says which group a piece of code uses, so one RAM address can carry one
name per environment (see 7.4).

---

## 2. The ROM itself

### 2.1 Scrambling

The ROM is hardware-scrambled (`research/vortex_decrypt.md`). Opcode fetches (M1 cycles) read
the bytes as stored; every other read (operands, data, tables, text) goes through the decoder.
So every byte has a "code" value and a "data" value, and only running the code tells which one
is meant. CPC X-Ray decodes on every read and records which kind of access each byte had (the
access map `vdos211x.m1map`).

Access map as of 2026-10-26 09:58 (after the XMON I test; `project/vdos211x.m1map`):

| Byte class | Count | Share |
|---|---|---|
| M1 (opcode) | 7981 | 48.7 % |
| data | 8369 | 51.1 % |
| never read | 34 | 0.2 % |
| conflicts | 0 | – |

Of the 34 never-read bytes, 26 lie in the |XMON block &EA9E-&FD59 and 8 outside it - all on the
ignore list `project/never_read_ignore.md`
(9.6).

Consequences for the source:

- **Inline words after a CALL** are data reads. Examples: the `defw` after `call bios_entry`,
  the far addresses after `rst #18`. They decode differently from what a disassembler sees as
  opcodes, and only a run shows their value.
- **Code that never ran** is shown with the static guess (`[static]`), or as `defb` where the
  generator cannot guess it.

### 2.2 ROM layout

| Range | Content | Layer | Status |
|---|---|---|---|
| &C000-&C003 | header: background ROM, mark 1, version &21, modification 3 | – | observed (see note) |
| &C004 | pointer to `rom_name_table` (&E9E2) | 1 | observed |
| &C006-&C092 | `rom_jumpblock`: ROM init + 46 RSX JPs (37 visible commands, then hidden &81-&89) | 1 | partly observed |
| &C093-&C0D1 | extended BIOS jumpblock (21 JPs), copied to &BE80 by `\|CPM,1` | 6 | observed |
| &C0D2-&C104 | CP/M 2.2 BIOS jumpblock (17 JPs), copied to &0500 / &AC00 | 6 | observed |
| &C105-&C12C | DOS indirections + `basic_error_patch`, copied to &BE8F | 2/1 | observed |
| &C12D-&C153 | `cas_jump_table` (13 JPs) | 1 | observed |
| &C154-&C1A5 | XPBs `xpb_3inch`, `xpb_vortex`, `dph_templates` | 5 | observed |
| &C1A6-&C1AF | `time_constants_default` | 5 | observed |
| &C1B0-&C1C1 | `bios_set_cmnd_buffer` | 6 | read |
| &C1C2-&C1E8 | `cas_dispatcher` | 1 | observed |
| &C1E9-&C31C | `rom_init`, KM DISARM BREAK hook, `post_boot_setup`, HELLO loader (copied to &BF00) | 1 | observed |
| &C31D-&C3F5 | `\|CPM` entry, CP/M BIOS functions, BIOS entry handler, CP/M interrupt | 6 | partly observed |
| &C3F6-&C574 | `\|CPM,1` boot (copies the jumpblocks, sets up CP/M) | 6 | partly observed, open |
| &C575-&C615 | `disc_init`, drive tables, retry count | 5 | observed |
| &C616-&C7C5 | CP/M character I/O, SIO driver | 6 | partly read |
| &C7D5-&CC83 | disc BIOS (SELDSK, READ, WRITE, sector functions, FDC) | 5 | partly observed, mostly open |
| &CC84-&CE5A | `bios_set_message`, messages printing, utilities, motor | 5/2 | observed |
| &D32A-&DA6B | CAS functions and the catalog | 2 | observed |
| &DCAE-&DF45 | header set-up, entry checks, internal BDOS call layer, error exits | 2 | observed |
| &DF46-&E731 | file name parser, internal BDOS functions (open, close, search, ...) | 2 | names only, bodies open |
| &E732-&E7BE | small helpers, file extension table | 2 | observed |
| &E7BF-&E9E1 | `message_table` (62 messages, German) | 2 | observed |
| &E9E2- | `rom_name_table` (RSX names, bit 7 = last character) | 1 | observed |
| rest | other RSX commands (relative files, FORMAT, ...) | 1 | observed (3.5) |
| &EA9E-&FD59 | `\|XMON`, the Z80 monitor with its disc monitor | 1 | start, Z, X, D, Y, L group 1 observed (3.5.18); other commands open |

Note on the version: the header bytes `01 21 03` mean mark 1, version 2.1 (BCD) and
modification 3. CPC X-Ray shows them in decimal as "1.333".

---

## 3. Layer 1 — firmware interface (BASIC environment)

### 3.1 Start-up

`rom_init` (&C1E9) is called by the firmware's ROM walk (KL INIT BACK, ROM 7 down to 0).
**Observed:**

1. **With AMSDOS in ROM 7:** VDOS takes AMSDOS's data area (&A700) as its own workspace
   (`vdos_workspace` &BE75) and reserves no RAM. It clears the first 256 bytes and calls
   `disc_init`.
2. **CAS redirection:** AMSDOS has made all 13 CAS jumpblock entries (&BC77-&BC9B) `RST 3 /
   defw &A88B`, a FAR CALL through **one** far address in its data area. VDOS changes only
   that far address (&A88B = `cas_dispatcher` &C1C2, ROM 5). After this every CAS call goes to
   VDOS.
3. It hooks KM DISARM BREAK and prints the banner (message &0E: " (C)1986   VDOS 2.11-X by
   vortex GmbH").

Two other cases:

- **Without AMSDOS** (**observed** with `output/machine_noamsdos.toml`, a machine without ROM 7):
  VDOS reserves &500 bytes below the highest free address (&ABFF → workspace &A700; ROM number
  &85, bit 7 = own workspace), keeps the 13 original tape CAS entries at workspace+&164
  (&A864), puts the far address `cas_dispatcher` / ROM 5 at workspace+&18B (&A88B) and writes
  the CAS entries itself as `RST 3 / defw &A88B` (`DF 8B A8`). HIMEM is &A67B, as with AMSDOS;
  banner and CAT work.
- **VDOS as ROM 0** (read, not run): VDOS starts CP/M instead of BASIC (`rom_init_foreground`
  → `cpm_cold_boot` &C3F6).

**Deferred set-up.** BASIC initialises its own indirections after the ROM walk, so VDOS cannot
patch them in `rom_init`. Instead (**observed**):

1. `hook_km_disarm_break` turns the firmware entry &BB48 into `RST 3 / defw &BE26` (far address
   to `km_disarm_break_hook` &C26E). It saves the original address (&9C82 on the 464) in
   `km_disarm_break_saved` (&BE24).
2. BASIC 1.0 calls KM DISARM BREAK **twice** during its start-up. On the first call VDOS
   unhooks, calls the real routine and hooks again. On the second call `post_boot_setup`
   (&C2B4) runs instead:
   - it copies the DOS indirections and `basic_error_patch` (&C105, 40 bytes) to &BE8F;
   - it sets BASIC 1.0's error indirection &AC04 (`basic_error_indirection`) to
     `JP basic_error_patch`;
   - unless a key is waiting, it copies the HELLO loader (&C2DE, 63 bytes) to &BF00 and runs it.

The manual (2.0) describes a different mechanism: a ticker that watches BASIC's READY
indirection. 2.11-X uses the KM DISARM BREAK hook instead.

### 3.2 HELLO loader (turnkey, 464 only) — &BF00 (RAM)

`hello_loader` does the following:

1. Finds the hidden RSX &88 (BIOS GET STATUS) with KL FIND COMMAND (name byte
   `bios_get_status_name`).
2. Switches the disc messages off and checks drive A.
3. Tries `CAS IN OPEN "HELLO"` and closes the file again.
4. Switches the messages back on.

If HELLO exists, it far-calls BASIC's routine &E9CF in ROM 0 with HL = `"HELLO"<0>`. Research
says this is RUN.

- **Observed:** the path where no HELLO exists.
- **Read:** the RUN path.

### 3.3 String parameters for RSX commands on BASIC 1.0 — `basic_error_patch` (&BEA1, RAM)

BASIC 1.0 only allows `@a$` as a string parameter of an RSX command. For `|DIR,"*.COM"` it
evaluates the string anyway and then raises error 13 (Type mismatch).

The patch sits in BASIC's error indirection. For error 13 in a statement that starts with `|`
or with the CALL token, it takes the string's descriptor address from BASIC's virtual
accumulator (`basic_vacc` &B0C2) as the parameter value, which is what `@a$` would pass. It then
drops the error path and lets BASIC go on.

**Observed** with `|DIR,"*.COM"`: the directory was listed correctly.

### 3.4 CAS dispatcher — &C1C2

Every CAS jumpblock entry &BC77-&BC9B is `RST 3 / defw &A88B`, a FAR CALL through the one far
address at &A88B, which points here (ROM 5). The firmware's FAR CALL leaves three words on the
stack, and below them the address after the called jumpblock entry (e.g. &BC80 for CAS IN
ABANDON at &BC7D). `cas_dispatcher` works like this (**observed**):

1. Interrupts off, IY = `vdos_workspace` (&A700), the caller's AF, BC, DE, HL into the
   alternate set. Interrupts stay off meanwhile, because the firmware keeps BC' (the gate array
   and ROM state) in the alternate set, which the dispatcher uses.
2. **One-shot hook** `cas_oneshot_ptr` (&BE77): if it is not 0, the dispatcher pushes it, clears it,
   restores the caller's registers and RETs there (see below).
3. Otherwise it takes the address after the jumpblock entry out of the frame (the frame moves up
   one word), so the routine returns straight to the CAS caller and not into the next entry.
4. It adds &04B3 to that address and RETs into `cas_jump_table` (&C12D + 3n), with the caller's
   registers back in place.

The jump table and the BASIC commands that were seen using each entry:

| Entry | Routine | Seen with |
|---|---|---|
| CAS IN OPEN | `vdos_cas_in_open` &D32A | LOAD, OPENIN |
| CAS IN CLOSE | `vdos_cas_in_close` &D4EE | LOAD (VDOS: DE, HL, IX changed - programs written for the firmware manual expect only A) |
| CAS IN ABANDON | `vdos_cas_in_abandon` &D4F4 | CAT |
| CAS IN CHAR | `vdos_cas_in_char` &D431 | INPUT#, LINE INPUT# (VDOS: IX changed - programs written for the firmware manual expect only A) |
| CAS IN DIRECT | `vdos_cas_in_direct` &D3CD | LOAD |
| CAS RETURN | `vdos_cas_return` &D4C6 | BASIC does not call &BC86, but every EOF runs the routine: CAS TEST EOF falls through into it after a character was read; &BC86 itself observed from machine code (VDOS: IX changed - programs written for the firmware manual expect all registers kept) |
| CAS TEST EOF | `vdos_cas_test_eof` &D4C2 | EOF |
| CAS OUT OPEN | `vdos_cas_out_open` &D4FB | SAVE, OPENOUT |
| CAS OUT CLOSE | `vdos_cas_out_close` &D53B | SAVE, CLOSEOUT |
| CAS OUT ABANDON | `vdos_cas_out_abandon` &D531 | CAT (VDOS: IX changed - programs written for the firmware manual expect IX kept) |
| CAS OUT CHAR | `vdos_cas_out_char` &D6E3 | PRINT# |
| CAS OUT DIRECT | `vdos_cas_out_direct` &D624 | SAVE |
| CAS CATALOG | `vdos_cas_catalog` &D8F6 | CAT |

The labels carry the prefix `vdos_`, because CPC X-Ray compares labels with the firmware names
case-insensitively (`cas_in_open` = `CAS_IN_OPEN`).

**The one-shot pointer &BE77 (`cas_oneshot_ptr`).** A one-shot CAS hook for outside or inside code. The mechanism is observed; its purpose is unknown (nothing in the known ROMs or on the discs sets it). During the RSX and CP/M tests a write breakpoint stays on it; writes from the ROM initialisation (AMSDOS clears &BE76/&BE77 = its sector buffer pointer, then VDOS `disc_init`) are expected. The manual calls it "Adresse einer DOS-Routine im
ROM" (default 0). What it does (**observed**):

- If &BE77 is not 0, the next CAS call goes there **once** instead of to the CAS routine;
  the dispatcher clears &BE77 before it RETs there.
- The target gets the caller's AF, BC, DE, HL (the CAS function's parameters), IY = the VDOS
  workspace, and the FAR CALL frame **unchanged** (not moved up). So it must deal with the frame
  itself: a plain RET would return into the next jumpblock entry. The simplest correct hook
  does its work and jumps back to `cas_dispatcher` (&C1C2): &BE77 is 0 by then, so the call is
  dispatched normally.
- Test: a hook at &9100 (`push af / ld a,&AA / ld (&90F8),a / pop af / jp &C1C2`), &BE77 =
  &9100, then CAT. The hook ran once - at CAS IN ABANDON, the first CAS call of CAT (frame word
  &BC80) - &BE77 was 0 again, and CAT listed the directory normally.
- **Nobody sets it:** no write to &BE77 in the OS, BASIC and AMSDOS ROMs (byte search for every
  load/store form with the address &BE77) or in VDOS (decoded source: only the read and the
  clear in `cas_dispatcher`), and
  none in the programs on the two disc images (the `77 BE` byte pairs there are `ld (hl),a /
  cp (hl)` of a RAM test, not the address). It is an interface for outside code, e.g. a
  program that wants to catch one CAS call.
- **The owner's reading (2026-10-25):** a way to define your own entry into the ROM (or RAM) and
  reach it with an ordinary CAS call. The write breakpoint stays on during the |XMON tests,
  in case XMON uses it.

### 3.5 RSX commands

`rom_name_table` holds the names, and `rom_jumpblock` the JPs, in this order:

- **Visible:** GET, PUT, FILES, OPEN, CLOSE, FIELD, CPM, DISC, DISC.IN, DISC.OUT, CAS, CAS.IN,
  CAS.OUT, A, B, SELECT, DIR, ERA, REN, RESET, FORMAT, CODE, ATTRIBUT, XMON, FAST, SLOW,
  DERROR, X, FRAME, AMSDOS, ROMOFF, ROMCAT, TAPE, TAPE.IN, TAPE.OUT, DRIVE, USER.
- **Hidden:** &81-&89, the disc BIOS functions (see 5.3).

Each command is worked through in the same way:
1. read the manual (VDOS 2.0 - not taken as exact for 2.11-X);
2. design tests for every case, errors included;
3. run them, annotate the source;
4. check the command's code for segments that are still unobserved: work out what condition
   would run each one, write a test for it and run it; what cannot be triggered from the
   command is named with its reason;
5. name every subroutine and label;
6. describe it here.

`|XMON` was left out at first; since 2026-10-25 it is analysed too (3.5.18). While the tests run, a write
breakpoint on &BE77 (`cas_oneshot_ptr`) stays set, to catch any code that sets the hook. cpcxray loses
breakpoints when the GUI restarts, so the breakpoint is set again after every restart.

Done: **all RSX commands except the `|XMON` commands** (3.5.1-3.5.17; XMON start 3.5.18). Everything in their code has run,
except the few places that are named in the sections with the reason why they cannot run.

#### 3.5.1 `|DIR[,"name"]` — `rsx_dir` &D795 (**observed**)

**Manual (2.0):** lists the directory, optionally filtered with the wildcards `*` and `?`. A
string may be given directly (`|DIR,"*.COM"`) or as `@a$`. SYS files are not shown.

**How it works:**

- `rsx_dir` shares its start and end with CAS CATALOG: `dir_start` (header line, name, first
  entry), `dir_next_line` (page pause) and `dir_print_free` (space line).
- **Unlike CAT,** |DIR lists the entries in **directory order**: not sorted, without sizes, 12
  characters + 3 spaces per column. The number of columns comes from the window width (MODE 2: 5,
  MODE 0: 1).
- **Each file once:** `dir_start` writes the caller's C into the **extent byte of the search
  name** (FCB byte 12). |DIR passes 0, so only the extent-0 entries match and every file is
  listed once. CAT passes &3F (`?`) and gets all entries, because its size calculation needs
  them.
- **Parameter:** `rsx_string_param` takes it as a string descriptor **without a type check**.
  More than one parameter jumps to `derr_count_check` in `rsx_derror` (shared "Eingabefehler").

**Tests** (drive A: 26 files, 3" system disc):

| Test | Result |
|---|---|
| `\|DIR` (MODE 2) | all 26 files in directory order, 5 columns, `119K in  26 Files,  50K frei` |
| `\|DIR,"*.COM"` (direct string) / `a$="*.BAS":\|DIR,@a$` | 22 COM files / EX1, EX2; the direct string works through `basic_error_patch` |
| `\|DIR,"D*.CO?"` | DDT, DUMP, DISCCOPY, DISCCHK (`*` and `?`) |
| `\|DIR,"NIX.*"` | only the space line, `0 Files` |
| `\|DIR,"B:*.BAS"` | `Laufwerk B: User 0`, F1Z.BAS (drive in the name) |
| ROINTIME.DEM (26K = two entries, extent 1 before extent 0 in the directory) | listed once |
| `\|ATTRIBUT` EX1.BAS "S", then `\|DIR,"*.BAS"`; then "D" again | EX1 hidden, then shown again |
| MODE 0 (1 column), `\|DIR`, ESC in the page pause | pause after 22 lines; ESC → `119K in  22 Files, 50K frei` at once |
| `\|DIR,"*.*","X"` | `Eingabefehler` (two parameters) |
| `\|DIR,"1:X"` | `Eingabefehler` (bad name) |
| `\|DIR,5` | `Eingabefehler`, but only by chance: 5 is taken as the descriptor address (&0005: length &C3, text at &0580 = &00 → bad character) |

**Differences from the manual:** the space line is `<used>K in <n> Files, <free>K frei` (2.0:
"228K belegt, 4 Dateien, 480K frei"). As in 2.0, used and free refer to the whole disc, and n
counts the files listed. A missing disc gives the usual "Diskette fehlt" dialog through
`search_first`, the same path as CAT (observed there).

**Unobserved segments (step 4):** none. Every instruction of `rsx_dir`, `dir_start`,
`dir_entry_address`, `dir_columns`, `dir_next_line`, `dir_print_free` and of the helpers
(`rsx_string_param`, `rsx_param`, `parse_filename_fcb`, `search_first` / `search_next`) has run
(no `[static]` line left). Both directions of the conditional exits were also seen: the
`ret nz` of `dir_columns` (normal / narrow window) and `dir_next_line` (go on / ESC). Not tested
yet, but on the same code: the header with a user other than 0 ("User 5"), which follows with
`|SELECT`.

**Named in this step:** `derr_count_check` (&D8A8, was `l_d8a8`). The comments of `dir_start`
(extent byte) and `vdos_cas_catalog` (C = &3F) are corrected.

#### 3.5.2 `|ERA,"name"` — `rsx_era` &DAB3 (**observed**)

**Manual (2.0):** deletes a file, a group (`*`, `?`) or with `*.*` the whole disc, in the current
user area. An R/O file cannot be deleted. Not found: "TEST    .BAS wurde nicht gefunden". A drive
letter in the name works (`|ERA,"A:PIP.COM"` from drive B). 2.11-X behaves exactly like this.

**How it works:**

1. `rsx_one_param`: exactly one parameter, else "Eingabefehler". It falls through into
   `rsx_string_param` (B, HL = the string).
2. `parse_filename_check`: wildcards are allowed; an empty name gives "Eingabefehler".
3. `delete_file`: the BDOS delete (`delete_body`) goes through the matching entries in directory
   order. For each one, `check_rodir` checks for R/O; if R/O, the error exit is taken and the
   remaining entries are not touched.
4. Nothing matched: `error_not_found`.

**Tests** (drive B, in memory):

| Test | Result |
|---|---|
| `\|ERA,"X.BAS"` | `X       .BAS wurde nicht gefunden` |
| `\|ERA,"T1.BAS"` | deleted |
| T0 (W), T2 (R/O), T3 (W) in this directory order, `\|ERA,"T?.BAS"` | T0 deleted, `T2      .BAS hat Schreibschutz`, T2 and T3 stay |
| after `\|ATTRIBUT` T2 "W": `\|ERA,"T?.BAS"` | T2, T3 deleted |
| `\|ERA,"A:EX2.BAS"` with B as current drive | deleted on A |
| `\|ERA,"*.*"` | disc B empty: `0K in 0 Files, 704K frei` |
| `\|ERA`, `\|ERA,"U1.BAS","X"`, `\|ERA,""`, `\|ERA,".BAS"`, `\|ERA,"1:X"` | `Eingabefehler` each |

After an error message an RSX command gives no `Break` (a CAS error from BASIC does).

**Unobserved segments (step 4):** none. Every instruction of `rsx_era`, `rsx_two_params` /
`rsx_one_param`, `parse_filename_check`, `delete_file`, `delete_body`, `check_rodir`,
`search_ext` and `return_dirloc` has run; both exits of `jp z,error_not_found` were seen.

**Named / corrected:** the header of `rsx_two_params`. The parameter string is the **last**
parameter (IX+0, BASIC passes them last first), and the routine falls through into
`rsx_string_param`. The old comment "not observed" was removed.

#### 3.5.3 `|REN,"new","old"` — `rsx_ren` &DA6B (**observed**)

**Manual (2.0):** renames old to new; no wildcards. If the new name exists: "DATEI   .NEU
existiert bereits"; if the old one is missing: "DATEI   .ALT wurde nicht gefunden". A drive letter
is allowed, but both names must be on the same disc.

**How it works:** the checks run in this order:

1. The **new** name (the first parameter; `rsx_two_params` delivers the last one first):
   - wildcards → "Eingabefehler";
   - exists → "existiert bereits".
2. The new name's FCB is kept in the record buffer (`record_buffer_de`, workspace+&E0).
3. The **old** name:
   - wildcards → "Eingabefehler";
   - a drive other than the new name's → "Eingabefehler".
4. The new name goes into the name FCB at +16, then the BDOS rename (`rename_body`):
   - R/O → "hat Schreibschutz";
   - nothing found → "wurde nicht gefunden".

**Tests** (drive B):

| Test | Result |
|---|---|
| `\|REN,"NEU.BAS","T.BAS"` | renamed |
| `\|REN,"NEU.BAS","X.BAS"` (NEU exists) / `\|REN,"W.BAS","W.BAS"` | `NEU     .BAS existiert bereits` / `W       .BAS existiert bereits` |
| `\|REN,"Y.BAS","Q.BAS"` | `Q       .BAS wurde nicht gefunden` |
| `"N*.BAS","X.BAS"`, `"Z.BAS","X.B?S"`, `"A:Z.BAS","B:X.BAS"`, one or three parameters, `"","Z.BAS"` | `Eingabefehler` each |
| `\|REN,"B:Z.BAS","X.BAS"` with B as current drive | renamed (same drive) |
| Z.BAS R/O: `\|REN,"W.BAS","Z.BAS"` | `Z       .BAS hat Schreibschutz` |
| Z.BAS SYS (hidden): `\|REN,"W.BAS","Z.BAS"`, then `\|DIR` | **W.BAS is visible**: the SYS attribute is lost |

**Finding:** |REN loses the attributes (SYS, and the archive bit, if any). The new name comes from
the parsed string with the bits cleared, and `copy_dir` writes all 11 name bytes into the entry. The
manual does not mention this.

**Unobserved segments (step 4):** none. Every instruction of `rsx_ren`, `rsx_bad_param`,
`record_buffer_de`, `rename_file` and `rename_body` has run.

**Named:**
- `rsx_bad_param` (&DACE, was `l_dace`): the shared "Eingabefehler" exit of |REN, |CODE and |ATTRIBUT.
- `record_buffer_de` / `record_buffer_hl` (&CD87 / &CD91, were `sub_cd87` / `sub_cd91`): DE / HL = workspace+&E0.

#### 3.5.4 `|ATTRIBUT,"name","x"` — `rsx_attribut` &DAD1 (**observed**)

**Manual (2.0):** sets the attributes S (SYS, hidden in CAT and |DIR), D (DIR, shown), R (R/O) and
W (R/W). R/O files are marked with `#` in CAT and cannot be deleted. The manual says |ERA of an
R/O file prints "PIP    .COM nur lesbar"; **2.11-X prints "<name> hat Schreibschutz"**.

**How it works:**

1. The attribute (the last parameter) must be exactly one character, upper or lower case. It is
   looked up in `attribute_letters` "SDRW", which gives the code 3/2/1/0. Code bit 1 selects the
   byte: SYS (extension byte 2) for S/D, R/O (extension byte 1) for R/W. Code bit 0 is the value.
2. `open_file` opens the file; its FCB gets the one bit, and the other attribute is kept.
3. `set_attributes` (BDOS function 30, `setattr`) writes FCB bytes 0-11 into **every** entry of
   the file (all extents).

**Tests** (drive A, in memory):

| Test | Result |
|---|---|
| `"EX1.BAS","r"` (lower case) | CAT `EX1     .BAS   2K#`; `\|ERA` → `hat Schreibschutz` |
| then `"s"` | hidden in `\|DIR`, still R/O (`\|ERA` refused) |
| `"D"` / `"W"` | shown again / deletable again |
| `"ROINTIME.DEM","S"` (2 entries) | hidden in CAT: both entries got the bit |
| `"D*.COM","S"` | **only DDT.COM** (the first match) hidden |
| `"B:W.BAS","S"` from drive A | works on B |
| attribute `"X"`, `"RW"`, `""`; one or three parameters | `Eingabefehler` |
| `"NIX.BAS","R"` | `NIX     .BAS wurde nicht gefunden` |
| name `""` | `        .    wurde nicht gefunden` (no empty-name check, unlike `\|ERA` / `\|REN`) |

**Findings:**
- A wildcard changes only the first matching file. `open_file` writes the found name into the
  FCB, so `set_attributes` then matches only that one file.
- An empty name is not refused as "Eingabefehler". It is searched for as a blank name, and the
  error is "not found".

**Unobserved segments (step 4):** none. Every instruction of `rsx_attribut` (including the
unknown-letter exit #DAE6) and of `set_attributes` has run.

**Named / corrected:**
- `set_attributes` / `set_attributes_body` / `sa_loop` (&E1C2): was `delete_matching`, a wrong
  name taken from the research ("|ERA"). The routine deletes nothing.
- In `rsx_attribut`: `attr_search`, `attr_found`, `attr_set_bit`, `attribute_letters`.

#### 3.5.5 `|A` / `|B` — `rsx_a` &D780, `rsx_b` &D783 (**observed**)

**Manual (2.0):** switches the default drive to A or B. 2.11-X does the same.

**How it works:** `set_default_drive` writes the drive number (0/1) into the default drive
(`iy+&06`) and **clears the drive's login byte** (workspace+drive). The next access to that drive
therefore logs it in again, as after a disc change: it reads the directory and rebuilds the
allocation vector. `clear_xpb_cache` sets `xpb_cache_drive` = &FF. Parameters are ignored.

**Tests:**

| Test | Result |
|---|---|
| login bytes before (&A700 / &A701) | FF FF |
| `\|A`, then `\|DIR` | &A700 = 0; `\|DIR` runs the login (breakpoint `bdos_select_fcb_drive` #DE61); the first `\|DIR` before it did not |
| `\|B:\|DIR` | &A706 (default drive) = 1, drive B listed |
| `\|A,5,"X"`, `\|B,"Q"` | the same as `\|A` / `\|B`, no error |

So `|A` / `|B` are also the way to make VDOS re-read a disc that was changed while it was not
watching: the disc change check (directory checksum) catches most changes anyway.

**Unobserved segments (step 4):** none (&D778-&D794).

**Named:** `set_default_drive` (&D785, was `l_d785`; `|SELECT` also jumps there),
`clear_xpb_cache` (&D778, was `l_d778`), and the `rsx_a` / `rsx_b` header.

#### 3.5.6 `|SELECT,"[user][drive]"`, `|DRIVE` and `|USER,n` — `rsx_select` &DB28, `rsx_user` &DB16 (**observed**)

**Manual (2.0):** `|SELECT,"6"` sets user area 6. `|SELECT,"B5"` is said to give user 5 on drive
B. `|DRIVE` and `|USER` are **not in the manual**. In the ROM, |DRIVE jumps to the same routine as
|SELECT.

**How `rsx_select` works:** the string is parsed with spaces skipped and letters upper case.

- **A digit first:** the user. One digit, or two digits as "1x" (10-15) or "0x". Then an
  optional drive letter A/B (`set_default_drive`, which also logs the drive in again).
- **A letter first:** only the drive. The rest of the string is ignored.
- Anything after the drive letter is ignored too.
- The user is stored **before** the drive letter is checked.

**`rsx_user`:** one number 0-15 → user (`rsx_number_param`). The drive is not changed.

**Tests:**

| Test | Result |
|---|---|
| `\|SELECT,"6":CAT` | `Laufwerk A: User  6` |
| `\|SELECT,"B5"` (manual) | **drive B, user stays 6** - the manual's order does not work in 2.11-X |
| `\|SELECT,"5B"` / `"15"` / `"07a"` | B, User 5 / User 15 / A, User 7 |
| `" 3 "`, `"12 B"`, `"4BX"` | User 3 / B, User 12 / B, User 4 (spaces skipped, the rest ignored) |
| `"16"`, `"20"`, `"C"`, `""`, `"   "`, `"1/"`, no or two parameters | `Eingabefehler`, nothing changed |
| `"3C"` | `Eingabefehler`, **but user 3 is set** |
| `\|DRIVE,"A"` | drive A (same routine) |
| `\|USER,9:CAT` / `\|USER,15` / `\|USER,0` | `User  9` / 15 / 0 |
| `\|USER,16`, `256`, `-1`, `&10`, no or two parameters, `"3"` (string) | `Eingabefehler` |
| user 9: `SAVE "U9"`; user 0: `\|DIR,"U9*.*"`, `\|ERA,"U9.BAS"` | 0 Files / `wurde nicht gefunden` - the areas are separate |

**Findings:**
- The manual's `"B5"` only selects the drive. The user number must come first (`"5B"`).
- An error after the user number (`"3C"`) leaves the new user set.

**Unobserved segments (step 4):** none (&DAC7-&DACD, &DB16-&DB6F). These tests also covered the
header with a user other than 0, which was left open for |DIR.

**Named:**
- `rsx_number_param` (&DAC7, was `sub_dac7`): exactly one number → HL.
- `set_user` (&DB5F, was `sub_db5f`).
- `sel_two_digits`, `sel_user_drive`, `sel_drive`, `sel_error` (were `l_db54`, `l_db63`, `l_db66`, `l_db6d`).

#### 3.5.7 `|RESET` and `|X` — `rsx_reset` &DB70, `rsx_x` &DB82 (**observed**)

**Manual (2.0):**
- |RESET tells VDOS that the disc was changed while a file was open for writing ("like CTRL+C
  under CP/M"); without it, up to 64K could be lost.
- |X swaps drives A and B.

**How it works:**
- **`rsx_reset`:**
  - CAS OUT CLOSE: the output file is written and closed properly, the .$$$ is renamed;
  - CAS IN CLOSE;
  - the login bytes of both drives are cleared.
  - A close with nothing open takes the CAS error exit (&0E, no message). That is safe:
    `out_check_open` / `in_check_open` call `cas_entry_setup` themselves, so `cas_error_exit` RETs
    back into `rsx_reset` (observed: to #DB76).
- **`rsx_x`:** |RESET, then `drives_swapped` 0 ↔ 1, then the XPBs are copied into the DPB slots
  again (`sdt_copy_xpbs`).

**Tests:**

| Test | Result |
|---|---|
| `\|RESET` with nothing open | nothing printed, `cas_last_error` &0E, login bytes &A700/&A701 = 0 |
| `OPENOUT "R1":PRINT #9,"hallo":\|RESET` | R1 written; `OPENIN` reads "hallo" back; a later `PRINT #9` → `Break` (BASIC still thinks the file is open) |
| `OPENIN "R1":\|RESET:LINE INPUT #9,a$` | `EOF met` |
| `\|A:\|X:CAT` / `\|B:CAT` / `\|X` | "Laufwerk A" = the Vortex disc, B = the 3" disc; `drives_swapped` &BE7F 0 → 1 → 0 |
| `\|RESET,5,"X"`, `\|X,1,2` | parameters ignored |

**Finding (XPB, from |X):**
- **Byte +&16** is **ATRK**, the current physical track, which `seek_track` uses (observed: 2 after
  CAT, &17 after reading ROINTIME.DEM = the emulator's head cylinder 23).
- **The start value** in the ROM tables (&27 / &4F) is only the initial value; the first seek
  overwrites it. The table comment "last track 39" was wrong.
- **The 3" XPB as drive A** has its flag byte already at +&17 (observed &28: bit 5 3" drive, bit 3
  motors running), so it has **no MTRK byte**.
- **As drive B** (after |X), `setup_drive_tables` writes MTRK &27 (39) to +&17 and the flag &20 to
  +&18, the layout of the Vortex XPB.
- **Checked with |FORMAT (3.5.10):** nothing reads MTRK of the 3" drive as A; FORMAT uses a fixed 40 tracks there.

**Unobserved segments (step 4):** none. &DB70-&DB8F has run, and so has the swapped branch of
`setup_drive_tables` (#C5F4-#C606, never run before).

**Named / corrected:** `x_copy_xpbs` (&DB8D, was `l_db8d`); the `xpb_3inch` table comments.

#### 3.5.8 `|DERROR[,n]` — `rsx_derror` &D8A1 (**observed**)

**Manual (2.0):**
- `|DERROR,0` / `,1` switch the disc error messages off / on.
- `|DERROR` without a parameter creates the variable DERR (BASIC 1.0 only) holding the error code;
  +128 when the message was printed. 72 means "no disc".
- `,2` / `,3` set the EOF mode (appendix "Das EOF Problem").
- With messages off, a failing LOAD gives BASIC's "File already open".

**How it works:**
- `n` 0/1 → `messages_off` &FF/0; `n` 2/3 → `eof_test_1a` &FF/0.
- With messages off, `disc_error_dialog` takes `ded_silent`: no message, no J/N question, answer N.
- **Without a parameter,** `derr_variable` builds the tokenized BASIC 1.0 statement `DERR=<code>`
  in the record buffer: `&0D 00 00 "DERR" &EF &19 <cas_last_error> &00` (variable, '=', 1-byte
  integer, end). It then far-calls BASIC &D654 to run it (`far_basic_statement`).
  - The ROM select byte is **&80**. No expansion ROM answers to it, so the board's own BASIC
    appears (observed: the FAR CALL reached ROM 0).

**Tests:**

| Test | Result |
|---|---|
| `\|DERROR,0:LOAD "NIX"` | no message; BASIC: `File already open` (as in the manual) |
| `\|DERROR,1:LOAD "NIX"`, then `\|DERROR:PRINT DERR` | `wurde nicht gefunden`, `Break`; DERR = **151** (23 + 128) |
| manual example: `ON ERROR GOTO 100`, `\|DERROR,0`, `LOAD "NIX"`, line 100 `\|DERROR:PRINT DERR` | DERR = **23** |
| drive A empty: `\|DERROR,0:CAT`, then `\|DERROR` | no dialog (`ded_silent` #CCA7, never run before); DERR = **72** |
| `\|DERROR,2` / `,3` | `eof_test_1a` &BE7C = &FF / 0 |
| `\|DERROR,4`, `256`, `-1`, `1,2`, `"1"` | `Eingabefehler` |

**Unobserved segments (step 4):** none. &D8A1-&D8F5 and `disc_error_dialog` / `ded_silent`
(&CC8F-&CCAA) have run.

**Named:** `derr_name` (&D8F2, was `d_d8f2`) and `far_basic_statement` (&D30A, was `far_d30a`; the
relative files use it too).

#### 3.5.9 `|CODE,n` — `rsx_code` &DAC0 (**observed**)

**Manual (2.0):** a personal protection key for `SAVE ,P` files, -32768 to 32767. `|CODE,0` or a
reset removes the key. A wrong key makes RUN produce "complete nonsense".

**How it works:** `rsx_code` stores n in `code_key` (&BE79). `crypt_record` codes and decodes every
128-byte record of a protected file. Each byte is XORed with two tables at once:
- with no key: the 11-byte `crypt_table` and the 13-byte `crypt_table_13`;
- with a key: the 2 key bytes instead of the 11-byte table.

The same operation codes and decodes. The key is not stored in the file.

**Tests:**

| Test | Result |
|---|---|
| `SAVE "PN",P`; `\|CODE,12325`: `SAVE "PC",P` | `code_key` = `25 30` |
| `RUN "PC"` with the key / `\|CODE,0:RUN "PN"` | `OK CODE` both |
| PN and PC decoded offline (tables / key + table) | the same BASIC line `10 PRINT "OK CODE":END` - checked byte for byte |
| `\|CODE,1:RUN "PC"` | garbage: `Syntax error in 12334` |
| `\|CODE,-1`, `32767`, `32768`, `&FFFF` | accepted (16 bits) |
| `\|CODE,"x"` | **accepted**: the key is the string descriptor's address (&B09C) - no type check |
| `\|CODE`, `\|CODE,1,2` | `Eingabefehler` |

**Unobserved segments (step 4):** none. &DAC0-&DAC6 has run, and so has the key branch of
`crypt_record` (#DDB2, never run before).

**Named:** the variable `code_key` (&BE79, 2 bytes), which was listed as still unnamed in 7.1.

#### 3.5.10 `|FORMAT,n` — `rsx_format` &DB90 (**observed**)

**Manual (2.0):** `|FORMAT,2` formats the Vortex disc ("Init-Seite 1 Spur 79"). `|FORMAT,1` asks
"FORMAT (S,D) ?" for the 3" drive: S = system/vendor format (sectors &41-&49, 2 reserved tracks),
D = data format (&C1-&C9). Then "Laufwerk A: Diskette eingelegt J/N ?". After |X, `|FORMAT,2` hits
the 3" drive.

**How it works:**

1. n = 1/2 → drive 0/1. Only the low byte is checked.
2. |RESET, motors off, then "Diskette eingelegt J/N ?". N does nothing.
3. **On the 3" drive** (drive number = `drives_swapped`): "Format (S,D) ?". The format is always
   40 tracks on one side; MTRK is not read.
4. **On the Vortex drive:** tracks = MTRK + 1, sides from flag bit 0.
5. The parameters are kept in the host buffer. `fmt_headers` builds the sector header table in the
   order 1,6,2,7,3,8,4,9,5 (step (SC+1)/2), the same as on the original disc.
6. All tracks of side 0 are formatted, then side 1. Only the tracks are written (filler &E5), so
   the directory is empty without more work.

**Tests:**

| Test | Result |
|---|---|
| `\|FORMAT,2`, N | `Laufwerk B: Diskette eingelegt J/N ? N`, disc unchanged |
| `\|FORMAT,2`, J | `Seite 1 Spur 79`; `\|DIR`: `0K in 0 Files, 704K frei` |
| `\|FORMAT,1`, J, X, ESC | X ignored, ESC aborts; the disc is unchanged (26 files) |
| `\|FORMAT,1`, J, S / D | CAT: `169K frei` (system) / `178K frei` (data); format detection finds both at once |
| write-protected disc (read-only copy in A) | `Seite 0 Spur  0`, `Laufwerk A: Diskette hat Schreibschutz - Wiederholen J/N ?`; N → Ready |
| `\|X`, then `\|FORMAT,2`, J | `Format (S,D) ?` (the 3" drive is B now); ESC; `\|X` back |
| `\|FORMAT`, `,0`, `,3`, `,1,2` | `Eingabefehler` |
| `\|FORMAT,257` | taken as drive A (257 = &0101: only the low byte is checked) |

**Differences from the manual:** 2.11-X asks J/N **before** "Format (S,D) ?" and prints "Seite"
instead of "Init-Seite". `|FORMAT,257` and other values with a high byte are not refused.

**Answer to 3.5.7:** FORMAT never reads MTRK of the 3" drive. It always uses 40 tracks, so the
missing MTRK byte of the 3" XPB as drive A does no harm here.

**Unobserved segments (step 4):** none (&DB90-&DCAD, `bios_format_track`, `frc_format`). The
lines after it (&DCAE-) belong to `bios_select_format` (hidden RSX &83).

**Not checked:** the sector order in the image. It comes from the code: checking it would need
the formatted disc saved as a file, and a changed disc is saved only when the owner asks.

**Named:**
- `fmt_ask_format`, `fmt_3inch`, `fmt_vortex`, `fmt_start`, `fmt_side`, `fmt_track`, `fmt_next_track`, `fmt_done`;
- `fmt_headers` / `fmt_header` (were `sub_dc76` / `sub_dca0`) with `fh_odd`, `fh_even`, `fh_done`.

#### 3.5.11 `|DISC`, `|DISC.IN`, `|DISC.OUT`, `|CAS`, `|CAS.IN`, `|CAS.OUT`, `|TAPE`, `|TAPE.IN`, `|TAPE.OUT` — &D724-&D777 (**observed**)

**Manual (2.0):** six ways to assign the input and output channel to the disc or the cassette.
`|CAS:CAT` asks "Press PLAY then any key". `|TAPE`, `|TAPE.IN` and `|TAPE.OUT` are not in the manual.
In the ROM they jump to the same routines as `|CAS`, `|CAS.IN` and `|CAS.OUT`.

**How it works:** the commands only change the CAS jumpblock (&BC77-&BC9D):
- **Disc** (`set_disc_entries`): every entry becomes `DF 8B A8`, i.e. RST 3 through the far address
  workspace+&18B (&A88B) → `cas_dispatcher`.
- **Tape** (`restore_tape_entries`): the original entries are copied back from workspace+&164 (input,
  7 entries), +&188 (CATALOG) and +&179 (output, 5 entries). With AMSDOS this is AMSDOS's own saved
  copy at the same offset (`CF xx xx`, RST 1 into the OS tape code).
- **CATALOG** always follows the input channel.

Parameters are ignored.

**Tests:**

| Test | Result (jumpblock: D = disc, T = tape) |
|---|---|
| start / `\|DISC` / `\|DISC.IN` / `\|DISC.OUT` | all D |
| `\|CAS` / `\|TAPE` | all T |
| `\|CAS.IN` / `\|TAPE.IN` | input + CATALOG T, output D |
| `\|CAS.OUT` | output T, input + CATALOG D |
| `\|TAPE.IN`, then `\|TAPE.OUT` | all T |
| `\|CAS:CAT` | `Press PLAY then any key:`, ESC → Ready |
| `\|CAS.OUT:SAVE "TT"` | `Press REC and PLAY then any key:` (ESC counts as a key: `Saving TT block 1`, then `Break`) |
| `\|DISC:CAT`; `\|DISC,1`, `\|CAS,"x"` | the disc again; parameters ignored |

**Unobserved segments (step 4):** none (&D724-&D777).

**Named:** `rsx_cas_in`, `rsx_cas_out`, `rsx_disc_in`, `rsx_disc_out` (headers), `restore_tape_entries`
(was `sub_d746`), `set_disc_entries` (was `sub_d765`), `sde_loop`.

#### 3.5.12 `|FAST`, `|SLOW`, `|FRAME` — `rsx_fast` &FD5A, jumpblock &C054 / &C05D (**observed**)

Not in the manual (2.0).

- **|FAST** speeds up text output in MODE 2. It points the indirection IND TXT WRITE CHAR (&BDD3)
  to the FAR CALL stub `fast_write_stub` (&B1BA → `fast_write_char` &FD7D in ROM 5). In MODE 0 and
  1 it does nothing. The details of `fast_write_char` (normal, inverse, user-defined characters)
  were analysed earlier.
- **|SLOW** is a direct `JP TXT_RESET`, which restores the indirections.
- **|FRAME** is a direct `JP MC_WAIT_FLYBACK`.

None of the three checks its parameters.

**Tests:**

| Test | Result (&BDD3) |
|---|---|
| start | `JP &134A` (firmware) |
| `MODE 1:\|FAST` | unchanged |
| `MODE 2:\|FAST`, `PRINT "schnell"` | `JP &B1BA`; output correct |
| `\|SLOW` | `JP &134A` again |
| `\|FAST,1,"x"`, `\|SLOW,5` | the same (parameters ignored) |
| `\|FRAME`, `\|FRAME,1,2` | returns; breakpoint on MC WAIT FLYBACK (&BD19) reached |

**Unobserved segments (step 4):** none in `rsx_fast` / `fast_install` / `fast_write_char`
(&FD5A-&FE15). |SLOW and |FRAME have no ROM code of their own.

#### 3.5.13 `|ROMCAT[,n]` — `rsx_romcat` &FE74 (**observed**)

**Manual (2.0):** has no |ROMCAT. It describes `|ROMS`, a table of the background ROMs 0-7 (No,
Name, Version); |ROMS does not exist in 2.11-X.

**How it works:**

- **`|ROMCAT`:**
  - prints "Himem:" (BASIC's HIMEM, &AE7B);
  - then for each ROM 0-7: number, the 4 header bytes (type, mark, version, modification), the
    data area ("Base", from `KL_ROM_IY_TABLE`, only for a background ROM of type 1) and the name
    (the first command name).
- **`|ROMCAT,n`:** lists ROM n's command names with their jump addresses.
  - Holding ESC pauses the list. ESC again ends it; another key goes on.
- **Helpers in RAM:** to read another ROM, `rsx_romcat` copies a small helper to **&BF00** and
  calls it there. &BF00 is over the HELLO loader's RAM copy, which is only needed at start-up.
  - `romcat_rom_info` (from &FF4A, 47 bytes) reads a ROM's header and name.
  - `romcat_rsx_entry` (from &FF79, 71 bytes) reads the next name and jump address; its entry
    counter is a self-modified operand at &BF0B.
- **Output:** `print_name_string` prints the first character with TXT WR CHAR, so the hidden
  one-byte names (&81-&89) show as a symbol. The hex output uses routines in the XMON area.

**Tests (MODE 2):**

| Test | Result |
|---|---|
| `\|ROMCAT` | `Himem: A677`; ROMs 0-4 and 6: `80 01 00 00 ---- BASIC` (empty slots show the on-board BASIC); `05 01 01 21 03 A6FC V ROM`; `07 01 00 05 00 A700 CPM ROM` |
| `\|ROMCAT,7` | AMSDOS's commands (`CCD1 DISC`, …, `D4C4 REN`), the hidden ones as `?` |
| `\|ROMCAT,5` | `C1E9 V ROM`, `CF7E GET`, `D015 PUT`, … |
| `\|ROMCAT,0` / `,3` (empty) | `C000 BASIC` |
| ESC held during `,5`; ESC again / space | the list pauses; ESC ends it / space goes on to the end |
| `\|ROMCAT,8`, `,-1`, `,1,2` | nothing at all (silent RET, no "Eingabefehler") |
| `\|ROMCAT,256` | ROM 0 (only the low byte of the number is read) |

**Finding, the 4 bytes at &A6FC:**
- VDOS's "Base" is &A6FC and HIMEM is &A677, 4 bytes below the &A67B of AMSDOS alone.
- `rom_init` returns HL unchanged, and the firmware stores HL+1 as the ROM's IY (firmware manual,
  10.4).
- So the 4 bytes are taken by the **firmware**, apparently as the link block for the ROM's
  command list (deduced, not documented in this form).
- This also explains the **IY = &A6FC** seen on the RSX path (3.5.x, |CODE / &84 tests). The
  firmware passes the ROM's area in IY; VDOS does not use it and loads `vdos_workspace` itself.

**Unobserved segments (step 4):** none (&FE16-&FFBF, including both RAM helpers).

**Named:**
- `print_dollar_string`, `print_name_string`, `print_crlf_message`;
- the texts `romcat_header_text`, `romcat_no_base_text`, `romcat_himem_text`, `romcat_rsx_header_text`;
- `romcat_next_rsx`, `romcat_table`, `romcat_next_rom`, `romcat_header_byte`, `romcat_no_base`,
  `romcat_base`, `romcat_name`;
- the RAM helpers `romcat_rom_info` / `romcat_rsx_entry` (groups `romcat` / `romcat_rsx`, contexts
  rom5:FF4A-FF78 / FF79-FFBF);
- the XMON output routines `xmon_hex_byte`, `xmon_hex_nibble`, `xmon_out_two_tabs`, `xmon_out_tab`,
  `xmon_out_lf_cr`, `xmon_out_char`.

**RAM comments:** with the cpcxray fix (grouped comments at RAM addresses), the HELLO loader's
line comments are in group `vdos`, and those of the two helpers are in `romcat` / `romcat_rsx`.
Each copy at &BF00 now shows only its own. Still open (cpcxray, requested): labels of another
group can show up inside a copy (e.g. `rre_skip_name_2` in `romcat_rom_info`).

#### 3.5.14 `|ROMOFF[,n,...]` and `|AMSDOS` — `rsx_romoff` &FC20, `rsx_amsdos` &FC3B (**observed**)

**Manual (2.0):**
- `|AMSDOS` switches VDOS off and leaves AMSDOS on. It resets the machine, so memory is lost.
- `|ROMOFF` switches all background ROMs off; `|ROMOFF,6,7` only ROMs 6 and 7.
- A reset switches them on again.

**How it works:**

1. A mask with one bit per ROM is built; a set bit means "off". `|ROMOFF` alone sets all (&FF),
   `|ROMOFF,n,...` sets the given ROMs, and `|AMSDOS` sets VDOS's own ROM (KL CURR SELECTION).
   `rom_off_bit` puts each bit where the start program reads it.
2. The 37-byte start program `romoff_start` is copied to &4001 and the mask to &4000.
3. MC START PROGRAM (C = 0) resets the firmware and runs the start program:
   - KL INIT BACK only for the ROMs 7..1 whose bit is clear;
   - a short delay;
   - `JP &C00C` into BASIC.
4. A number ≥ 8 or with a high byte ends |ROMOFF at once with `RET`: no message, no reset. BASIC
   passes the parameters last first.

**Tests** (only what VDOS causes; AMSDOS's own behaviour is not analysed):

| Test | Result |
|---|---|
| `\|ROMOFF,8`, `,256`, `,"x"`, `,3,9` | nothing (no message, no reset) |
| `\|ROMOFF,6` (empty slot) | restart with VDOS and AMSDOS as before |
| `\|ROMOFF,5` / `\|AMSDOS` | VDOS off: `\|DIR`, `\|ROMCAT` → "Unknown command"; HIMEM &A67B |
| `\|ROMOFF` | all off: HIMEM &AB7F, CAT on tape ("Press PLAY then any key:") |
| `\|ROMOFF,7` | VDOS without AMSDOS: `\|ROMCAT` "05 … A700 V ROM", "07 … 0000 CPM ROM"; HIMEM &A67B; `\|DIR` works |
| `\|ROMOFF,5,7` | both off: HIMEM &AB7F, `\|DIR` unknown |

**`cas_oneshot_ptr` during these tests:**
- The write breakpoint saw the init clears: AMSDOS ROM 7 &CAB0, and VDOS `clear_memory` &CDA5.
- While VDOS was off, it also saw AMSDOS's own writes (&C976, its sector buffer pointer &BE76/77).
- By agreement these were only logged: only the VDOS ROM is of interest.

**Unobserved segments (step 4):** none (&FC20-&FC68 and the start program &4001-&4025).

**Named:** `romoff_next_param`, `romoff_restart`, `rom_off_bit` (`rob_loop`, `rob_next`), the RAM
start program `romoff_start` (`rs_next_rom`, `rs_delay_1-3`); operand overrides at &4020 (stack
&C000) and &4023 (BASIC &C00C, not a VDOS label).

#### 3.5.15 Relative files: `|FILES`, `|OPEN`, `|FIELD`, `|GET`, `|PUT`, `|CLOSE` — &CE5B-&D329 (**observed**)

**Manual (2.0):** random access files with up to 16 channels (numbers 0-127). Usage:
1. `|FILES,ch,max,...` reserves 90 bytes + buffer per channel below HIMEM;
2. `|OPEN,"name",len,ch` opens or creates a file;
3. `|FIELD,ch,l1,l2,...` splits the record into fields;
4. `|GET,ch,rec,@a$,...` / `|PUT,ch,rec,...` read / write record rec;
5. `|CLOSE,ch` closes it.

The manual lists the error messages 39-45, 53 and 55. |GET needs `@`; |PUT also takes direct strings.

**How it works:**

- **`rsx_files`:**
  - releases an old area (`rel_free_area`; HIMEM must still be where |FILES left it, else
    "MEMORY-fehler");
  - reserves the new area below BASIC's HIMEM and lowers HIMEM through two BASIC routines
    (`rel_set_himem`: &FC3E, &F4F5, ROM select &80);
  - **area** (`rel_area` &BEB7): +0 number of channels, +1/2 size, +3 a scratch line, the
    blocks from +&131;
  - **block** (&5A + max bytes): +0 channel (bit 7 open), +1/2 link, +3/4 maximum, +5/6 current
    length, +7/8 record number, +9/10 buffer address, +&0D FCB (36 bytes), +&31 field table
    (32), +&5A record buffer;
  - `rel_files_flag` (&0026, low RAM) = &FF while channels are defined.
- **`rsx_open`** puts the name into the channel's FCB, then `open_file`, or `make_file` if the
  file doesn't exist.
- **`rsx_field`** stores the field lengths (1-255) in the field table and checks their sum
  against the record length.
- **`rel_record_position`:** byte = record × length (16 × 16 → 32 bits), random record
  = byte / 128. A record ≥ 65536 gives "Recordnummer zu gross".
- **`rsx_put`:**
  - clears the channel buffer and copies each string into its field (longer: cut; shorter:
    rest 0);
  - writes the record 128-byte record by record; part records are read first and merged
    (`rel_read_random` / `rel_write_random`, with the format detection switched off).
- **`rsx_get`:**
  - reads the record into the channel buffer;
  - gives each field to its variable with `rel_assign_string`: VDOS builds the tokenized
    statement `name$="…"` in the scratch line and lets BASIC run it, so BASIC allocates a string
    of the right length;
  - the real bytes are then copied into that string, so quotes in the data survive;
  - trailing zero bytes are not taken.

**Tests** (drive A, in memory):

| Test | Result |
|---|---|
| manual example: `\|FILES,1,100`, `\|OPEN,"ADRESS.REL",47,1`, `\|FIELD,1,12,20,15`, `\|PUT` records 1 and 174, `\|GET` both | `Mueller\|Koeln\|123456`, `Meier\|Essen\|0123`; in the file record n starts at n × 47 (sparse file) |
| 300-byte record, fields 100/150/50: 120 × "A", `sag "hallo"`, `kurz` | 100 A's (cut), `sag "hallo"` (quotes kept), `kurz` (length 4) |
| more strings than fields / more variables than fields | the rest ignored / the variable unchanged |
| record 0; records never written (1, 40, 2000) | usable; read as empty, no error |
| 65535 × 30 bytes / 29000 × 300 bytes | ok / `Recordnummer zu gross` (variables unchanged) |
| two channels at once (30 and 300 bytes) | both work |
| `\|OPEN` twice / channel not in `\|FILES` / len > maximum / channel 200 / no `\|FILES` | `Kanal bereits offen` / `Kanal nicht definiert` / `Feld zu lang` / `Kanalnummer falsch` / `Feld nicht definiert` |
| `\|FIELD` sum > length / `\|PUT` before `\|FIELD` / `\|CLOSE` or `\|GET` of a closed channel | `Feld zu lang` / `Feld nicht segmentiert` / `Kanal nicht offen` |
| wrong parameter counts, field length 0 or 256, odd `\|FILES` pairs, a channel twice, channel 128 in `\|FILES` | `Eingabefehler` |
| `\|GET` into variables that do not exist yet | BASIC `Improper argument` (as the manual says) |
| directory full, `\|PUT` into a record that needs a new extent | `Laufwerk A: Directory voll` |
| `MEMORY HIMEM-100`, then `\|FILES` again | `MEMORY-fehler` |
| `\|FILES` alone | everything released, HIMEM back |

**Findings (bugs and differences):**
1. **Error 55 "Rekord enthält keine Daten" (2.11-X text: "Record leer", msg &37) cannot occur** -
   confirmed 2026-10-26 by simulation: random_seek sets &FF and Z is still set at &E5ED; only with
   Z cleared by hand does `rel_no_data` run ("Record leer"). Bugfix proposal in todo 3.
   - `random_seek` sets the return code &FF for a record in a missing extent, then leaves
     through `set_file_write_flag`.
   - VDOS implements that with `set 7,(hl)`, which keeps the Z flag, so `read_random_body`
     (`call z,sub_e4c2`) reads anyway and overwrites &FF with 1.
   - |GET only tests for &FF, so the record reads as empty (observed: return code &01 at
     #CFC2).
   - From memory, DR CP/M's `setfwf` uses `ori` there, which clears Z (not checked against the
     source).
2. **`|FILES` with a maximum length 0 is not refused.** A = &21 is loaded, but CY stays clear
   (&D197), so the `jp c` at &D1B6 is skipped.
3. **A channel ≥ 128 in `|FILES` gives "Eingabefehler"**, not "Kanalnummer falsch": &2C is
   loaded, but `error_bad_name` loads &21 itself.
4. **Record lengths 256, 512, … are unusable.** The "open" test (&CF4B) checks only the low byte
   of the length (observed: `|OPEN …,256` → `|FIELD` "Kanal nicht offen").
5. **Direct strings in `|PUT` leak BASIC's temporary strings** (`basic_error_patch`). The 5th
   `|PUT` with two literals → "String expression too complex", after which BASIC can be in a bad
   state. The manual's `|PUT,1,15,"Mueller",…` therefore only works a few times; use `@a$`.
6. **Message texts differ from the manual:** "Kanal bereits offen" / "Kanal nicht offen" /
   "Recordnummer zu gross" (2.0: "geöffnet" / "geöffnet" / "Rekordnummer").

**Unobserved segments (step 4):** none any more - `rel_no_data` (&D010) was run by simulation
(finding 1). Everything else in &CE5B-&D329 and `read_random` / `write_random` / `random_seek`
(&E5B2-&E67F) has run, including the "Directory voll" exit #E67B.

**Named:** `rel_check_channel`, `rel_block_pointers`, `rel_find_channel`, `rel_channel_param`,
`rel_channel_number`, `rel_getput_start`, `rel_copy_part`, `rel_next_record`,
`rel_record_position`, `rel_free_area`, `rel_clear`, `rel_block_link`, `rel_check_duplicates`,
`rel_set_himem` (`far_basic_himem_1/2`), `rel_assign_string` (`ras_*`), `rsx_bad_param_2`,
`rel_no_data`, and the labels inside the commands (`open_*`, `fld_*`, `get_*`, `put_*`,
`files_*`); the variables `rel_area` (&BEB7), `rel_files_flag` (&0026) and `rel_saved_sp` (&BE80).

#### 3.5.16 `|CPM[,n]` — `rsx_cpm` &C32B (**observed**, the RSX side only)

**Manual (2.0):**
- `|CPM`: the Amstrad CP/M from the 3" disc (drive B as a 40-track drive).
- `|CPM,1`: Vortex's 44K CP/M from the 3" drive, B = Vortex drive with 708K.
- `|CPM,2`: the same from the Vortex disc, which becomes drive A.

**How it works:**
- **No parameter, or n = 0** (low byte): FAR CALL to AMSDOS's own CP/M boot (`cpm_amsdos_boot`,
  ROM 7 &C1DC). From then on VDOS is not involved.
- **n = 1 / 2:** `drives_swapped` = 0 / 1, then `rom_init_foreground` → MC START PROGRAM with
  `cpm_cold_boot` (Part B, todo).
- **Other n:** Eingabefehler.

**Tests:**

| Test | Result |
|---|---|
| `\|CPM` / `\|CPM,0` | `CP/M 2.2 - Amstrad Consumer Electronics plc` |
| `\|CPM,1` | that line (the boot sector comes from the 3" disc), then ` 44K CP/M vers. 2.2-07/86    vortex GmbH`, `A>`; `drives_swapped` = 0 |
| `\|CPM,2` | only the vortex line, `A>`; `drives_swapped` = 1 |
| `\|CPM,3`, `-1`, `259` | `Eingabefehler` (259 = &0103: low byte 3) |
| `\|CPM` with a disc that cannot be booted (IBM blank) | AMSDOS: `Drive A: read fail` / `Failed to load boot sector`, `Retry, Ignore or Cancel?`; Cancel asks again - AMSDOS does not return |

**Differences from the manual:** the CP/M banner reads 07/86 (2.0: 03/86).

**Unobserved segments (step 4):** `jp l_c48a` (#C325) after the FAR CALL into AMSDOS. It would
only run if AMSDOS's boot returned; with this AMSDOS it does not, even on a disc that cannot be
booted.

**`cas_oneshot_ptr` under CP/M:** the one-shot pointer cannot work there. CP/M programs never call
CAS, and `cpm_cold_boot` clears it with `disc_init`. Writes under CP/M are only logged.

**Named:** `cpm_amsdos_boot` (was `l_c322`), `far_amsdos_cpm` (was `far_c328`), `cpm_vdos_boot`
(was `l_c33e`).

#### 3.5.17 Hidden RSX &81-&89 — the disc BIOS functions (**observed**)

Their one-byte names (&81-&89, bit 7 = the last character) can't be typed in BASIC. Programs find
them with KL FIND COMMAND, like AMSDOS's BIOS functions (firmware manual ch. 19); CP/M uses the
extended BIOS jumpblock instead. Tested from machine code with a general caller at &9200 (KL FIND COMMAND, registers from
memory, RST 3, results back to memory).

| RSX | Routine | Test | Result |
|---|---|---|---|
| &81 | `bios_set_message` | A = &FF, then &00 | old value back (&00 / &FF), `messages_off` set |
| &82 | `bios_setup_disc` | block with motor off &00F0; then HL = &C1A6 (ROM defaults) | `disc_time_constants` &BE44 = 28 00 F0 00 00 14 C4, step rate 4, disc works; defaults back. Exit CY = 0 (registers corrupt, as callers written for AMSDOS expect) |
| &83 | `bios_select_format` | A = &FF, E = 1 / A = &C1, E = 0 / A = &41 / A = &FE twice | HL = &ABDD (drive B's flags) / 3" XPB in data format (DSM &B3, sector &C1) / back / `fast_flag` &FF + \|FAST patch (**no mode check**), then 0 + TXT RESET |
| &84 | `bios_read_sector` | sector 3 of the track written below; multi-sector (`set_eot` test, 4.5b) | identical; CY = 1, A = 0 |
| &85 | `bios_write_sector` | drive B, logical track 158, sector 3, 512-byte pattern | CY = 1, A = 0; read back identical |
| &86 | `bios_format_track` | drive B, track 158, headers 79/0/1..9/2 | CY = 1; a fresh sector holds &E5 |
| &87 | `bios_move_track` | E = 1, D = 40 | ATRK = 20, head on cylinder 20 |
| &88 | `bios_get_status` | units 0-3; drive A empty; write-protected disc | ST3 &20 / &29 / &22 / &2B (units 2/3 = A/B again: only US0 is wired); empty: ST3 &00, CY = 1; **write-protected: CY = 0, A = &54** |
| &89 | `bios_set_retry_count` | A = 5, then &10 | old value back, `retry_count` set, HL kept |

BC, DE and HL come back unchanged from the sector functions (the `disc_begin` frame).

**Findings:**
- **&88 cannot report a write-protected disc as a status.** `sense_drive_status` judges the
  SENSE DRIVE STATUS result like a normal command, by bits 7-6 of its first byte. That byte is ST3
  here, and the write-protect bit 6 looks like "abnormal end", so the call reports an error
  (`fdc_result` = &60). The HELLO loader has a branch for exactly this case (&BF12: CY = 0, then bit
  5 "ready" of &BE4B). **Observed** with `output/hello_test.dsk` (a new system disc with HELLO.BAS,
  inserted read-only): `fdc_result` &60, bit 5 set → "HELLO STARTED" after the reset.
- **&83 with A = &FE** switches the CP/M FAST flag at &BE7C. Under BASIC that byte is
  `eof_test_1a`, so the call also switches the &1A end-of-file test, and it installs |FAST in any
  screen mode.

**Unobserved segments (step 4):** none in the nine routines and the RSX jumpblock entries
&C080-&C09A. `bios_set_reg_save` (#CE2A, extended BIOS only, no RSX) remains for Part B.

#### 3.5.18 `|XMON` — `rsx_xmon` &ED20 (start, command recognition, Z, X, D, Y and L group 1 **observed** 2026-10-25/26; the other commands are open)

**Status (2026-10-26):**

| Command | State |
|---|---|
| start, `*` prompt, command recognition, ESC exit | observed |
| Z (RAM bank) | completely run |
| X (firmware ROM switch) | observed |
| D (dump) | completely run, except a start at &FFxx (would read ROM 5) |
| Y (ROM select) | observed from BASIC (&FF, &07, ESC); CP/M branch open |
| L (disassembler) | **complete** (base, CB, ED, DD/FD, DD CB/FD CB, count mode, pause); only the unused table entries stay never read |
| R (registers) | **complete** (show, edit with RETURN / ',' / non-hex key / ESC) |
| P (printer echo) | **complete** except a busy printer (cpcxray reports it ready) |
| A (text into memory) | **complete** |
| B (breakpoints) | **complete** (their use: see G) |
| C (search) | **complete** |
| F (fill) | **complete** |
| G (go) | **complete** |
| T (trace) | **complete** (all paths; 6 bugs / weaknesses observed) |
| M (move) | **complete** (bug in the overlapping copy) |
| S (substitute) | **complete** |
| I (load a file) | **complete** from BASIC (disc); tape and the CP/M branch open |
| O (save a file) | **complete** from BASIC (disc; bug: ESC leaves the file open); tape and the CP/M branch open |
| @ (disc monitor) | **complete** from BASIC (all 12 commands, `>>`, `E:xx`); only the CP/M branches open; bug: T / G keep an invalid position |

`|XMON` starts Vortex's Z80 machine-code monitor. The manual describes all its commands:
A, @ (disc monitor), B, C, D, F, G, I, L, M, O, P, R, S, T, X, Y and ESC. The owner started it
from BASIC. Observed so far: the start, up to the waiting `*` prompt.

| Step | Routine | Observed |
|---|---|---|
| &BE00 = 0, AF (A = 0) and BC on the caller's stack | `rsx_xmon` | ran (meaning of &BE00 open) |
| MODE 2 and `rsx_fast` | `rsx_xmon` | screen cleared, MODE 2 |
| From BASIC or CP/M? | `xmon_cpm_mode` &EB22: A = &BEDD, Z = BASIC | Z (&BEDD = 0); the CP/M branch &ED34-&ED3E has not run |
| Clear &BEC9 (X switch: RAM at &0000) and &BEE0; clear &BF00-&BF17 | `xmon_init` &ED3F | the 24 bytes are 0 |
| The ROM shown at &C000 | `xmon_rom` &BEC8 | 5 |
| Copy RAM &0080-&0094 to &AD76 | `xmon_save_low_ram` &FC8E | taken from RAM (all 0), not from the firmware ROM; OUT to the gate array with C' bit 5 cleared changes no ROM bit |
| Save the caller's SP; stack &BF80 | `xmon_saved_sp` &BEDE | &BFF4; &BEF8 = &BF80 |
| RST 6 → breakpoint handler | `xmon_set_far_jump` &EE2F | &0030 = `FD E5 DF D0 BE` (PUSH IY / RST 3 / DEFW &BED0); `xmon_break_far` &BED0 = &F8D9, ROM 5 (`xmon_breakpoint`) |
| Prompt and wait for a key | `xmon_command_loop` &ED74, `xmon_get_key` &FAF2 | `*`; first empties the key buffer, then waits in `wait_key_cursor` (PC &FB14) |

**Command recognition** (traced 2026-10-25, keys `\` and `R`, trace `output/trace_xmon_d_return.jsonl`):

1. `xmon_get_key` (&FAF2): empties the key buffer, waits, makes the key upper case; Z = ESC (&FC).
2. `xmon_command_key` (&ED92): keys below `@` are ignored without an echo. Others are echoed and
   looked up with `xmon_find_command` in `xmon_command_table` (&EDC5).
3. `xmon_find_command` (&EDB2): B = the count byte (18), then 3-byte entries (key, routine
   address). Found: `load_hl_indirect` fetches the address, **`ex (sp),hl` puts it in place of
   the return address**, `ex de,hl` gives HL back, and `ret` jumps to the command. The command
   runs on the caller's stack, with DE = the return address &EDA1. This is the same as the
   remembered "push hl / ret", done with one register swap. Not found: `ex de,hl / ret` back to
   &EDA1, which prints &08 (back), &10 (delete) and &07 (beep), then waits for the next key.
4. ESC (read, not run): `pop af` takes the byte that `rsx_xmon` pushed (A = 0) and, below `@`,
   calls TXT RESET. From BASIC it ends in `xmon_exit_basic` (&FCA8: clears BASIC's input buffer
   &ACA4, 200 bytes, then RET to the RSX caller); under CP/M it does RST 0.

| Key | Routine | | Key | Routine | | Key | Routine |
|---|---|---|---|---|---|---|---|
| B | `xmon_cmd_breakpoints` &EEA0 | | O | `xmon_cmd_output` &F011 | | M | `xmon_cmd_move` &F745 |
| D | `xmon_cmd_dump` &EEFF | | L | `xmon_cmd_list` &F048 | | A | `xmon_cmd_ascii` &FCC5 |
| F | `xmon_cmd_fill` &EF74 | | S | `xmon_cmd_substitute` &F70B | | X | `xmon_cmd_firmware` &EE79 |
| G | `xmon_cmd_go` &EFA2 | | P | `xmon_cmd_printer` &F9F0 | | Y | `xmon_cmd_rom_select` &EDFC |
| I | `xmon_cmd_input` &EFB5 | | T | `xmon_cmd_trace` &F7A4 | | C | `xmon_cmd_search` &FCE7 |
| R | `xmon_cmd_registers` &F9A7 | | Z | `xmon_cmd_z` &EE15 | | @ | `xmon_disc_monitor` &EA9E |

The table bytes are classified by the owner (key as a string byte, address as a word table), so
every command routine now has a name. **Z** is in the table but not in the manual; it
turned out to be the RAM bank select (below).

**Z — the RAM bank** (not in the manual; observed 2026-10-25): `xmon_cmd_z` (&EE15) shows the
current setting through `xmon_input_byte` (&FA45) and reads a new one: 0 = off, 1-8 = bank 0-7.
The result goes to `xmon_bank` (&BEE0) as 0 or &20 + bank ("03" -> &22). With a bank set, Z
shows bank + 1 as the default (observed: &22 -> "Z03", RETURN keeps it).
- `xmon_input_byte` shows the default without printer echo (`xmon_hex_byte_quiet` &FA1B). Each hex
  digit (`xmon_hex_digit` &EE8D) is shifted in from the right and shown in place; RETURN ends.
- Every command ends in `xmon_command_done` (&EE80): a new line, then the `*` prompt. If &BE00 is
  not 0, it goes to &EABB instead (read: back into the disc monitor).
- **XMON's memory access** (&FB7C, read): it copies 21 bytes of code from &FCB0 to RAM &0080
  (that is why `xmon_save_low_ram` keeps &0080-&0094 at &AD76) and writes `xmon_bank` to
  **port &FBBD**, the bank port of the Vortex RAM expansion (owner: bits 7/6 ignored, bit 5 = on,
  bits 2-0 = bank). It then
  selects `xmon_rom`, sets the gate array, runs `call &0080`, and puts the saved RAM back.
- **Danger for the analysis:** this RAM code reads the ROM paged in at &C000. If `xmon_rom` = 5
  (the start value), memory commands on &C000-&FFFF read VDOS as data, and cpcxray records that
  with no way to switch it off.
- So: no XMON memory commands on &C000-&FFFF while `xmon_rom` = 5. Y only under control. Take a
  snapshot before each command and check `analysis_status` after it.
- **ESC exit observed:** `pop af` gives A = 0, then TXT RESET, then `xmon_exit_basic` clears
  &ACA4 (200 bytes), and BASIC shows "Ready".

**X — the firmware ROM switch** (traced 2026-10-25): `xmon_cmd_firmware` (&EE79) only inverts
`xmon_firmware_rom` (&BEC9; observed &FF -> 0) and touches no gate array port. The switch takes
effect per byte in `xmon_read_byte`: with &FF the reads of &0000-&3FFF see the firmware ROM,
with 0 the RAM (observed with D0000,003F both ways; with X off &0030 shows XMON's own RST 6
`FD E5 DF D0 BE` in RAM).

**D — the hex dump** (all variants run 2026-10-25):
- `xmon_cmd_dump` (&EEFF) reads the start with `xmon_input_word` (&FA7E; default
  `xmon_dump_address` &BED9). Then:
  - `,` and an end address: dump up to the end;
  - RETURN after the start (`D0000` + RETURN): end = start + &100;
  - RETURN alone (`D` + RETURN): the default is taken (observed 0100 -> &0100-&01FF);
  - ESC in the address input: no dump, straight to `xmon_command_done`, `*` prompt.
- `xmon_dump_lines` prints a line (address, 16 hex bytes) while the next line start is below
  the end; `xmon_dump_address` then holds the next address (observed &0200).
- SPACE pauses, SPACE continues, ESC ends (owner test D0000,0200: &EF67 / &EF6A observed).
- **`xmon_read_byte` (&FB6A)**, used by D, L and the other memory commands:
  - below &8000 (`xrb_low`): it reads directly. It writes `xmon_bank` to port &FBBD, switches
    the lower ROM per the X switch, sets gate-array bit 5, reads, then restores the system
    bank from (&001F).
  - from &8000 on (`xrb_high` &FB6E): the RAM reader at &0080, see Y below.
- Not run: a start at &FFxx (it would read ROM 5 as data; blocked by the rules above).

**Y and reading from &8000 on** (owner, 2026-10-25: `Y` -> `FF`, then `DC000`):
- `xmon_cmd_rom_select` (&EDFC) shows |ROMCAT's ROM list. It enters `romcat_table` at &FEDE,
  so the "Himem" line is missing. The ROM-header reader goes to &BF00 and overwrites
  `xmon_break_area`: breakpoints set before Y are lost.
- Then `xmon_input_byte` reads the new `xmon_rom`.
- `xmon_read_byte` from &8000 (`xrb_high` &FB6E) copies the 21-byte reader from &FCB0 to RAM
  &0080 (`xmon_ram_reader`) and calls it. The reader:
  1. selects ROM `xmon_rom` on port &DFxx;
  2. sets the gate array with **the upper ROM off if `xmon_rom` >= &FC**, then a second value
     with bits 6/5 set (purpose open);
  3. reads the byte, switches the upper ROM on and selects VDOS again.
- Afterwards &0080-&0094 is restored from &AD76.
- With &FF the dump showed the screen RAM. The access map stayed clean at &C000-&FFFF; only
  the code that ran and its operands were added, plus &FCB0-&FCC4 as data (the copy source).
- **So `xmon_rom` = &FC-&FF is the safe setting for reads from &C000 on.**
- Also observed (2026-10-26):
  - Y 07 with DC000,C03F: AMSDOS's header was shown, the ROM 5 map stayed unchanged;
  - Y + ESC: `xmon_rom` is kept (&FA5C / &FA5D);
  - a non-hex key in `xmon_input_byte` (&FA67): it only beeps (`xmon_hex_digit` prints &07,
    NC) and is ignored.
- Open: the CP/M branch of Y (&EDFF); the purpose of the second gate-array value with bits 6/5; the non-hex key in
  `xmon_input_word` (&FAAC).

**L — the disassembler** (group 1 tested 2026-10-25/26: all 244 base opcodes &00-&FF without
CB / DD / ED / FD, loaded at &4000 from `output/xmon_l/base_opcodes.bin`):
- `xmon_cmd_list` (&F048) reads the start (default `xmon_list_address` &BED5). With ',' and an
  end address it lists while the next instruction starts below the end; RETURN instead lists
  23 lines (count mode, observed - see the mini test below). Each line is printed by `xmon_list_line` (&F089).
- `xmon_list_line` decodes into `xmon_decoded` (&ACA5-&ACA9 in BASIC's input buffer):
  length - 1, mnemonic, operand 1, operand 2, index prefix.
  - &00-&3F come from `xmon_opcodes_00` (&F4A4) and &C0-&FF from `xmon_opcodes_c0` (&F564),
    3 bytes each: bits 7-6 = length - 1, bits 5-0 = mnemonic, then the two operand codes.
  - &40-&7F (LD r,r' / HALT) and &80-&BF (ALU) are built from the opcode bits.
  - CB / ED / DD / FD have their own branches. ED &40-&7B uses `xmon_opcodes_ed40` (&F64A);
    `xmon_index_opcodes` (&F624) is searched after DD / FD.
- Output: the bytes in hex, then the mnemonic from `xmon_mnemonics` (&F336, 4 characters each).
  The operands come from `xmon_list_operand` (&F280): codes &00-&29 are names from
  `xmon_operand_names` (&F44E, bit-7 strings, counted); &C0-&F8 = RST, &F9/&FA = (n),
  &FB = relative, &FC = n, &FD = (nn), &FE = nn, &FF = none.
- **RST &08 / &10 / &18 are 3-byte instructions** (table entry `A6 C8 FF`). XMON skips the CPC
  inline word, like the firmware does; the word shows in the byte column only, not as an operand
  (observed 2026-10-26 with `CF 34 12`: `40FA  CF3412    RST  08`). RST &20-&38 have length 1;
  that includes **RST &28 (FIRM JUMP)**, which has an inline word in the firmware: XMON lists the
  word as instructions (`EF 34 12`: `RST 28`, `INC (HL)`, `LD (DE),A`). The test file
  `output/xmon_l/base_opcodes.bin` now has `defw &1234` after RST 1, 2, 3 and 5 only (the RSTs
  with firmware inline bytes; old file `base_opcodes_v1.bin`). XMON shows the RST number as
  `08`, not `&08`.
- **Bug:** operand code &F9 (`OUT (n),A`, `IN A,(n)`) jumps to the output without reading the
  byte. It shows H = &F4, the high byte of the name table pointer: `D3 56` -> `OUT (&F4),A`.
  The code &FA does the same output correctly.
- Other variables: `xmon_list_address` &BED5 (the next address to list), `xmon_branch_target`
  &BEE3 (the target computed for relative jumps), `xmon_decoded` &ACA5 (5 bytes, see above).
- **The tables in the source** (2026-10-26): `xmon_opcodes_00`, `xmon_opcodes_c0` and
  `xmon_opcodes_ed40` are written with one entry per line (3 bytes), and each line is commented
  with the opcode, the instruction and its length, e.g. `defb #88,#11,#FE ; &01: LD BC,nn - 3
  bytes`. The comments were computed from the decoded table bytes
  (`output/xmon_l/table_comments.txt`, 188 entries). They also mark the prefix entries
  (CB / DD / ED / FD = `FF FF FF`, not used), the RST inline word and the &F9 bug.
  - The entries of `xmon_opcodes_00` and `xmon_opcodes_c0` have run (group 1). Those of
    `xmon_opcodes_ed40` are decoded statically only (read: only ED &49) and wait for the ED group.
  - Some entries show as text although the range is classified `byte_data`: the generator
    writes a run of printable bytes ending in a bit-7 byte as a string. Examples: &20 JR NZ,e =
    `"_#","{"+#80` = &5F &23 &FB (in the ROM, scrambled: &7F &03 &DB); &28 JR Z,e; and
    `xmon_index_opcodes` &F624. The bytes are correct (source identical); only the notation is
    odd. cpcxray offers no way to force hex here: a note for the cpcxray developer.
- **Mini test of the base path** (2026-10-26, `output/xmon_l/mini_test.bin`, 38 bytes, expected
  output in `mini_test_expected.txt`, `xmon_rom` = 00): every line as expected.
  - Count mode `L4000` + RETURN: **23 lines** (&4000-&401C), not the 22 that &16 suggests. The
    count is checked after each line and counted down to 0, and the line for 0 is still shown;
    then the end test with end = start stops.
  - Pause: `L4000,7FFF`, SPACE -> stops after 4 lines (waits in `xmon_get_key`), SPACE -> goes
    on, SPACE -> stops, ESC -> `*` prompt (`xmon_list_pause` &FB00).
  - Negative relative jumps (`xlo_back` &F322): `18 FE` -> `JR &4000`, `20 80` at &4004 ->
    `JR NZ,&3F86`, `38 81` at &400A -> `JR C,&3F8D`.
  - D0 D1 D8 D9 E0 E1 (swallowed as inline bytes in group 1): RET NC, POP DE, RET C, EXX,
    RET PO, POP HL.
  - Access map: exactly the 41 predicted bytes became known (&F07C-&F07E, &F322-&F32A,
    &F3E2-&F3E5, the 6 table entries, &FB00-&FB06); nothing known changed, 0 conflicts.
- **CB group** (2026-10-26, `output/xmon_l/cb_test.bin`: CB &00-&FF at &4000-&41FF, built with
  `make_cb_test.py` from `cb_test.asm` via sjasmplus, expected output `cb_test_expected.txt`;
  listed in 11 blocks of 24 lines): all 256 lines as expected. `xll_cb` (&F0D4):
  - length 2; the second byte decides;
  - &00-&2F: rotates, mnemonic &0A + bits 5-3 (RLC RRC RL RR SLA SRA);
  - &30-&37: the undocumented **SLL is shown as `-??-`**, without operands (&F0ED);
  - &38-&3F: SRL (minus 8, then the same formula);
  - &40-&FF: `xll_cb_bits` (&F0F1): BIT / RES / SET = mnemonic &10 + bits 7-6; the bit number
    is operand name &08 + bits 5-3 ("0"-"7"); the register is always bits 2-0.
  - Access map: 82 bytes became known (&F0D4-&F0F9, the mnemonics RLC ... SET &F35E-&F385 and
    `-??-` &F3F2-&F3F5); nothing known changed, 0 conflicts.
- **ED group** (2026-10-26, `output/xmon_l/ed_test.bin`: ED &00-&FF at &4000-&420B, 524 bytes,
  `make_ed_test.py` / `ed_test.asm`, expected output `ed_test_expected.txt` computed from XMON's
  code and compared with the real Z80 before the run; 11 blocks of 24 lines): all 256 lines as
  expected.
  - ED &00-&3F: `-??-` (2 bytes).
  - ED &40-&7B: `xmon_opcodes_ed40`. Every documented instruction as on the Z80 (`IN B,(C)`,
    `LD (&1234),BC`, `IM 0`, `LD A,R`, `RRD` ...). The undocumented duplicates are `-??-` with
    length 2: the NEG / RETN / IM copies, `IN (C)` (&70), `OUT (C),0` (&71), NOP &77, and also
    `LD (nn),HL` / `LD HL,(nn)` at &63 / &6B - on the Z80 these are 4 bytes, so after them XMON
    would list the word as instructions (the test file has no word there).
  - ED &7C-&FF (`xll_ed_high` &F1C5): &A0-&BB with bit 2 = 0 are the 16 block instructions,
    mnemonic &36 + bits 4-3 * 4 + bits 1-0; everything else `-??-`.
  - **ED &8B shows `OTDR`**: a special case `cp #8B` at &F1C5 sets mnemonic &45. ED &8B is no Z80
    instruction (OTDR is ED &BB, which the formula already gives) - a bug; patch proposal in the
    todo (&F1C6 &8B -> &00).
  - Access map: 312 bytes became known (&F1C5-&F1F3, the mnemonics NEG ... OTDR &F3F6-&F44D,
    `xmon_opcodes_ed40` &F64A-&F664 and &F668-&F6FD); nothing known changed, 0 conflicts. All
    mnemonics are now read except the duplicates POP / PUSH at &14 / &15.
  - The generator then wrote the whole mnemonic table as one `defb` of more than 128 bytes,
    which sjasmplus refuses; one comment per entry (`; &nn: NAME`) splits it into lines again
    (note for the cpcxray developer).
- **DD / FD group** (2026-10-26, `output/xmon_l/ddfd_test.bin`, 315 bytes, 95 lines,
  `make_ddfd_test.py` / `ddfd_test.asm`; the expected output comes from a model of XMON's decoder
  built from its own ROM tables): all 95 lines as expected. DD gets the full set, FD a sample (the
  code differs only in the prefix value &65 and the IY names).
  - The C0 table entries of DD / FD are unused (`FF FF FF`): `xll_dd` / `xll_fd` (&F1F8 / &F1F4)
    store the prefix (&64 IX / &65 IY) in `xmon_decoded+4` and the byte after the opcode in
    **`xmon_index_disp` &BEFD** (manual: "Distanz bei relativen Z80 Befehlen"; it is the d of
    (IX+d), relative jumps do not use it).
  - The 38 opcodes of `xmon_index_opcodes` (&F624) are decoded by the **base decoder** (`jp
    xll_opcode`); `xmon_list_operand` turns HL into IX / IY (&F2C2) and (HL) into `(IX+&dd)`
    (&F2A7), `xll_show` adds the prefix and the displacement to the length (&F13D). All 38 as on
    the Z80, e.g. `LD (IX+&05),&12`, `LD IX,(&1234)`, `EX (SP),IX`.
  - DD / FD E9: `JP (IX)` / `JP (IY)` (&F267).
  - DD / FD CB d op (&F20F): rotates, BIT / RES / SET on (IX+d), 4 bytes; all 32 documented ones
    right.
  - **Display weaknesses** (all observed, all as predicted from the code):
    1. an invalid `DD xx` (`DD 00`, `DD 76`, `DD 7C`) is shown as 3 bytes `-??-` - length 2 from
       `xll_ed_store` plus the prefix; one byte too many (on the Z80 the DD is ignored and xx
       runs). Likewise `DD CB d` with an odd op: 3 bytes, the op byte is listed on its own;
    2. `DD CB d 36` (the undocumented SLL) is shown as `SRL` (&F228 turns y = 7 into 6, and 6
       stays 6: both give mnemonic &10);
    3. the undocumented `DD CB d op` with a register (even op, low bits <> 6, e.g. 00 / 02 / 04)
       show as the plain `(IX+d)` form (only bit 0 is checked);
    4. the displacement is shown unsigned: d = -3 -> `(IX+&FD)`.
  - Access map: 215 bytes became known (&F13D-&F151, &F1F4-&F27F, &F2AD-&F2B6, &F2C8-&F2CD,
    `xmon_index_opcodes` &F624-&F649); nothing known changed, 0 conflicts.
- **L is complete.** In &F048-&F6FD only these stay never read: the POP / PUSH duplicates at
  mnemonic &14 / &15 (&F386-&F38D; no table entry and no code path gives &14 / &15) and the four
  unused prefix entries CB / DD / ED / FD of `xmon_opcodes_c0` (&F585, &F5BB, &F5EB, &F61B).
- **Proof that these stay unreachable** (2026-10-26):
  - statically: the mnemonic number in `xmon_decoded+1` is written only by the table paths
    (no table entry holds &14 / &15) and by &F0AE / &F0B2 (&09 / &08), &F0BF (&00-&07), &F0E1
    (&0A-&10), &F0ED / &F1F0 (&2F), &F0F6 / &F23B (&11-&13), &F22D (&0A-&10), &F1E2 (&36-&45),
    &F1C9 (&45), &F26D (&17) - never &14 / &15. `xmon_opcodes_c0` is indexed only at &F1AE,
    after CB / ED / DD / FD have branched off (&F198-&F1A7); the base decoder after DD / FD
    (&F264) only runs for the 38 index opcodes, none of them a prefix.
  - empirically: `output/xmon_l/ddfd_full.bin` (`make_ddfd_full.py`, 3616 bytes, 1278 lines) holds
    every DD xx, FD xx, DD CB d op and FD CB d op, laid out with XMON's own lengths. Together with
    the base, CB and ED tests every possible input has now run through the decoder once. One
    `L4000,4E20` listed it in step (the last screen equals the expected text) and the access map
    did not change by a single byte: &F386-&F38D and the four prefix entries stay never read.

**R — the user registers** (2026-10-26; R runs no user code):
- `xmon_cmd_registers` (&F9A7): `xmon_show_registers` (&F960) prints the names `-AF- -BC- -DE-
  -HL- -IX- -IY- -SP- -XP-` (`xmon_register_names` &F950; XP = the user PC) and the values, then
  CR: the cursor waits at the start of the value line.
- R then edits the values in place, left to right: the 7 pairs `xmon_user_af` ... `xmon_user_sp`
  (&BEEC-&BEF9), then `xmon_user_pc` (&BEFB; the internal byte &BEFA is skipped). Each value goes
  through `xmon_edit_word` (&F9D6 = `xmon_input_word` with the old value as default, then shown
  again and four spaces to the next column) and is **stored at once**.
- Observed: 8 x RETURN changes nothing (new line, `*`); `1234` RETURN, `5678` `,`, `G` (no hex
  digit: beep, ignored - closes the gap &FAAC in `xmon_input_word`), `9ABC` RETURN, ESC at HL:
  AF / BC / DE changed (`34 12 78 56 BC 9A` at &BEEC), HL kept, `*` at once. Afterwards set back
  to 0000. The access map: exactly the 47 predicted bytes became known, 0 conflicts.
- **Bug, confirmed with P:** `xmon_edit_word` calls `xmon_hex_byte_quiet` twice without putting
  the printer switch back (&BEFE -> &BEFF, as `xmon_input_byte` / `_word` do); the second call even
  saves the cleared switch in &BEFE. Observed: P on (&BEFE / &BEFF = 00 01), R, RETURN -> 00 00:
  the printer echo is off for good. Patch proposal (2 bytes, in place): call `xmon_hex_byte`
  instead (todo, "Bugfix proposals").
- New variables: `xmon_user_af`, `_bc`, `_de`, `_hl`, `_ix`, `_iy`, `xmon_user_pc` (manual: "User
  AF" ... "User PC"; `xmon_user_sp` existed).

**P — the printer echo** (2026-10-26): `xmon_cmd_printer` (&F9F0) toggles bit 0 of
`xmon_printer_switch` (&BEFF); it switches on only when MC BUSY PRINTER reports the printer
ready (A is kept by that call, so the other bits stay as they were). Observed: P -> 00 -> 01,
P -> 01 -> 00. With the echo on, `xmon_out_char` (&FADA) also sends each character to the printer,
&09 as a space, and **waits without a time-out while the printer is busy** (&FAEA) - a printer
that goes busy after P hangs XMON. `xmon_hex_byte_quiet` switches the echo off for one value and
keeps the switch in `xmon_printer_saved` (&BEFE). Not observed: P with a busy printer.

**A — a text into memory** (2026-10-26; writes only, to &4000 / &9000):
- `xmon_cmd_ascii` (&FCC5): the address (default and new value: `xmon_fill_address` &BED7, which
  the manual names as F's address - shared), `,`, then `xmon_input_text` (&F001) ->
  `xmon_input_line` (&EE3F; only called from A): at most C = 255 characters into &ACA5, keys in
  upper case (`xmon_get_key`), DEL deletes one (ignored at the start), a full buffer ignores
  further keys, RETURN ends, ESC ends the command. The length goes to `xmon_text_length` (&ACA4);
  an empty text ends the command without writing. The bytes go out through **`xmon_write_byte`**
  (&FB2B, also used by F, S and M).
- Observed: `A4000`, `xYz` DEL `Q` -> &4000 = `58 59 51` ("XYQ"); `A` + RETURN takes the default
  4000, an empty text writes nothing; `AB` + ESC writes nothing; 256 characters -> exactly 255
  written (&4000-&40FE); `A9000`, `Z` -> &9000.
- `xmon_write_byte`: Vortex bank (`xmon_bank`) to port &FBBD, then the gate array value C' with
  bit 5 set and, for &8000 and up, bit 6 too (observed &86 -> &A6 at &4000, &86 -> &E6 at &9000;
  bits 7-6 = 11 is the RAM configuration register), the write, C' back, and the system bank
  from (&001F) to &FBBD. Their meaning with a real Vortex RAM expansion is open; the branch for
  (&001F) <> 0 was simulated 2026-10-26: (&001F) = &01 set by hand (restored to 0), then
  F4000,4000,77 / D4000 / D9000 -> `set 5,a` at &FB5B / &FC14 / &FBCC, A = &21 (bank 1 + bit 5
  "expansion on") to port &FBBD each time; cpcxray ignores the port (no Vortex RAM emulated).
- **Bug (observed):** `xmon_input_line` fills the whole 255-byte buffer &ACA5-&ADA3 with spaces
  before reading, and the text goes there too. XMON's copy of the user's RAM &0080-&0094
  (`xmon_save_low_ram`, at &AD76-&AD8A) lies inside that buffer. After any A the next memory read
  from &8000 on (`xmon_ram_reader`, which puts &AD76.. back to &0080..) writes spaces or text into
  &0080-&0094: observed `A9000,Z`, `D8000,8001` -> &0080-&0094 = 21 spaces; after the long text
  "123456789ABCDEF012345". Under CP/M &0080 is the command line / DMA buffer. Restored by hand
  after the test. Patch proposal (1 byte): A's maximum 255 -> 209 (todo, "Bugfix proposals").

**B — the breakpoints** (2026-10-26; B only stores, it writes nothing into the program):
- `xmon_cmd_breakpoints` (&EEA0) shows `-B1-` ... `-B8-` and the 8 addresses, then edits them in
  place with `xmon_edit_word` like R (RETURN / `,` take a value; ESC ends B at once, the entries
  done so far stay changed).
- `xmon_break_area` (&BF00) holds **8 entries of 3 bytes**: address low, high, and the byte found
  at that address when it was set. G (`xmon_run`) reads that byte again at every start and puts
  it back after the stop, so the value B stores is only a preview - it is never used.
- That byte is read with `ld a,(de)`, as the CPU sees it, **not** through `xmon_read_byte`: X, Y
  and Z do not apply, and an address from &C000 on would read VDOS itself (not tried - it would
  pollute the access map).
- Observed (the area set to 0 first, as `xmon_init` leaves it; before that it still held Y's ROM
  reader, which would have made B4 = &C000): 8 x RETURN -> each entry `00 00 01` (the byte at
  &0000); B1 = 4000, B2 = 4001 `,`, ESC at B3 -> `00 40 30` / `01 40 31`, B3-B8 kept; then set
  back. 97 bytes became known, 0 conflicts. As in R, the printer echo is switched off by
  `xmon_edit_word` (the same bug).

**C — search memory** (2026-10-26, Y = 00):
- `xmon_cmd_search` (&FCE7): `C addr,len` - the sequence address (default &ACA5, A's text buffer,
  so a text just written with A can be searched at once), `,`, the length through
  `xmon_input_byte_0` (&FA44: `xor a`, then `xmon_input_byte` - default 00; length 0 ends at once).
- It searches **all of memory &0000-&FFFF**, whatever the sequence address; every byte goes
  through `xmon_read_byte` (`xmon_search_byte` &FD44), so X, Y and Z apply. From &C000 on it reads
  the ROM of Y: **with Y = 5 it would read all of VDOS as data** - for the analysis Y must be 00 or
  &FF (Y = 00: the BASIC ROM, observed hits at &D769 ... &FEA0). With the sequence at &8000 or above
  each compare goes through the RAM reader at &0080, which puts &0080-&0094 back from &AD76 every
  time (clean here, &AD76 had been set back after the A test).
- Hits are printed 10 per line; a key pauses (ESC while listing only pauses, ESC in the pause
  ends), like D and L.
- Observed: `C4000,02` with A5 5A at &4000 / &5000 / &6000 and A5 00 at &4010 -> `4000 5000 6000`;
  `C4000,00` -> nothing; `C8000,01` (A5) -> 30 hits in 3 lines; `C8001,01` (00) with SPACE / SPACE /
  ESC. 118 bytes became known, nothing known changed, 0 conflicts.
- Read, not tried: the end test comes before the compare once HL has wrapped, so a hit at &FFFF is
  never reported.

**F — fill memory** (2026-10-26, only &4000-&403F):
- `xmon_cmd_fill` (&EF74) -> `xmon_fill_range` (&EF7D, also called by the disc monitor at &ED0C):
  start (default `xmon_fill_address`, **stored at once**), `,`, end (default = start), `,`, value
  (`xmon_input_byte_0`, default 00); then `xmon_write_byte` from start to end **inclusive**. The
  loop writes first and compares after, so an end below the start writes exactly one byte.
- `xmon_fill_address` (&BED7) is one default for **both A and F** (observed: after `A9000` F
  offered 9000).
- Observed: `F4000,400F,AA` -> &4000-&400F = AA, &4010 kept; `F4020,4010,BB` -> only &4020;
  `F` + 3 x RETURN -> `F4020,4020,00`; `F4030` + ESC at the end -> nothing written, &BED7 = &4030.
  48 bytes became known, 0 conflicts.
- Writes and cpcxray: a CPU write always goes to RAM, also under a paged-in ROM
  (`machine/memory.py`, FR-MCH-06), and writes are not part of the access map - so F / A / S / M
  can never change a ROM image or the map; only reads of ROM 5 are a risk.

**G — run a program** (2026-10-26; own test program at &4000: `3E 12 / 01 56 34 / 00 / F7`):
- `xmon_cmd_go` (&EFA2): the start address (default `xmon_user_pc`) becomes the user PC, its byte
  goes to `xmon_run_byte` (&BEEB), then `jp xmon_run` with DE = &EDA1 - the return address left
  by `xmon_find_command`, negative, used as "stop at the first breakpoint".
- **`xmon_run`** (&F879, shared with T): trace count -> `xmon_trace_count` (&BEE9), start ->
  `xmon_run_address` (&BEE7); for each of the 8 breakpoints the byte at its address is kept again
  (so B's saved byte is refreshed) and **RST 6 (&F7)** is written there - except at the start
  address. Unused entries (0000) all write &F7 to &0000 while the program runs (observed; put back
  afterwards). &0030 = `PUSH IY / RST 3 / DEFW &BED0`. XMON's SP -> `xmon_run_sp` (&BEE5), SP =
  user SP, `xmon_user_jump` (&BEFA) = `JP` + user PC, the user registers are loaded and a `RET`
  enters the program. Breakpoint bytes are read and written directly - an address from &C000 on
  would read VDOS (not tried).
- **`xmon_breakpoint`** (&F8D9): RST 6 -> &0030 -> FAR CALL to ROM 5. It keeps HL DE BC AF IX,
  puts the breakpoint bytes back **last entry first** (so &0000 gets its first saved byte back),
  puts `xmon_run_byte` back at `xmon_run_address`, drops the FAR CALL frame (observed on the stack:
  `B9FC 0000 0586 0035`, then the IY from &0030, then the RST return address), keeps IY, PC
  (return address - 1) and SP, returns to XMON's stack and shows the registers. Then the trace
  count is counted down: negative -> `*` prompt (G); else the next T step (&F947, open).
- Observed: B1 = 4005, `G4000` -> stop at 4005 with `1200 3456 0000 0000 0000 0000 BF80 4005`
  (&4005 = F7 and &0000 = F7 while running, both put back; stack frame as above); B1 = 0,
  `G4000` -> stop at the program's own RST 6, XP = 4006 (the PC points at the F7 itself: a second
  G with the default would run it again); B1 = 4005, `G4005` -> no breakpoint at the start, stop
  at 4006. 220 bytes became known, 0 conflicts.
- Before G / B: clear &BF00-&BF17 if Y ran - Y's ROM reader left B4 = &C000 again, and `xmon_run`
  would read VDOS's byte there.

**T — single step** (2026-10-26; own programs at &4000-&40F2, Y = 00):
- `xmon_cmd_trace` (&F7A4, never run before, decoded from the raw bytes): start (default user PC),
  RETURN = 1 step, `,` = count (default 1), DE = count - 1. Each step (`xtr_step` &F7BC) clears the
  trace flags (&BEFF bits 7-5), lists the instruction with `xmon_list_line` and decides by its
  mnemonic where to put RST 6:
  | instruction | breakpoints |
  |---|---|
  | JP / JR / DJNZ / CALL | the target (`xmon_branch_target`; JP (HL) / (IX) / (IY): the user register) and the next instruction; trace flag bit 7 |
  | RET, RET cc | none: XMON does the RET itself (`xtr_ret`: PC = (SP), SP + 2) |
  | RST &08 / &28 | the word on the user stack (where the routine returns to) |
  | RST &10 / &18 | only the word on the user stack |
  | RST &00 / &20 / &30 / &38 | none: done like a RET |
  | anything else | the next instruction |
  then `xmon_run`; `xmon_breakpoint` puts the target byte back (`xmon_branch_byte` &BEE2, when bit 7
  is set), shows the registers, counts down and - key = pause, ESC in the pause = end - goes on.
- Observed and correct: LD, DJNZ backwards, JR, CALL, JP (HL) / (IX) / (IY), RET (15 steps from
  &4000, every register as expected); RST &08 (LOW JUMP to the RET at &000F) and RST &28 (FIRM
  JUMP to the ROM's RET at &000F) step over to the caller; key pause / ESC.
- **Bugs and weaknesses (all observed):**
  1. **RET cc is always taken**: `RET NZ` with Z = 1 "returned" (XP &40E3 instead of &40F2).
  2. **After a done RET the trace runs away**: `xtr_ret` jumps to &F931, behind the loads of HL / DE
     in `xmon_breakpoint`; the return address becomes the step count (&BEE9 = &400C) and HL = the
     user SP the next address to list ("BF80 NOP"). The next "step" put its breakpoint at &BF81
     and started the program at its PC - which ran into `JR $` and never came back (XMON was
     recovered by writing F7 into the loop and ESC in the pause). Patch proposal (1 byte): jump to
     &F92A instead.
  3. **RST &00 / &20 / &30 / &38 are done like a RET** (observed with &F7: it popped &0000).
  4. **RST &08 / &28: unbalanced stack**: the branch at &F804 jumps to `xtr_target_hl` without the
     `PUSH HL` of the other branch, so `POP HL` at &F86F takes a word from XMON's stack (observed
     &0044) as the "next" address; F7 is written there (put back after the stop) and XMON's SP
     moves by 2. The next-instruction breakpoint is lost, harmless here because the routine
     returns to the stack address.
  5. **A jump to itself never runs** (`DJNZ $`): the target breakpoint is the PC itself.
  6. **After RST &10 / &18 the program runs on to the caller** of the current routine (FAR CALL
     at &4044: stop at &4093, the RET at &4047 ran unstepped).
- All bytes XMON put into the program were found back afterwards (&0000, &0044, &BF81, &4063 ...).
  T reads branch targets through `xmon_read_byte` (Y applies), the breakpoints of B directly.
- 231 bytes became known, nothing known changed, 0 conflicts; T and the shared code are complete.

**M — move memory** (2026-10-26; data `11 22 33 44 55 66 77` at &4000; never run before - read
with the offline code view `output/tools/xdis.py`: raw opcodes, decoded operands):
- `xmon_cmd_move` (&F745): start (default 0000), `,`, end (default = start), `,`, target (default
  = end); reads through `xmon_read_byte` (Y applies), writes through `xmon_write_byte`.
- Target above the end, or at / below the start: copy upwards (`xcm_forward`); start < target <=
  end: copy downwards from the end (`xcm_backward`).
- Observed: `M4000,4006,5000` -> copy; `M4002,4006,4000` -> `33 44 55 66 77 66 77` (overlap
  downwards, right); `M4000,4003,4002` -> `11 22 33 11 22 33 44` - **bug**: the downward copy starts
  at target + length instead of target + length - 1 (`INC BC` before the `ADD`), so the copy lands
  one byte too high (right: `11 22 11 22 33 44 77`); `M` + 3 x RETURN -> `M0000,0000,0000`.
- Patch proposal without new space: reorder the one-byte instructions &F78E-&F792
  (`03 E1 EB 09 EB` -> `E1 EB 09 EB 03`, the same bytes in the ROM file, opcodes are not scrambled).
- Read, not tried: an end below the start gives a length of nearly 64K and overwrites all memory.
- 97 bytes became known, 0 conflicts.

**S — change memory** (2026-10-26; `41 05 9A 11` at &4000):
- `xmon_cmd_substitute` (&F70B): start (default `xmon_subst_address` &BED3), then one line per
  address: the address, the byte as a character (a space below &20 and from &80), the byte in
  hex, and `xmon_input_byte` with the old value as default. RETURN writes the value - **always**,
  through `xmon_write_byte`, also when unchanged - and goes on; ESC ends S. The current address is
  stored at the start of each line.
- Observed: `4000  A  41  41` RETURN, `4001     05` + `55`, `4002     9A` + `7` (-> A7), `4003     11`
  ESC -> `41 55 A7 11`, &BED3 = &4003. 60 bytes became known, 0 conflicts.
- Manual corrections: the line has a character column the manual does not show; &BED3 is S's
  address, not M's as the manual's table says (M starts at a fixed 0000).

**I — load a binary file** (2026-10-26; disc only, the images unchanged):
- `xmon_cmd_input` (&EFB5): not under CP/M; the name through `xmon_input_filename` (&EFFC: HL
  kept in `xmon_run_address` as scratch, at most 16 characters, empty = end), then CAS IN OPEN
  (VDOS; after `|CAS.IN` the tape - manual), CAS IN DIRECT to the file's own load address,
  `xmon_show_file_info` (&EFE0, also used by the CP/M start at &ED39) prints `(load length entry)`,
  CAS IN CLOSE and then CAS IN ABANDON as well; back to the prompt at &ED78.
- The 2K buffer passed to CAS IN OPEN is DE = &EFBE - the return address `xmon_input_text` leaves
  in DE, not a real buffer (RAM under the ROM: the screen).
- Observed: `I` + RETURN -> `*`; `INIX.BIN` -> `NIX     .BIN wurde nicht gefunden`;
  `IB:F1Z.BIN` -> `(BF00  0050  0000)`, &BF00-&BF4F = the file; `IB:READ.ME` (no AMSDOS header) ->
  `(EFBE  0000  0000)` and **nothing loaded**: for a file without header VDOS sets the load address
  to the buffer and the length to 0, and `vdos_cas_in_direct` takes only the low 16 bits of its
  byte count (&800000) - 0 records. I cannot load files without header.
- Not observed: a load error (`jr nc` at &EFCB), the tape, the CP/M branch. 78 bytes became known,
  0 conflicts.
- Note: F1Z.BIN loads to &BF00 - inside XMON's own RAM area &BE00-&BFFF. After this test the owner
  ruled that XMON tests stay out of &BE00-&BFFF; the load test at &4000 was done with a file saved
  by O (below).

**O — save a binary file** (2026-10-26; on the disc copy `output/xmon_o_test.dsk` in B:, never
saved; test data only at &4000):
- `xmon_cmd_output` (&F011): not under CP/M; the name through `xmon_input_filename`, CAS OUT OPEN
  (VDOS: the file appears as `name.$$$`), then three `xmon_input_word` values - address, length,
  entry - each offering the previous value as its default (first HL from CAS OUT OPEN = &A7B8, the
  header buffer; then the start; then the length). CAS OUT DIRECT with A = 2 (binary), CAS OUT
  CLOSE (`.$$$` -> the real name), back through `xmon_file_done` (&EFD7, shared with I) to the
  prompt. Errors go to `xco_abandon` (&F043: CAS OUT ABANDON) without a message.
- The 2K buffer passed to CAS OUT OPEN is DE = &F01A, again a leftover return address (whether
  VDOS uses it was not checked).
- Observed round trip: `OB:XT.BIN,4000,0032,4000` -> header type 2, load &4000, length &0032,
  entry &4000, then the 50 bytes; `F4000,4031,00`; `IB:XT.BIN` -> `(4000  0032  4000)` and the 50
  bytes back, &4032 on untouched. (Header bytes from offset &45 hold an old buffer's text - unused.)
- **Bug (observed):** ESC in an input of O jumps from `xmon_input_word` straight to
  `xmon_command_done`; the output file stays open. `OB:XE.BIN` + ESC left `XE.$$$` (0 bytes) in the
  directory; the next `OB:XF.BIN` failed silently at once (CAS OUT OPEN: file already open), its
  `xco_abandon` freed the channel; a third `OB:XF.BIN,4000,0032,4000` wrote XF.BIN correctly.
  `XE.$$$` stays on the disc (ABANDON does not delete the entry). Only ESC in the address input
  was tried; length / entry use the same routine (read). Bugfix proposal: todo 3.
- Not observed: a write error (`jr nc` at &F03C), the tape, the CP/M branch. 57 bytes became
  known (I/O &EFB5-&F047 now completely read), 0 conflicts.

**@ — the disc monitor, entry and key loop** (2026-10-26, from BASIC, B: = the Vortex disc copy,
nothing written):
- `xmon_disc_monitor` (&EA9E): `flush_host_buffer`, &BE04 = &FF (XPB cache invalid), **&BE00 =
  &FF** (so `xmon_command_done` returns to `xdm_status_prompt` &EABB instead of `*`),
  `bios_set_message` &FF (messages off; the old value and `sek_drive` go on the stack), SP kept in
  **&BE09** (`bdos_dph`, borrowed). Then `xdm_select_drive` (&EBA2): SELDSK of `sek_drive`, the
  DPB part of the XPB to &BE15, T = `dpb_off`, S = 0, B = `dma_address` = host buffer - &80; it
  ends with a jump into the status line / prompt and never returns - so `call &EB27` at &EAB8
  is **dead code** (no reference found; probably the start-up sector read of 2.0).
- Status line (`xdm_status_line` &EBED): `L:01  T:02  S:00  B:A8BA  G:00`. **Differs from the
  manual (2.0, `L:00 T:00 S:41 B:A93E`):** S is the 128-byte record of the track (`sek_record`,
  from 0), B the DMA address (a record buffer &80 below the host buffer &A93A), and **G** is new:
  the CP/M block ((T - OFF) * SPT + S) >> BSH (`xdm_block_number` &EC3E), shown only from the
  first data track on. L / T / S / B come from `sek_drive` / `sek_track` / `sek_record` /
  `dma_address` - the status line does not use the manual's &BEC1-&BEC5.
- Key loop `xdm_key` (&EAC3): SP from &BE09, ESC -> `xdm_exit`, keys below 'A' ignored ('1'
  observed), others echoed and looked up in `xmon_disc_command_table` (&EAFD, 12 entries:
  L T S B R W D C A F P G - **F and G are not in the manual**, P is the main monitor's
  `xmon_cmd_printer`); an unknown letter ('Z' observed) is erased again with &08 / &10.
- `xdm_exit` (&EAE7): `flush_host_buffer`, `sek_drive` and `messages_off` restored, &BE00 = 0,
  &BE04 = &FF, `*` (observed). &BE09 keeps &BFF0 - `bdos_dph` is not restored (harmless under
  BASIC; under CP/M not checked).
- 279 bytes became known by the start alone (|XMON 680 -> 401 never read), 0 conflicts.

**@ — the 12 disc monitor commands** (2026-10-26, from BASIC; buffer set to &4000 first; W only on
the B: copy, in memory, the original record written back; A: untouched; a snapshot after each):

| Key | Routine | Observed |
|---|---|---|
| B | `xdm_cmd_buffer` &EB91 | B4000 -> `B:4000`; ESC in the input -> status line, `>` (through `xmon_command_done`, &BE00 = &FF) |
| R | `xdm_cmd_read` &EC97 / `xdm_read_record` &EB27 | T2 S0 of B: -> the first directory record at &4000; first `deblock_flags` bit 6 cleared, so the sector is really read again |
| D | `xdm_cmd_dump` &EC9D | D + RETURN: 128 bytes; D,12: S+1, status line, R, dump per record; key pauses, ESC ends; from S23 on to T:03 S:00. Dead code: `jp` at &ECFA (DJNZ always jumps) |
| S | `xdm_cmd_record` &EB7E | S23 ok (`G:01`); S24 (= SPT) -> `>>`, S unchanged |
| T | `xdm_cmd_track` &EB5F / `xdm_check_block` &EB6E | T00 (reserved: no G), T05 (`G:03`), TA0 -> `>>` **but T:A0 stays set (bug)** |
| L | `xdm_cmd_drive` &EB9C | L00 (A:), L05 -> `>>` (sek_drive kept), L01; L resets T, S and B (B back to &A8BA) |
| G | `xdm_cmd_block` &EC66 (not in the manual) | G03 -> T:04 S:18; GB1 -> `>>` **but T:9F S:0C stay (same bug)**; byte input: blocks 0-255 only |
| C | `xdm_cmd_change` &ECFD -> `xmon_cmd_substitute` &F70E | 4001 &50 -> &51, ESC; leaves `xmon_subst_address` at &4002 |
| A | `xdm_cmd_text` &ED03 -> `xmon_cmd_ascii` &FCC8 | A4000,VDOS; the main A's bug too (&AD76-&AD8A = spaces, restored by hand) |
| F | `xdm_cmd_fill` &ED09 -> `xmon_fill_range` (not in the manual) | F4000,407F,E5 |
| P | `xmon_cmd_printer` &F9F0 (the main P) | &BEFF 0 -> 1 -> 0 |
| W | `xdm_cmd_write` &EB3D | write type 1 (immediate): GB0 (T:9E S:10, free, E5), F 5A, W, F 00, R -> 5A; E5 written back and checked |

- Errors: `>>` = `xdm_error` &EBDA (status line with the old values, then `>>`); disc errors =
  `xdm_disc_error` &EB4F: **`E:xx`** in hex (manual: `ERR:xx`) - observed `E:45` (FDC bits 6, 2, 0:
  sector / ID not found) for R on track &A0 (reached through the T bug).
- **Bug:** T (&EB65) and G (&EC8C) store the new position before `xdm_check_block`; after `>>` the
  invalid position stays and R / W use it (the manual says nothing is changed). Bugfix proposal:
  todo 3.
- &ED12-&ED1F: 14 bytes, raw 00, no reference found - most likely free space (todo 3). Run on
  purpose (owner's request: PC = &ED12, breakpoint at &ED20): 14 NOPs, registers unchanged; now M1
  and shown as `nop` in the source.
- Never read in &EA9E-&ED1F now: the dead call &EAB8, the CP/M branches &EB31 / &EB44 / &EBA8
  (XMON under CP/M - last), and the dead `jp` &ECFA.

Research (`research/vdos211x.asm`), checked:

- **Confirmed:**
  - `check_vdos_mode` (named `xmon_cpm_mode`), `backup_low_mem` (the copy itself),
    `xmon_setup_RST6` (a general FAR CALL builder: `xmon_set_far_jump`), `restore_SP` /
    `xmon_mainloop` (`xmon_command_loop`);
  - the variables UPPER_ROM_NUMBER &BEC8, FAR_ADDRESS_FOR_BREAKPOINT &BED0,
    STACKPOINTER_SAVE &BEDE.
- **Corrected:**
  - &ED21 does not load a variable, it writes 0 to &BE00;
  - &F8D9 is not a "menu pointer" but the RST 6 target.
- **Manual ("Variablen des Diskettenmonitors" / "Variablen des Monitors", &BEC1-&BF80):**
  agrees with what the start sets:
  - &BEC8 ROM number (Y), &BEC9 X switch 0 / &FF, &BED0 far address for the breakpoint;
  - &BEDD CP/M flag 0 = VDOS / &FF = CP/M, &BEDE SP at entry, &BEF8 user SP;
  - &BF00 the 24-byte breakpoint work area, &BF80 the monitor stack.

  As variables now: `xmon_rom`, `xmon_firmware_rom`, `xmon_break_far`, `xmon_cpm_flag`,
  `xmon_saved_sp`, `xmon_user_sp`, `xmon_break_area`. The rest of the tables (disc monitor
  &BEC1-&BEC7, the command addresses &BED3-&BED9, the user registers) waits until the
  commands have run. &BE00 is not in the manual's tables.
- **&BE77:** the write breakpoint was not set during this start (lost with the GUI restart).
  Afterwards &BE77 was still 0, so the start left nothing there. Set again for the command tests.
- **Now answered:**
  - why &0080-&0094 is saved: XMON puts its 21-byte RAM reader there (`xmon_ram_reader`, from
    &FCB0) and restores the RAM afterwards;
  - the ESC exit from BASIC: observed (`pop af`, TXT RESET, `xmon_exit_basic`, "Ready"). The
    RST 0 under CP/M is read only.
- **Not checked yet:** who sets the CP/M flag &BEDD to &FF; the use of the user registers.

---

## 4. Layer 2 — DOS (BASIC environment)

### 4.1 Workspace and file headers

`IY` = VDOS workspace (&A700, AMSDOS's data area). Fields used by the CAS layer:

| IY+ | Content |
|---|---|
| &05 / &06 | current user / default drive |
| &14 | saved FCB drive byte |
| &21 | BDOS return code |
| &23/&24 | SP for the error exit |
| &25 | name FCB (32 bytes: drive, name, extension; from `parse_filename`) |
| &45 / &69 | input FCB / output FCB (36-byte CP/M FCBs; byte 0 = &FF means closed) |
| &8D / &B3 | input header / output header (IX) |
| &E0 | 128-byte record buffer |

A **header** (IX) has this layout:

| IX+ | Content |
|---|---|
| &00 | access mode: 0/&FF none yet, 1 = char, 2 = direct |
| &01 | 2K buffer address |
| &03 | pointer to the next character in the buffer |
| &05 | the AMSDOS-style header that CAS IN/OUT OPEN return in HL: user, name and extension (&06), file type (&17), bytes in the buffer (&18), load address (&1A), first block flag &FF (&1C), length (&1D), entry address (&1F) |
| &21-&23 | 24-bit byte count (input: bytes left; output: bytes written) |

### 4.2 Reading — **observed**

- **`vdos_cas_in_open`** parses the name. Without an extension it tries no extension, then
  `.BAS`, `.BIN` and **`.BAK`**, in this order: `LOAD "XYZ"` gave four searches (AMSDOS tries
  three). It reads record 0 and takes it as the AMSDOS header if the checksum over &43 bytes
  matches. Otherwise the file has no header and the record is read again as data.
- **`vdos_cas_in_char`** reads through the 2K buffer (`in_char_get`, refilled with up to 16
  records).
- **`vdos_cas_in_direct`** reads full records straight to memory and the last part record
  through the record buffer.
- **`vdos_cas_test_eof`** reads a character and puts it back.
- **Protected files** (type bit 0) are decoded with `crypt_record`. It XORs with the `|CODE`
  string &BE79/&BE7A or a ROM table (**read**, not run).
- **End of file — `eof_test_1a` (&BE7C):** with 0 only the physical end of the file counts;
  with &FF, &1A (CP/M end of file) also ends it. `|DERROR,3` sets 0, which is also the default
  after a reset. `|DERROR,2` sets &FF.
  - The manual appendix "Das EOF Problem" gives the reason. BASIC reads ASCII files *and* BASIC
    programs (MERGE) through CAS IN CHAR. A byte &1A inside a program (e.g. line number 26)
    stops MERGE with "EOF met"; that is AMSDOS's MERGE bug. Without the test, an ASCII file
    returns the &1A padding of its last record.
  - **Observed:** the 2-line file TD gave 117 extra characters with 0, and stopped at &1A with
    &FF (set by POKE).
  - AMSDOS always tests &1A (firmware manual, CAS TEST EOF).
  - The RAM table of the 2.0 manual ("0 = teste EOF Marker") has the meaning backwards. The
    appendix and the code agree with each other.
  - Under CP/M the same byte is the FAST flag (`fast_flag`, toggled by `bios_select_format`
    with A = &FE).

### 4.3 Writing — **observed**

- **`vdos_cas_out_open`** writes to `<name>.$$$`.
- **`out_flush_buffer`** writes a place holder record for the header before the first data (not
  for ASCII files), full records straight, and a part record padded with &1A.
- **`vdos_cas_out_close`** writes the rest of the buffer and closes the file. A name without an
  extension gets `.BAS` or `.BIN` by type. For non-ASCII files `out_write_header` writes the
  header as record 0 (24-bit length at +&40, checksum at +&43). Then `out_rename` renames .$$$
  to the name; an existing file first becomes `.BAK` (**read**: that path was not run).
- **`vdos_cas_out_abandon`** writes nothing; the .$$$ file stays.

### 4.4 Catalog (CAT and `|DIR`) — **observed**

`vdos_cas_catalog` and `rsx_dir` share the start (`dir_start`) and the end (`dir_print_free`):

- `dir_start` prints "Laufwerk X: User n" and works out the number of columns from the window
  width.
- The entries are collected sorted by user, name and extension, as 14-byte table entries
  (`dir_insert_sorted`). Of a file with several extents only the last one is kept. SYS files are
  left out.
- The listing is printed in columns as `NAME    .EXT   nK`, with `#` after read-only files.
- `dir_next_line` pauses after 22 lines; ESC there ends the listing (**read**).
- The last line reads e.g. "119K in  26 Files,  50K frei". The free space is counted from the
  allocation vector of the BDOS copy of the drive's DPB (&BE0D-&BE23). The single fields are
  read from the code and not yet checked one by one.

### 4.5 Internal BDOS

The file functions under the CAS layer are **Vortex's implementation of the CP/M 2.2 BDOS file
functions in the ROM**: they follow Digital Research's BDOS routine by routine (same algorithms,
FCB / directory / allocation vector structures and calls), with a few VDOS changes (&DDF6-&E785, group `bdos`). Observed for every command of 4.5a.

**Call layer.** `bdos_call_name` / `_in` / `_out` / `_fcb` / `_again` (&DDF6-&E00A) store the
FCB address in `bdos_fcb` (&BE24), clear the return code (iy+&21) and call the function body
with `bdos_return` as its return address. The wrappers are `open_file`, `close_file`,
`make_file`, `delete_file`, `rename_file`, `search_first` / `search_next`, `read_record_in` and
`write_record_out`.

**The DR routines** (DR's name in brackets):

| Address | Routine |
|---|---|
| &DE23 | `bdos_select_fcb_drive` (`reselect`/`selectdisk`): SELDSK, copy DPH addresses and the DPB to &BE09-&BE23 |
| &DE62 | `login_drive` (`initialize`): on the first select of a drive (login byte IY+drive = 0), clear the ALV, mark the directory blocks, read the whole directory and mark every used entry's blocks (`scan_disk_map`) |
| &E211 / &E227 / &E23B / &E251 | search first / next / `search` / `search_next_entry`: compare 12 or 15 bytes, `?` matches, the extent compared under EXM, bit 7 (attributes) ignored |
| &E367 / &E3B4 / &E433 / &E2E6 / &E1E5 | open / close (disk map merge) / make / delete / rename bodies |
| &E46A | `open_next_extent` (`open_reel`) |
| &E4BB / &E4FA | read / write sequential, with `index_block`, `block_to_record`, `get_block` (free block next to the previous one), `seek_record` (record → track = record / SPT + OFF, sector via SECTRAN) |
| &E680 | `read_dir`: next directory entry, read the record, directory checksum (CSV) |
| &E5B2-&E67D | random read/write (`rseek`): read only, probably used by the relative files |

**VDOS changes against DR's BDOS:**

1. **Disc full.** When `get_block` finds no free block, write sequential jumps straight to
   `error_disc_full` (DR returns code 2). The blocks already taken by the extent stay used in
   the ALV, but no directory entry holds them. Only a login rebuilds the ALV. Observed in 4.5a.
2. **Disc change.** A directory checksum that differs means the disc was changed. If a file is
   open on that drive, VDOS closes it with "Laufwerk A: Diskette wurde gewechselt" / "\<name\>
   wurde geschlossen" (`error_disc_changed` &DF17). Otherwise it logs the drive in again
   (`login_drive`), which also rebuilds the allocation vector. Both cases observed (4.5b).
3. **Errors.** Read-only files and disc errors end the CAS call through VDOS's error exits.

**File name parser** (VDOS's own, &DF46-&E02F):

- It parses `[d:]name[.ext]` into the name FCB: upper case, `*` becomes `?`, the delimiters are
  in `delimiter_table` (&E030).
- The character before `:` must be a drive letter A-P, so `1:NAME` gives "Eingabefehler".
- A name longer than 8 characters is cut.
- Without an extension, the extension bytes are set to &FF.

**&BE24-&BE2D has two uses:** the boot hook borrows it (`km_disarm_break_*`, group `vdos`), and
then it is the BDOS's data area (`bdos_fcb`, `dir_count`, `actual_record`, `bdos_dma`,
`virtual_record`, `record_count`, group `bdos`). The context `rom5:DDF6-E785` → `bdos` gives
each code its own names.

The BDOS reaches the disc through the **DOS indirections** at &BE8F (RAM, copied from &C105):

| Indirection | Target |
|---|---|
| `dos_seldsk` | &C7D5 |
| `dos_settrk` | `bios_settrk` |
| `dos_setsec` | `bios_setsec` |
| `dos_setdma` | `bios_setdma` |
| `dos_read` | &C89A |
| `dos_write` | &C8AA |

These are the same routines the CP/M BIOS uses (see 6.3): VDOS's DOS and CP/M share one disc
BIOS.

### 4.5a The BASIC disc commands, walked through — **observed** (2026-10-25)

Every BASIC disc command was run in the emulator, with a trace of the CAS jump table. Before
each command BASIC calls IN ABANDON and OUT ABANDON. Call counts in the trace can be too high,
because an interrupt at the traced instruction records it twice.

| BASIC | CAS functions | Result on disc / screen |
|---|---|---|
| `SAVE "TB"` | OUT OPEN, OUT DIRECT, OUT CLOSE | `TB.BAS` (header + data) |
| `SAVE "TA",A` | OUT OPEN, OUT CHAR …, OUT CLOSE | `TA.`, no extension, no header |
| `SAVE "TP",P` | OUT OPEN, OUT DIRECT, OUT CLOSE | `TP.BAS`, protected (`crypt_record` runs) |
| `SAVE "TBIN",B,&4000,&100[,entry]` | OUT OPEN, OUT DIRECT, OUT CLOSE | `TBIN.BIN` |
| `SAVE "TB"` again / a third time | as above | old file → `TB.BAK`; an older `.BAK` is deleted |
| `CAT` | CATALOG | sorted, 2 columns in MODE 1; page pause after 22 rows (MODE 0) |
| `LOAD "TB"`, `LOAD "TB.BAK"`, `LOAD "tb"` | IN OPEN, IN DIRECT, IN CLOSE | program back; lowercase is fine |
| `LOAD "TA"` (ASCII), `MERGE`, `CHAIN MERGE` | IN OPEN, IN CHAR … | program back / merged |
| `LOAD "TBIN"[,&5000]` | IN OPEN, IN DIRECT, IN CLOSE | needs `MEMORY &3FFF` first (BASIC: "Memory full") |
| `RUN "TB"`, `CHAIN "TB"` | IN OPEN, IN DIRECT, IN CLOSE, OUT CLOSE | runs |
| `RUN "TBIN2"` | IN OPEN, IN DIRECT, IN CLOSE | runs the code (here RET: machine restarts) |
| `OPENOUT`, `PRINT #9`, `WRITE #9`, `CLOSEOUT` | OUT OPEN, OUT CHAR …, OUT CLOSE | ASCII file |
| `OPENIN`, `INPUT #9`, `LINE INPUT #9`, `EOF`, `CLOSEIN` | IN OPEN, IN CHAR …, TEST EOF, IN CLOSE | see `eof_test_1a` (4.2) |
| `NEW` with a file open | IN ABANDON, OUT ABANDON | an output `.$$$` file stays (0 bytes) |
| 30K ASCII file (800 lines) | OUT CHAR / IN CHAR | 2 extents, 2K buffer refills; all lines back |
| 10K binary file | OUT DIRECT / IN DIRECT | back at another address |
| `LOAD "B:TB"`, `SAVE "B:TB"` | as above | drive B works |

Errors:

| Command | Message (VDOS) | Then BASIC |
|---|---|---|
| `LOAD "NOFILE"`, `OPENIN "NOFILE"` | `NOFILE  .    wurde nicht gefunden` | `Break` |
| `LOAD "A*B"`, `LOAD ""` | `Eingabefehler` | `Break` |
| `LOAD "TOOLONGNAME"` | cut to 8 characters → `TOOLONGN` not found | `Break` |
| `SAVE "1:TU"` | `Eingabefehler`: **no user number in names** (AMSDOS allows `10:NAME`; VDOS sets the user with `\|SELECT` only) | `Break` |
| second `OPENOUT` | error &0E | `File already open` |
| `SAVE` of 20K with 14K free | `Laufwerk A: Diskette voll`; `.$$$` stays | `Break` |

After "disc full", a smaller SAVE that fits failed again with "Diskette voll". After a reset it
worked. So the blocks already given to the failed file stay marked as used in VDOS's RAM until
the drive is logged in again, as in CP/M before a warm boot. This was observed; the mechanism is
inferred.

### 4.5b Error situations and the turnkey start — **observed** (2026-10-25)

Each test was run in the emulator and annotated straight away:

| Test | What happened | Code path |
|---|---|---|
| HELLO autostart | `SAVE "HELLO"`, reset: "HELLO STARTED" without any input | `hello_loader` → FAR CALL BASIC 1.0 &E9CF, the `RUN "file"` routine (opens the file; binary → MC BOOT PROGRAM, BASIC → load and run); RUN does not return |
| No disc (CAT, drive A empty) | `Laufwerk A: Diskette fehlt - Wiederholen J/N ?` | `seek_wait` → `fdc_result_check`: ST0 not ready + seek end → message &07 → `disc_error_dialog` |
| … answer J after inserting the disc | CAT goes on and lists the directory | NZ back to `seek_track`, which seeks again at once without counting a try |
| … answer N | BASIC shows only `Ready` | fatal: `disc_end` CY = 0 → `host_read_write` → `read_buffer` → `error_disc_status` (&DEF5) → `cas_error_exit` |
| Write protected (SAVE) | `Laufwerk A: Diskette hat Schreibschutz - Wiederholen J/N ?` | `fdc_rw_result`: ST1 bit 1 → message &08. The first write refused is the directory write of `make_body` (OUT OPEN creating TW.$$$). J after making the disc writable: retried at once, SAVE completed (TW.BAS) |
| Disc changed, no file open (CAT) | the new disc is listed (`0K in 0 Files, 169K frei`) | `read_dir`: checksum differs → `rdc_relog` → `login_drive` |
| Disc changed, input file open (`OPENOUT` after `OPENIN "TCH"`) | `Laufwerk A: Diskette wurde gewechselt` / `TCH . wurde geschlossen` / `Break` | `read_dir` → `rdc_close` → `error_disc_changed`: file closed, drive logged out. The next `LINE INPUT #9` gets &0E, which BASIC shows as `EOF met` |
| Directory full (`SAVE` F1 … F70 in a loop, blank 64-entry disc) | `Laufwerk A: Directory voll`, `Break in 40` at F65 | OUT OPEN → `make_file` finds no empty entry → `error_dir_full` → `error_with_drive` (drive from the output FCB). No `.$$$` is left |
| ESC in the page pause (CAT of 64 files in MODE 0) | listing stops, space line at once: ` 64K in  64 Files, 105K frei` | `dir_next_line`: KM WAIT CHAR = &FC → `pop af`, `jp dir_print_free` |
| Free space on a completely full disc (4 × 40K + a failing 5th) | CAT: `167K in 5 Files, 2K frei`. Correct is 169K / 0K: the ALV has all 171 bits set | **display bug confirmed**: `dir_print_free` tests bits 7, 0, 1 of the last ALV byte (&E0); bits 0/1 (no blocks) count as free |
| Lost blocks after "Diskette voll" | a small SAVE fails too ("Diskette voll"), although the directory has 5K free; after a disc change and back: CAT `5K frei`, SAVE works | the new login (`rdc_relog` → `login_drive`) rebuilds the ALV from the directory |
| Old `.$$$` of a failed SAVE | the next SAVE of the same name leaves one single `S1.BAS` | `vdos_cas_out_open` deletes `<name>.$$$` before `make_file` |
| Wrong key at "Wiederholen J/N ?" (X, then N) | beep, X not echoed, then N accepted | `ask_yes_no`: BEL via TXT OUTPUT, wait again |
| Name with leading spaces (`LOAD "  EX2"`) | file found | `next_nonspace` skips them (4 times: the name is parsed twice) |
| Blank **data format** disc under BASIC: CAT, SAVE, LOAD | `0K in 0 Files, 178K frei`; `TD.BAS` saved and loaded | `seldsk` → `detect_format` (READ ID: R = &C1) → `select_format` → `sf_patch` with `format_params_data`. Format detection is on under BASIC too, as in AMSDOS |
| Blank **IBM format** disc (made offline: `output/tools/make_ibm_dsk.py`) | `153K frei` after one file; `TI.BAS` saved and loaded | `detect_format`: READ ID R = &01-&08 → `select_format` IBM branch → `format_params_ibm` (SPT 32, DSM 155, OFF 1; directory on track 1) |
| 80K ASCII file on **drive B** (Vortex: 4K blocks, EXM = 3), 1200 lines written and read back | written correctly (checked byte for byte from the image); read back: **1202** lines | Head 1 on odd tracks (`unit_head`), `open_copy` rc 0/128, same-entry path of `open_next_extent`, `one_copy` all observed. **The end of the file**: `out_flush_buffer` writes only ONE &1A after the data; the rest of the last record keeps the old contents of the record buffer (here `=0` CR LF `50 WHILE NOT E`). Without the &1A test (default `\|DERROR,3`) BASIC reads that rest as two extra lines |
| **Directory full while a file grows** (63 files + a file > 16K on a 64-entry disc) | `Laufwerk A: Directory voll`, `Break in 30` | after record 127 `open_next_extent` → `make_entry` finds no entry → `one_error` (code 1); the record itself was written, so `ws_ok` returns 0; the next write finds record 128 of a full extent → code 1 → `write_record_out` → `error_dir_full` |
| **File > 512K** on drive B (2100 lines of 249-252 bytes, 528093 bytes; BIGA, XPATCH.COM, MOVCPM.COM erased first to get 584K free) | written correctly (checked byte for byte, `output/huge_from_disc.bin`); read back 2102 lines (the single-&1A end, as above) | after extent 31 `open_next_extent` → `one_next_module`: S2 (FCB+14) &00 → &01 when writing, &80 → &81 when reading, `and #0F` ≠ 0 → `one_open` → `search_name` finds / `make_entry` makes the module-1 entry → `one_copy`. Only the module-16 error (8M) did not run |
| CAT in a window narrower than one entry (`WINDOW 1,8,1,25:CAT`) | one column, the entries wrap | `dir_columns`: 0 columns → B = 1 |
| Drive that does not exist (`LOAD "C:X"`) | `Eingabefehler`, `Break` | `bdos_select_fcb_drive`: SELDSK returns HL = 0 → `bsfd_bad_drive` → `error_bad_name` |
| `SAVE` over an R/O file (R/O set with `\|ATTRIBUT`) | `RO      .BAS hat Schreibschutz`, `Break`; RO.$$$ stays next to the untouched RO.BAS | `out_rename`: the old file is renamed to .BAK first → `rename_body` → `check_rodir` → `error_read_only` (msg &19) |
| CAT of the > 512K file | `HUGE . 512K` although it holds 516K; the total line is right | **second display weakness**: `dir_compare_names` / the size loop use the extent byte only, not the module S2 - the size of a file > 512K is shown modulo 512K (table entry checked: &0200 K) |
| CAS RETURN (&BC86) from machine code (BASIC does not call &BC86; its EOF runs `vdos_cas_return` through CAS TEST EOF, which falls through into it after a character was read): READ.ME, CAS IN CHAR × 2, CAS RETURN, CAS IN CHAR | CR, LF, then LF again; AF, BC, DE, HL, IY kept, **IX not** (&1234 → &A78D, the firmware manual says all registers are preserved) | jump entry #C13C → `vdos_cas_return`: pointer - 1, bytes in buffer + 1, bytes in file + 1 |
| **Read error** (injected: 16 READ results ST0 &40, ST1 &20 at `frr_done`), LOAD on B | `Laufwerk B: Lesefehler - Wiederholen J/N ?` - N: `Break`; J: LOAD ends normally | `fdc_sector_rw` → `fsr_failed` → `disc_error_dialog` (msg = command low nibble &06); J → `fsr_retry_all`, N → `disc_end` |
| **Write error** (injected into WRITE &45 only), SAVE on B | `Schreibfehler - Wiederholen J/N ?` - N: `Break`, `WE2.$$$` (0 bytes) stays | same path, msg &05; the failed write was the directory write of the new entry |
| **Seek error** (injected: 16 SENSE INTERRUPT results ST0 &70) | only `Break` - no message, no question | `seek_track`: `st_retry` → `fdc_clear_interrupts`, `djnz` → `jp disc_end` |
| **Merge error at close** (injected: FCB block &A3 → &A4 before the second close of `SAVE "MG"`) | nothing - `Ready`; the file is intact | `close_body` → `merge_error`: `dec (iy+#21)` turns the entry position 3 (from `search_name`) into 2, not &FF → `bdos_fcb_call` gives A = 3, NZ ("ok"); the entry is not rewritten; `vdos_cas_out_close` ignores the code anyway. Same `dcr lret` as in DR CP/M 2.2 |
| **One-shot CAS hook &BE77** (test hook at &9100 that sets a marker and re-enters `cas_dispatcher`) | hook entered once (at CAS IN ABANDON of CAT), &BE77 cleared, CAT normal | `cas_dispatcher` #C1D0: `push hl`, clear &BE77, RET to the hook with the caller's registers and the FAR CALL frame unchanged. Nothing in the ROMs or on the discs sets &BE77 → variable `cas_oneshot_ptr` |
| **Multi-sector read** (RSX &84 from machine code, C = 1, B = 2, drive flag bit 4 set by hand) | sectors 1 and 2 of track 0 in one call, = image; CY = 1 | `set_eot` EOT = B; `disc_end` clears bit 4 (one call only). Nothing in the ROM sets bit 4 |
| **Start without AMSDOS** (`output/machine_noamsdos.toml`, no ROM 7) | banner, `Ready`, HIMEM &A67B, CAT works | `rom_init`: own workspace &A700 (&500 below &ABFF), ROM number &85, tape CAS entries saved at &A864, far address &A88B → `cas_dispatcher`, CAS entries `DF 8B A8` |

Coverage of the CAS layer after these tests: every line of the CAS functions, headers,
catalog, `crypt_record` and the error exits has run; the &BE77 path of `cas_dispatcher` (an
outside hook, set nowhere in the ROM) ran with a test hook (3.4).

### 4.6 Errors and messages — **observed**

- **Error exits** (&DEE7-&DF2E): print the message unless `messages_off` (&BE7B) is set, store
  the code in &BE82, restore the SP saved by `cas_entry_setup`, and return to the CAS caller
  with CY = 0 and A = code (+&80 when the message was printed).
- **Codes** are the message numbers:

  | Code | Meaning |
  |---|---|
  | &17 | not found |
  | &18 | exists |
  | &19 | read-only |
  | &21 | Eingabefehler (bad input) |
  | &15 | disc full |
  | &16 | directory full |
  | &0E | file not open (no message) |

- **`print_message`** prints message n of `message_table` (&E7BF, 62 German messages). Messages
  end with &FF, and a byte &80+n nests message n (&80 = CR LF). The codes &C0-&C3 insert a file
  name, a number in DE, a drive letter or a number in C. They are tested before the nesting, so
  messages &40-&43 could not be nested.

---

## 5. Layer 3/4 — the disc BIOS (shared by both environments)

### 5.1 Set-up — **observed**

`disc_init` (&C575) does the following:

- switches all motors off and clears VDOS's fixed RAM &BE01-&BF00 (`drives_swapped` is kept);
- sets up the motor ticker (`motor_event_block` &BE6D, routine `motor_event` &CE18, **open**);
- copies the default time constants and sends FDC SPECIFY (`bios_setup_disc`);
- builds the DPHs and DPBs of both drives (`setup_drive_tables`);
- sets the retry count to 16.

The **XPBs** are 25 bytes each: a CP/M DPB of 15 bytes plus a Vortex extension.

| XPB | Format |
|---|---|
| `xpb_3inch` &C154 | 3" system format: 36 records per track, 1K blocks, 171 blocks, 64 directory entries, 2 system tracks, sectors &41-&49 |
| `xpb_vortex` &C16D | Vortex drive: 36 records per track, 4K blocks, 177 blocks (708K), 128 directory entries, sectors 1-9, two heads, 80 tracks |

`drives_swapped` (&BE7F, toggled by `|X`) decides which XPB goes to drive A.

### 5.2 Disc functions

The CP/M-style disc functions are used by the internal BDOS (via the DOS indirections) and by
CP/M (via the BIOS jumpblock):

| Function | Routine | Status |
|---|---|---|
| SETTRK | `bios_settrk` &C360: track C to &BE54 | observed |
| SETSEC | `bios_setsec` &C365: sector C to &BE55 | observed |
| SETDMA | `bios_setdma` &C36A: buffer address BC to &BE60 | observed |
| HOME | `bios_home` &C355: track 0, falls into SETTRK | observed |
| SECTRAN | `bios_sectran` &C36F: no translation, HL = BC | observed |
| SELDSK | `seldsk` &C7D5: DPH of drive C, FDC SPECIFY with the drive's step rate; format detection of the 3" disc by READ ID (`detect_format` → `select_format`): on under BASIC and CP/M (`autodetect_format`, set by `rom_init` and the `\|CPM,1` boot), off only during relative-file record access | observed (system and data format) |
| READ / WRITE | `read_record` &C89A / `write_record` &C8AA: deblocking after Digital Research's algorithm (DEBLOCK.ASM, the sample DR gives BIOS writers) - 128-byte records in a 512-byte host buffer (workspace+&23E), variables `sek_*`, `hst_*`, `una_*`, `deblock_flags` (&BE53-&BE5D) | observed |

Below these functions:

- **Sector I/O:** `fdc_sector_rw` (&C9DE) handles every sector transfer. It opens a disc
  operation (`disc_begin`: motor on, a frame so that every path ends in `disc_end`), seeks,
  sends the command and moves the data in non-DMA mode (`fdc_transfer`).
- **Retries:** up to `retry_count` tries; every 4th try recalibrates first.
- **Errors:** after the last try VDOS prints the error message and asks "- Wiederholen J/N ?".
  The message number is the low nibble of the FDC command: &06 "Lesefehler", &05
  "Schreibfehler", &0D "Formatierfehler". "Diskette fehlt" (&07) and "Diskette hat
  Schreibschutz" (&08) come from the result check. This path is read from the code; there were
  no disc errors in the tests.
- **Motor timing:** one ticker (`motor_ticker` &BE67, `motor_event`) times both the motor-on
  delay (flag bit 3 = running) and the motor-off delay.
- **XPB access:** `xpb_byte_address` caches the drive (`xpb_cache_drive` &BE04 and the two
  addresses after it). Every CAS call sets &BE04 to &FF, so the tables are looked up again.
- **Drive flag bytes:** `drive_flag` (&CC2A) returns the flag byte of drive E (bits: 0 two
  heads, 3 motors running, 4 multi-sector, 5 3" drive, 6 head position known).
  `drive_a_flag` (&CC28, `ld e,0`) is only a preload of `drive_flag` with drive A. It is
  **never called**, and why it exists is not known. Checked 2026-10-25:
  - no call or jump in the ROM and no jumpblock entry;
  - the bytes `28 CC` are in no sector of either disc image;
  - a breakpoint on &CC28 was never hit while VDOS.COM, FAST, CASCOPY, DISKTOOL, FILECOPY,
    XPATCH, XPATCH30, P22, P30 and INSTALL ran under `|CPM,2`.

  Classified as code by the owner. The bytes were never read; the vortex mask at &CC28 is 0,
  so raw and decoded bytes are the same.

### 5.3 Sector functions = hidden RSXs &81-&89

These are the extended BIOS functions of CP/M 2.2 on the CPC, with the same names as in AMSDOS.
They are reachable as hidden RSXs under BASIC and through the extended jumpblock &BE80-&BE98
under CP/M.

| RSX | Routine | What it does | Status |
|---|---|---|---|
| &81 | `bios_set_message` &CC84 | A = 0 messages on, &FF off; returns the old setting | read, fully commented |
| &82 | `bios_setup_disc` &CBBE | 7 time constants + FDC SPECIFY | observed |
| &83 | `bios_select_format` &DCAE | as AMSDOS (A = first sector number &41/&C1/&01 → `select_format`), plus A = &FF: address of drive E's flag byte, A = &FE: toggle `fast_flag` | read (the format selection ran via `detect_format`) |
| &84 | `bios_read_sector` &C9C0 | E drive, D track, C sector (B last: multi-sector), HL buffer; FDC READ DATA (&66) | observed |
| &85 | `bios_write_sector` &C9C7 | as &84, FDC WRITE DATA (&45) | observed |
| &86 | `bios_format_track` &C9CE | E drive, D track, HL sector headers; FDC FORMAT (&4D) | read |
| &87 | `bios_move_track` &CAA8 | E drive, D track (seek) | observed |
| &88 | `bios_get_status` &CB79 | SENSE DRIVE STATUS of unit A (as passed; `drives_swapped` not applied), A = ST3 | observed |
| &89 | `bios_set_retry_count` &C5A4 | A = new count, returns the old one | observed |

The research called &83 a "drive assignment". The code shows it is AMSDOS's SELECT FORMAT, with
two extra VDOS functions.

### 5.4 Hardware

| Hardware | Port / code | Status |
|---|---|---|
| uPD765 FDC | main status &FB7E, data &FB7F; `fdc_write_byte` &CC06 waits for RQM | observed |
| motor port | &FA7E (`motor_off` &CE35) | observed |
| retries | `retry_count` &BE64 | observed |
| time constants | `disc_time_constants` &BE44-&BE4A | observed |

---

## 6. CP/M environment

### 6.1 `|CPM` and `|CPM,1`

- **`|CPM` without a parameter** hands over to AMSDOS's own CP/M boot: a FAR CALL to &C1DC in
  **ROM 7** (far address at &C328). **Observed:** AMSDOS's CP/M 2.2 started. VDOS's jumpblocks
  are not used.
- **`|CPM,1` / `|CPM,2`** set `drives_swapped` and start VDOS's own CP/M boot (&C3F6-&C4xx).
  **Observed** with `|CPM,1` and disc A: the Vortex 44K CP/M started ("44K CP/M vers.
  2.2-07/86 vortex GmbH") and DIR works. The boot does the following:
  1. clears memory and calls `disc_init`;
  2. copies the **extended BIOS jumpblock** &C093 to **&BE80** (LDIR at &C417);
  3. writes the IOBYTE and other CP/M bytes;
  4. installs `bios_entry` (&B046) and the interrupt vector;
  5. reads the boot sector to &0100 and enters it with **BC = &C0D2**. The boot sector copies
     the **CP/M BIOS jumpblock** &C0D2 to &0500 (LDIR at &0108); it ends up at **&AC00**, the
     BIOS address of the 44K CP/M.

  The &AC00 copy is made by WBOOT (`wboot_body`, every warm boot); the boot sector itself
  jumps to &0503 = WBOOT. Details in 6.7.

### 6.2 The two jumpblocks

**CP/M 2.2 BIOS jumpblock**, RAM &AC00, labels `cpm_*` (group `cpm`):

| Entry | Function | Routine | Entry | Function | Routine |
|---|---|---|---|---|---|
| 0 | BOOT | `bios_boot` &C31D | 9 | SELDSK | `bios_seldsk` &C350 → &C7D5 |
| 1 | WBOOT | `bios_wboot` &C34B → &C4AA | 10 | SETTRK | `bios_settrk` &C360 |
| 2 | CONST | `bios_const` &C616 | 11 | SETSEC | `bios_setsec` &C365 |
| 3 | CONIN | `bios_conin` &C61A | 12 | SETDMA | `bios_setdma` &C36A |
| 4 | CONOUT | `bios_conout` &C61E | 13 | READ | `bios_read` &C377 → &C89A |
| 5 | LIST | `bios_list` &C62A | 14 | WRITE | `bios_write` &C372 → &C8AA |
| 6 | PUNCH | `bios_punch` &C622 | 15 | LISTST | `bios_listst` &C62E |
| 7 | READER | `bios_reader` &C626 | 16 | SECTRAN | `bios_sectran` &C36F |
| 8 | HOME | `bios_home` &C355 | | | |

**Extended BIOS jumpblock**, RAM &BE80, labels `cpm_ext_*` (group `cpm`):

| RAM | Function | Routine |
|---|---|---|
| &BE80-&BE98 | SET MESSAGE … SET RETRY COUNT | the nine routines of 5.3 |
| &BE9B | ENTER FIRMWARE | `bios_enter_firmware` &C3EA |
| &BE9E | SET REG SAVE (+ "motors off") | `bios_set_reg_save` &CE27 |
| &BEA1 | SET SIO | `bios_set_sio` &C718 |
| &BEA4 | SET CMND BUFFER | `bios_set_cmnd_buffer` &C1B0 |
| &BEA7-&BEBC | SIO input status A/B, output status A/B, input A/B, output A/B | `bios_sio_a_in_status` … `bios_sio_b_out` |

The SIO routines drive a Z80 DART (control ports &FADD channel A, &FADF channel B) and an 8253
baud rate timer (&FBDF). None of them were run, because no serial interface is fitted.

### 6.3 BIOS entry handler — **observed**

CP/M owns all Z80 registers, but the firmware needs BC' (the gate array port and ROM state), its
IY and its interrupt vector. A BIOS function that needs the firmware ends with:

```
        call bios_entry          ; &B046: JP bios_entry_handler (or bios_entry_fast)
        defw target              ; ROM routine to run in the firmware's environment
```

`bios_entry_handler` (&C37C) then does this:

1. switches to the alternate set and saves the caller's SP (`bios_caller_sp` &B0D2);
2. moves to its own stack below &C000;
3. saves the caller's AF', BC', DE', HL', IX and IY;
4. loads the firmware's BC' (`firmware_bc_alt` &B04B);
5. `bios_entry_enter` (&C3D1) sets the interrupt vector &0039 back to the firmware's
   (`firmware_int_vector` &B049 = &B939), loads IY from `cpm_rom_iy` (&BE7D), and jumps to the
   target with the caller's main registers;
6. when the target returns (`beh_return`), it keeps the firmware's BC' again and sets &0039 back
   to `bios_interrupt`;
7. it restores the caller's registers and returns to the **caller of the BIOS function**. The
   word after the CALL is never skipped, so the CALL is always the last instruction.

**Observed:**

- **DIR under CP/M:** the console output came through `bios_char_io` &C630 with the target
  &C635 (the next instruction).
- **SELDSK, READ, WRITE, WBOOT** have the targets &C7D5, &C89A, &C8AA, &C4AA, all decoded as
  data reads. WRITE's target is static only, because DIR does not write.

Related routines:

- **`bios_interrupt`** (&C3E5): while CP/M code runs, &0038 jumps here. It runs the firmware's
  interrupt routine (`call bios_entry / defw &0038`) in the firmware's environment, so the
  keyboard and the tickers keep working. **Observed:** an interrupt in CP/M code reached &B939.
- **`bios_set_reg_save`** (&BE9E): A = 0 selects `bios_entry_handler` (saves the registers, the
  default); A = &FF selects `bios_entry_fast` (&C3B3, no saving, so CP/M must leave BC' alone).
  Any other A falls into "motors off at once", which is why the manual calls the entry "motor
  off". **Read.**
- **`bios_enter_firmware`** (&BE9B): `CALL &BE9B / DEFW address` for CP/M programs. It moves the
  return address past the word, so it returns to the caller. **Read.**
- **`install_entry_handler`** (&C46A): puts `JP bios_entry_handler` into &B046 and saves BC'.
  **Read.**

### 6.4 Character I/O — `bios_char_io` &C630, `char_io_table` &C652 (**observed** 2026-10-25)

CONST, CONIN, CONOUT, READER, PUNCH, LIST and LISTST load L = &00, &09, &12, &1B, &24, &2D, &36
and jump to `bios_char_io`. It goes through `bios_entry` into the firmware's environment, takes
the function's 9-byte entry in `char_io_table`, rotates the IOBYTE (&0003) by the entry's first
byte (RLCA × n brings the function's field to bits 1-2), picks one of the four routine addresses
by the field value and jumps there with IX = &B04D (console state) and A = 0.

| Function | IOBYTE field | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| CONST | CON: bits 0-1 | TTY: SIO A in status | **CRT:** `con_crt_status` | BAT: always ready | UC1: SIO B in status |
| CONIN | CON: | TTY: SIO A in | **CRT:** `con_crt_in` | BAT: A = 0 | UC1: SIO B in |
| CONOUT | CON: | TTY: SIO A out | **CRT:** `con_crt_out` | BAT: ignored | UC1: SIO B out |
| READER | RDR: bits 2-3 | TTY: SIO A in | PTR: &1A (end of file) | UR1: SIO B in | UR2: keyboard |
| PUNCH | PUN: bits 4-5 | TTY: SIO A out | PTP: ignored | UP1: SIO B out | UP2: screen |
| LIST | LST: bits 6-7 | TTY: SIO A out | CRT: **ignored** | LPT: printer | UL1: SIO B out |
| LISTST | LST: | TTY: SIO A out status | CRT: ready | LPT: printer status | UL1: SIO B out status |

SIO = the extended jumpblock entries &BEA7-&BEBC (vortex RS232C interface, Z80 DART; observed
by I/O injection, see "Serial interface" below). The default IOBYTE &81 (set by
`cpm_cold_boot`, also by the Amstrad boot sector from its configuration sector) is CON: = CRT:,
RDR: = TTY:, PUN: = TTY:, LST: = LPT:.

Against DR's manual (6.6): BAT (CON: = 2) is not batch mode (READER in, LIST out) but a dead
console; LST: = CRT: drops the characters instead of showing them.

**Device routines:**
- **`con_crt_status`** &C691: KM READ CHAR; a key is put back with KM CHAR RETURN for CONIN.
  It also counts down `con_cursor_count` (&B04D). CONOUT sets it to &FF and hides the cursor;
  after 255 status calls without output the cursor comes back, so programs that poll while they
  print do not make it flicker.
- **`con_crt_in`** &C6A4: first the **autostart string** (`autostart_count` &B051 characters at
  `autostart_ptr` &B04F, from SET CMND BUFFER), else cursor on and `wait_key_cursor` (blinking
  cursor).
- **`con_crt_out`** &C6D9: TXT OUTPUT, control characters unfiltered (CPC control codes). After a
  control character a cursor outside the window is placed and removed again, so the pending
  scroll is done at once.
- **`char_list_out`** &C6FD / **`char_list_status`** &C6F7: MC PRINT CHAR (50 tries) / MC BUSY
  PRINTER; after 50 failures "Drucker nicht bereit - Wiederholen J/N ?": J = retry, N = warm
  boot.
- Stubs `char_in_eof` (&1A), `char_status_ready` (&FF), `char_out_none` (RET).

**Autostart string** (INSTALL "CP/M Parameter" → "Autostart String"): stored in the Vortex
parameter sector. The Vortex boot sector (`|CPM,2`) passes it at every start through SET CMND
BUFFER (&BEA4, `bios_set_cmnd_buffer`: A → `autostart_flag` &B04E, length + 128 bytes →
&B051, pointer = &B052). A key pressed while the string runs comes first; with flag &FF (the
boot sector's value) the string then goes on, with flag 0 the key cancels the rest.

**Serial interface (SIO, &C718-&C7D4)** — Z80 DART, control ports &FADD (A) / &FADF (B), data
ports &FADC / &FADE; 8253 baud rate timer &FBDC-&FBDE, control &FBDF.

- Static check: from the nine entries (SET SIO and the eight SIO functions) the control flow
  reaches 105 instructions that cover all 189 bytes, with no gaps, overlaps or targets outside
  (`output/tools/reach.py`). The instruction starts are the same as in the generated source.
  The area holds no data. The parameters come from outside: SET SIO's 12-byte block.
- `bios_set_sio`: channel reset (&18), WR4, WR5, WR3 per channel from the block, then the
  counters 0, 1, 2 (mode 3). **Observed** (port writes logged during the `|CPM,2` boot):
  FADD/FADF `18 04 44 05 6A 03 E1`, FBDF `36` FBDC `07 00`, FBDF `76` FBDD `07 00`, FBDF `B6`
  FBDE `0D 00`.
  - The Vortex counters 7/7/13 are INSTALL's defaults: channel A send 19200, channel A receive
    19200, channel B 9600. The timer clock is therefore about 2 MHz (derived). The Amstrad
    sector passes 13/13/13.
- `sio_in_status`: RR0 bit 0. If nothing is there, DTR is pulsed (WR5 | &80, look again, WR5
  back), so the sender may only send while CP/M polls.
- `sio_out_status`: RR0 bit 2. `sio_in_wait` / `sio_out_wait` loop on them and then use the
  data port (control - 1).
- **Finding (VDOS code, independent of the emulator):** the WR5 copies `sio_wr5` (&BE01 for A,
  &BE02 for B) are selected with `bit 0,c`. That bit is 1 for both &DD and &DF, so both channels
  use &BE02 (observed: &BE01 = &00, &BE02 = &6A). Probably meant to tell the channels apart. It
  makes no difference while both channels have the same WR5 (&6A in both configurations).
- Without injection the emulator answers every IN with &FF: RR0 then reads "ready / character
  there", output disappears and input reads &FF.

**I/O injection** (`output/tools/sio_sim.py`): an `io_in` breakpoint on &FADC-&FADF (mask
&FFFC), then A is replaced:
- control port: RR0 with bit 2 set, or clear for the first n "busy" reads, and bit 0 set when a
  queued character is waiting (clear for the first n reads, to run the DTR path);
- data port: the next queued character.

OUTs are logged. With `GATE=1` each queued line is only released after the channel has sent
`>`, so the CCP does not swallow characters while a program ends.

Every line of &C616-&C7D4 and every table entry has run (with injection for the SIO).

**Tests** (`|CPM,1` / `|CPM,2`, discs `output/cpm_A.dsk` / `cpm_B.dsk`):

| Test | Result |
|---|---|
| `STAT DEV:` / `STAT VAL:` | CON: CRT:, RDR: TTY:, PUN: TTY:, LST: LPT: (IOBYTE &81); device names TTY/CRT/BAT/UC1 … match the table's columns |
| `PIP LST:=DUMP.ASM` | `bios_list` → `char_list_out`; the emulator has no printer, MC PRINT CHAR succeeds at once |
| same, CY cleared 50 times after MC PRINT CHAR (injection at &C703) | "Drucker nicht bereit - Wiederholen J/N ?"; J → printing goes on; N → warm boot, `A>` |
| `STAT LST:=CRT:`, `PIP LST:=DUMP.ASM` | IOBYTE &41; nothing printed (`char_out_none`) |
| `STAT PUN:=UP2:`, `PIP PUN:=S.TXT` | the text on the screen (`con_crt_out`); afterwards output invisible, cursor top left - PIP closes PUN: with &1A (seen on the SIO test), which TXT OUTPUT takes as SET WINDOW |
| `STAT RDR:=PTR:`, `PIP R.TXT=RDR:` | an empty R.TXT (`char_in_eof`) |
| INSTALL: autostart string `DIR` + &0D, install, restart | INSTALL writes the parameter sector through &BE8C WRITE SECTOR and calls BOOT (&AC00 → `bios_boot`); the restarted CP/M runs DIR by itself; at the next `\|CPM,2` again (SET CMND BUFFER from the boot sector, return &0164, A = &FF, HL = &0330) |
| key X held during the start | flag &FF: CCP gets "xDIR" (`XDIR?`); flag 0 (A set to 0 at &C1B0): only "x" |
| `STAT LST:=TTY:`, `PIP LST:=S.TXT` + injection | the file sent on &FADC (`sio_out_status`, `sow_loop`) |
| `STAT RDR:=TTY:`, `PIP R.TXT=RDR:`, first status "empty" | WR5 &EA / &6A (DTR pulse), then H, I, CR, LF, &1A read from &FADC; `TYPE R.TXT` = HI |
| `LST:=UL1:` / `RDR:=UR1:` | the same on channel B (&FADE) |
| `STAT CON:=TTY:`, commands through the injection, `CON:=UC1:`, `CON:=CRT:` | the CCP worked over channel A, then B, then back on the screen (IOBYTE &81) |
| `LS.COM` (CALL LISTST, A → &0050) with LST: TTY (busy) / UL1 / LPT / CRT | 00 / FF / FF / FF |
| `PUN:` TTY / UP1 / PTP, `PIP PUN:=S.TXT` | 94 bytes on A / on B (40 × &00, text, **&1A**, 40 × &00) / nothing |
| `RDR:=UR2:`, `PIP R3.TXT=RDR:`, typed OK + Ctrl-Z | R3.TXT = OK |
| `STAT CON:=BAT:` | dead console (the table entries read; no input or output) |


### 6.8 Extended jumpblock — all 21 entries observed (2026-10-25)

Test programs written to &0100 with `memory_write`, saved with the CCP's `SAVE 1 NAME.COM` and run
under `|CPM,1`. The results are stored at &0050 (on the copy `output/cpm_A.dsk`).

| Entry | Caller / test | Result |
|---|---|---|
| &BE80-&BE89 SET MESSAGE … READ SECTOR | the boot sectors | 6.7 |
| &BE8C WRITE SECTOR | INSTALL (writes the parameter sector) | 6.4 |
| &BE8F FORMAT TRACK | `XB.COM`: drive B, track 158, headers 79/0/1-9/2 at &0180 | CY = 1, A = 0; `DIR B:` still fine |
| &BE92 MOVE TRACK | `XB.COM`: drive B, track 20 | CY = 1, A = 0 |
| &BE95 GET STATUS | `XB.COM`: unit 1 | CY = 1, ST3 &29 (ready, two-sided, unit 1) |
| &BE98 SET RETRY COUNT | `XB.COM`: 5, then 16 | old value 16, then 5 |
| &BE9B ENTER FIRMWARE | INSTALL at its start: `CALL &BE9B / DEFW &BE89` (READ SECTOR of the parameter sector) | returns behind the word: breakpoint at &011C, SP &9E06 (balanced), CY = 1 |
| &BE9E SET REG SAVE | `RS.COM`: &FF, CONOUT "X", 0, &55 | old mode 0; "X" through `bios_entry_fast` / `bef_return`; old mode &FF, `bios_entry_target` back to &C37C; &55 = motors off, A = 0 |
| &BEA1 SET SIO, &BEA4 SET CMND BUFFER, &BEA7-&BEBC SIO | boot sectors, IOBYTE devices | 6.4 |

**Register save, checked with marker registers** (`FM.COM`: IX &1234, IY &5678, DE' &2222, HL' &3333,
A' &AA, then about 27 ms of waiting (interrupts), store, CONOUT, store; once with SET REG SAVE &FF,
once with 0):

| | IX | IY | DE' | HL' | A' |
|---|---|---|---|---|---|
| &FF, after the interrupts only | &1234 | &AB68 | &0038 | &C3E5 | &00 |
| &FF, after CONOUT | &B04D | &AB68 | &1400 | &C3E5 | &86 |
| 0, after the interrupts | &1234 | &5678 | &2222 | &3333 | &AA |
| 0, after CONOUT | &1234 | &5678 | &2222 | &3333 | &AA |

Interrupts also run through `bios_entry_fast` in mode &FF (first stop there: return &C3E8 from
`bios_interrupt`, interrupted at &011F). So with SET REG SAVE &FF a CP/M program cannot use IY or
the alternate registers at all, and IX not across BIOS calls. Mode 0 keeps everything.

`RS.COM`: `3E FF CD 9E BE 32 50 00 0E 58 CD 0C AC AF CD 9E BE 32 51 00 3E 55 CD 9E BE 32 52 00 C3 00 00`.

---

## 7. RAM map

### 7.1 BASIC environment (group `vdos`, workspace &BE00-&BFFF)

| Address | Name | Content |
|---|---|---|
| &BE24 | `km_disarm_break_saved` | boot: original KM DISARM BREAK address; later the internal BDOS's current FCB |
| &BE26 | `km_disarm_break_far` | far address of the hook (&C26E, ROM 5) |
| &BE2D | `disarm_break_count` | KM DISARM BREAK calls left until `post_boot_setup` (2) |
| &BE40 | `dph_drive_a` | address of drive A's DPH (drive B's follows) |
| &BE44 | `disc_time_constants` | 7 bytes, set by `bios_setup_disc` |
| &BE64 | `retry_count` | retries after a disc error (16) |
| &BE6D | `motor_event_block` | event block of the motor ticker |
| &BE75 | `vdos_workspace` | VDOS workspace base (&A700) |
| &BE77 | `cas_oneshot_ptr` | one-shot CAS hook: not 0 → the next CAS call goes there once, then it is cleared (3.4); default 0, set by nothing in the ROMs or on the discs |
| &BE7B | `messages_off` | 0 = disc messages shown, &FF = suppressed (`\|DERROR,1` / `,0`) |
| &BE7C | `eof_test_1a` | 0 = only the physical end (default, `\|DERROR,3`), &FF = &1A ends a file (`\|DERROR,2`) |
| &BE7F | `drives_swapped` | 0 = 3" drive is A, 1 = Vortex drive is A |
| &BE8F-&BEA0 | `dos_seldsk` … `dos_write` | DOS indirections (RAM copy) |
| &BEA1-&BEB6 | `basic_error_patch` | RAM copy |
| &BF00-&BF3E | `hello_loader` | RAM copy |

XMON variables (group `vdos`; the manual's tables "Variablen des Diskettenmonitors" /
"Variablen des Monitors" &BEC1-&BF80; only those whose start value was observed, 3.5.18):

| Address | Name | Content |
|---|---|---|
| &BEC8 | `xmon_rom` | the upper ROM shown at &C000 (Y command); start: this ROM (5) |
| &BEC9 | `xmon_firmware_rom` | X switch: 0 = firmware ROM off (RAM at &0000-&3FFF), &FF = on; start: 0 |
| &BED0 | `xmon_break_far` | far address of the RST 6 at &0030: `xmon_breakpoint` &F8D9, ROM 5 |
| &BEDD | `xmon_cpm_flag` | 0 = VDOS active, &FF = CP/M active; observed 0 from BASIC |
| &BEDE | `xmon_saved_sp` | the caller's SP (observed &BFF4) |
| &BEF8 | `xmon_user_sp` | SP for G / T; start: &BF80 |
| &BF00-&BF17 | `xmon_break_area` | B1-B8: 8 x (address low, high, saved byte); cleared at the start - the same RAM as the HELLO loader copy |
| &BF80 | — | top of the monitor stack |
| &BED3 | `xmon_subst_address` | S: the current address (the manual says M - corrected) |
| &BED5 | `xmon_list_address` | L: the next address to list |
| &BED9 | `xmon_dump_address` | D: the next address to dump (default 0100 at the start) |
| &BEE0 | `xmon_bank` | Z: 0 = Vortex RAM off, &20 + bank = on (written to port &FBBD) |
| &BEE3 | `xmon_branch_target` | L: target of a relative jump |
| &BEEC-&BEF7 | `xmon_user_af` ... `xmon_user_iy` | R: the user pairs AF BC DE HL IX IY for G / T |
| &BEFB | `xmon_user_pc` | R: the user PC ("XP") |
| &BEFE | `xmon_printer_saved` | the printer switch kept by `xmon_hex_byte_quiet` |
| &BEFF | `xmon_printer_switch` | bit 0 = printer echo (P); bits 7-5 = trace flags (T) |
| &BED7 | `xmon_fill_address` | the start address of F and A (one shared default) |
| &ACA4 | `xmon_text_length` | A: the text length; the text at &ACA5 (255 bytes) |
| &BEE2 | `xmon_branch_byte` | T: the byte under the branch-target breakpoint |
| &BEE5 | `xmon_run_sp` | G / T: XMON's own SP while the program runs |
| &BEE7 | `xmon_run_address` | G / T: the start address of the run |
| &BEE9 | `xmon_trace_count` | T: steps left; negative = stop (G) |
| &BEEB | `xmon_run_byte` | G: the byte at the start address |
| &BEFA | `xmon_user_jump` | `JP` + user PC, entered by RET |
| &BEFD | `xmon_index_disp` | L: the displacement d of (IX+d) / (IY+d) (manual: "Distanz bei relativen Z80 Befehlen") |
| &ACA5-&ACA9 | `xmon_decoded` | L: the decoded instruction (length - 1, mnemonic, operand 1 / 2, index prefix), in BASIC's input buffer |

Still without a name (the commands have not run): &BE00 (disc monitor flag, read in
`xmon_command_done`), &BEC1-&BEC7 (disc monitor drive / track / sector / buffer), &BECD (far
address for FAST), &BED7 (now named), the rest of &BEE0-&BEFF
(internal values, user registers AF-IY, PC).

Disc BIOS variables (group `vdos`, used under both BASIC and CP/M):

| Address | Names |
|---|---|
| &BE03 | `autodetect_format` |
| &BE04-&BE08 | `xpb_cache_drive`, `xpb_cache_dph`, `xpb_cache_xpb` |
| &BE4B | `fdc_result` (7 bytes) |
| &BE53-&BE5D | deblocking: `sek_drive/track/record`, `hst_drive/track/sector`, `deblock_flags`, `una_count/drive/track/record` |
| &BE5E | `seek_command` |
| &BE5F | `step_rate` |
| &BE60 | `dma_address` |
| &BE62 | `sector_buffer` |
| &BE65 | `disc_frame_sp` |
| &BE67 | `motor_ticker` |
| &BE74 | `fdc_command` |
| &BEBF / &BEC0 | `fdc_sector`, `fdc_last_sector` |
| &BE82 | `cas_last_error` |

BDOS variables (group `bdos`, context `rom5:DDF6-E785`):

| Address | Names |
|---|---|
| &BE09-&BE14 | `bdos_dph`, `bdos_xlt`, `bdos_dirbuf`, `bdos_dpb`, `bdos_csv`, `bdos_alv` |
| &BE15-&BE23 | the DPB copy: `dpb_spt`, `dpb_bsh`, `dpb_blm`, `dpb_exm`, `dpb_dsm`, `dpb_drm`, `dpb_al`, `dpb_cks`, `dpb_off` |
| &BE24-&BE2D | `bdos_fcb`, `dir_count`, `actual_record`, `bdos_dma`, `virtual_record`, `record_count` |

&BE77 is `cas_oneshot_ptr`, the one-shot CAS hook (3.4).

Still unnamed: &BE42 (address of the 3" XPB). &BE79 is `code_key` (3.5.9).

### 7.2 BASIC 1.0 (group `basic`)

| Address | Name | Content |
|---|---|---|
| &AC04 | `basic_error_indirection` | the error indirection that VDOS patches |
| &AE34 | `basic_stmt_ptr` | byte before the current statement |
| &B0C2 | `basic_vacc` | BASIC's virtual accumulator |

### 7.3 CP/M environment (group `cpm`)

| Address | Name | Content |
|---|---|---|
| &AC00-&AC32 | `cpm_boot` … `cpm_sectran` | CP/M BIOS jumpblock (RAM copy) |
| &B046 | `bios_entry` | `JP` to the entry handler |
| &B047 | `bios_entry_target` | its jump address |
| &B049 | `firmware_int_vector` | the firmware's interrupt jump address (&B939) |
| &B04B | `firmware_bc_alt` | the firmware's BC' (&7F86) |
| &B0D2 | `bios_caller_sp` | the CP/M caller's SP during a firmware call |
| &B0D4 | `reg_save_mode` | 0 = save registers, &FF = fast |
| &BE7C | `fast_flag` | FAST flag under CP/M (toggled by `bios_select_format`, A = &FE; read) |
| &BE7D | `cpm_rom_iy` | IY for ROM code under CP/M (&AB68; what it points to: open) |
| &BE80-&BEBE | `cpm_ext_set_message` … `cpm_ext_sio_b_out` | extended BIOS jumpblock (RAM copy) |
| &0500 | – | first copy of the BIOS jumpblock (made by the boot sector) |

### 7.4 One RAM, two meanings

&BE80-&BEBE holds the DOS indirections and `basic_error_patch` under BASIC, and the extended BIOS
jumpblock under CP/M. Both copies come from ROM 5: &C105 for BASIC, &C093 for CP/M. The
annotations keep them apart like this:

- the context `rom5:C093-C104` uses the group `cpm`;
- the rest of ROM 5 uses `vdos`;
- the handler code `rom5:C37C-C3F5`, `C462-C478` and `CE3F-CE5A` uses `cpm`.

So each RAM copy shows its own names.

---

## 8. Corrections to the earlier sources

| Topic | Earlier source | 2.11-X (checked) |
|---|---|---|
| Start-up mechanism | manual: a ticker watches BASIC's READY indirection | KM DISARM BREAK hook, two calls (observed) |
| &BE7C &1A test | manual RAM table: 0 = test &1A | 0 = no test (default, `\|DERROR,3`), &FF = test (`\|DERROR,2`) - as the manual appendix "Das EOF Problem" says (observed) |
| Extended BIOS &BEA1 | manual: "position head indirection" | SET SIO (read) |
| Extended BIOS &BE9E | manual: "motor off at once"; research: SET REG SAVE | both: A = 0/&FF reg save, else motors off (read) |
| SIO entry order | research: D0 IN STATUS, D0 IN, … | in status A/B, out status A/B, in A/B, out A/B (code, manual) |
| `sub_c1dc` | generated label at &C1DC | the far address names &C1DC in ROM 7; no label in ROM 5 (CPC X-Ray fixed) |
| &C093 / &C0D2 | research: `RAM_JMP_BLK`, 2nd half unnamed | extended jumpblock and CP/M BIOS jumpblock (observed) |
| ROM version | CPC X-Ray shows "1.333" | BCD: version 2.1, modification 3 |
| Hidden RSX &83 | research / notes: drive assignment | SELECT FORMAT (A = first sector number, the same values as AMSDOS's) + &FF flags address, &FE FAST (read) |
| Internal BDOS | research: VDOS's own file functions | Vortex's implementation of the CP/M 2.2 BDOS file functions, routine by routine after DR's BDOS, with VDOS changes (disc full, disc change) (observed) |
| Disc full | — | blocks of the failed extent stay used until the next login, by reset or disc change (observed) |
| CAT free space | — | display bug: up to 2K too much "frei" when the last ALV byte is used (observed on a full disc) |
| &BE77 | manual: "Adresse einer DOS-Routine im ROM", default 0 | one-shot CAS hook in `cas_dispatcher`: used once, then cleared; the target gets the caller's registers and the unchanged FAR CALL frame; nothing sets it (observed with a test hook) |
| &ED21 (`rsx_xmon`) | research: "load variable??? to A" | stores 0 to &BE00 (observed) |
| &F8D9 | research: `LD BC,$f8d9` "menu pointer" | the RST 6 target `xmon_breakpoint`, reached through the far address &BED0 (observed: &0030 = PUSH IY / RST 3 / DEFW &BED0) |

Research names that were confirmed: the CAS jump table targets, the hidden RSX targets and the
extended jumpblock targets.

### 8.0 VDOS behaviour that programs written for AMSDOS / the firmware manual may not expect

VDOS's behaviour is the reference (section 1). This table only lists where a program written
for AMSDOS or the firmware manual expects something else.

| Topic | Expected by programs written for AMSDOS / the firmware manual | VDOS (observed) |
|---|---|---|
| CAS IN OPEN extension search | none, `.BAS`, `.BIN` | none, `.BAS`, `.BIN`, **`.BAK`** |
| User number in file names | `10:NAME` | not accepted ("Eingabefehler"); user via `\|SELECT` |
| End of an ASCII file | rest of the last record &1A (AMSDOS and CP/M) | one &1A, the rest of the record is old buffer data |
| Registers of CAS entries | CAS RETURN keeps all registers; CAS IN CHAR / IN CLOSE change only A (disc); CAS OUT ABANDON keeps all but AF, BC, DE, HL | IX is left at the input / output header after CAS RETURN, IN CHAR, IN CLOSE and OUT ABANDON; IN CLOSE also changes DE and HL (marker registers IX = &1234, BC = &1111, DE = &2222, HL = &3333) |
| SETUP DISC block byte 6 / byte 4 | one step rate for both drives / write current off time | combined step rate (3" high nibble, Vortex low nibble) / unused; the Amstrad CP/M boot sector's value is converted by WBOOT (6.6) |


### 8.1 Header pass and check of the static decoding (todo Part C, 2026-10-25)

**Header conventions** (every routine header): `Tasks`, `Input`, `Output`, `Changed`, `Called by` /
`Entered from`, `Calls`, start address `[#xxxx]` in the first line.

- `Changed` = every register that differs on return, results included (so a result register
  appears under `Output` and under `Changed`).
- `IY = VDOS workspace` is an input of the CAS and BDOS routines (set by `cas_dispatcher`).
- A fall-through is written as "falls through into X" (`Calls`) and "Y (falls through)"
  (`Entered from`), not as a call.

How: offline register analysis of the listing (`output/tools/regflow.py`: liveness for Input,
"holds the entry value" for Changed, routine summaries to a fixpoint, firmware exits from the
Soft 968 manual), applied with `hdr_apply.py` (223 headers changed). Uncertain cases were
checked in the emulator with marker registers (IX = &1234, BC = &1111, DE = &2222, HL = &3333
before the call). Not covered: the CP/M BIOS side (Part B) and the specials `cas_dispatcher`,
`rom_init`, `setup_drive_tables`, `rsx_files`, whose headers were written by hand.

**VDOS register behaviour of the CAS entries** (observed; programs written for the firmware
manual expect fewer changed registers): CAS RETURN, CAS IN CHAR, CAS IN CLOSE and CAS OUT ABANDON
leave IX at the input / output header; CAS IN CLOSE also changes DE and HL (see 8.0). RSX &88
GET STATUS reports a write-protected disc as an error (3.5.17).

**Static decoding of never-run code.** The vortex rule XORs only non-M1 bytes, with a mask
(&00/&08/&20/&28) fixed by the address. A never-run instruction is therefore decoded correctly
as long as its boundaries are right, so the check is whether the operands make sense
(`output/tools/static_operands.py`, `output/tools/never_code.py`):

- 177 never-run instructions with operands: all branch targets lie on instruction starts; the
  only RAM addresses with no name (&BEC8-&BEF8, &BE00) belong to |XMON (now partly named,
  7.1 and 3.5.18).
- **Code shown as data, corrected** (classified as code by the owner rule in the analysis):
  `bios_entry_fast` &C3B3-&C3D0 (it was commented as code, but the source showed data-decoded
  defb such as `#FB,#20,#F1` instead of `di / ex af,af' / exx`), and &C6F7-&C717 (`char_list_status`,
  `char_list_out`, stubs `char_in_eof`, `char_status_ready`, `char_out_none`; the character I/O
  table of `bios_listst` points at exactly these addresses).
- **Numbers shown as ROM labels, corrected** (`operand_set` value): I/O ports &FADD (DART),
  &FBDF (8253), &FB7E (FDC status), &FA7E (motor), the offsets -5 / -1 / -20 (&FFFB, &FFFF,
  &FFEC) and &EA00 = -&1600 (CCP + BDOS size) in the CP/M boot.
- Data blocks that remain defb are consistent: the `bios_listst` table holds addresses of
  real entry points; &C49E is the string "BASIC".
- Not judged: the |XMON block &EA9E-&FD59 (skipped at first; its start is observed since
  2026-10-25, 3.5.18) and &FFC0-&FFFF - judged 2026-10-26: `rom_tail_copy`, a
  fully scrambled duplicate of &FF40-&FF7F (end of `rsx_romcat`, `romcat_rom_info`, start of
  `romcat_rsx_entry`), unreachable; read once as data on purpose (LDIR to &4100), shown as defb
  with the decoded values and the code as comments.

---

## 9. Open questions and next steps

1. **Disc BIOS and internal BDOS:** commented (2026-10-25). Never run:
   - (read/write/seek errors: observed by injecting FDC results, 4.5b; the recalibrate inside
     the retries is from the code: bit 2 of the tries left);
   - two-byte block maps (DSM ≥ 256): the DR BDOS algorithm for larger formats. VDOS's own DPBs all
     have DSM < 256, but a user's driver for another disc format that installs its own DPH / DPB
     with DSM ≥ 256 uses them at once - observed 2026-10-26 with a 2K-block DPB (DSM &15F) on drive
     B (`test_single_map`): CAT, SAVE 18K, LOAD identical, |ERA; the module 16 error (8M) not run;
   - random access.
2. **CAT display, two weaknesses (both confirmed, 4.5b):** `dir_print_free` can show up to 2K
   (3") too much free space when the last ALV byte holds used blocks; file sizes over 512K are
   shown modulo 512K (the module byte S2 is not counted).
3. **CP/M:** the `|CPM,1` boot &C3F6-&C574 (and who copies the BIOS jumpblock to &AC00), WBOOT
   &C4AA, the character I/O table behind `bios_char_io`, `cpm_rom_iy`, `bios_entry_fast`. A
   small CP/M test program could run the fast handler and ENTER FIRMWARE.
4. **RSX commands:** all done except the `|XMON` commands. Observed (3.5.18): the start,
   command recognition, Z, X, D, Y, L, R, P, A, B, C, F, G, T, M, S and I (complete). Open: R, B, F,
   G, O, P, T, M, A, C, the disc monitor (@) and the breakpoint / trace paths.
5. **Single questions:**
   - `crypt_record` with a `|CODE` string.
   - (solved: &BE77 is a one-shot CAS hook that nothing in the ROMs or on the discs sets, 3.4)
6. **Coverage:** 34 of 16384 bytes have never been read (access map 2026-10-26 after XMON under
   CP/M and the two-byte block simulation: M1 7981, data 8369, 0 conflicts) - all on the ignore list
   `project/never_read_ignore.md` (dead code, unreachable entries, XMON table entries).
