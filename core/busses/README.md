# Folder: `core/busses/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-12  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** Internal Routing Layer for Reflex and Command Systems  
**License:** MIT  
**FLAT Registered In:** MAGIC_BUSES.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder defines Aurora’s internal routing and message distribution infrastructure — the **“magic buses”** that coordinate commands, interrupts, diagnostics, and programmatic edits across the reflex engine, GUI, and external agents.

These buses form Aurora’s **signal backbone** — loosely coupled, purpose-specific conduits that allow discrete components to communicate while remaining structurally independent.

This is the nervous system.  
Aurora reacts because these buses deliver intent.

---

## Responsibilities

- Route command instructions between GUI, reflex dispatcher, and core control modules
- Broadcast diagnostic status, scan results, and system health
- Enable logic edits and programmatic ST injection across code generation pathways
- Carry structured commands issued from user input or reflex-generated events
- Dispatch interrupts, overrides, or AI-guided abort sequences

---

## Key Files

| Module               | Role |
|----------------------|------|
| `bus_controller.py`      | Initializes and exposes all buses as named module-level objects. This is the primary access point. |
| `edit_bus.py`            | Handles tagging, logic injection, structural editing, and automation-directed code mutations. |
| `control_bus.py`         | Routes runtime instructions: start, stop, sync, reset, deploy. |
| `diagnostic_bus.py`      | Dispatches scan reports, error flags, and health-status telemetry. |
| `command_bus.py`         | Accepts structured commands from UI, reflex logic, or scripted agents. |
| `interrupt_bus.py`       | Provides interrupt and override channels for abort-safe execution. |

---

## Planned Expansions

| Module                   | Description                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------|
| `ai_agent_hooks.py`      | Will bridge bus events with AI interfaces to enable guided editing, runtime corrections, or co-authoring sequences. |

---

## Integration Notes

- Each bus follows a **pub/sub signal model**, but operates internally without external network dependencies
- Buses are not coupled to reflex execution order — they **route intent**, not control it
- All core systems may listen to or dispatch on buses, including:
  - GUI elements (`core/gui/`)
  - Reflex and sequencer layers (`core/control/`)
  - External integrations (`core/network/`)

---

## FLAT Compliance

- Registered in `MASTER_INDEX.txt` and `MAGIC_BUSES.txt`
- Each bus module is logged under its corresponding structural purpose
- No bus should carry hidden state: all transit must be observable and traceable during reflex diagnostics

---

## Notes

This folder was originally prototyped under OpenSIM DCS and adapted for Aurora’s reflex engine.

Each sub-bus under `/busses/` has an aligned purpose and may eventually interface with a corresponding folder (e.g., `control_bus` → `/core/control/`, `edit_bus` → `/core/utils/`, `interrupt_bus` → reflex sequence overrides).

Aurora isn’t centrally orchestrated — she’s **modularly triggered**.  
These are the conduits where signal becomes intent.

---

**She doesn’t shout across the system.  
She rides the buses.**
