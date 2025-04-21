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

def inject_simulator(sim):
    global simulator_instance
    simulator_instance = sim
    print("[SimulatedDispatcher] Simulator connected.")

def dispatch_step(step: dict) -> str:
    """
    Handle a single sequence step in simulation mode.
    Instead of browser actions, prompt and response are handled via UI.
    """
    if simulator_instance is None:
        print("[SimulatedDispatcher] ERROR: No simulator attached.")
        return "(Simulator not ready)"

    command = step.get("command", "").strip()

    # If no command, attempt reflex resolution
    if not command:
        reflex_id = step.get("reflex_action", 0)
        if reflex_id:
            try:
                command = resolve_reflex_action(reflex_id)
                if command:
                    print(f"[SimulatedDispatcher] Resolved reflex_action {reflex_id} to command: {command}")
                else:
                    print(f"[SimulatedDispatcher] ERROR: reflex_action {reflex_id} returned nothing.")
            except Exception as e:
                print(f"[SimulatedDispatcher] ERROR resolving reflex_action {reflex_id}: {e}")

            # === INSERT TRANSLATION LOGIC HERE ===
            if command and command.upper() == "LAUNCH BROWSER":
                command = "PROMPT: [Simulated browser launch triggered.]"

    # Still nothing? Bail.
    if not command:
        print("[SimulatedDispatcher] ERROR: Step has no command after reflex resolution. Skipping.")
        return "(No command found in step)"

    if command.startswith("PROMPT:"):
        prompt_text = command[len("PROMPT:"):].strip()
        from PySide6.QtCore import QMetaObject, Qt, Q_ARG

        QMetaObject.invokeMethod(
            simulator_instance,
            "inject_prompt",
            Qt.QueuedConnection,
            Q_ARG(str, prompt_text)
        )

        print(f"[SimulatedDispatcher] Prompt sent to simulator: {prompt_text[:80]}")

        # Block until simulated response is received
        print("[SimulatedDispatcher] Waiting for user response...")

        try:
            reply = response_queue.get(timeout=300)  # Wait max 5 minutes
            print(f"[SimulatedDispatcher] Received simulated reply: {reply}")
        except Exception as e:
            print(f"[SimulatedDispatcher] ERROR: response queue timeout or crash: {e}")
            return "(Simulated) Dispatcher timeout or abort."

        # Check for expected trigger
        expected_key_id = step.get("expected", 0)
        expected_token = None
        print(f"[SimulatedDispatcher] DEBUG: Step metadata -> step_order = {step.get('step_order')}, expected_id = {expected_key_id}")

        if expected_key_id:
            try:
                from data.db_interface import resolve_key_phrase
                expected_token = resolve_key_phrase(expected_key_id)
                print(f"[SimulatedDispatcher] DEBUG: Resolved expected_token = '{expected_token}'")
            except Exception as e:
                print(f"[SimulatedDispatcher] WARNING: Could not resolve expected token {expected_key_id}: {e}")

        if expected_token:
            if expected_token in reply:
                print(f"[SimulatedDispatcher] Expected token '{expected_token}' FOUND in reply.")
                return "(Simulated) Trigger match: step complete."
            else:
                print(f"[SimulatedDispatcher] Expected token '{expected_token}' NOT FOUND. Holding at this step.")
                return "(Simulated) Trigger missing: step incomplete."
        else:
            print("[SimulatedDispatcher] No expected token defined. Proceeding by default.")
            return reply

    elif command.startswith("WAIT:"):
        seconds = int(command[len("WAIT:"):].strip())
        print(f"[SimulatedDispatcher] Simulated wait for {seconds} seconds.")
        time.sleep(seconds)
        return f"(Simulated) Waited {seconds} seconds."

    elif command.upper().startswith("CHECK:"):
        token = command[6:].strip().strip("/")
        print(f"[SimulatedDispatcher] Simulated check for token: /{token}/ (not implemented)")
        return f"(Simulated) CHECK:/{token}/"

    else:
        print(f"[SimulatedDispatcher] Unhandled command: {command}")
        return f"(Simulated) Unhandled: {command}"
