# === FILE NAME: core/control/reflex_dispatcher.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/control/reflex_dispatcher.py
Authors: ChatGPT and Mark
Created: 2025-04-16
Location: Evans, Colorado
Project: Aurora

This module is the reflex dispatcher for sequence steps. Each step's command
string is interpreted and routed to a reflex action (e.g., prompt injection,
DOM parse, interrupt check). Designed for modular expansion.

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

Reflex Dispatcher

Parses a sequence step and triggers the corresponding reflex behavior.
Supports prompt submission and keyword-based wait cycles for session control.
"""

import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from core.web.session_driver import SessionDriver
from selenium.webdriver.common.by import By

driver = None

def init_driver():
    global driver
    if driver is None:
        print("[ReflexDispatcher] Initializing session driver...")
        driver = SessionDriver(headless=False)
        driver.start_session()

def dispatch_step(step: dict) -> str:
    """
    Interpret and execute a single step from a sequence.
    Args: step (dict): A dictionary with step info, including 'command'.
    Returns: str: Result message.
    """
    # Reflex action takes precedence over command if present
    if step.get("reflex_action"):
        import sqlite3
        try:
            from core.data.db_interface import DB_PATH, resolve_long_phrase
        except ModuleNotFoundError:
            import sys, os
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
            from data.db_interface import DB_PATH, resolve_long_phrase

        reflex_id = step["reflex_action"]
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT direction, is_phrase, long_phrase, key FROM keys WHERE id = ?", (reflex_id,))
        row = cur.fetchone()
        conn.close()
        # Examine "direction" (1=in, 2=out, 3=bidir, 4=internal) "is_phrase", "long_phrase_id", on "row"
        #
        if row:
            direction, is_phrase, long_phrase_id, key_value = row
            if direction == 4:
                if is_phrase > 0 and long_phrase_id > 0:
                    phrase = resolve_long_phrase(long_phrase_id)
                    print(f"[ReflexDispatcher] Reflex {reflex_id} → long_phrase → {phrase}")
                    return dispatch_step({"command": phrase})
                elif key_value:
                    print(f"[ReflexDispatcher] Reflex {reflex_id} → key → {key_value}")
                    return dispatch_step({"command": key_value})
                else:
                    print(f"[ReflexDispatcher] Reflex {reflex_id} has no usable string.")
                    return f"Reflex {reflex_id} empty."
            else:
                print(f"[ReflexDispatcher] Reflex {reflex_id} ignored — direction != 4")
                return f"Reflex {reflex_id} skipped — not internal"

    # Fallback to normal command handling
    command = step.get("command", "")
    print(f"[ReflexDispatcher] Dispatching command: {command}")

    if command.upper() == "LAUNCH BROWSER":
        init_driver()
        return "Browser launched via internal reflex."

    if command.startswith("PROMPT:"):
        prompt_text = command[len("PROMPT:"):].strip()
        init_driver()
        driver.submit_prompt(prompt_text)
        wait_for_response_completion()
        return f"Prompt submitted: {prompt_text[:40]}..."

    elif command.startswith("WAIT:"):
        seconds = int(command[len("WAIT:"):].strip())
        print(f"[ReflexDispatcher] Waiting {seconds} seconds...")
        time.sleep(seconds)
        return f"Waited {seconds} seconds."

    elif command == "CHECK:/CODE COMPLETE/":
        html = driver.get_current_html()
        if "/CODE COMPLETE/" in html:
            return "Completion token detected."
        return "No completion token found."

def wait_for_response_completion(timeout=60, pause_threshold=3.0):
    """
    Wait for the assistant response to stabilize by monitoring DOM text growth.
    """
    print("[ReflexDispatcher] Monitoring assistant message for completion...")
    end_time = time.time() + timeout
    last_length = 0
    last_change = time.time()

    while time.time() < end_time:
        bubbles = driver.browser.driver.find_elements(
            By.CSS_SELECTOR, 'div[data-message-author-role="assistant"] div.markdown.prose p'
        )
        code_blocks = driver.browser.driver.find_elements(
            By.CSS_SELECTOR, 'div[data-message-author-role="assistant"] pre code'
        )

        try:
            all_text = (
                "\n".join(b.text.strip() for b in bubbles if b.text.strip()) +
                "\n".join(c.text.strip() for c in code_blocks if c.text.strip())
            )
        except Exception as e:
            print(f"[ReflexDispatcher] DOM read error: {e}")
            time.sleep(0.25)
            continue

        current_length = len(all_text)

        if current_length > last_length + 10:
            last_length = current_length
            last_change = time.time()

        elif time.time() - last_change >= pause_threshold:
            print("[ReflexDispatcher] Assistant response appears complete.")
            return

        time.sleep(0.25)

    print("[ReflexDispatcher] Timeout: Response may be incomplete.")

if __name__ == "__main__":
    demo_step = {"command": "PROMPT: Hello world from SHOW MODE!"}
    print(dispatch_step(demo_step))
