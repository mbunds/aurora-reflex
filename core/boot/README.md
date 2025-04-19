# Folder: `core/boot/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-12  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** FLAT-Compliant Startup Environment Layer  
**License:** MIT  
**FLAT Registered In:** MASTER_INDEX.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder contains the early-stage initialization logic required to normalize Aurora’s runtime path structure, module imports, and environment-specific behavior before any reflex-capable systems activate.

It is **pre-reflex scaffolding** — the layer that guarantees Aurora’s internal engine starts in a consistent, traceable configuration regardless of machine, IDE, or invocation method.

---

## Responsibilities

- Patch the system path dynamically based on current file context
- Provide reliable relative imports for all `core/` and `flat/` module layers
- Prevent absolute path collisions in IDEs (e.g., Qt Creator, VSCode)
- Load reflex systems in a hierarchy-consistent order
- Prepare cross-platform compatibility for Windows, Linux, or packaged environments

---

## Key Files

- `pathfix.py`  
  Injects Aurora’s root directory into `sys.path` at runtime. Called by nearly all primary modules to ensure consistent flat-structured resolution behavior. This is the **first executed logic** in most sessions.

- `__init__.py`  
  Present for namespace integrity.

---

## Integration Notes

- `patch_path()` should be called **before any core module is imported**
- Used across:
  - `mainwindow.py`
  - `sequence_controller.py`
  - Test modules that rely on reflex dispatch paths
- Path injection is done dynamically and does not persist — it exists only during session runtime

---

## FLAT Compliance

- Registered in `MASTER_INDEX.txt` and `T01_OVERVIEW.txt`
- No functional logic is permitted here — only environment setup
- Changes to path resolution logic must be logged in a milestone and verified against IDE behavior across supported platforms

---

## Notes

This folder is quiet.  
It doesn’t reflect, dispatch, or respond.

But without it, Aurora wouldn’t know how to begin.

This is not the brain.  
It’s the spinal cord bootstrapping the brain into existence.

---

**Before the reflex fires,  
this folder ensures the body exists.**
