# === FILE: tests/test_submit_prompt_demo.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: tests/test_submit_prompt_demo.py
Authors: ChatGPT and Mark
Created: 2025-04-13
Location: Evans, Colorado
Project: Aurora

This module performs a demonstration of programmatic prompt submission:
- SessionDriver
- HTMLParser
- ElementMapper

It assumes access to a live browser environment.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora reflexive test suite. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T01_OVERVIEW.txt
    - This test supports branch T01-B01_HTML_CONNECT
    - Will be included in future unified test runner

---

Programmatic Prompt Entry and Submission Test

This suite verifies the live behavior of browser sessions, HTML extraction, DOM parsing,
and semantic element mapping. This module will inject then submit a prompt. SSE/FLAT ensures
stability across expected interface structures.
"""
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.web.session_driver import SessionDriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = SessionDriver(headless=False)
    driver.start_session()

    driver.submit_prompt("Aurora test session phase 17.  Please name this session AURORA_TEST_17. This prompt is from session T02-B03_INNERTEXT_REFACTOR. This is a test of the auto-prompt submission system, please write a complete Python script that loads a YAML configuration file using the PyYAML library, validates specific required fields, and prints a summary report. Use a class to encapsulate the logic and include a CLI that accepts the config file path. Include argument parsing, error handling, field validation, and a usage example at the bottom. Output a single, complete, well-formatted code block. Render the code using the full-screen code editor. Make your last response be /CODE COMPLETE/")

    def wait_for_response_completion(
        driver,
        timeout=60,
        pause_threshold=3.0,
        min_growth=10,
        min_blocks=4,
        min_chars=500
    ):
        """Wait for assistant response to stabilize, tracking both <p> and <code> blocks."""
        print("[Wait] Monitoring assistant message for stability...")
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

                # Fast exit if CODE COMPLETE marker is detected
                if "/CODE COMPLETE/" in all_text:
                    print("[Wait] CODE COMPLETE marker found — skipping wait.")
                    return

            except Exception as e:
                print(f"[Wait] DOM changed during read: {e}. Retrying...")
                time.sleep(0.25)
                continue

            current_length = len(all_text)
            total_blocks = len(bubbles) + len(code_blocks)

            if current_length > last_length + min_growth:
                last_length = current_length
                last_change = time.time()

            elif (
                time.time() - last_change >= pause_threshold and
                current_length >= min_chars and
                total_blocks >= min_blocks
            ):
                print("[Wait] Assistant response appears complete.")
                return

            time.sleep(0.25)

        print("[Wait] Timeout: Assistant response never stabilized.")

    wait_for_response_completion(driver)
    driver.last_html = driver.browser.get_page_source()
    html = driver.get_current_html()
    print("[Demo] Captured HTML after prompt submission.")
    print(html[:1500])

    from core.web.html.html_parser import HTMLParser
    parser = HTMLParser(html)

    bubbles = parser.list_message_bubbles()

    if bubbles:
        print(f"\n[Demo] Found {len(bubbles)} message bubbles.")
        for i, bubble in enumerate(bubbles):
            text = bubble.get_text(strip=True)
            print(f"[Bubble {i+1}]: {text or '[empty]'}")

        latest = bubbles[-1]
        print(f"\n[Debug] Raw extracted <p>: {repr(latest)}")
        latest_text = latest.get_text(strip=True)

        if latest_text:
            print("\n[Demo] Latest AI Response:")
            print(latest_text)
        else:
            print("\n[Demo] Message bubble was empty.")
    else:
        print("\n[Demo] No message bubbles found.")

    code_blocks = parser.list_code_blocks()

    if code_blocks:
        print(f"\n[Demo] Found {len(code_blocks)} code block(s).")
        for i, block in enumerate(code_blocks):
            print(f"\n[Code Block {i+1}]:\n{block.get_text(strip=True)}")
    else:
        print("\n[Demo] No <pre><code> blocks found. Checking for Monaco editor lines...")
        monaco_lines = parser.list_monaco_code_lines()
        if monaco_lines:
            print(f"\n[Demo] Found {len(monaco_lines)} Monaco editor line(s). Stitching code block...")
            stitched = "\n".join(line.get_text(strip=True) for line in monaco_lines)
            print("\n[Editor Code Block Captured]:")
            print(stitched)
            # Sanitize the flattened code using code_sanitizer
            from core.web.code_sanitizer import sanitize_flattened_code
            print("\n[Sanitizer] Running code restoration...")
            restored = sanitize_flattened_code(stitched)
            print("\n[Restored Code Block]:")
            print(restored)
        else:
            print("\n[Demo] No Monaco code lines found either.")
            # Final fallback: extract using innerText via ElementMapper
            print("\n[Demo] Attempting innerText-based extraction via ElementMapper...")
            elements = driver.browser.driver.find_elements(
                By.CSS_SELECTOR, 'div[data-message-author-role=\"assistant\"] pre code'
            )
            from core.web.html.element_mapper import extract_code_blocks_by_innertext
            innertext_blocks = extract_code_blocks_by_innertext(elements)

            if innertext_blocks:
                print(f"\n[Demo] Extracted {len(innertext_blocks)} block(s) via innerText:")
                for i, block in enumerate(innertext_blocks):
                    print(f"\n[innerText Block {i+1}]:\n{block}")
            else:
                print("\n[Demo] No blocks recovered via innerText fallback.")

    driver.close_session()
