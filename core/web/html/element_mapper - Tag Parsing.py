# === FILE: core/web/html/element_mapper.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/html/element_mapper.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

This module maps extracted HTML elements (via BeautifulSoup) to standardized
internal identifiers used across the Aurora automation system. This mapping
enables consistent logic, regardless of changing DOM structures.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T01_OVERVIEW.txt
    - This file participates in the T01-B01_HTML_CONNECT branch.
    - Subject to structural flattening for AI inspection.

---

Element Mapper

Takes parsed DOM elements and assigns canonical names or functional tags.
Supports DOM stabilization across changing frontend versions.
"""

class ElementMapper:
    def __init__(self):
        self.map = {}

    def register(self, label: str, dom_element):
        """Register a DOM node under a canonical label."""
        self.map[label] = dom_element

    def get(self, label: str):
        """Retrieve a registered DOM node by label."""
        return self.map.get(label, None)

    def auto_map_from_parser(self, parser):
        """Naively extract and register common UI elements."""
        self.register("prompt_box", parser.find_text_input_area())
        self.register("send_button", parser.find_send_button())
        self.register("message_bubbles", parser.list_message_bubbles())
        print(f"[ElementMapper] Registered elements: {list(self.map.keys())}")
