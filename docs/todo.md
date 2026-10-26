# VDOS 2.11-X analysis - to do

Open points only; done points are in `project/vdos_rom_analysis.md` and
`project/project-annotation-progress.md` (old full list: `output/doc_history/todo_2026-10-26_073210.md`).
Tick a point off when it was observed in the emulator and annotated; if a point turns out to be
unreachable, say so in its comments and here.

Rules for all tests:
- Disc: work on in-memory changes or on copies under `output/`; never save over `disk/`.
- Analysis: `analysis_status` before every `analysis_save` (0 conflicts, M1 must not drop);
  `output/tools/snapshot.sh` after every successful step; analysis off while programs other
  than VDOS run under CP/M. The &BE77 write breakpoint stays set (re-set after a GUI restart).

Never-read bytes ignored on purpose (clear what they are, but unreachable): `project/never_read_ignore.md`
(all 34 never-read bytes, 2026-10-26).

Never-read bytes in total (access map 2026-10-26 13:00): 34 - 26 in |XMON, 8 outside it; all on the ignore list.

---

## 1. |XMON

`|XMON` (#EA9E-#FD59): the monitor (vdos_rom_analysis.md 3.5.18). Rules for every test:
  snapshot before, `analysis_status` after (0 conflicts); no memory command on &C000-&FFFF
  while `xmon_rom` = 5 (set Y to &FF first); write tests, test files and loads only from &4000 - never into &BE00-&BFFF (XMON's own variables
  and stacks; owner 2026-10-26) (cpcxray writes always go to RAM, never to a ROM image, and
  are not in the access map - only reads of ROM 5 are a risk); &BE77 write
  breakpoint on; never save a changed disc image (I/O/@ W only on a copy, saved only when the
  owner asks). After A: check / restore &0080-&0094 and &AD76-&AD8A (A's buffer overwrites XMON's
  low-RAM copy - bug, doc 3.5.18).

  Done: start / `*` prompt / command recognition / ESC exit (BASIC), Z (complete), X, D
  (complete except a start at &FFxx - blocked), L (complete; test files in `output/xmon_l/`), R (complete), P (complete except a busy printer), A (complete; the system bank <> 0 branch
  simulated with (&001F) = &01), B (complete), C (complete), F (complete), G, T, M and S (complete), I and O (complete from BASIC on disc; tape via |CAS.IN / |CAS.OUT and the CP/M branch
  open; O round trip at &4000 on `output/xmon_o_test.dsk`, never saved), the non-hex key in
  `xmon_input_word` (&FAAC, observed in R).

  Stay never read for good (decided 2026-10-26; not traced further): proven unreachable
  (static list of all producers + an exhaustive run of every possible input, doc 3.5.18), and
  the data decoding checked - the bytes are table data, the source holds the data-decoded values,
  which match their neighbours (the raw values do not):
  - &F386-&F38D `xmon_mnemonics` entries &14 / &15: "POP",#09 / "PUSH" (duplicates of &28 / &2A);
  - &F585-&F587 `xmon_opcodes_c0` entry &CB: FF FF FF (prefix placeholder);
  - &F5BB-&F5BD `xmon_opcodes_c0` entry &DD: FF FF FF;
  - &F5EB-&F5ED `xmon_opcodes_c0` entry &ED: FF FF FF;
  - &F61B-&F61D `xmon_opcodes_c0` entry &FD: FF FF FF.

  **Not complete:**
  - [ ] **Y** - from BASIC done (&FF, &07, ESC); the CP/M branch (&EDFF) observed 2026-10-26. Open: the purpose of the
    second gate-array value with bits 6/5 in `xmon_ram_reader`.

  **Not started** (manual: "Der VDOS Befehl |XMON"):
  - [ ] **@** (`xmon_disc_monitor` &EA9E) - complete from BASIC 2026-10-26 (all 12 commands, `>>`,
    `E:xx`; doc 3.5.18). Open only: the CP/M branches &EB31 / &EB44 / &EBA8 (with XMON under CP/M,
    below) and &BE09 (`bdos_dph`) left at the disc monitor's SP after ESC - check under CP/M.
    Stay never read for good: the dead call &EAB8, the dead `jp` &ECFA. (&ED12-&ED1F: run on purpose
    2026-10-26, 14 NOPs.)
  - [x] **XMON under CP/M** - done 2026-10-26: XMON.COM checked (reads only (&C004), the name
    table and one jumpblock operand - all data already), |CPM,2, XMON -> CP/M branch &ED34-&ED3E
    observed ("(0100  0000  0100)", "*"); Y under CP/M observed (does nothing, xmon_rom stays 5 -
    so under CP/M no XMON memory command on &C000-&FFFF). The disc monitor's BIOS
    branches &EB31 / &EB44 / &EBA8 observed (R, W on the disc copy, L); ESC from @ and ESC = RST 0
    (&ED91, warm boot to A>) observed.

---

## 2. Outside |XMON

- [ ] **Rest of the CP/M start chain.**
  - (done 2026-10-26: `boot_no_cpm_disc` #C483-#C489 - `|CPM,1` with a blank system disc in A:
    (cpcxray draft), message, J = again, N = BASIC afresh; the read-error branch not tried.)
  - (done 2026-10-26: VDOS as ROM 0 - `output/machine_vdos_rom0.toml`, ROM copy
    `output/vdos211x_rom0.rom` as its own target rom0: boots straight into CP/M, `A>`; no new ROM
    byte read. Map / coverage: `output/vdos211x_rom0_boot.*`, trace up to the motor spin-up:
    `output/trace_rom0_boot.txt`.)
  - (done 2026-10-26: same machine, blank system disc in A:, N at "keine CP/M Diskette" ->
    `cpm_back_to_basic` -> KL FIND COMMAND "BASIC" never returns: the 464 ROM scan stops only at
    a type-&80 ROM, and VDOS answers every number with type &01. So #C49B `jp rsx_cpm` is not
    reached there either - commented as unreachable on the 464.)
  - Probably unreachable, comment as such: `jp l_c48a` after the AMSDOS CP/M boot (#C325-#C327,
    the AMSDOS boot does not return) and `jp rsx_cpm` when "BASIC" is not found (#C49B-#C49D).
- [ ] **Headers of the CP/M BIOS routines** (left out in the header pass): Input / Output /
  Changed for BOOT, WBOOT, SELDSK, HOME, SETTRK, SETSEC, SETDMA, READ, WRITE, SECTRAN and their
  ROM bodies, after DR's manual section 6.6 (`output/cpm22-m.txt`); check uncertain ones with
  marker registers.
- [ ] **Smaller remainders.**
  - `basic_error_patch` &BEAE-&BEB0: the CALL-token branch - test `CALL &xxxx,"text"`.
  - `hello_run` &BF32 (one byte of the HELLO loader): find its condition.
  - (done 2026-10-26: `fwb_fdc_sends` #CC19-#CC1B run by FDC status injection &D0.)
- [x] **`rel_no_data` (#D010-#D014, msg &37) - done 2026-10-26 by simulation:** |GET,1,2000 on a
  47-byte file with only record 1 (extent 5 missing) -> random_seek sets &FF (&E675), Z still set at
  &E5ED (the bug, observed); Z cleared by hand -> rel_no_data -> "Record leer" (the manual: error
  55 "Rekord enthaelt keine Daten"). Bugfix proposal in section 3.
- [ ] **Clean-up.**
  - Remove the stale "(not observed)" comments in the relative-file code (`random_call`,
    `read_random_body`, `write_random_body`, `random_seek`): they ran in the tests.
- [ ] **cpcxray developer notes** (write the instructions for the developer, with the why):
  - Access map: under CP/M the VDOS ROM is always paged in. Data reads of ROM 5 by code
    outside the ROM (a CP/M program in RAM, XMON's RAM reader) are recorded like VDOS's own
    reads, which pollutes the map. Wish 1: record (or optionally ignore) only data reads made
    by code inside the target. Wish 2: a way to replace or reset a map and database (today
    `m1map_load` / `analysis_load` only merge, and there are no backups on save).
  - Generator: a fully read string table is written as one `defb` of more than 128 bytes, which
    sjasmplus refuses (`xmon_mnemonics` after the ED test; worked around with one comment per
    entry). Wish: split long `defb` lines.
  - Generator: it leaves &BEA7, &BEAA, &BEB3, &BEB6 in `char_io_table` as hex, because they
    fall inside instructions of the vdos RAM copy at &BEA1...

Stay never read for good (decided, commented): `drive_a_flag` #CC28-#CC29 (never called); the
two-byte block maps #E06C-#E55B are not unreachable - used by any format with DSM >= 256 (e.g. a
user's driver with its own DPH / DPB); observed 2026-10-26 with a 2K-block DPB (`test_single_map`). (&FFC0-&FFFF: judged 2026-10-26 -
`rom_tail_copy`, a fully scrambled duplicate of &FF40-&FF7F, unreachable; read once on purpose.)

---

## 3. Bugfix proposals

Patches for bugs found during the analysis - to try later on a copy of the ROM (never change
`roms/`). Each one: where, why, the patch (decoded value and the byte in the scrambled ROM file),
and the test that shows it works. The place is also marked in the source with a comment block
starting `*** BUGFIX PROPOSAL`.

- [ ] **XMON L: RST &28 (FIRM JUMP) ignores its inline word.**
  - Bug: on the CPC, RST 1 (&08 LOW JUMP), RST 2 (&10 SIDE CALL), RST 3 (&18 FAR CALL) and
    RST 5 (&28 FIRM JUMP) are followed by a 2-byte inline word. XMON's table
    `xmon_opcodes_c0` gives RST 1-3 length 3 (byte 0 = &A6), but RST 5 length 1 (byte 0 =
    &26). So `EF 34 12` lists as `RST 28`, `INC (HL)`, `LD (DE),A` instead of one 3-byte
    instruction (observed 2026-10-26, `output/xmon_l/base_opcodes.bin`).
  - Where: only the table byte. No code tests the RST number - `xll_table` (&F114: bits 7-6
    of byte 0 = length - 1) and `xll_byte_loop` / &F15C (next address = after the length)
    treat every RST alike.
  - Patch: **&F5F1 &26 -> &A6** (entry &EF, byte 0); in the scrambled ROM file **offset &35F1:
    &2E -> &AE** (computed with the vortex decoder; &AE is the only raw value giving &A6).
    Result: `EF3412    RST  28`, like `CF3412    RST  08`.
  - Optional second patch (not tried): show the inline word as an operand - byte 2 of the
    entries &FF (none) -> &FE (nn): RST 1 &F593 (raw &F7 -> &F6), RST 2 &F5AB (raw &FF -> &FE),
    RST 3 &F5C3 (raw &FF -> &FE), RST 5 &F5F3 (raw &F7 -> &F6). Expected `RST 28,&1234`
    (path &F2D7-&F2EB as for `JP nn`); side effect: &FE also sets `xmon_branch_target`.
  - Test: a patched copy under `output/` in a test machine (config/machine.toml stays
    unchanged), `L` over `base_opcodes.bin` at &4000.

- [ ] **XMON L: `OUT (n),A` / `IN A,(n)` always show `(&F4)`.**
  - Bug: operand code &F9 = "(n)" (used only by the entries &D3 and &DB) jumps at &F2D2
    (`jr z,xlo_port`) straight to the output, without reading the port byte; H still holds &F4,
    the high byte of the name table pointer (observed: `D3 56` -> `OUT (&F4),A`). Code &FA does
    the same output correctly (reads H = n first) but no table entry uses it.
  - Patch (1 byte, no new space needed): **&F2D3 &57 -> &02** - the jr then goes to &F2D6
    (`ld hl,(xmon_list_address)`), reads the last two instruction bytes like &FA-&FE, and the
    `inc a` chain (&F9 -> &FA, &FB, &FC, &FD at &F30B, not zero) ends in `xlo_port` with H = n.
    In the scrambled ROM file **offset &32D3: &5F -> &0A** (operand byte, decoded; &0A is the
    only raw value giving &02). From reading the code only; not tried.
  - Alternative (2 bytes, table only): operand code &F9 -> &FA in the entries &D3 (&F59E, raw
    &D1 -> &D2) and &DB (&F5B7, raw &D1 -> &D2).
  - Test: `L` over `D3 56` / `DB 56`: expected `OUT (&56),A` / `IN A,(&56)`.
- [ ] **XMON O: ESC in an input leaves the output file open.**
  - Bug (observed 2026-10-26): `xmon_input_word` ends the command on ESC with `jp
    xmon_command_done`; O (&F011) has opened the file with CAS OUT OPEN before its three inputs,
    so ESC leaves it open (`XE.$$$` in the directory). The next O fails silently (file already
    open) and only frees the channel through `xco_abandon`; the third O works. The `.$$$` entry
    stays on the disc.
  - Patch idea: call CAS_OUT_ABANDON before CAS OUT OPEN (3 bytes) - or read the three values
    first and open the file afterwards (reorder &F017-&F032; the name must survive in &ACA5 and
    the values on the stack). No free byte found in O; the reorder needs no new space but HL /
    DE / B of the name must be set up again before CAS OUT OPEN - still to work out. First
    check that CAS_OUT_ABANDON with no file open is harmless in VDOS (not checked).
  - Test: `OB:XE.BIN` + ESC, then `OB:XF.BIN,4000,0032,4000` must write XF.BIN at once.

- [ ] **XMON @: T and G keep an invalid position after `>>`.**
  - Bug (observed 2026-10-26): `xdm_cmd_track` stores the track at &EB65 and `xdm_cmd_block` T / S
    at &EC8C / &EC91 before `xdm_check_block`; on `>>` the position past the last block stays set,
    and the next R / W / D uses it (observed: TA0 `>>`, then R -> `E:45`). A W there could write
    beyond the CP/M area. The manual says an input error changes nothing.
  - Patch idea: check first, then store - e.g. T: keep the old track (`push af` of sek_track) and
    put it back on the error path, or compute the check from A before `ld (sek_track),a`. Needs a
    few more bytes; candidate space: **&ED12-&ED1F (14 bytes, raw 00 = 14 NOPs - run on purpose, no
    reference found)** - also a candidate for the O patch (3 bytes) above. Still to work out.
  - Test: TA0 -> `>>` and T unchanged; GB1 -> `>>` and T / S unchanged.

- [ ] **|GET never reports "Record leer" (set_file_write_flag keeps Z).**
  - Bug (observed 2026-10-26): DR's setfwf uses ORI, which clears Z; VDOS's `set 7,(hl)` at
    &E10B keeps it, so after random_seek's error exit (&E678 `jp set_file_write_flag`)
    read_random_body (&E5ED `call z,sub_e4c2`) reads anyway and the code &FF becomes 1: a record
    in a missing extent reads as empty instead of "Record leer" (msg &37).
  - Patch idea (uses the free bytes): &E678 `jp &ED12` instead of `jp &E108`; at &ED12:
    `call &E0F9` (get_module) / `ld a,(hl)` / `or #80` / `ld (hl),a` / `ret` (8 of the 14 NOPs).
    Only the error exit changes. Opcodes raw, operands scrambled - the raw bytes still to be
    computed with the vortex encoder. Not tried.
  - Test: the simulation scenario without the hand-made Z: |GET,1,2000 -> "Record leer".

- [ ] **CAT shows up to 2K too much free space** (4.5b): `dir_print_free` tests bits 7, 0, 1 of
  the last ALV byte; bits 0 / 1 (no blocks there) count as free. Patch still to work out - first
  check whether it fits in place.
- [ ] **CAT shows file sizes over 512K modulo 512K** (4.5b): `dir_compare_names` / the size
  loop use the extent byte only, not the module byte S2. Patch still to work out; probably needs
  more code than fits in place.

- [ ] **XMON L: ED &8B is shown as `OTDR`.**
  - Bug: `xll_ed_high` (&F1C5) starts with `cp #8B` / `ld a,#45` (OTDR). ED &8B is no Z80
    instruction; OTDR is ED &BB, which the block formula already gives (observed: both ED 8B and
    ED BB show `OTDR`).
  - Patch (1 byte, in place): **&F1C6 &8B -> &00** - A is &7C or more here, so the compare never
    matches and ED &8B falls through to "-??-". In the scrambled ROM file **offset &31C6:
    &AB -> &20** (operand byte; &20 is the only raw value giving &00). From reading the code
    only; not tried.
  - Test: `L` over `ED 8B` / `ED BB`: expected `-??-` / `OTDR`.

- [ ] **XMON L: DD / FD display weaknesses** (observed 2026-10-26, doc 3.5.18). No patch worked
  out yet; most need more code than fits in place:
  1. invalid `DD xx` / `FD xx` (and `DD CB d` + odd op) shown as 3 bytes, one too many:
     `xll_index_op` (&F25F) jumps to `xll_invalid` (length 2), and `xll_show` (&F13D) adds 1 for
     the prefix. Better: show the prefix alone (1 byte) and go on with xx.
  2. `DD CB d 36` (SLL) shown as `SRL`: &F228 `cp #07 / jr nz / dec a` maps 7 to 6, so 6 and 7
     both give mnemonic &10. Better: y = 6 -> "-??-" (as the CB branch does at &F0ED).
  3. undocumented `DD CB d op` with a register (low bits <> 6) shown as the plain (IX+d) form:
     only bit 0 is checked at &F219. Better: low bits <> 6 -> "-??-".
  4. displacement shown unsigned (`(IX+&FD)` for -3); cosmetic.

- [ ] **XMON R switches the printer echo off.**
  - Bug: `xmon_edit_word` (&F9D6) shows each value with `xmon_hex_byte_quiet` twice and never puts
    the switch back (&BEFE -> &BEFF); the second call saves the cleared switch. Observed: P on,
    R, RETURN -> &BEFE / &BEFF 01 01 -> 00 00.
  - Patch (2 bytes, in place): call `xmon_hex_byte` (&FA28) instead of `xmon_hex_byte_quiet`
    (&FA1B) at &F9DF and &F9E3: **&F9E0 &1B -> &28** (raw offset **&39E0: &1B -> &28**) and
    **&F9E4 &1B -> &28** (raw offset **&39E4: &3B -> &08**). The switch is then never touched,
    and the printer gets the final value of each register. Not tried.
  - Test: P on, R, a few RETURNs: &BEFF stays 01.

- [ ] **XMON A destroys XMON's copy of the user's RAM &0080-&0094.**
  - Bug: `xmon_input_line` (&EE3F) fills its buffer &ACA5-&ADA3 (C = 255 from A) with spaces and
    puts the text there; XMON's low-RAM copy (`xmon_save_low_ram`, &AD76-&AD8A) lies inside it.
    The next read from &8000 on writes spaces / text into &0080-&0094 (observed: `A9000,Z`,
    `D8000,8001` -> 21 spaces at &0080). Under CP/M &0080 is the command line / DMA buffer.
  - Patch (1 byte, in place): A's maximum **&FCD2 &FF -> &D1** (209 characters; the buffer then
    ends at &AD75, just below the copy); raw offset **&3CD2: &F7 -> &D9**. Only A calls
    `xmon_input_line`, so nothing else changes. Not tried. (Moving the copy would keep 255
    characters but needs more changes.)
  - Test: `A9000,Z`, `D8000,8001`: &0080-&0094 unchanged.

- [ ] **XMON T: bugs of the single step** (all observed 2026-10-26, doc 3.5.18).
  1. After a done RET (`xtr_ret` &F82A) the step count becomes the return address and the next
     listing starts at the user SP - T runs away and can lose control. Patch (1 byte, in place):
     **&F839 &31 -> &2A** (jp &F92A instead of jp &F931; raw offset **&3839: &39 -> &22**) - HL = PC
     and DE = the count are loaded again (the RET step itself is then not counted). Not tried.
  2. RET cc is always taken (`xtr_ret` does not test the condition). Needs code (test the
     condition against the user F) - no patch yet.
  3. RST &00 / &20 / &30 / &38 are done like a RET (&F826 falls into `xtr_ret`). Better: treat
     them as "next instruction" (RST 4 RAM LAM returns there). No patch yet.
  4. RST &08 / &28: `POP HL` at &F86F without a `PUSH HL` (&F804 -> &F860). A word from XMON's
     stack becomes the "next" address, F7 is written there, XMON's SP moves. No patch yet (needs
     a PUSH HL on that path).
  5. A jump to itself (DJNZ $ / JR $) never runs; 6. after RST &10 / &18 the code to the caller
     runs unstepped - design weaknesses.

- [ ] **XMON M: an overlapping copy upwards lands one byte too high.**
  - Bug: `xcm_backward` (&F786) sets DE = target + length (the `INC BC` at &F78E comes before the
    `ADD HL,BC`), one too high. Observed: `M4000,4003,4002` on `11 22 33 44 55 66 77` ->
    `11 22 33 11 22 33 44` instead of `11 22 11 22 33 44 77`.
  - Patch (5 bytes, in place, no new space): reorder &F78E-&F792 `03 E1 EB 09 EB` ->
    `E1 EB 09 EB 03` (ld b,h / ld c,l / pop hl / ex de,hl / add hl,bc / ex de,hl / inc bc); the
    same bytes at file offset &378E-&3792 (opcodes are stored unscrambled). Not tried.
  - Test: `M4000,4003,4002` -> `11 22 11 22 33 44 77`.
- [ ] **XMON M: an end below the start copies nearly 64K** (read, not tried) - a guard
  (`jr c` to the prompt after the length) needs a few bytes.

Space for patches that do not fit in place: &ED12-&ED1F (14 NOPs, no reference) and &FFC0-&FFFF
(64 bytes, `rom_tail_copy`: a fully scrambled duplicate of &FF40-&FF7F that nothing reaches or
copies - checked 2026-10-26, safe to overwrite).
