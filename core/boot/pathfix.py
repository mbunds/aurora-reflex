# === FILE NAME: core/boot/pathfix.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/boot/pathfix.py
Authors: ChatGPT and Mark
Created: 2025-04-17
Location: Evans, Colorado
Project: Aurora

This utility module provides a centralized method to patch the Python sys.path
during local development. It ensures consistent import resolution from any
submodule within the Aurora project when executed in non-package mode.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T02_INITIAL_PROCESSING.txt
    - Category: Bootstrap Utility
    - Used by all modules requiring guaranteed path stability across contexts.

---

Path Bootstrap Utility

Call patch_path() at the top of any deep module to ensure that the root
project path is visible to Python, enabling absolute imports of all
core.* modules and subpackages.
"""

import sys
import os

def patch_path():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if root not in sys.path:
        sys.path.insert(0, root)
        print(f"[PATHFIX] Root path added: {root}")
    #else:
        #print("[PATHFIX] Root path already present.")
