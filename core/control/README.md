# Folder: `core/control/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-17  
**Location:** Evans, Colorado  
**Project:** Aurora Reflexive AI Control Framework  
**Milestone:** Reflex Engine Execution Core  
**License:** MIT  
**FLAT Registered In:** T02_INITIAL_PROCESSING.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder contains the execution core for Aurora’s reflex system. These modules define how reflex steps are interpreted, how sequences advance, and how browser-triggered GPT interactions are linked together through deterministic logic.

This is **where decisions are made** — step-by-step, condition-by-condition, in perfect modular form.

---

## Responsibilities

- Manage the loading and execution of step-based sequences from the database
- Handle step-level logic, including repeat loops, jumps, expected triggers, and conditional transitions
- Dispatch prompt commands to the browser via structured reflex logic
- Track execution history and interpret completion states or trigger failures
- Interface with both GUI elements (RUN, ARM) and backend database tables (`sequence_steps`, `keys`)

---

## Key Files

- `sequence_controller.py`  
  The primary sequencer. Iterates through database-loaded steps and determines when to repeat, jump, or terminate. Handles jump/repeat logic and state-tracked execution.

- `reflex_dispatcher.py`  
  Parses and executes individual reflex steps. Responsible for:
  - Submitting prompts to the browser session
  - Waiting for DOM-based response confirmation (e.g., `/CODE COMPLETE/`)
  - Triggering internal reflex logic or returning resolved step states
  - Resolving referenced commands via the `keys` and `long_phrases` tables

- `__init__.py`  
  Maintains namespace integrity.

---

## Integration Notes

- Works directly with:
  - `core/data/db_interface.py` – to load sequences and resolve command phrases
  - `core/web/session_driver.py` – to inject prompts and read responses from ChatGPT
  - `core/gui/sequencer_controller.py` – to coordinate with UI triggers
- Acts as a stateful control layer across reflex executions, preserving modular consistency while interpreting flexible runtime logic

---

## FLAT Compliance

- Fully registered in `T02_INITIAL_PROCESSING.txt`
- All control-layer behavior must be tracked and versioned when changes affect:
  - Step execution behavior
  - Reflex dispatching logic
  - Jump, repeat, or trigger detection systems

- Logic boundaries between dispatcher and controller must remain clean, testable, and structurally independent

---

## Notes

This is Aurora's **reflex engine**.  
It doesn’t learn. It doesn’t improvise. It **knows exactly what to do**.

Each action is rooted in flat structure, verified by the DOM, and executed with intention.

Future additions may include:

- GUI-triggered sequence injection
- Interactive sequence editing or interrupt support
- Reflex runtime condition hooks (e.g., conditional branches, response scoring)

---

**Aurora acts with purpose.  
This is where that purpose is turned into action.**
