# === FILE: core/api/lnx/README.md ===

# AURORA – Linux API Command Layer

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

This folder contains **Linux-specific implementations** of Aurora API commands. These operations are executed in response to reflex tokens or parsed instructions and serve as the system-facing backbone for file operations, process launches, directory control, and external system calls on POSIX-compliant machines.

Commands in this folder are dynamically selected at runtime based on platform detection in `core/api/__init__.py`.

---

## Responsibilities

- Implement secure, shell-safe execution of reflex-initiated system commands
- Handle basic file and folder manipulation (open, write, move, list, delete)
- Execute terminal commands via Python subprocess layer
- Reflect meaningful success/failure status for downstream reflex processing
- Mirror Windows functionality in form and naming when applicable

---

## Integration Path

1. A reflex token such as `/OPEN FOLDER: /home/mark/projects/` is detected  
2. `reflex_dispatcher.py` parses the request and identifies it as a system command  
3. `core/api/` routes the request to `lnx/` based on host OS  
4. A Linux-safe handler like `open_folder(path)` is called and logged

---

## Example Commands

```txt
/OPEN FOLDER: /var/log/
/LAUNCH APP: gedit/
/WRITE FILE: /tmp/output.log/
/EXECUTE COMMAND: ls -la/
/CODE COMPLETE/

---

## Safety and Philosophy

This module executes commands that **affect real state**.  
It must never be used for arbitrary shell passthrough unless:

- The command is sanitized  
- The operation is registered  
- The output is structured  

This is not a bash proxy.  
This is Aurora **touching the real world**, carefully.

---

## FLAT Compliance

- Registered in: `T03_SEQUENCING.txt`
- Indexed in: `MASTER_INDEX.txt`
- Mirrors platform intent and structure defined in `core/api/win/`
- All commands must be testable and reflex-addressable via tokenized instructions

---

## Notes

This module will grow to support more complex Linux operations, including:

- Permission handling
- File monitoring
- Reflex-triggered network ops
- Process backgrounding
- Temporary mountpoint management
- Reflex-based init process scaffolds

---

**On Linux, she learns to move.  
This is where the hands meet the terminal.**
