# === FILE: tests/test_session_driver.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: tests/test_session_driver.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

This module performs integrated unit tests across the browser interface pipeline:
- SessionDriver
- HTMLParser
- ElementMapper

It assumes access to a live browser environment. Use `headless=True` to enable testing
in CI pipelines or when visual inspection is not required.

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

SessionDriver Integration Test

This suite verifies the live behavior of browser sessions, HTML extraction, DOM parsing,
and semantic element mapping. It ensures stability across expected interface structures.
"""
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.web.session_driver import SessionDriver

class TestSessionDriverIntegration(unittest.TestCase):
    def setUp(self):
        self.driver = SessionDriver(headless=True)
        self.driver.start_session()
        self.parser = self.driver.get_parser()
        self.mapper = self.driver.get_mapper()

    def test_html_capture(self):
        html = self.driver.get_current_html()
        self.assertTrue(html)
        self.assertIn("<html", html.lower())
        print(f"[Test] Captured HTML length: {len(html)}")

    def test_parser_extraction(self):
        prompt_box = self.parser.find_text_input_area()
        message_bubbles = self.parser.list_message_bubbles()

        print(f"[Test] Prompt box found: {'Yes' if prompt_box else 'No'}")
        print(f"[Test] Message bubbles found: {len(message_bubbles)}")

        self.assertIsNotNone(prompt_box)
        self.assertIsInstance(message_bubbles, list)

    def test_element_mapping(self):
        prompt_box = self.mapper.get("prompt_box")
        send_button = self.mapper.get("send_button")
        bubbles = self.mapper.get("message_bubbles")

        print(f"[Test] Mapped prompt_box: {'Yes' if prompt_box else 'No'}")
        print(f"[Test] Mapped send_button: {'Yes' if send_button else 'No'}")
        print(f"[Test] Mapped message_bubbles: {len(bubbles) if bubbles else 0}")

        self.assertIn("prompt_box", self.mapper.map)
        self.assertIn("send_button", self.mapper.map)
        self.assertIsNotNone(prompt_box)

    def tearDown(self):
        self.driver.close_session()

if __name__ == "__main__":
    unittest.main()
