# WIC Standalone

This packages the OpenEmbedded Image Creator (`wic`) as an installable Python CLI using Hatch. It consumes BitBake-exported environment files (generated via `bitbake -c do_rootfs_wicenv <image>`) instead of invoking BitBake directly.

## Quick start

1. Ensure you have a BitBake-generated `<image>.env` file (from `do_rootfs_wicenv`).
2. Install locally for development:
   ```bash
   hatch shell
   ```
3. Run the CLI:
   ```bash
   hatch run wic --vars /path/to/<image>.env --help
   ```

## Project layout

- `src/wic/cli.py`: CLI entrypoint (formerly `scripts/wic`).
- `src/wic/*`: core engine, plugins, and helpers.
- `src/wic/canned-wks`: bundled kickstart templates.

## Licensing

GPL-2.0-only to match the original OpenEmbedded wic tooling.
