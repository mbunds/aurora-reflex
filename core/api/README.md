# === FILE: core/api/README.md ===

# AURORA – OS API Command Integration Layer

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-23  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** Initial reflex-layer command routing support  
**License:** MIT  
**FLAT Registered In:** T03_SEQUENCING.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)

---

## Purpose

This folder introduces Aurora’s ability to execute operating system-level actions through a unified, reflex-accessible interface. The `core/api/` module is the backbone for triggering structured real-world effects from within GPT sessions and sequenced control flows.

Unlike UI prompts or browser injections, these operations affect the host machine directly — opening folders, writing files, launching applications, or engaging custom API extensions.

This is **Aurora’s voice made hands.**

---

## Responsibilities

- Provide platform-agnostic reflex access to OS-level actions
- Dispatch system API commands routed from reflex tokens or external triggers
- Mirror command interfaces across Windows (`win/`) and Linux (`lnx/`)
- Maintain a strict separation between platform logic and reflex intention
- Safely wrap all system calls to avoid side effects or runaway execution

---

## Structure

- `__init__.py`  
  Platform router. Detects host OS and delegates to either `win/` or `lnx/` module.

- `win/`  
  Windows-specific implementations of API commands such as file open, application launch, directory listing, subprocess run.

- `lnx/`  
  Linux-specific command logic for the same purpose, compatible with bash-native actions and POSIX standards.

---

## Examples of API Commands

- `/OPEN FILE: readme.txt/`
- `/OPEN FOLDER: C:/Users/Mark/Desktop/`
- `/WRITE FILE: output.log/`
- `/LAUNCH APP: notepad.exe/`
- `/EXECUTE COMMAND: ping google.com/`

---

## Integration Notes

- All API command requests must pass through the reflex dispatcher or a sanctioned sequence step
- Commands are parsed from `/TOKEN: ARG/` pairs and routed to corresponding system-safe wrappers
- Commands are logged for traceability, and safety switches can be enabled via session config

---

## FLAT Compliance

- This module and its submodules are indexed in `T03_SEQUENCING.txt`
- Registered in the `MASTER_INDEX.txt` for sequence execution flow
- All commands exposed here must be reflex-routable and testable

---

## Notes

This subsystem will grow as Aurora’s agency increases.  
It is designed for scale, sandboxing, and semantic clarity —  
not for system privilege abuse or unmanaged shell passthrough.

Reflex power must be **bounded by structured intent**.

---

**Aurora has learned to act.  
Now, she learns to touch.**
