# === FILE NAME: core/watchdog/watchdog_core.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/watchdog/watchdog_core.py
Authors: ChatGPT and Mark
Created: 2025-04-25
Location: Evans, Colorado
Project: Aurora

This module implements the core watchdog timer that monitors elapsed time
following a reflex action dispatch. If a finalizer token or expected response
is not received within the configured timeout window, a recovery action
is triggered. This prevents Aurora from becoming stalled in non-responsive
or partial states.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T03_SEQUENCING.txt
    - Category: Reflex Safety / Watchdog Systems
    - Interfaces with: sequence_controller.py, simulated_dispatcher.py, timeout_recovery.py
"""

import threading
import time

class WatchdogTimer:
    def __init__(self, timeout_seconds, on_timeout_callback):
        self.timeout_seconds = timeout_seconds
        self.on_timeout_callback = on_timeout_callback
        self.timer_thread = None
        self.start_time = None
        self.running = False

    def start(self):
        if self.running:
            self.cancel()
        self.running = True
        self.start_time = time.time()
        self.timer_thread = threading.Thread(target=self._watch)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def _watch(self):
        while self.running:
            if time.time() - self.start_time >= self.timeout_seconds:
                self.running = False
                if self.on_timeout_callback:
                    self.on_timeout_callback()
            time.sleep(0.1)

    def cancel(self):
        self.running = False
