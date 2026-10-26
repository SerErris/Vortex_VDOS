# Vortex VDOS

A fully commented disassembly of **VDOS 2.11-X**, the disc operating system ROM (16K, upper ROM)
of the Vortex X disc drives for the Amstrad CPC 464 (vortex GmbH, 1986), with its documentation.
VDOS is public domain (vortex letter of 13 Feb 1995, `docs/VDOSisPD.pdf`). Public repository:
https://github.com/SerErris/Vortex_VDOS.

The owner writes in German; reply in German. Code, comments and the English documents stay in
English; the user manual is German.

## Files

| Path | What | Rules |
|---|---|---|
| `src/VDOS-2.11-X.asm` | the commented sjasmplus source of the original ROM | the **reference**: must keep building byte-identical to the release ROM; no bug fixes here |
| `docs/vdos_rom_analysis.md` | the analysis: ROM layout, RSX commands, disc BIOS, internal BDOS, CP/M boot, XMON, RAM map, tests | English |
| `docs/bugs.md` | all 25 known bugs: place, behaviour, cause, fix (patch bytes), test | English; the base for 2.12-X |
| `docs/todo.md` | open points of the analysis | English |
| `docs/Vortex_X-Laufwerke_Manual_2.11-X.md` | the user manual (German), the 2.0 original updated for 2.11-X, with the chapter "Bekannte Fehler in VDOS 2.11-X" | keep the style of the original; edit minimally |
| `docs/VDOSisPD.pdf` | the public domain letter | never change |
| `rom/` | build output (ROM images) | in `.gitignore` - never commit |
| `docs/Vortex_X-Laufwerke_Manual_EN_2.11-X.md` | the US English translation of the manual (screen output still German) | keep in step with the German manual |
| `tools/build_index.py`, `tools/index_terms_*.txt` | builds the linked index of both manuals | run after every manual change (see `src/MAINTAIN.md`) |
| `src/MAINTAIN.md` | maintainer notes: what a release contains, how to build and upload | maintainer only |

## Build and check

```
mkdir -p rom
cd rom
sjasmplus ../src/VDOS-2.11-X.asm      # sjasmplus is /usr/local/bin/sjasmplus
sha256sum VDOS-2.11-X.rom
```

`OUTPUT` in the source writes to the current directory, so always assemble from `rom/`. The
2.11-X image is 16384 bytes, SHA-256
`cdff2b5e372c740dd5bdf351b89d9ce955d07ba974b144ba4bc2475afcbfac5b`. Check this after every change
to `src/VDOS-2.11-X.asm` (comments only - the bytes must not change).

## The ROM

- The original EPROM on the Vortex controller is **scrambled**: opcode fetches (M1) pass
  unchanged, every other read (operands, data, tables) is decoded by the controller. The source
  here is the **decoded** image (every byte as the CPU sees it). It runs in a normal upper ROM
  slot, not in the controller socket. A scrambled image for the controller socket would need the
  vortex encoder, which is not in this repository.
- Header `01 21 03`: background ROM, mark 1, version 2.1 (BCD), modification 3.
- Layout (details in `docs/vdos_rom_analysis.md` 2.2): BIOS &C000-&CE5A, DOS / RSX commands /
  messages up to &EA9D, XMON monitor &EA9E-&FD59, |FAST &FD5A, |ROMCAT &FE74-&FFBF.
- Free space for patches: &ED12-&ED1F (14 NOPs, unreferenced) and &FFC0-&FFFF (64 bytes,
  `rom_tail_copy`, an unreachable duplicate of &FF40-&FF7F).

## Next work: VDOS 2.12-X (bug fixes)

The owner's plan: bug fixes are made **only in the assembler source of a new version**, not in
2.11-X.

1. Copy `src/VDOS-2.11-X.asm` to `src/VDOS-2.12-X.asm`, set `OUTPUT "VDOS-2.12-X.rom"` and
   change the version where it shows (the header bytes at &C001-&C003 and the sign-on message
   &0E " (C)1986   VDOS 2.11-X by vortex GmbH").
2. Fix the bugs one at a time from `docs/bugs.md`. Each entry gives the place (address and
   label), the cause and a proposed fix; in the source the places are marked with `*** BUG` /
   `*** BUGFIX PROPOSAL` comments. None of the patches has been tried yet.
3. Keep the code layout where possible: the RSX jumpblock at &C006, the extended BIOS jumpblock
   &C093, the CP/M BIOS jumpblock &C0D2 and the CAS jump table &C12D are entry points that other
   programs (CP/M, INSTALL, FILECOPY ...) call by address. Longer patches go into the free space,
   reached by a jump.
4. Comment every change in the source style (a line comment saying what the code means and that
   it is a 2.12-X fix, with the bug number from `docs/bugs.md`).
5. Each fix needs a test. There is no emulator in this repository; the owner tests in the CPC
   X-Ray emulator in the analysis project `/home/chris/vdosdecode` (MCP server `cpcxray` /
   `cpcxray-gui`). Say which fixes were tested and which only assembled.
6. Update `docs/bugs.md` (state per bug) and the manual's bug chapter for 2.12-X.

## Source conventions

- sjasmplus syntax, hex as `#C000` in code; in comments CPC notation `&C000`.
- Labels lowercase with underscores; firmware names uppercase (`TXT_OUTPUT`, `KL_FIND_COMMAND`).
- A header block per routine (Subroutine, Tasks, Input, Output, Called by, Calls) and a comment on
  nearly every line that says what it means, not what the instruction does.
- Never present a guess as a fact: say "observed" (seen in the emulator) or "read" (from the
  code).

## Releases

- Every release carries **two assets: the ROM file and the current manual**; after any change of
  the manual it is uploaded again to the current release. The procedure (commands) is in
  `src/MAINTAIN.md`.
- Release and upload instructions are for the maintainer only: never put them into `README.md`
  (that is for end users).
- Commit, push and release only when the owner asks; publishing is outward-facing. End commit
  messages with the attribution line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Not part of this repository: the emulator working files of the analysis project (annotations,
  access maps, traces, test discs, `never_read_ignore.md`, the work log).
