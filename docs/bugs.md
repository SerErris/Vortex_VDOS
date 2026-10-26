# VDOS 2.11-X - bugs found, and how to fix them

All bugs found while analysing VDOS 2.11-X (`roms/vdos211x.rom`, ROM 5) in the cpcxray
emulator, 2026-10-24 to 2026-10-26. Each entry: where (address and label in
`project/vdos211x.asm`), what happens (observed or read), why, the fix, and a test. The places
are also marked in the source with `*** BUG` / `*** BUGFIX PROPOSAL` comments.

**Patch values - two ROM files:**
- `output/vdos211x_decoded.rom` (the clear image: every byte as the CPU sees it): write the
  **decoded value** at the address (file offset = address - &C000).
- `roms/vdos211x.rom` (the original, scrambled for the Vortex decoder): opcode bytes are stored
  unchanged, operand and data bytes scrambled - write the **raw value** given here. Where only an
  idea exists, the raw bytes still have to be computed with the vortex encoder.
- Never change `roms/`; try every patch on a copy, in a test machine under `output/`.

**Space for longer patches:** &ED12-&ED1F (14 NOPs, nothing refers to them) and &FFC0-&FFFF
(64 bytes, `rom_tail_copy`, an unreachable duplicate of &FF40-&FF7F).

None of the patches has been tried yet.

## Overview

| # | Area | Bug | Fix | Effort |
|---|---|---|---|---|
| 1 | relative files | `\|GET` never reports "Record leer" | jump + 8 bytes in the free NOPs | small, free space |
| 2 | relative files | `\|FILES` with maximum length 0 accepted | idea | small |
| 3 | relative files | channel >= 128 in `\|FILES`: wrong message | idea | 1-2 bytes |
| 4 | relative files | record lengths 256, 512 ... unusable | idea | small |
| 5 | relative files | literal strings in `\|PUT` leak BASIC temporary strings | workaround | - |
| 6 | CAT | up to 2K too much free space | idea | small |
| 7 | CAT | file sizes over 512K shown modulo 512K | idea | larger |
| 8 | files | ASCII file end: rest of the last record not filled | idea | small |
| 9 | `\|ATTRIBUT` | a wildcard changes only the first file | idea | larger |
| 10 | `\|ATTRIBUT` | an empty name is not refused | idea | small |
| 11 | `\|FORMAT` | values with a high byte accepted | idea | small |
| 12 | SIO | both DART channels share one WR5 copy | idea | 1 byte |
| 13 | CP/M | WBOOT on a write-protected disc says "keine CP/M Diskette" | message | small |
| 14 | XMON L | RST &28 ignores its inline word | 1 byte | in place |
| 15 | XMON L | `OUT (n),A` / `IN A,(n)` show `(&F4)` | 1 byte | in place |
| 16 | XMON L | ED &8B shown as `OTDR` | 1 byte | in place |
| 17 | XMON L | DD / FD display weaknesses | ideas | larger |
| 18 | XMON R | switches the printer echo off | 2 bytes | in place |
| 19 | XMON A | destroys XMON's copy of &0080-&0094 | 1 byte | in place |
| 20 | XMON T | runs away after an emulated RET | 1 byte | in place |
| 21 | XMON T | RET cc, RST, jump-to-self weaknesses | ideas | larger |
| 22 | XMON M | overlapping copy upwards one byte too high | reorder 5 bytes | in place |
| 23 | XMON M | end below the start copies nearly 64K | guard | small, free space |
| 24 | XMON O | ESC in an input leaves the output file open | idea | 3 bytes |
| 25 | XMON @ | T and G keep an invalid position after `>>` | idea | small, free space |

---

## Relative files (|FILES / |OPEN / |FIELD / |GET / |PUT)

### 1. |GET never reports "Record leer" (error 55)

- **Where:** `set_file_write_flag` &E108 (`set 7,(hl)` at &E10B); `random_seek` error exit
  `rsk_error` &E66E (`jp set_file_write_flag` at &E678); `read_random_body` &E5ED
  (`call z,read_seq_core`); `rsx_get` &CFC6 (`jr z,rel_no_data`).
