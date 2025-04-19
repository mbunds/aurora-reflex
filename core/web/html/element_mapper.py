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

from selenium.webdriver.remote.webelement import WebElement
from typing import List, Callable, Dict


def extract_code_blocks_by_innertext(elements: List[WebElement]) -> List[str]:
    """
    Takes a list of <pre><code> elements and extracts the visible code using innerText.
    """
    code_blocks = []
    for element in elements:
        try:
            text = element.get_attribute('innerText') or ''
            if text.strip():
                code_blocks.append(text.strip())
        except Exception as e:
            print(f"[ElementMapper] Warning: Failed to extract innerText: {e}")
    return code_blocks


class ElementMapper:
    """
    Centralized DOM element parser registry.
    Maps canonical route tags to element extraction functions.
    """

    def __init__(self):
        self.registry: Dict[str, Callable[[List[WebElement]], List[str]]] = {}
        self._register_defaults()

    def _register_defaults(self):
        self.register("innertext_code_blocks", extract_code_blocks_by_innertext)

    def register(self, key: str, func: Callable[[List[WebElement]], List[str]]):
        if key in self.registry:
            print(f"[ElementMapper] Warning: Overwriting parser for key: {key}")
        self.registry[key] = func

    def extract(self, key: str, elements: List[WebElement]) -> List[str]:
        if key not in self.registry:
            raise KeyError(f"[ElementMapper] No parser registered under key: {key}")
        return self.registry[key](elements)
