#   === FILE: core/gui/README.md ===

# Aurora – GUI Subsystem

**Location:** `core/gui/`  
**Created:** 2025-04-17  
**Authors:** ChatGPT and Mark  
**Project:** Aurora Reflexive AI Control Framework  
**Scope:** FLAT Registered Module – `T02_INITIAL_PROCESSING.txt`

---

## Overview

This directory contains all GUI-bound controller modules and interface adapters
that translate internal Aurora control logic into interactive user experiences.

All widgets, layout managers, and event handler bridges between the frontend
(Qt UI elements) and backend (control/data modules) live in this namespace.

---

## Conventions

- Modules here should follow **strict separation** of view and logic.
- UI elements (from `.ui_form`) must be referenced via `self.ui`.
- All model/view logic (e.g., populating a `QListView`) should be handled by helper modules such as `sequencer_controller.py`.

---

## Current Modules

- `__init__.py` – Initializes the `core.gui` namespace
- `sequencer_controller.py` – Handles sequence and step population into Qt widgets

---

## FLAT Compliance

This folder participates in the **T02_INITIAL_PROCESSING** session.
All changes and module additions must be reflected in:
- `MASTER_INDEX.txt`
- `T02_INITIAL_PROCESSING.txt`

---

> _“Visual flow is the first layer of reflex. Let it be modular.”_  
