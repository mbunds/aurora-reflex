# === FILE: core/web/html/html_parser.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/html/html_parser.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora

HTML parser module responsible for transforming raw DOM content into a usable structure
for element mapping, command recognition, and reflex dispatch.

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
        # Initialize the BeautifulSoup DOM parser with the raw HTML
        self.soup = BeautifulSoup(raw_html, 'lxml')

    def find_text_input_area(self):
        """Locate the main user prompt text input area (usually <textarea> or equivalent)."""
        return self.soup.find('textarea')  # Simple selector; may evolve with UI updates

    def find_send_button(self):
        """Find the visible 'send' button, if present in the DOM."""
        return self.soup.find('button', string=lambda x: x and 'send' in x.lower())

    def list_message_bubbles(self):
        """
        Extract all <p> elements from the chat region.
        These typically contain assistant/user response text within Markdown regions.
        """
        return self.soup.select('div.markdown.prose p')

    def list_code_blocks(self):
        """
        Extract all <pre><code> blocks.
        Used for structured assistant responses like generated scripts or CLI output.
        """
        return self.soup.select('div.markdown.prose pre code')

    def list_monaco_code_lines(self):
        """
        Fallback: If the ChatGPT interface uses Monaco (e.g. when editing),
        this captures each code line separately to allow reconstruction.
        """
        return self.soup.select('div.cm-line')

    def debug_dump(self):
        """Print a partial, formatted snapshot of the DOM — useful for testing or tracing."""
        print(self.soup.prettify()[:1500])  # Trim output to avoid clutter