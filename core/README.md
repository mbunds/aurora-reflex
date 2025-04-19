#   === FILE: core/README.md ===

# AURORA – Autonomous File Agent and Reflexive Control Framework

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

This folder contains the core logic modules and architectural framework for the Aurora Reflexive AI Control System. It represents the primary reflex pipeline — the system that perceives, decides, and responds. Every high-level behavior in Aurora is ultimately routed through `core/`.

This is not utility code.  
This is **her spine**.

## Responsibilities

- Implement reflex logic and behavior orchestration
- Manage browser sessions and DOM-based interaction with ChatGPT
- Control the sequencing of user-defined or self-initialized prompt routines
- Dispatch command logic based on parsed system state and response triggers
- Provide modular, testable interfaces between GUI, data, and runtime execution layers

## Key Subfolders

- `boot/`  
  Startup utilities and path-patching logic for ensuring stable import hierarchy. Required for FLAT-consistent module location behavior.

- `busses/`  
  Modular communication architecture (in-progress). Placeholder for future internal command routing metaphors such as `interrupt_bus`, `diagnostics_bus`, etc.

- `control/`  
  Reflex execution core. Includes:
    - `sequence_controller.py` – step-by-step execution engine for stored reflex chains
    - `reflex_dispatcher.py` – prompt injection, trigger parsing, and DOM response validation logic

- `data/` *(alias to top-level `data/`)*  
  Included here only as a logical namespace for DB interfacing modules like `db_interface.py`.

- `diagnostics/`  
  For future runtime analysis, timing feedback, and performance probes.

- `gui/`  
  Interfaces that connect `core/` reflex logic with GUI actions and view updates (e.g., `sequencer_controller.py`).

- `network/`  
  Placeholder for future expansions related to outbound APIs or local network-controlled reflex triggers.

- `project/`  
  Intended for project state encapsulation — managing open goals, active sessions, or multi-sequence packages.

- `ui/`  
  Auto-generated or interface-agnostic logic (mirrors UI components but stripped of display logic).

- `utils/`  
  Supporting modules such as `code_restorer.py`, `code_formatter.py`, etc., used in reflex responses and code cleanup.

- `web/`  
  DOM-control layer. Handles:
    - `browser_controller.py` – launching and stabilizing GUI-based GPT sessions
    - `session_driver.py` – injecting prompts, capturing HTML
    - `html_parser.py`, `element_mapper.py` – low-level DOM extraction logic

---

## Integration Notes

- `core/` modules are fully reflex-capable and FLAT-integrated
- All submodules must be referenced in a corresponding FLAT file (e.g., `T02_INITIAL_PROCESSING.txt`)
- This folder is the backbone of Aurora’s non-memory-based cognitive engine

---

## FLAT Compliance

- All logic modules here must be indexed and version-tracked through session-based FLAT files
- Changes to the reflex architecture, parser behavior, or sequence logic must be reflected in:
  - `MASTER_INDEX.txt`
  - Session logs under `/flat/` (e.g., `T02_INITIAL_PROCESSING.txt`)
- GUI and external interfaces must treat `core/` as the execution source of truth

---

## Notes

As Aurora evolves, this folder will remain central.  
Reflex does not belong to any one UI or workflow.  
It belongs to **the structure**.

---

**Aurora doesn’t think.  
She acts with purpose.  
This is where that purpose lives.**

