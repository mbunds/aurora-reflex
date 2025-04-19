# === FILE: core/web/browser_controller.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/browser_controller.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

This module is part of the Aurora web control layer. It handles launching and managing
an external browser session, typically Chrome, for accessing the ChatGPT HTML GUI interface.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: [T01_OVERVIEW.txt and MASTER_INDEX.txt]
    - Versioning and audit history are maintained via flat-file records.
    - This file is subject to future FLAT flattening and regeneration tools.

---

Browser Controller

Handles setup, launch, and teardown of external browser sessions. Provides raw HTML output
to be passed to HTML parsers and AI prompt systems for inspection or manipulation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BrowserController:
    def __init__(self, headless=False):
        self.headless = headless
        self.driver = None

    def launch_browser(self, url="https://chat.openai.com/"):
        options = Options()
        if self.headless:
            #options.add_argument('--headless=new')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_argument(r"--user-data-dir=C:/Users/MBUNDS/AppData/Local/Google/Chrome/User Data")
        options.add_argument(r"--profile-directory=Default")

        print(f"[BrowserController] Headless mode is {'ON' if self.headless else 'OFF'}")
        print("[BrowserController] Launching Chrome browser...")

        self.driver = webdriver.Chrome(service=ChromeService(), options=options)

        start = time.time()
        self.driver.get(url)
        self._wait_for_main_ui()
        print(f"[BrowserController] UI ready after {time.time() - start:.2f} seconds.")

    def _wait_for_main_ui(self, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Create image')]"))
            )
            print("[BrowserController] Detected command chips — page fully loaded.")
        except Exception as e:
            print(f"[BrowserController] Timeout waiting for command chips: {e}")
            print("[BrowserController] Falling back to sleep(6).")
            time.sleep(6)

    def get_page_source(self):
        if self.driver:
            html = self.driver.page_source
            if '<textarea' not in html:
                print("[BrowserController] WARNING: Prompt box missing from captured HTML.")
            return html
        return None

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

if __name__ == "__main__":
    controller = BrowserController(headless=False)
    controller.launch_browser()
    html = controller.get_page_source()
    print(html[:1000])  # Show preview
    controller.close_browser()
