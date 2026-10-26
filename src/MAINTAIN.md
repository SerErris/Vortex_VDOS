# Maintaining Vortex VDOS

Notes for the maintainer only (not needed to build or use the ROM).

## What a release contains

Every release has a tag `v<version>` (e.g. `v2.11`) and **two assets**:

| Asset | Source |
|---|---|
| `VDOS-<version>-X.rom` | the decoded 16K ROM image, assembled from `src/VDOS-<version>-X.asm` into `rom/` |
| `Vortex_X-Laufwerke_Manual_<version>-X.md` | the current user manual from `docs/` |

The release notes say what the version is (original or fixed bugs), mention that VDOS is public
domain (`docs/VDOSisPD.pdf`) and that the ROM goes into a normal upper ROM slot, not the Vortex
controller socket (the image is decoded).

## Build the ROM

```
mkdir -p rom
cd rom
sjasmplus ../src/VDOS-2.11-X.asm
sha256sum VDOS-2.11-X.rom
```

`rom/` is in `.gitignore`. 2.11-X must give SHA-256
`cdff2b5e372c740dd5bdf351b89d9ce955d07ba974b144ba4bc2475afcbfac5b`.

## Update the current release

After a change of the manual (or a rebuilt ROM), replace the assets of the current release:

```
gh release upload v2.11 rom/VDOS-2.11-X.rom docs/Vortex_X-Laufwerke_Manual_2.11-X.md --clobber
```

`--clobber` replaces assets with the same name. Check the result:

```
gh release view v2.11
```

## A new version

1. Build the new ROM (e.g. `src/VDOS-2.12-X.asm` -> `rom/VDOS-2.12-X.rom`).
2. Commit and push the source and the documents.
3. Create the release with both assets:
   ```
   gh release create v2.12 rom/VDOS-2.12-X.rom docs/Vortex_X-Laufwerke_Manual_2.12-X.md \
       --title "VDOS 2.12-X" --notes "..."
   ```
4. Update the download links in `README.md` (they point to the `v2.11` assets).
