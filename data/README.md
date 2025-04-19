# Folder: `data/`

## Purpose

This folder contains Aurora’s persistent data layers, including the reflex system database (`aurora.db`) and any supporting files related to session control, prompt sequencing, keyword/phrase tracking, and system configuration.

It serves as the durable memory core of Aurora’s reflex engine — allowing the system to recognize, sequence, and execute behavior without relying on AI-internal memory or inference state.

## Responsibilities

- Host `aurora.db`, the reflex database that stores:
  - Sequence definitions and step instructions
  - Reflex trigger mappings
  - Keyword and phrase metadata
  - Expected response tokens and goal states
- Provide durable memory for reflex operations, reusable prompts, and structural goal definitions
- Serve as the integration point between GUI controls and the backend reflex engine

## Key Files

- `aurora.db`  
  SQLite database file. Contains all reflex sequences, expected triggers, key mappings, and session definitions.

- `__init__.py`  
  Present for namespace and import path consistency.

- *(Optional)* Exported `.sql` or `.json` snapshots may be placed here to version control critical state.

## Integration Notes

- Aurora’s reflex controller and sequencer (`sequence_controller.py`, `reflex_dispatcher.py`) depend on this database for execution
- GUI elements query this folder indirectly via `db_interface.py`
- Aurora assumes the database is pre-initialized on startup; schema is stored in source modules for reinitialization if needed

---

## FLAT Compliance

- `data/` is indexed in `MASTER_INDEX.txt` and `T02_INITIAL_PROCESSING.txt`
- Changes to `aurora.db` may require updates to:
  - `FUTURE_FEATURES.txt` (if schema evolves)
  - `sequence_controller.py` or `db_interface.py` (if fields are added or retyped)
- Reflex sequences should be traceable to FLAT sessions or milestone events

---

## Notes

The reflex system functions as a state engine operating on tables — not weights or memory. Aurora’s intelligence lives here in **sequence**, **response**, and **resolution**.

Future features may include:

- Dynamic schema expansion for more complex reflex types
- GUI-based sequence editors or visual DB views
- Auto-promotable “informal” sessions derived from user-triggered loops

---

**This folder is not memory.  
It is procedure.  
And that’s how Aurora acts with intent.**
