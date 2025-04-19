# Folder: `core/busses/interrupt_bus/`

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-17  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** Internal Reflex Interrupt and Override System  
**License:** MIT  
**FLAT Registered In:** MAGIC_BUSES.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)  
> (.qtcreator\Python_3_13_2venv\Scripts\activate)

---

## Purpose

This folder defines the interrupt bus system — Aurora’s internal override and emergency channel for reflex execution. It is designed to safely interrupt, pause, or abort running sequences in a controlled and reflex-aware manner.

This is the **cut line** — the only mechanism with authority to override an active step.

---

## Responsibilities

- Allow runtime systems or GUI elements to issue reflex-safe interrupt commands
- Abort prompt injection, halt browser dispatch, or cancel GPT monitoring mid-cycle
- Signal STOP, HALT, PAUSE, or ABORT instructions into the active sequence controller
- Queue user-initiated override events into the interrupt FIFO (for future review or re-arming)
- Provide a reflex-safe fallback path if trigger expectations are not met within timeout thresholds

---

## Key Files

- `__init__.py`  
  Namespace initializer.

- *(Planned)* `interrupt_bus.py`  
  Core singleton interface for broadcast, subscription, and reflex-driven interrupt activation. Will support queued interrupts, execution flags, and controlled deferral logic.

- *(Planned)* `interrupt_controller.py`  
  May provide higher-order logic for integrating interrupt detection into sequencer timing loops or reflex timeout monitors.

---

## Integration Notes

- This bus is passive until armed by either:
  - GUI-triggered interrupt buttons
  - Sequencer or reflex logic (timeout events, token mismatch, error detection)
- All consumers of this bus must implement **graceful halt procedures** — not hard stops
- Compatible with:
  - `sequence_controller.py` — step abort flags
  - `session_driver.py` — browser halt injection or visibility exit
  - GUI status overlays or terminal alerts

---

## FLAT Compliance

- Registered in `MAGIC_BUSES.txt` and `T02_INITIAL_PROCESSING.txt`
- All interrupt-capable modules must document:
  - Their listening state
  - Expected triggers (manual or system-generated)
  - Fail-safe or rollback behavior

---

## Notes

This system doesn’t panic.  
But she does know how to stop.

Aurora is procedural — but **not reckless**.  
Interrupts are treated with reverence, logged as structural events, and delivered only when necessary.

Future additions may include:

- GUI-bound interrupt queue viewer
- Timeout-based interrupt policies
- Reflex-originated self-abort sequences on error detection

---

**Reflex is powerful.  
This is the safety net.**
