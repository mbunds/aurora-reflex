# === FILE: core/web/html/html_parser.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/html/html_parser.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

This module parses raw HTML content retrieved from a browser session
and converts it into a structure usable by internal mapping and AI systems.

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
    - Future versions may include interactive AI feedback loops.

---

HTML Parser

This parser ingests raw HTML (from Selenium or other sources), uses BeautifulSoup to
extract element trees or UI regions of interest (prompt box, message history, buttons),
and exposes data for use in element mapping and command routing.
"""

from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, raw_html: str):
        self.soup = BeautifulSoup(raw_html, 'lxml')

    def find_text_input_area(self):
        """Attempt to locate the user prompt input field."""
        return self.soup.find('textarea')  # Naive placeholder

    def find_send_button(self):
        """Attempt to locate the 'send' button."""
        return self.soup.find('button', string=lambda x: x and 'send' in x.lower())

    def list_message_bubbles(self):
        """Return a list of actual message text <p> elements inside chat."""
        return self.soup.select('div.markdown.prose p')

    def list_code_blocks(self):
        """Return all <pre><code> text blocks."""
        return self.soup.select('div.markdown.prose pre code')

    def list_monaco_code_lines(self):
        """Return all individual lines of code from Monaco-style editor blocks."""
        return self.soup.select('div.cm-line')

    def debug_dump(self):
        """Print formatted tree snippet (for diagnostics)."""
        print(self.soup.prettify()[:1500])  # Limit preview

    def list_innertext_code_blocks(self):
        return self.soup.select('code.whitespace-pre')