- **What happens (observed):** a record in an extent that does not exist (e.g. `|GET,1,2000` on a
  file with only record 1) reads as an empty record, not as error 55 (2.11-X text "Record leer",
  msg &37; the manual: "Rekord enthält keine Daten").
- **Why:** `random_seek` sets the return code &FF and leaves through `set_file_write_flag`. DR's
  BDOS sets the bit with `ORI 80h`, which clears Z; VDOS's `SET 7,(HL)` leaves Z set, so
  `read_random_body` reads anyway and the code &FF becomes 1. Simulated: with Z cleared by hand
  at &E5ED, `rel_no_data` runs and "Record leer" appears.
- **Fix:** &E678 `jp &ED12` instead of `jp set_file_write_flag`; at &ED12 (free NOPs):
  `call get_module` (&E0F9) / `ld a,(hl)` / `or #80` / `ld (hl),a` / `ret` (8 bytes) - Z is then
  clear as in DR. Only the error exit changes; open / make keep the old routine.
  Decoded image: &E678 `C3 12 ED`, &ED12 `CD F9 E0 7E F6 80 77 C9`. Scrambled file: opcodes as
  given, the operand bytes (&E679-&E67A, &ED13-&ED14, &ED17) still to be encoded.
- **Test:** the simulation without the hand-made Z: a file with record 1, `|GET,1,2000,@a$` ->
  "Record leer".

### 2. |FILES with a maximum length 0 is not refused

- **Where:** `rsx_files` &D17A (&D197 / &D1B6).
- **What happens (read):** a maximum record length 0 is accepted.
- **Why:** A = &21 ("Eingabefehler") is loaded, but CY stays clear (&D197), so the `jp c` at &D1B6
  is skipped.
- **Fix:** set CY on that path (e.g. `scf` before the test, or test for 0 with `or a` / `jp z`).
  Needs one or two bytes - check the code around &D197 for room.
- **Test:** `|FILES,1,0` -> "Eingabefehler".

### 3. A channel >= 128 in |FILES gives "Eingabefehler", not "Kanalnummer falsch"

- **Where:** `rsx_files` (the channel check), `error_bad_name`.
- **Why:** &2C (msg "Kanalnummer falsch") is loaded, but the path jumps to `error_bad_name`, which
  loads &21 itself.
- **Fix:** jump to `error_message` (with A = &2C) instead of `error_bad_name` on that path.
- **Test:** `|FILES,128,100` -> "Kanalnummer falsch".

### 4. Record lengths 256, 512, ... are unusable

- **Where:** the "open" test in `rsx_field` (&CF4B: `ld a,#00 / or l / ... jp z` - only L,
  the low byte of the record length).
- **What happens (observed):** `|OPEN ...,256` is accepted, then `|FIELD` says "Kanal nicht offen".
- **Why:** the test looks at the low byte of the record length only; for 256, 512 ... it is 0.
- **Fix:** test both bytes (`ld a,(ix+5) / or (ix+6)`), or keep a separate "open" flag.
- **Test:** `|OPEN,"T.REL",256,1`, `|FIELD,1,100,100,56`, `|PUT` / `|GET` work.

### 5. Literal strings in |PUT leak BASIC's temporary strings

- **Where:** `basic_error_patch` (RAM &BEA1) / the |PUT string handling.
- **What happens (observed):** the 5th `|PUT` with two literal strings -> "String expression too
  complex", and BASIC can be in a bad state after it. The manual's own example
  `|PUT,1,15,"Mueller",...` therefore works only a few times.
