# === FILE NAME: core/watchdog/watchdog_manager.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/watchdog/watchdog_manager.py
Authors: ChatGPT and Mark
Created: 2025-04-25
Location: Evans, Colorado
Project: Aurora

This module provides high-level control over the watchdog system,
handling timer initialization, cancellation, and timeout escalation
via recovery routines. It acts as the central interface between
runtime step execution and reflexive fault handling.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T03_SEQUENCING.txt
    - Category: Reflex Supervision / Watchdog Manager
    - Interfaces with: watchdog_core.py, timeout_recovery.py, sequence_controller.py
"""

from core.watchdog.watchdog_core import WatchdogTimer
from core.watchdog import timeout_recovery

# Global watchdog timer instance
_active_watchdog = None

def start_watchdog(timeout_seconds, context=None):
    """
    Start a new watchdog timer for the current step or reflex operation.
    """
    global _active_watchdog
    print(f"[WatchdogManager] Starting watchdog timer: {timeout_seconds} seconds")

    def on_timeout():
        print("[WatchdogManager] Watchdog triggered timeout event.")
        timeout_recovery.retry_current_step(context)

    _active_watchdog = WatchdogTimer(timeout_seconds, on_timeout)
    _active_watchdog.start()

def cancel_watchdog():
    """
    Cancel any active watchdog timer.
    """
    global _active_watchdog
    if _active_watchdog:
        print("[WatchdogManager] Cancelling active watchdog timer.")
        _active_watchdog.cancel()
        _active_watchdog = None
