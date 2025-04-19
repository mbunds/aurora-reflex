# === FILE: core/web/session_driver.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/session_driver.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

This module manages the coordination of browser-based ChatGPT sessions.
It serves as a controller layer above `browser_controller.py`, handling
session logic such as initialization, error handling, and future features
like cookie management or authentication persistence.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T01_OVERVIEW.txt
    - This file participates in the T01-B01_HTML_CONNECT branch of development.
    - All session behaviors are tracked and logged through flat file modules.

---

Session Driver

Orchestrates browser session startup, teardown, and HTML retrieval.
Acts as the outer wrapper for user-facing session control logic.
"""

import time

from core.web.browser_controller import BrowserController
from core.web.html.html_parser import HTMLParser
from core.web.html.element_mapper import ElementMapper  # NEW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionDriver:
    def __init__(self, headless=False):
        self.browser = BrowserController(headless=headless)
        self.last_html = None
        self.parser = None

    def start_session(self):
        print("[SessionDriver] Launching ChatGPT browser session...")
        self.browser.launch_browser()
        self.last_html = self.browser.get_page_source()
        print("[SessionDriver] HTML captured. Initializing parser...")
        self.parser = HTMLParser(self.last_html)
        print("[SessionDriver] Initializing element mapper...")
        self.mapper = ElementMapper()
        #self.mapper.auto_map_from_parser(self.parser)
        print("[SessionDriver] ElementMapper ready.")

    def get_mapper(self):
        return self.mapper

    def get_current_html(self):
        return self.last_html

    def get_parser(self):
        return self.parser

    def close_session(self):
        print("[SessionDriver] Closing browser session...")
        self.browser.close_browser()
        print("[SessionDriver] Session closed.")

    def submit_prompt(self, text: str):
        """Programmatically submit a prompt to the ChatGPT web GUI."""
        print(f"[SessionDriver] Submitting prompt: {text}")

        wait = WebDriverWait(self.browser.driver, 15)

        # Wait for presence, not clickability
        textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"]')))

        # Scroll it into view
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

        # Force focus by clicking it
        textarea.click()

        # Now send the keys
        textarea.clear()
        textarea.send_keys(text)
        textarea.send_keys(Keys.ENTER)

        self.last_html = self.browser.get_page_source()

        # Optional fallback — click the Send button if needed:
        # send_button = self.browser.driver.find_element(By.XPATH, "//button[contains(., 'Send')]")
        # send_button.click()

        print("[SessionDriver] Prompt submitted.")

    def wait_for_assistant_response(self, timeout=30):
        """Wait for assistant message bubble that confirms rendering is complete."""
        print("[SessionDriver] Waiting for assistant message bubble to confirm render...")
        wait = WebDriverWait(self.browser.driver, timeout)
        try:
            # Check for a ChatGPT response bubble that includes confirmation language
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, 'div.markdown.prose'),
                    "/CODE COMPLETE/"
                )
            )
            print("[SessionDriver] Assistant confirmed render in message bubble.")
        except Exception as e:
            print(f"[SessionDriver] WARNING: Assistant render confirmation not found: {e}")

if __name__ == "__main__":
    driver = SessionDriver(headless=False)
    driver.start_session()
    driver.wait_for_any_code_render()
    input_field = driver.get_mapper().get("prompt_box")  # ← updated
    print("[SessionDriver] Prompt input field found:", input_field)
    html = driver.get_current_html()
    print(html[:2000])  # Preview
    driver.close_session()
