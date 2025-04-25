# === FILE: core/watchdog/README.md ===

# AURORA – Reflex Supervision and Watchdog System

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-25  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** Initial implementation of reflex watchdog and recovery framework  
**License:** MIT  
**FLAT Registered In:** T03_SEQUENCING.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)

---

## Purpose

This folder implements the **watchdog system** for Aurora's reflex engine.  
It supervises session runtime behaviors, detects unresponsive or stalled steps,  
and triggers structured recovery operations if reflex completion thresholds are not met.

The watchdog is essential for ensuring Aurora maintains flow control even  
when external systems (such as GPT sessions, DOM handlers, or network services)  
fail, stall, or degrade.

This is **Aurora's survival reflex**.

---

## Responsibilities

- Monitor elapsed time after reflex dispatch
- Detect missing finalizers or stalled session responses
- Trigger recovery behaviors such as:
  - Retry step
  - Abort sequence
  - Generate diagnostic reports
- Provide centralized reflex safety and liveness enforcement
- Future support for liveness health probes and heartbeat monitoring

---

## Structure

- `watchdog_core.py`  
  Core low-level watchdog timer implementation based on background threading.

- `timeout_recovery.py`  
  Reflex recovery routines activated by timeout events.

- `watchdog_manager.py`  
  High-level orchestrator that manages timer lifecycle and recovery integration.

---

## Integration Path

1. A step is dispatched in `sequence_controller.py`
2. `watchdog_manager.start_watchdog(timeout_seconds, context)` is called
3. If finalizer token is received, `watchdog_manager.cancel_watchdog()` is triggered
4. If timeout occurs, `timeout_recovery` routines are called automatically
5. Sequence either retries, aborts, or escalates based on reflex context

---

## Example Triggers

```txt
- Missing /CODE COMPLETE/ after 30 seconds
- No DOM bubbles detected during prompt response window
- Internal API command fails without confirmation
