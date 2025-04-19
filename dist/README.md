# Folder: `dist/`

## Purpose

This folder is used for storing distributable versions of the Aurora system. It may contain packaged builds, deployment artifacts, installer bundles, or exported module collections prepared for testing, delivery, or archival.

While Aurora is primarily driven by its live development pipeline, this folder acts as the structural location for all compiled or packaged output created during export or release cycles.

## Responsibilities

- Host `.zip`, `.tar.gz`, or other archive formats representing Aurora releases
- Contain bundled versions of the system for transport, backup, or delivery
- Act as a staging location for PyInstaller, `cx_Freeze`, or future GUI bundlers
- Provide a target directory for CI/CD tools or manual build scripts

## Key Files

- `__init__.py`  
  Present only for structural consistency; not functionally required in distribution folders.

- *(Planned)* `aurora_v0.3.0-dev.zip`  
  Test-stage compressed package of Aurora including all modules, graphics, resources, and FLAT files.

## Integration Notes

- This folder is **not tracked** for operational purposes during runtime
- Build scripts may target `dist/` for output during release cycles
- It is safe to exclude this folder from reflex loops or structural file watching routines

---

## FLAT Compliance

- `dist/` is referenced in `MASTER_INDEX.txt` and `T01_OVERVIEW.txt` as a distribution endpoint
- All contents within this folder must be traceable to a corresponding FLAT session and module history
- Changes to this folder do **not trigger system state changes** — only reflect completed output

---

## Notes

Future packaging tasks may include:

- Executable or frozen builds of Aurora for standalone systems
- Sequence + module + prompt bundle exports
- Build validation pipelines for reflex-capable instances

This folder is not for design.  
This is for **delivery**.

---

**Aurora runs from source.  
But she ships from here.**
