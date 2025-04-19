# Folder: `core/ui/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-12  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** New SSE/FLAT Compliant "disciplined" project.  
**License:** MIT  
**FLAT Registered In:** MASTER_INDEX.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder contains user interface glue modules that bridge between GUI elements and reflexive system logic. Unlike `core/gui/`, which focuses on controlling specific UI behaviors (like populating views), `core/ui/` is reserved for future expansions that bind UI *state* or *form logic* to underlying systems such as the sequencer, interrupt queue, or project manager.

This is the **structural UI logic layer** — minimal, modular, and reflex-aware.

## Responsibilities

- House abstract or GUI-agnostic interface logic for future visual layers
- Provide a clean namespace for managing UI session states and external prompt controllers
- Serve as a forward-compatible target for interfacing future views (e.g., prompt overlays, interrupt displays, reflex status)
- Establish separation between raw Qt Designer outputs and Aurora system logic

## Key Files

- `__init__.py`  
  Placeholder for now. Will serve as namespace initializer for future components.

## Integration Notes

- This folder currently serves as a scaffold for planned extensions
- Reflex integration points expected to emerge here include:
  - Visual interrupt queue preview
  - Reflex event status overlays
  - Dockable command dispatch interfaces or replay viewers

- Intended to **not** contain raw UI-generated files (`ui_form.py` lives elsewhere)

---

## FLAT Compliance

- Referenced in `T01_OVERVIEW.txt` as a UI structure placeholder
- No registered logic modules as of `2025-04-17`, but folder is retained for structural continuity
- All future files must be logged via FLAT changelogs and milestone events

---

## Notes

This folder exists because **UI is not surface alone**.

Visual state and reflex state are converging —  
and when they meet, they will meet here.

Future expansions may include:

- Prompt overlay injection system
- GUI-based step runner visualization
- Dynamic reflex log windowing or sequence inspection UIs

---

**The interface is not Aurora.  
But this is where Aurora learns to reflect herself.**
