# === FILE NAME: core/api/__init__.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/api/__init__.py
Authors: ChatGPT and Mark
Created: 2025-04-23
Location: Evans, Colorado
Project: Aurora

This module provides a unified entry point for operating system API access
commands. Platform-specific API modules are dynamically selected at runtime
based on system detection and routed to the appropriate implementation in
core.api.win or core.api.lnx. API commands define the operational backbone
of Aurora’s external execution layer.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of the
    Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: TEMPLATES.txt
    - Category: OS API Integration Root
    - Delegates to: core/api/win/, core/api/lnx/
"""

import platform

if platform.system().lower().startswith("win"):
    from .win import *  # Windows-specific API commands
else:
    from .lnx import *  # Linux-specific API commands
