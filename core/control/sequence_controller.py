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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SEQUENCES BEGIN HERE. A DISPATCHER FUNCTION IS CALLED WHEN A DISPATCH MESSAGE HAS BEEN COMPOSED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.db_interface import load_sequence_steps # ************************************ Chat with aurora.db to use the "load_sequence_steps" function <<<<<<<<<<<<<<<<<<<<<<<<

class SequenceController:
    def __init__(self, sequence_id: int, simulated: bool = False, simulator_gui=None):
        self.simulated = simulated
        self.simulator_gui = simulator_gui
        self.sequence_id = sequence_id
        self.steps = load_sequence_steps(sequence_id) # ******************************** Chat with aurora.db to retrieve the sequence id. This defines the steps to be retrieved...
        self.index = 0 # <<<<<<<<<<< Maybe 1-based instead?
        self.index_store = 0 # <<<<< Sequence control after?
        self.loop_count = 0 # <<<<<< Works afaik
        self.resume = 0 # <<<<<<<<<< Works afaik
        self.history = []
        if simulated:
            from core.control import simulated_dispatcher as dispatcher # ************* If we're simulated, grab the "simulated_dispatcher" routine
        else:
            from core.control import reflex_dispatcher as dispatcher # **************** If we're not simulated, grab the "reflex_dispatcher" routine

        self.dispatch_step = dispatcher.dispatch_step # ******************************* CALL DISPATCH ROUTINE, RETURNS STEPS **********************

    def run(self): # ****************************************************************** Imaginatively named function "run" - run a loop

        print(f"[SequenceController] Starting sequence {self.sequence_id}...") # ****** Debug print sequence startup data

        while self.index < len(self.steps): # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RMEMEBER: STEPS ARE INDEXED FROM OUTSIDE THIS ROUTINE <<<<<

            if self.resume:

                """ SUB STEP ROUTINE BLOCK
                if "substeps" in step and step.get("repeat_count", 0) < len(step["substeps"]):
                    substep_text = step["substeps"][step["repeat_count"]]
                    print(f"[SequenceController] Processing substep: {substep_text}")
                    result = self.dispatch_step({"instruction": substep_text})
                else:
                    result = self.dispatch_step(step)
                """

                step = self.steps[self.index_store] # ******************************* While running after first pass

            else:

                step = self.steps[self.index] # ************************************* For first entry

            print(f"[SequenceController] Length of self.steps is: {len(self.steps)}")
            print(f"[SequenceController] Executing step_order {step['step_order']} (index {self.index}): {step.get('instruction')}")

            result = self.dispatch_step(step) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Call the dispatcher

            if isinstance(result, str) and "step complete" in result: # ************* If the function returned "step complete" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                print(f"[SequenceController] Step {self.index} Complete. Awaiting next trigger. Holding...")
                self.index += 1
                self.resume = 1
                self.index_store = self.index

                prompt_text = (f"[SequenceController] Step {self.index} Complete. Awaiting next trigger. Holding...") # <<<<<<<<<<<<<<<<< UPDATE LOG WINDOW
                from PySide6.QtCore import QMetaObject, Qt, Q_ARG

                if self.simulator_gui:
                    QMetaObject.invokeMethod(
                        self.simulator_gui,
                        "update_response_log",  # ********************************* Write to GUI "response_log"; this is defined in PromptSimulatorWindow
                        Qt.QueuedConnection,
                        Q_ARG(str, prompt_text)
                    )
                continue

            elif isinstance(result, str) and "step incomplete" in result: # ************ If the function returned "step incomplete" **************
                print(f"[SequenceController] Step {self.index} incomplete due to missing response trigger. Holding...")
                self.resume = 1
                self.index_store = self.index

                prompt_text = (f"[SequenceController] Step {self.index} Inomplete. Awaiting retry. Holding...") # <<<<<<<<<<<<<<<<< UPDATE LOG WINDOW
                from PySide6.QtCore import QMetaObject, Qt, Q_ARG

                if self.simulator_gui:
                    QMetaObject.invokeMethod(
                        self.simulator_gui,
                        "update_response_log",  # ********************************* Write to GUI "response_log"; this is defined in PromptSimulatorWindow
                        Qt.QueuedConnection,
                        Q_ARG(str, prompt_text)
                    )
                continue

            else:
                print(f"[SequenceController] Step {self.index} would have runaway. Result was: {result}")
                self.resume = 0
                #break
                continue

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
            if step.get('jump') not in (None, 0):
                target_step_order = step['jump']
                rpt = step.get('jmp_rpt', 0)

                if rpt == 0 or self.loop_count < rpt:
                    # Locate the step with matching step_order
                    target_index = next(
                        (i for i, s in enumerate(self.steps) if s["step_order"] == target_step_order),
                        None
                    )

                    if target_index is None:
                        print(f"[SequenceController] ERROR: jump target step_order {target_step_order} not found. Skipping jump.")
                    else:
                        loop_display = f"{self.loop_count + 1}/{rpt}" if rpt else f"{self.loop_count + 1}/(infinite)"

                        if target_index == self.index and rpt == 0:
                            print(f"[SequenceController] ERROR: Infinite self-jump detected at index {self.index}. Aborting sequence.")
                            break

                        print(f"[SequenceController] Jumping to step_order {target_step_order} (index {target_index}) — loop {loop_display}")
                        self.index = target_index
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

