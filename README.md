# Vortex VDOS 2.11-X

A fully commented disassembly of **VDOS 2.11-X**, the disc operating system ROM of the Vortex
X disc drives for the Amstrad CPC 464 (vortex GmbH, 1986).

The source in `src/` reassembles byte for byte into a **decoded** 16K ROM image. Every routine,
variable and table is named and commented. The comments say what the code does and why, and
whether a behaviour was observed in an emulator or only read from the code.

VDOS is **public domain**: vortex Computersysteme GmbH released it in 1995 (see
[License](#license-public-domain)). Download the ROM:
**[VDOS-2.11-X.rom](https://github.com/SerErris/Vortex_VDOS/releases/download/v2.11/VDOS-2.11-X.rom)**
(release [v2.11](https://github.com/SerErris/Vortex_VDOS/releases/tag/v2.11)).

## The ROM and its scrambling

The original EPROM on the Vortex controller is scrambled. The controller's logic passes opcode
fetches (Z80 M1 cycles) through unchanged and decodes every other read: operands, data and
tables. The file is therefore not readable as Z80 code as it is.

This disassembly was made by running VDOS in an emulator that applies the same decoding, and by
recording for every ROM byte whether it is fetched as an opcode or read as data (the access map).
With that map each byte can be written as the CPU sees it, and the result is a plain ROM that
needs no decoding hardware.

- Bytes read as opcodes: 7981. Bytes read as data: 8369. Bytes read both ways: 0.
- Never read: 34 bytes: dead code and unused table entries, see `docs/vdos_rom_analysis.md`.

## Files

| Path | Content |
|---|---|
| `src/VDOS-2.11-X.asm` | the commented source (sjasmplus) |
| `docs/vdos_rom_analysis.md` | the analysis: ROM layout, RSX commands, disc BIOS, internal BDOS, CP/M boot, XMON monitor, RAM variables, tests |
| `docs/bugs.md` | all bugs found, with the place, the cause and how to fix them |
| `docs/todo.md` | open points of the analysis |
| `docs/VDOSisPD.pdf` | vortex's letter of 13 February 1995 that releases VDOS as public domain |

The documents mention working files of the analysis (emulator configurations, test discs,
traces under `output/`, the cpcxray annotation file); those are not part of this repository.

## Building

```
cd src
sjasmplus VDOS-2.11-X.asm
```

This writes `VDOS-2.11-X.rom` (16384 bytes) next to the source; it is identical to the release
file (SHA-256 `cdff2b5e372c740dd5bdf351b89d9ce955d07ba974b144ba4bc2475afcbfac5b`).

## Using the ROM

The release `v2.11` has the decoded ROM `VDOS-2.11-X.rom`.

- Put it into a **normal upper ROM slot** (a ROM board, e.g. slot 5 as in the original set-up), not into the socket of
  the Vortex controller: the controller would scramble the already decoded bytes again.
- VDOS needs disc hardware: the uPD765 FDC at &FB7E / &FB7F and the motor port &FA7E (the 3"
  drive through a DDI-1 compatible interface), and the Vortex drives for drive B:. The Vortex RAM
  expansion (port &FBBD) is only needed for its bank functions.
- With AMSDOS in ROM 7, VDOS shares AMSDOS's data area; without AMSDOS it reserves its own.

## Status

The 2.11 release is the original VDOS 2.11-X, unchanged: the source documents the ROM as it
is, bugs included. The bugs are listed in `docs/bugs.md`; fixes are planned for a new version
(2.12-X), made in the source.

## License: public domain

VDOS was written by vortex GmbH (© 1986). In a letter of **13 February 1995** vortex
Computersysteme GmbH, Flein (signed by the managing director Monika Armbruster), released the
disc operating system VDOS for the Amstrad / Schneider CPC as **public domain** - on the
condition that this causes vortex no technical support work. The letter:
[`docs/VDOSisPD.pdf`](docs/VDOSisPD.pdf).

So the ROM ([VDOS-2.11-X.rom](https://github.com/SerErris/Vortex_VDOS/releases/download/v2.11/VDOS-2.11-X.rom))
may be used and passed on freely. Please do not contact vortex with questions about VDOS; use the
issues of this repository instead.

## Credits

VDOS: vortex GmbH. The disassembly and the documentation were made with the CPC X-Ray emulator.
