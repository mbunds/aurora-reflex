# === FILE NAME: core/control/sequence_controller.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/control/sequence_controller.py
Authors: ChatGPT and Mark
Created: 2025-04-16
Location: Evans, Colorado
Project: Aurora

Main orchestrator for executing sequence-driven reflex logic. This module reads
step instructions from the database, triggers reflex execution via dispatcher,
tracks jump/repeat state, and evaluates completion or interrupts.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T02_INITIAL_PROCESSING.txt
    - This file participates in the T02-B04_SEQ_CONT branch of development.
    - All session behaviors are tracked and logged through flat file modules.

---

Sequence Controller

Executes step-based sequences stored in the database. Supports step jumping,
bounded loops, reflex triggering, and future interrupt integration.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.db_interface import load_sequence_steps

class SequenceController:
    def __init__(self, sequence_id: int, simulated: bool = False):
        self.simulated = simulated
        self.sequence_id = sequence_id
        self.steps = load_sequence_steps(sequence_id)
        self.index = 0
        self.loop_count = 0
        self.history = []
        if simulated:
            from core.control import simulated_dispatcher as dispatcher
        else:
            from core.control import reflex_dispatcher as dispatcher

        self.dispatch_step = dispatcher.dispatch_step

    def run(self):
        print(f"[SequenceController] Starting sequence {self.sequence_id}...")
        while self.index < len(self.steps):
            step = self.steps[self.index]
            print(f"[SequenceController] Executing step_order {step['step_order']} (index {self.index}): {step.get('instruction')}")

            result = self.dispatch_step(step)

            self.history.append({
                "index": self.index,
                "step": step,
                "result": result
            })

            # Handle per-step repeat logic
            step_repeat = step.get("repeat", 0)
            if step_repeat > 0:
                if "repeat_count" not in step:
                    step["repeat_count"] = 1
                else:
                    step["repeat_count"] += 1

                if step["repeat_count"] < step_repeat:
                    print(f"[SequenceController] Repeating step {self.index} ({step['repeat_count']}/{step_repeat})")
                    continue
                else:
                    print(f"[SequenceController] Step {self.index} reached repeat limit. Continuing.")
                    step["repeat_count"] = 0  # Optional cleanup

            # Check for jump
            if step.get('jump') is not None:
                target = step['jump']
                rpt = step.get('jmp_rpt', 0)
                if rpt == 0 or self.loop_count < rpt:
                    loop_display = f"{self.loop_count + 1}/{rpt}" if rpt else f"{self.loop_count + 1}/(infinite)"
                    target_step = self.steps[target]
                    print(f"[SequenceController] Jumping to step_order {target_step['step_order']} (index {target}) — loop {loop_display}")
                    self.index = target
                    self.loop_count += 1
                    continue
                else:
                    print("[SequenceController] Jump limit reached. Continuing.")
                    self.loop_count = 0

            self.index += 1

        print(f"[SequenceController] Sequence {self.sequence_id} completed.")

if __name__ == "__main__":
    from data.db_interface import get_sequence_id_by_name

    seq_id = get_sequence_id_by_name("SHOW MODE")
    if seq_id is None:
        print("[SequenceController] ERROR: Sequence 'SHOW MODE' not found.")
        sys.exit(1)

    controller = SequenceController(sequence_id=seq_id)
    controller.run()
