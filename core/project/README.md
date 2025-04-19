# Folder: `core/project/`

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

This folder defines the structure and logic for managing *projects* within the Aurora system. A project represents a collection of related goals, sequences, reflex definitions, and generated output — bound by a common context or user intention.

Where `core/control/` governs how Aurora executes, `core/project/` governs **why**.

## Responsibilities

- Represent persistent or in-session project containers
- Maintain project metadata (e.g., creation time, root path, active reflex history)
- Enable sequence grouping and scope-aware reflex execution
- Provide a namespace for managing user-defined goals, workspaces, and long-running session intents
- Track current context across GUI, sequence dispatcher, and future planning modules

## Key Files

- `__init__.py`  
  Present for namespace integrity. This folder is structurally reserved for active development.

- *(Planned)* `project_manager.py`  
  Will initialize and track open projects, maintain context during reflex sessions, and handle sequence-scoped folder generation.

- *(Planned)* `goal_tracker.py`  
  Will manage open-ended vs. defined goals, handle user-assisted refinements, and monitor long-term project structure emergence.

## Integration Notes

- Future connection points:
  - GUI will surface project initialization options
  - Sequencer will be able to “lock” into a project context for scoped reflex behavior
  - Generated FLAT files and logs will be able to reference a current project ID or name

- Project folders may eventually generate their own local `flat/`, `data/`, or `logs/` stubs for scoped tracking

---

## FLAT Compliance

- This folder is indexed in `MASTER_INDEX.txt` and `T01_OVERVIEW.txt` as a planned orchestration layer
- All future modules must define their relationship to project scope in FLAT changelogs
- Reflex sequences that operate on or within project contexts must record state boundary interactions

---

## Notes

Aurora's intelligence emerges from structure.  
But structure without **context** is just noise.

This folder is where her **long-term intent** will begin.

Future directions include:

- Automatic project generation from FLAT or cue-sheet inputs
- Goal-based reflex bundles and scoped reflex suppression
- Project-aware interrupt queue mapping

---

**The reflex has learned to act.  
Now it will learn to organize.**
