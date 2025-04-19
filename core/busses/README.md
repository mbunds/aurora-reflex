#   === FILE: core/busses/README.md ===

# AURORA – "Pseudo Pub/Sub Control Layer" (Magic Buses)

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-12  
**Location:** Evans, Colorado  
**Project:** AURORA
**FLAT Registered In:** MAGIC_BUSES.txt  
**License:** MIT  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)

---

## Overview

The `core/busses/` folder implements the **internal routing and coordination system** for AURORA interfaces into AI-enabled projects such as the OpenSIM DCS Manager.

It defines the central event/message buses — referred to as **"magic buses"** — that enable logic modules, GUI elements, and AI agents to communicate through a **loosely coupled, structured messaging system**.

These buses are the nervous system of OpenSIM DCS — forming the backbone of:
- Logic automation
- Programmatic editing
- Runtime command orchestration
- Health reporting
- User and AI interrupt routing

---

## Primary Components

| Module             | Purpose |
|--------------------|---------|
| `bus_controller.py`   | Instantiates and exposes all buses as module-level singletons. |
| `edit_bus.py`         | Handles logic editing, tag manipulation, and ST injection signals. |
| `control_bus.py`      | Routes start/stop/deploy/reset/sync commands across tabs or PLCs. |
| `diagnostic_bus.py`   | Dispatches health reports, runtime scan results, and fault indicators. |
| `command_bus.py`      | Accepts structured commands from GUI, scripts, or AI interfaces. |
| `interrupt_bus.py`    | Provides overrides and emergency abort channels for ongoing processes. |

---

## Coming Soon

| Planned Module        | Description |
|------------------------|-------------|
| `ai_agent_hooks.py`     | Will connect subscribed bus events to AI agents for intelligent guidance, live editing, or auto-response feedback. |

---

## Notes

- NEW PROJECT: This is a new file refactored from its twin in the OpenSIM DCS project. Folder structures are different between these projects.
- NEW PROJECT: There are five folders above "busses"meant to contain functions related to the bus "purpose":
- NEW PROJECT: [command_bus]
- NEW PROJECT: [control_bus]
- NEW PROJECT: [diagnostic_bus]
- NEW PROJECT: [edit_bus]
- NEW PROJECT: [interrupt_bus]

- Each bus supports **bidirectional communication** and may act as both a signal router and state tracker.
- The entire control layer is designed with **AI participation and runtime modularity** in mind.