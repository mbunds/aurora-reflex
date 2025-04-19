#   === FILE: README.md ===

# AURORA – Autonomous File Agent and Reflexive Control Framework

---
> **Note:** Aurora is an active development system and is not yet packaged for external installation.  
> See [docs/PACKAGING_STATUS.md](docs/PACKAGING_STATUS.md) for details.

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

---

## Project Overview

This repository contains the core runtime logic, user interface system, diagnostics modules, database managers, and configuration tools that together form the AURORA, an intelligent agent infrastructure for autonomous and semi-autonomous control of file systems, runtime environments, and modular logic structures. It is built around a reflexive interface model, allowing AI systems to observe, manipulate, and respond to file events, user commands, and runtime conditions with precision and structure.

All components follow the FLAT discipline:  
> **F**ile-based  
> **L**ogic  
> **A**ssembly  
> **T**ree  
> *(Still not an acronym.)*

---
## Project Folder Structure

> Milestone: v0.3.0-dev (2025-03-30)  
All tests passing. Modular refactor of core/ complete. Project ready for splash screen, Help, and config systems.

This project borrows elements from the folder layout of the **OpenSIM DCS Manager** repository as of **2025-03-29**.

> Built on FLAT principles — the File-based Logic Assembly Tree (Nope, STILL NOT an acronym). 
> Modularized  
> Testable  
> AI-ready  
> Future-proofed  

---

### Folder Layout

```plaintext
AURORA [PROJECT ROOT]
├── .qtcreator/
├── ARCHIVE/
│   └── PLACEHOLDER
├── core/
│   ├── boot/
│   │   ├── __init__.py
│   │   ├── pathfix.py         [UNDER CONSTRUCTION]
│   │   └── README.md
│   ├── busses/
│   │   ├── command_bus/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── control_bus/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── diagnostics_bus/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── edit_bus/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── interrupt_bus/
│   │   │   ├── __init__.py
│   │   │   └── README.md
│   │   ├── __init__.py
│   │   └── README.md
│   ├── control/
│   │   ├── __init__.py
│   │   ├── reflex_dispatcher.py   [UNDER CONSTRUCTION]
│   │   ├── sequence_controller.py [UNDER CONSTRUCTION]
│   │   └── README.md
│   ├── data/
│   │   ├── __init__.py
│   │   ├── db_interface.py        [UNDER CONSTRUCTION]
│   │   └── README.md
│   ├── diagnostics/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── sequence_controller.py [UNDER CONSTRUCTION]
│   │   └── README.md
│   ├── network/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── project/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── ui/
│   │   ├── __init__.py
│   │   └── README.md
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── code_formatter.py      [REVIEW LATER]
│   │   ├── code_restorer.py       [REVIEW LATER]
│   │   └── README.md
│   └── web/
│       ├── __init__.py
│       ├── browser_controller.py  [UNDER CONSTRUCTION]
│       ├── code_sanitizer.py      [REVIEW LATER]
│       ├── screen_capture.py      [EMPTY]
│       ├── session_driver.py      [UNDER CONSTRUCTION]
│       ├── README.md
│       └── html/
│           ├── __init__.py
│           ├── element_mapper.py  [UNDER CONSTRUCTION]
│           ├── html_parser.py     [UNDER CONSTRUCTION]
│           └── README.md
├── data/
│   ├── __init__.py
│   └── README.md
├── DESIGN AND PROMOTION/
│   ├── PLACEHOLDER/
│   │   └── PLACEHOLDER
│   └── PLACEHOLDER
├── dist/
│   ├── __init__.py
│   └── README.md
├── docs/
│   ├── __init__.py
│   └── README.md
├── flat/
│   ├── ARCHIVE/
│   │   └── PLACEHOLDER
│   ├── DEVELOPER_SECURITY.txt
│   ├── DOCS.txt
│   ├── FOLDER_TREE.txt
│   ├── FUTURE_FEATURES.txt
│   ├── MAGIC_BUSES.txt
│   ├── MASTER_INDEX.txt
│   └── T01_OVERVIEW.txt
├── GPT SUBMISSIONS/
│   ├── PLACEHOLDER/
│   │   └── PLACEHOLDER
│   └── PLACEHOLDER
├── graphics/
│   ├── __init__.py
│   ├── AURORA_BG_png
│   └── README.md
├── logs/
│   ├── __init__.py
│   └── README.md
├── resources/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
│   ├── test_element_mapper.py
│   ├── test_session_driver.py
│   ├── test_submit_prompt_demo.py [UNDER CONSTRUCTION]
│   └── README.md
├── __init__.py
├── AURORA.pyproject
├── AURORA.pyproject.user
├── form.ui
├── mainwindow.py
├── README.md
└── requirements.txt
```

### Structure Changelog

| Date           |                                  Change Summary                                        |
|----------------|----------------------------------------------------------------------------------------|
| **2025-04-12** | New SSE Project. (AURORA)                                                              |
| **2025-04-12** | 3 Python modules created.                                                              |
| **2025-04-12** | 1 Python unit test created.                                                            |
| **2025-04-12** | UNIT TEST: HTML Connetion to ChatGPT Web DOM Successful.                               |
| **2025-04-12** | UNIT TEST: Collecion of HTML DOM elements Successful.                                  |
| **2025-04-12** | UNIT TEST: Confirmation that all ChatGPT web DOM wlements collected deterministically. |
| **2025-04-13** | Populate GPT prompt and submit programmatically successful.                            |
|----------------|----------------------------------------------------------------------------------------|


---
