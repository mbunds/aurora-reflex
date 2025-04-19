#   === FILE: README.md ===

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

AURORA [PROJECT ROOT]
	FOLDER [.qtcreator]
	FOLDER [ARCHIVE]
		FILE (PLACEHOLDER)
	FOLDER [core]
	        FOLDER [boot]
		        FILE (__init__.py)
			FILE (pathfix.py)[UNDER CONSTRUCTION]
			FILE (README.md)
		FOLDER [busses]
			FOLDER [command_bus]
				FILE (__init__.py)
				FILE (README.md)
			FOLDER [control_bus]
				FILE (__init__.py)
				FILE (README.md)
			FOLDER [diagnostics_bus]
				FILE (__init__.py)
				FILE (README.md)
			FOLDER [edit_bus]
				FILE (__init__.py)
				FILE (README.md)
			FOLDER [interrupt_bus]
				FILE (__init__.py)
				FILE (README.md)
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [control]
			FILE (__init__.py)
			FILE (README.md)
			FILE reflex_dispatcher.py[UNDER CONSTRUCTION]
			FILE sequence_controller.py[UNDER CONSTRUCTION]
		FOLDER [data]
			FILE (__init__.py)
			FILE db_interface.py[UNDER CONSTRUCTION]
			FILE (README.md)
		FOLDER [diagnostics]
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [gui]
		        FILE (__init__.py)
			FILE (README.md)
			FILE (sequence_controller.py)[UNDER CONSTRUCTION]
		FOLDER [network]
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [project]
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [ui]
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [utils]
		        FILE (code_foramtter.py)[REVIEW LATER]
			FILE (code_restorer.py)[REVIEW LATER]
			FILE (__init__.py)
			FILE (README.md)
		FOLDER [web]
		        FILE (__init__.py)
			FILE (browser_controller.py)[UNDER CONSTRUCTION]
			FILE (code_sanitizer.py)[REVIEW LATER]
			FILE (README.md)
			FILE (screen_capture.py)[EMPTY]
			FILE (session_driver.py)[UNDER CONSTRUCTION]
			FOLDER [html]
			        FILE (__init__.py)
				FILE (element_mapper.py)[UNDER CONSTRUCTION]
				FILE (html_parser.py)[UNDER CONSTRUCTION]
				FILE (README.md)
	FOLDER [data]
		FILE (__init__.py)
		FILE (README.md)
	FOLDER [DESIGN AND PROMOTION]
		FOLDER [PLACEHOLDER]
			FILE (PLACEHOLDER)
		FILE (PLACEHOLDER)
	FOLDER [dist]
		FILE (__init__.py)
		FILE (README.md)
	FOLDER [docs]
		FILE (__init__.py)
		FILE (README.md)
	FOLDER [flat]
		FOLDER [ARCHIVE]
			FILE (PLACEHOLDER)
		FILE (DEVELOPER_SECURITY.txt)
		FILE (DOCS.txt)
		FILE (FOLDER_TREE.txt)
		FILE (FUTURE_FEATURES.txt)
		FILE (MAGIC_BUSES.txt)
		FILE (MASTER_INDEX.txt)
		FILE (T01_OVERVIEW.txt)
	FOLDER [GPT SUBMISSIONS]
		FOLDER [PLACEHOLDER]
			FILE (PLACEHOLDER)
		FILE (PLACEHOLDER)
	FOLDER [graphics]
		FILE (__init__.py)
		FILE (AURORA_BG_png)
		FILE (README.md)
	FOLDER [logs]
		FILE (__init__.py)
		FILE (README.md)
	FOLDER [resources]
		FILE (__init__.py)
		FILE (README.md)
	FOLDER [tests]
		FILE (__init__.py)
		FILE:(test_element_mapper.py)
		FILE:(test_session_driver.py)
		FILE:(test_submit_prompt_demo.py[UNDER CONSTRUCTION]
		FILE (README.md)
	FILE (__init__.py)
	FILE (AURORA.pyproject)
	FILE (AURORA.pyproject.user)
	FILE (form.ui)
	FILE (mainwindow.py)
	FILE (README.md)
	FILE (requirements.txt)

---
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
