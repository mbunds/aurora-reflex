# Folder: `core/data/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-17  
**Location:** Evans, Colorado  
**Project:** Aurora Reflexive AI Control Framework  
**Milestone:** SSE/FLAT Compliant Data Logic Layer  
**License:** MIT  
**FLAT Registered In:** MASTER_INDEX.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder contains Python modules that interface with Aurora’s runtime database, `aurora.db`, located at the project root under `/data/`. These modules expose structured access to reflex sequences, step definitions, and keyword mappings, enabling internal systems to retrieve, update, and validate reflex state cleanly.

This is the **logic layer** that sits between flat storage and reflex execution.

## Responsibilities

- Load, query, and normalize data from the SQLite3 database
- Provide list-structured access to reflex sequence definitions and step metadata
- Resolve foreign key references (e.g., `long_phrases`, `keys`) into usable execution strings
- Serve the sequencer, reflex dispatcher, and GUI interface with preprocessed, ready-to-run data

---

## Key Files

- `db_interface.py`  
  Main data bridge. Handles:
  - Sequence and step loading via `load_sequence_steps()`
  - Reflex string lookup via `resolve_key_phrase()` and `resolve_long_phrase()`
  - Dynamic project-root path resolution to ensure compatibility across development environments

- `__init__.py`  
  Maintains namespace integrity.

---

## Integration Notes

- This folder supports `/data/aurora.db`, but does **not** store data itself
- Used by:
  - `sequence_controller.py` to pull reflex routines
  - `reflex_dispatcher.py` to decode step references
  - `sequencer_controller.py` to populate visual step listings
- Implements runtime resolution paths to eliminate environment-coupled file errors

---

## FLAT Compliance

- Modules in this folder are tracked in `T02_INITIAL_PROCESSING.txt`
- Any update to schema-aware query logic must be logged in FLAT with accompanying schema snapshot or milestone reference
- Keyword/trigger lookup routines must reflect `keys` and `long_phrases` table structure

---

## Notes

This folder does not contain the reflex.  
It enables it.

By abstracting raw data structures into clean, usable runtime forms, Aurora is able to treat her memory like architecture — not guesswork.

Future expansions may include:

- Schema versioning compatibility check
- Reflex edit/writeback tooling
- Project-context-aware database partitioning

---

**Aurora’s memory lives in `/data`.  
This is where she learns how to use it.**
