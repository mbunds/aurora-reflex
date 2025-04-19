# === FILE: core/utils/code_formatter.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/utils/code_formatter.py
Authors: ChatGPT and Mark
Created: 2025-04-15
Location: Evans, Colorado
Project: Aurora

This module post-processes restored code blocks to enforce stylistic consistency
and aesthetic alignment with standard Python formatting. Designed to follow
code_restorer.py and finalize cleaned output for user or storage.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - To be registered in: [T02_INITIAL_PROCESSING.txt]
    - This file participates in branch T02-B02_CODE_CAPTURE_CLEAN

---

Code Formatter Utility

Final pass beautifier that makes restored code style-compliant.
"""

import textwrap
import re

def beautify_code(source_code: str) -> str:
    """
    Apply whitespace normalization, import line splitting,
    and paragraph indentation consistency to restored Python code.

    Args:
        source_code (str): The restored Python code block.

    Returns:
        str: A polished, readable, consistent Python source block.
    """
    lines = source_code.splitlines()
    formatted = []

    for line in lines:
        line = line.rstrip()

        # Normalize import line spacing
        if re.match(r'^import [a-zA-Z0-9_, ]+$', line):
            for imp in line.split(','):
                formatted.append(imp.strip())
            continue

        # Normalize excessive spacing
        line = re.sub(r' +', ' ', line)
        line = re.sub(r' :', ':', line)

        formatted.append(line)

    # Normalize paragraph indentation
    block = "\n".join(formatted)
    block = textwrap.dedent(block)

    return block.strip() + "\n"

if __name__ == '__main__':
    sample = """
import os, sys, yaml

class Demo:  def say_hi(self):   print("Hi")
    """
    print("\n--- Beautified Output ---\n")
    print(beautify_code(sample))
