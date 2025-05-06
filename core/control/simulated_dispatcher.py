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

04/23/2025 - UNDER EXAMINATION FOR REFACTOR - REFLEX_TOKEN_PARSER.PY WILL PASS STEP PERMISSIVES

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
from core.utils.reflex_token_parser import parse_reflex_tokens_with_args
from core.api import launch_app, open_folder  # From routed __init__.py (platform-safe)

# Ensure 'data' is in sys.path for correct resolution of db_interface
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.db_interface import resolve_reflex_action
from PySide6.QtCore import QMetaObject, Qt, Q_ARG

# This global is populated externally
simulator_instance = None
response_queue = Queue() # ########################## DISPATCHER RESPONSE_QUEUE DEFINED IN PROMPT_SIMULATOR_WINDOW - CRITICAL ##############

def log_to_gui(msg: str):
    if simulator_instance:
        QMetaObject.invokeMethod(
            simulator_instance,
            "update_injected_prompt",
            #"update_response_log",
            Qt.QueuedConnection,
            Q_ARG(str, msg)
        )

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
                log_to_gui(f"[SimulatedDispatcher] Resolved expected {expected_id} to expected: {expected}") # ####################### LOG TO GUI
            else:
                print(f"[SimulatedDispatcher] ERROR: expected {expected_id} returned nothing.") # ************ Debug print failure to resolve value in expected_id
        except Exception as e:
            print(f"[SimulatedDispatcher] ERROR resolving expectd {expected_id}: {e}") # ********************* Debug print error resolving value in expected_id

    # *************************************************************************** If no command, attempt reflex resolution

    reflex_id = step.get("reflex_action", 0) # <- <- <- <- <- <- CAUSE OF THREAD RUNAWAY <- <- <- <- <- <-
    if reflex_id:
        try:
            reflex = resolve_reflex_action(reflex_id)
            if reflex:
                print(f"[SimulatedDispatcher] Resolved reflex_action {reflex_id} to reflex: {reflex}")
            else:
                print(f"[SimulatedDispatcher] ERROR: reflex_action {reflex_id} returned nothing.")
        except Exception as e:
            print(f"[SimulatedDispatcher] ERROR resolving reflex_action {reflex_id}: {e}")

    # *************************************************************************** Still nothing? Bail. <- <- <- <- <- <- WON'T HAPPEN AFTER REFACTOR
    if not expected:
        print("[SimulatedDispatcher] ERROR: Step has no value in the field named  expected. Skipping.")
        return "(Value for expected not found in step)"

    elif not reflex:
        print("[SimulatedDispatcher] ERROR: Step has no value in the field named reflex. Skipping.")
        return "(Value for expected not found in step)"

    # *************************************************************************** Check the contents of the "expected" field <- <- <- <- <- <- AUTO TO NEXT LINE? FIRST EXECUTION?
    if expected: # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> We have a value in "expected" <<<<<<<<<<<<<<<<<<
        print(f"[SimulatedDispatcher] Command: {expected_id}; Expected Command: {expected}")
        # Block until simulated response is received
        print("[SimulatedDispatcher] Waiting for prompt input...")
        while response_queue.empty(): # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> RESPONSE QUEUE HOLD HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            time.sleep(0.1)

        reply = response_queue.get() # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> We have the simulated response representing that expected from the AI <<<<<<<<<<<<<<<<<<<<
        print(f"[SimulatedDispatcher] Received simulated reply: {reply}")
        if reply == "HALT":
            return reply

        # ==========================================================
        # Parse reflex tokens and attempt API command dispatch
        # ==========================================================
        #from core.utils.reflex_token_parser import parse_reflex_tokens_with_args
        #from core.api import launch_app, open_folder  # Routed by OS

        """
        Parses reflex-style tokens of the format /TOKEN/ or /TOKEN: ARGUMENT/ from response text.

        Args:
            response_text (str): The full GPT response or any string Aurora should parse.
            expected (str, optional): If provided, the parser will check if the final token matches this.

        Returns:
            dict: {
                "expected_matched": bool,  # Whether the final token matched expected.
                "finalizer": str or None,  # The last token found.
                "all_tokens": list of str, # All /TOKEN/ strings found.
                "arguments": dict,         # Mapping of each token to its ARGUMENT (or None if not present).
                "raw": str,                # The original response text.
                "match_reason": str,       # Explanation if no tokens were found.
            }
        """

        parsed = parse_reflex_tokens_with_args(reply, expected) # >>>>>>>>>>>>>>>>>>>>>>>> Supply the parsing function with "reply" and "expected" for comparison.

        if parsed["expected_matched"]: # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> If the function returns this string, "expected_matched".
            print("[SimulatedDispatcher] Expected token matched. Proceeding with reflex command(s)...")

            for token, arg in parsed["arguments"].items(): # >>>>>>>>>>>>>>>>>>>>>>>>>>>>> Test for specific reflex tokens, in this instance "system commands"....
                if token == "/LAUNCH APP/": # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> In this instance looking for the string "/LAUNCH APP/"...
                    result = launch_app(arg)# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> If so launch this...
                    print(f"[SimulatedDispatcher] [EXEC] launch_app('{arg}') → {result}")
                elif token == "/OPEN FOLDER/": # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> In this instance looking for the string "/OPEN FOLDER/"...
                    result = open_folder(arg)# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> If so launch this...
                    print(f"[SimulatedDispatcher] [EXEC] open_folder('{arg}') → {result}")

            return "(Simulated) Trigger match: step complete."
        else:
            print(f"[SimulatedDispatcher] Finalizer '{expected}' not found in reply. Holding at step.")
            return "(Simulated) Trigger missing: step incomplete."


        #  *********************************************************************** Check for trigger in the "expected" field <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        expected_key_id = step.get("reflex_action", 0)# ************************** Assign the string value in the "reflex_action" field
        expected_token = None

        if expected_key_id:# ***************************************************** If the "expected_key_id" value is not empty
            try:
                expected_token = resolve_reflex_action(expected_key_id)# ********* Chat with aurora.db to see if there is a match to expected_token. <- <- <- <- <- <- MATCH TOKEN
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
            return reply # ******************************************************** Back to routine return user input

    else:
        print(f"[SimulatedDispatcher] Unhandled command: {expected}")
        return f"(Simulated) Unhandled: {expected}"

    print(f"[SimulatedDispatcher] Prompt sent to simulator: {reply}")
