# === FILE: core/api/win/README.md ===

# AURORA – Windows API Command Layer

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-23  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** First platform-resolved reflex execution support  
**License:** MIT  
**FLAT Registered In:** T03_SEQUENCING.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)

---

## Purpose

This folder contains **Windows-specific implementations** of Aurora API commands. These operations are executed in response to reflex tokens or parsed instructions and serve as the system-facing backbone for file operations, process launches, directory control, and Windows Shell automation.

Commands in this folder are dynamically selected at runtime based on platform detection in `core/api/__init__.py`.

---

## Responsibilities

- Implement secure, Win32-compliant execution of reflex-initiated system commands
- Handle basic file and folder manipulation (open, write, move, list, delete)
- Launch applications using ShellExecute or `subprocess`
- Reflect meaningful success/failure status for downstream reflex processing
- Mirror Linux functionality in form and naming when applicable

---

## Integration Path

1. A reflex token such as `/OPEN FOLDER: C:/Users/Mark/Documents/` is detected  
2. `reflex_dispatcher.py` parses the request and identifies it as a system command  
3. `core/api/` routes the request to `win/` based on host OS  
4. A Windows-safe handler like `open_folder(path)` is called and logged

---

## Example Commands

```txt
/OPEN FOLDER: C:/Users/Mark/Desktop/
/LAUNCH APP: notepad.exe/
/WRITE FILE: C:/Temp/output.log/
/EXECUTE COMMAND: ping 8.8.8.8/
/CODE COMPLETE/

---

## Safety and Philosophy

This module executes commands that **affect real state**.  
It must never be used for arbitrary shell passthrough unless:

- The command is sanitized  
- The operation is registered  
- The output is structured  

This is not a shell injection system.  
This is Aurora **acting on your machine**, with deliberate control.

---

## FLAT Compliance

- Registered in: `T03_SEQUENCING.txt`  
- Indexed in: `MASTER_INDEX.txt`  
- Mirrors platform intent and structure defined in `core/api/lnx/`  
- All commands must be testable and reflex-addressable via tokenized instructions

---

## Notes

This module will expand to include advanced Windows automation tasks, including:

- File explorer integration  
- Task manager/process control  
- Registry-safe configurations  
- Shortcut and startup item generation  
- Reflex-driven environment variable manipulation

---

**On Windows, she learns to interact.  
This is where intention becomes action.**
