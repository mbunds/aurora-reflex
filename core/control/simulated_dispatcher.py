# === FILE NAME: core/control/simulated_dispatcher.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/control/simulated_dispatcher.py
Authors: ChatGPT and Mark
Created: 2025-04-20
Location: Evans, Colorado
Project: Aurora

Simulated dispatcher module that replaces browser interaction with GUI-driven
manual prompt/response exchange. Used for development, testing, and verification
of sequence behavior without launching an actual ChatGPT session.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T03_SEQUENCING.txt
    - This file participates in the T02-B04_SEQ_CONT branch of development.
    - Used in place of reflex_dispatcher during simulation mode.
---

Simulated Reflex Dispatcher

Provides prompt injection and wait emulation without launching a browser.
Prompts appear in the PromptSimulatorWindow; replies are entered manually.
"""

import time
import os
import sys
from queue import Queue

# Ensure 'data' is in sys.path for correct resolution of db_interface
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.db_interface import resolve_reflex_action

# This global is populated externally
simulator_instance = None
response_queue = Queue()


def inject_simulator(sim): # ************************************* Called by prompt_simulator_window
    global simulator_instance
    simulator_instance = sim
    print("[SimulatedDispatcher] Simulator connected.")

def dispatch_step(step: dict) -> str: # *************************** Define function "dispatch_step"
    """
    Handle a single sequence step in simulation mode.
    Instead of browser actions, prompt and response are handled via UI.
    """
    if simulator_instance is None:
        print("[SimulatedDispatcher] ERROR: No simulator attached.")
        return "(Simulator not ready)"

    expected_id  = step.get("expected", 0) # ********************** Get the value from the "expected" field and assign it to expected_id
    if expected_id: # ********************************************* If the value in expected_id is not empty
        try:
            expected = resolve_reflex_action(expected_id) # ******* Chat with aurora.db to return the value in the "expected_id" field and assign it to "expected"
            if expected: # **************************************** If expected is not empty
                print(f"[SimulatedDispatcher] Resolved expected {expected_id} to expected: {expected}") # **** Debug print resolved value in expected
            else:
                print(f"[SimulatedDispatcher] ERROR: expected {expected_id} returned nothing.") # ************ Debug print failure to resolve value in expected_id
        except Exception as e:
            print(f"[SimulatedDispatcher] ERROR resolving expectd {expected_id}: {e}") # ********************* Debug print error resolving value in expected_id

    # If no command, attempt reflex resolution

    reflex_id = step.get("reflex_action", 0)
    if reflex_id:
        try:
            reflex = resolve_reflex_action(reflex_id)
            if reflex:
                print(f"[SimulatedDispatcher] Resolved reflex_action {reflex_id} to reflex: {reflex}")
            else:
                print(f"[SimulatedDispatcher] ERROR: reflex_action {reflex_id} returned nothing.")
        except Exception as e:
            print(f"[SimulatedDispatcher] ERROR resolving reflex_action {reflex_id}: {e}")

    # Still nothing? Bail.
    if not expected:
        print("[SimulatedDispatcher] ERROR: Step has no value in the field named  expected. Skipping.")
        return "(Value for expected not found in step)"

    elif not reflex:
        print("[SimulatedDispatcher] ERROR: Step has no value in the field named reflex. Skipping.")
        return "(Value for expected not found in step)"

    # *************************************************************************** Check the contents of the "expected" field
    if expected.startswith("PROMPT:"):
        print(f"[Command Starts With:] {expected_id}; command: {expected}")
        # Block until simulated response is received
        print("[SimulatedDispatcher] Waiting for user response...")
        while response_queue.empty():
            time.sleep(0.1)

        reply = response_queue.get()
        print(f"[SimulatedDispatcher] Received simulated reply: {reply}")

        #  *********************************************************************** Check for trigger in the "expected" field

        expected_key_id = step.get("reflex_action", 0)# ************************** Assign the string value in the "reflex_action" field
        expected_token = None

        if expected_key_id:# ***************************************************** If the "expected_key_id" value is not empty
            try:
                expected_token = resolve_reflex_action(expected_key_id)# ********* Chat with aurora.db to see if there is a match to expected_token
            except Exception as e:
                print(f"[SimulatedDispatcher] WARNING: Could not resolve expected token {expected_key_id}: {e}")# *************** If oops

            if expected_token:# ************************************************** If the "expected_token" value is not empty
                if expected_token in reply:# ************************************* If expected_token matches the user input
                    print(f"[SimulatedDispatcher] Expected token '{expected_token}' FOUND in reply.")#*************************** Debug print token found
                    return "(Simulated) Trigger match: step complete."# ********** Back to routine report "step complete" >>>>>>>>>>>>>>>>>
                else:
                    print(f"[SimulatedDispatcher] Expected token '{expected_token}' NOT FOUND. Holding at this step.")# ********* Debug print token not found
                    return "(Simulated) Trigger missing: step incomplete."# ****** Back to routine report "step incomplete" >>>>>>>>>>>>>>>
        else:
            print("[SimulatedDispatcher] No expected token defined. Proceeding by default.")# ******** If the "expected_key_id" value is empty
            return reply# ******************************************************** Back to routine return user input

    elif expected.startswith("WAIT:"):
        seconds = int(expected[len("WAIT:"):].strip())
        print(f"[SimulatedDispatcher] Simulated wait for {seconds} seconds.")
        time.sleep(seconds)
        return f"(Simulated) Waited {seconds} seconds."

    elif expected.upper().startswith("CHECK:"):
        token = expected[6:].strip().strip("/")
        print(f"[SimulatedDispatcher] Simulated check for token: /{token}/ (not implemented)")
        return f"(Simulated) CHECK:/{token}/"

    else:
        print(f"[SimulatedDispatcher] Unhandled command: {expected}")
        return f"(Simulated) Unhandled: {expected}"

    prompt_text = expected
    from PySide6.QtCore import QMetaObject, Qt, Q_ARG

    QMetaObject.invokeMethod(
        simulator_instance,
        "inject_prompt",
        Qt.QueuedConnection,
        Q_ARG(str, prompt_text)
    )

    print(f"[SimulatedDispatcher] Prompt sent to simulator: {prompt_text[:80]}")

