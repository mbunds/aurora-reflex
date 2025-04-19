# === FILE: core/web/code_sanitizer.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/web/code_sanitizer.py
Authors: ChatGPT and Mark
Created: 2025-04-15
Location: Evans, Colorado
Project: Aurora

This module bridges extracted flattened code blobs from GUI DOM
captures (Monaco or <pre><code>) to restored, human-readable format
by delegating logic to `code_restorer.py`.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Will be registered in: [T02_INITIAL_PROCESSING.txt]
    - This file participates in branch T02-B02_CODE_CAPTURE_CLEAN
    - Versioning and audit history are maintained via flat-file records.

---

Code Sanitizer Wrapper

Converts stripped Python code captured from GUI output into formatted, indented source.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from core.utils.code_restorer import restore_code_structure
from core.utils.code_formatter import beautify_code

def sanitize_flattened_code(raw_blob: str) -> str:
    """
    Sanitize flattened Python code (typically from ChatGPT GUI DOM capture).

    Args:
        raw_blob (str): Flattened code string (often a stitched Monaco block)

    Returns:
        str: Restored, human-readable, and style-consistent Python code
    """
    print("[Sanitizer] Starting code restoration...")
    restored = restore_code_structure(raw_blob)
    print("[Sanitizer] Running final beautification...")
    beautified = beautify_code(restored)
    print("[Sanitizer] Formatting complete.")
    return beautified

if __name__ == '__main__':
    print("[Sanitizer] Demo mode activated. Using embedded example.")
    flattened = """
#!/usr/bin/env python3importyamlimportargparseimportosimportsysclassDemo:def__init__(self):self.x=5defrun(self):print("Hello")if__name__=='__main__':Demo().run()
"""
    print("\n--- Sanitized Code ---\n")
    print(sanitize_flattened_code(flattened))

