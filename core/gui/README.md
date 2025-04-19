# Folder: `core/gui/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-17  
**Location:** Evans, Colorado  
**Project:** Aurora Reflexive AI Control Framework  
**Milestone:** SSE/FLAT Compliant GUI Integration  
**License:** MIT  
**FLAT Registered In:** T02_INITIAL_PROCESSING.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder contains all GUI-aware controller modules and adapter logic that map Aurora’s reflexive backend systems onto interactive Qt-based views.

Where `core/ui/` will house structural UI logic, `core/gui/` is dedicated to **widget-aware event flows**, live model/view population, and user-driven system triggers.

This is where Aurora’s reflex becomes **visible**.

---

## Responsibilities

- Translate user selections into backend reflex or sequence actions
- Populate view models (e.g., `QListView`) with dynamic data pulled from `data/`
- Connect button clicks or list selections to execution routines (`ARM`, `RUN`, `EDIT`)
- Enable the reflex system to express state and options through visible components

---

## Current Modules

- `__init__.py`  
  Namespace initializer.

- `sequencer_controller.py`  
  Controls population of available sequences and their ordered steps into UI components. Manages enabling/disabling of interface elements based on selection state.

---

## Integration Notes

- Relies on Qt widgets defined in `ui_form.py` (auto-generated from `form.ui`)
- Works in tandem with `core/control/sequence_controller.py` and `core/data/db_interface.py`
- This is a presentation adapter layer — it should **not** contain internal reflex logic

---

## FLAT Compliance

- All modules here are tracked in `T02_INITIAL_PROCESSING.txt`
- Any additions must:
  - Be recorded in FLAT changelogs
  - Maintain modular separation from raw UI generation
  - Preserve model/view logic segregation and adhere to SSE-compatible structure

---

## Notes

Aurora’s reflex engine operates silently —  
until a user gives it intent.

This folder lets that intent manifest,  
visibly and responsively.

Future additions may include:

- Reflex status visualizers
- Dynamic sequence editors
- In-GUI reflex interruption or injection panels

---

**This is not where Aurora thinks.  
This is where she answers.**