- **Fix:** release the temporary string descriptors after the copy (as BASIC's own commands do),
  or refuse literals. Workaround for users: pass variables (`@a$`).

## CAT

### 6. CAT shows up to 2K too much free space

- **Where:** `dir_print_free` &D7C5 (doc 4.5b).
- **What happens (observed):** a completely full 3" disc shows "167K in 5 Files, 2K frei"; correct
  is 169K / 0K (all 171 ALV bits set).
- **Why:** in the last ALV byte the bits 7, 0, 1 are tested; bits 0 / 1 belong to no block and
  count as free.
- **Fix:** count only the bits up to DSM in the last byte (mask with the bits that exist), or count
  free blocks over 0..DSM instead of byte by byte. Work out whether it fits in place.
- **Test:** a full disc -> "0K frei".

### 7. CAT shows file sizes over 512K modulo 512K

- **Where:** `dir_compare_names` &DA3A / the size loop of CAT.
- **What happens (observed):** a 516K file shows as "512K" (the total line is right).
- **Why:** only the extent byte is used, not the module byte S2.
- **Fix:** add S2 x 512K (S2 x 32 extents) to the size. Probably needs more code than fits in
  place.
- **Test:** a file over 512K on drive B -> its real size.

## Files

### 8. ASCII files: the rest of the last record is not filled with &1A

- **Where:** `out_flush_buffer` &D65C.
- **What happens (observed):** an 80K ASCII file on drive B ended with `&1A "=0" CR LF "50 WHILE
  NOT E"` - old bytes of the record buffer. Readers that stop at &1A (CP/M, `|DERROR,2`) are fine;
  with the default (`|DERROR,3`) BASIC read 1202 lines instead of 1200.
- **Why:** only one &1A is written after the data; the rest of the record keeps whatever the
  record buffer held.
- **Fix:** fill the rest of the record with &1A (as CP/M and AMSDOS do).
- **Test:** write 1200 lines, read back with the default setting -> 1200 lines.

## |ATTRIBUT and |FORMAT

### 9. |ATTRIBUT with a wildcard changes only the first matching file

- **Where:** `rsx_attribut`, `set_attributes` / `sa_loop` &E1C2.
- **Why:** `open_file` writes the found name into the FCB, so `set_attributes` then matches only
  that one file.
- **Fix:** keep the search pattern in a separate FCB and loop with search first / next.

### 10. |ATTRIBUT with an empty name is not refused

- **What happens:** an empty name is searched for as a blank name; the error is "not found"
  instead of "Eingabefehler".
- **Fix:** test the name length and jump to `error_bad_name`.

### 11. |FORMAT accepts values with a high byte

- **What happens (observed):** `|FORMAT,257` formats drive A (only the low byte is checked).
- **Fix:** check the high byte too (as the other RSX parameter checks do).

## SIO

### 12. Both DART channels share one WR5 copy

- **Where:** `dart_init_channel` &C767 (`dic_store_wr5`), `sio_wr5` &BE01.
- **What happens (observed):** &BE01 = &00, &BE02 = &6A - channel A's copy is never written.
- **Why:** the channel is told apart by `bit 0,c` of the control port, but bit 0 is 1 for both
  &FADD and &FADF. No effect today, because both channels use the same WR5 (&6A).
- **Fix:** test bit 1 of the port (&DD / &DF differ there) - one operand byte of the BIT.

## CP/M

### 13. WBOOT on a write-protected disc says "keine CP/M Diskette"

- **Where:** `wboot_no_cpm_disc` &C4A3.
- **What happens (observed):** the deblocking flush before the warm boot fails on a
  write-protected disc, and the message is "keine CP/M Diskette - Wiederholen J/N ?" although the
  disc is a good CP/M disc.
- **Fix:** give the flush its own message ("Diskette hat Schreibschutz", msg &08) before the warm
  boot message.

## XMON - L (disassembler)

### 14. RST &28 (FIRM JUMP) ignores its inline word

- **Where:** `xmon_opcodes_c0` entry &EF, byte 0 at &F5F1.
- **What happens (observed):** `EF 34 12` lists as `RST 28`, `INC (HL)`, `LD (DE),A`; RST 1-3 are
  listed as 3 bytes.
- **Why:** the table gives RST 5 length 1 (&26), RST 1-3 length 3 (&A6).
- **Fix:** &F5F1 &26 -> **&A6**; scrambled file offset &35F1: &2E -> **&AE**. Optional: show the
  word as an operand - byte 2 of the RST 1 / 2 / 3 / 5 entries &FF -> &FE (&F593, &F5AB, &F5C3,
  &F5F3; raw &F7 -> &F6, &FF -> &FE, &FF -> &FE, &F7 -> &F6).
- **Test:** L over `EF 34 12` -> one line `RST 28`.

### 15. OUT (n),A / IN A,(n) always show (&F4)

- **Where:** `xmon_list_operand`, &F2D2 (`jr z,xlo_port`).
- **Why:** operand code &F9 jumps to the output before the port byte is read; H still holds &F4.
- **Fix:** &F2D3 &57 -> **&02** (the jr goes on to the byte reader); scrambled offset &32D3: &5F ->
  **&0A**. Alternative: operand code &F9 -> &FA in the entries &D3 (&F59E) and &DB (&F5B7), raw
  &D1 -> &D2.
- **Test:** `D3 56` / `DB 56` -> `OUT (&56),A` / `IN A,(&56)`.

### 16. ED &8B is shown as OTDR

- **Where:** `xll_ed_high` &F1C5 (`cp #8B` / `ld a,#45`).
- **Why:** a special case for ED &8B; OTDR is ED &BB, which the formula already gives.
- **Fix:** &F1C6 &8B -> **&00** (the compare never matches); scrambled offset &31C6: &AB -> **&20**.
- **Test:** `ED 8B` -> `-??-`, `ED BB` -> `OTDR`.

### 17. DD / FD display weaknesses

1. Invalid `DD xx` / `FD xx` (and `DD CB d` + an odd op) are shown as 3 bytes, one too many
   (`xll_index_op` &F25F -> `xll_invalid`, `xll_show` adds 1 for the prefix). Better: show the
   prefix alone and go on with xx.
2. `DD CB d 36` (SLL) is shown as `SRL` (&F228 maps 7 to 6). Better: "-??-".
3. Undocumented `DD CB d op` with a register (low bits <> 6) is shown as the plain (IX+d) form
   (only bit 0 tested at &F219). Better: "-??-".
4. The displacement is shown unsigned (`(IX+&FD)` for -3) - cosmetic.

No patch worked out; most need more code than fits in place.

## XMON - R, A, T, M, O

### 18. R switches the printer echo off

- **Where:** `xmon_edit_word` &F9D6 (calls at &F9DF / &F9E3).
- **What happens (observed):** P on, R, RETURN -> &BEFE / &BEFF 01 01 -> 00 00.
- **Why:** each value is shown with `xmon_hex_byte_quiet` twice; the switch is never put back.
- **Fix:** call `xmon_hex_byte` (&FA28) instead of `xmon_hex_byte_quiet` (&FA1B): &F9E0 &1B ->
  **&28**, &F9E4 &1B -> **&28**; scrambled offsets &39E0: &1B -> **&28**, &39E4: &3B -> **&08**.
- **Test:** P on, R, some RETURNs: &BEFF stays 01.

### 19. A destroys XMON's copy of the user's RAM &0080-&0094

- **Where:** `xmon_cmd_ascii` &FCC5 (`ld c,#FF` at &FCD1), `xmon_input_line` &EE3F.
- **What happens (observed):** after `A9000,Z` the next read from &8000 on writes 21 spaces into
  &0080-&0094 (under CP/M the command line / DMA buffer).
- **Why:** the text buffer &ACA5-&ADA3 (255 bytes) contains the low-RAM copy &AD76-&AD8A, and the
  input routine fills the whole buffer with spaces.
- **Fix:** A's maximum 255 -> 209: &FCD2 &FF -> **&D1**; scrambled offset &3CD2: &F7 -> **&D9**
  (the buffer then ends at &AD75, below the copy).
- **Test:** `A9000,Z`, `D8000,8001`: &0080-&0094 unchanged.

### 20. T runs away after an emulated RET

- **Where:** `xtr_ret` &F82A, the jump at &F838.
- **What happens (observed):** after a stepped RET the step count becomes the return address, the
  next listing starts at the user SP; in a `JR $` loop XMON lost control.
- **Fix:** &F839 &31 -> **&2A** (`jp &F92A` instead of `jp &F931`: HL = PC and DE = count are
  loaded again); scrambled offset &3839: &39 -> **&22**.
- **Test:** T over a CALL / RET pair: the listing goes on after the CALL.

### 21. T: further single-step weaknesses (observed)

1. RET cc is always taken - `xtr_ret` does not test the condition against the user F.
2. RST &00 / &20 / &30 / &38 are done like a RET (&F826 falls into `xtr_ret`); better: "next
   instruction".
3. RST &08 / &28: `POP HL` at &F86F without a `PUSH HL` (&F804 -> &F860) - a word of XMON's stack
   becomes the next address, F7 is written there.
4. A jump to itself (`DJNZ $` / `JR $`) never runs.
5. After RST &10 / &18 the called code runs unstepped.

No patches yet; 1, 3 need extra code (free space).

### 22. M: an overlapping copy upwards lands one byte too high

- **Where:** `xcm_backward` &F786 (`INC BC` at &F78E before `ADD HL,BC`).
- **What happens (observed):** `M4000,4003,4002` on `11 22 33 44 55 66 77` -> `11 22 33 11 22 33 44`
  instead of `11 22 11 22 33 44 77`.
- **Fix:** reorder &F78E-&F792 `03 E1 EB 09 EB` -> **`E1 EB 09 EB 03`** (one-byte opcodes, the same
  bytes in both files, offset &378E-&3792).
- **Test:** `M4000,4003,4002` -> `11 22 11 22 33 44 77`.

### 23. M: an end below the start copies nearly 64K (read)

- **Fix:** after the length is computed, `jr c` to the prompt (a guard of a few bytes; free space).
- **Test:** `M4003,4000,5000` -> nothing copied.

### 24. O: ESC in an input leaves the output file open

- **Where:** `xmon_cmd_output` &F011 (CAS OUT OPEN at &F01A before the three `xmon_input_word`).
- **What happens (observed):** `OB:XE.BIN` + ESC leaves `XE.$$$`; the next O fails silently (file
  already open) and only frees the channel; the third O works. The `.$$$` entry stays.
- **Why:** ESC in `xmon_input_word` jumps straight to `xmon_command_done`.
- **Fix:** call CAS OUT ABANDON before CAS OUT OPEN (3 bytes, through the free space), or read the
  three values first and open the file afterwards. Check first that CAS OUT ABANDON with no file
  open is harmless in VDOS.
- **Test:** `OB:XE.BIN` + ESC, then `OB:XF.BIN,4000,0032,4000` writes XF.BIN at once.

### 25. @ (disc monitor): T and G keep an invalid position after ">>"

- **Where:** `xdm_cmd_track` &EB5F (store at &EB65), `xdm_cmd_block` &EC66 (stores at &EC8C /
  &EC91), `xdm_check_block` &EB6E.
- **What happens (observed):** `TA0` -> `>>`, but T stays &A0; the next R -> `E:45`. A W there
  could write beyond the CP/M area. The manual says an input error changes nothing.
- **Fix:** check first, then store - e.g. keep the old track / record and put them back on the
  `xdm_error` path, or check from A / HL before the stores. A few bytes; free space &ED12.
- **Test:** `TA0` -> `>>`, T unchanged; `GB1` -> `>>`, T / S unchanged.

---

## Not bugs, but worth knowing

- **|CPM without a parameter** jumps into AMSDOS's CP/M loader without a firmware reset; the RSX
  chain still points into VDOS's RAM block at &A6F8, which CP/M's system tracks overwrite, so
  AMSDOS.COM's KL FIND COMMAND "BASIC" may walk a garbage chain ("BASIC not found"). Workaround:
  `|AMSDOS` first, or reset.
- **XMON under CP/M:** Y does nothing there, `xmon_rom` stays 5 - every memory command on
  &C000-&FFFF shows VDOS.
- **XMON I** cannot load files without an AMSDOS header (VDOS reports length 0).
- **Message texts differ from the manual (2.0):** "Kanal bereits offen" / "Kanal nicht offen" /
  "Recordnummer zu gross" / "Record leer"; the disc monitor prints "E:xx" instead of "ERR:xx".
- **Dead code** (no effect): `call xdm_read_record` at &EAB8, `jp xds_done` at &ECFA, see
  `project/never_read_ignore.md`.
