# Folder: `core/busses/command_bus/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-17  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** Structured Command Routing Channel  
**License:** MIT  
**FLAT Registered In:** MAGIC_BUSES.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder defines Aurora’s **structured command bus**, responsible for transporting declarative user or reflex-generated commands into action-ready signal routes. These commands represent **intent**, distinct from control or edit flows.

It is the message channel through which sequences, users, or AI agents say:  
> “Do this next.”

---

## Responsibilities

- Accept structured commands from GUI controls, sequences, or prompt-reflex routines
- Dispatch command tokens like `LOAD`, `INJECT`, `BUILD`, `INIT`, or `SEED`
- Route instructions to the proper handler system (e.g., reflex controller, UI display, data manager)
- Provide an abstraction layer between command origin (user/reflex) and execution context
- Allow reflex routines to issue system-level requests without directly coupling logic layers

---

## Key Files

- `__init__.py`  
  Namespace initializer.

- *(Planned)* `command_bus.py`  
  Central interface for dispatching normalized commands (typically string tokens or wrapped structures). May support both atomic and compound directives.

- *(Planned)* `command_router.py`  
  Will interpret command content, validate parameters, and invoke the corresponding logic path (e.g., call `sequence_controller.run()`).

---

## Integration Notes

- Complements:
  - `control_bus/` – for runtime flow
  - `edit_bus/` – for ST/logical mutation
  - `diagnostic_bus/` – for health signal after execution

- Can originate from:
  - Button clicks or menu actions
  - AI-injected instructions
  - Self-modifying reflex routines or nested sequence steps

- Should support typed command tokens with optional payloads (e.g., `"SEED_PROJECT"`, `{folder: 'x'}`)

---

## FLAT Compliance

- Registered in `MAGIC_BUSES.txt`
- All command strings or tokens must be:
  - Loggable
  - Traceable to their originating module
  - Reflex-safe (i.e., they do not bypass reflex supervision or validation)

---

## Notes

This is Aurora’s **directive channel**.  
When a user clicks, when a reflex concludes, when a plan resolves — this is where the action command emerges.

It does not govern how the system runs.  
It tells the system what to do.

Future extensions may include:

- Prompt-defined command expansion (AI-injected `"RUN_SEQUENCE XYZ"`)
- Natural language-to-command token parsing
- Reflex-agent co-pilot logic generating command packets

---

**Aurora does not act randomly.  
She acts when told — through this.**
