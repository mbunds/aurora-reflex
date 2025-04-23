# === FILE NAME: core/api/lnx/__init__.py ===

"""
Aurora – Linux API Command Layer
----------------------------------

Module: core/api/lnx/__init__.py
Authors: ChatGPT and Mark
Created: 2025-04-23
Location: Evans, Colorado
Project: Aurora

This module defines platform-specific API commands for Linux systems.
It is loaded dynamically at runtime by core.api.__init__.py based on host OS.
Linux-specific functions for file handling, application launching,
or system diagnostics should be implemented here.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    Manual edits should be made carefully unless under controlled development branches.

FLAT Compliance:
    - Registered in: T03_SEQUENCING.txt
    - Category: API - Linux Platform

DEV NOTES (Linux Edition):

When parsing a structured GPT response like:

    /LAUNCH APP: gedit/
    /OPEN FOLDER: /home/mark/projects/
    /CODE COMPLETE/

...your reflex dispatcher might extract:

    if token == "/LAUNCH APP/":
        result = launch_app(arg)  # Launches the application using subprocess.Popen([arg])

    elif token == "/OPEN FOLDER/":
        result = open_folder(arg)  # Opens the path using xdg-open

Linux-specific handlers are defined in:
    core/api/lnx/__init__.py

Each command must be:

Parsed with arguments (arg)
Executed using Linux-safe subprocess handling

- Logged or returned with a reflex-compatible status string
- Tokens and argument mapping are typically obtained from:
- parse_reflex_tokens_with_args(response_text)
- or higher-level command blocks parsed from structured response sequences

Ensure xdg-open and direct subprocess.Popen() calls are safe and properly backgrounded, particularly in environments without GUI context (e.g., SSH-only servers).
"""

def open_file(path):
    raise NotImplementedError("Windows API handler not yet implemented.")

import subprocess
import os

def launch_app(path):
    """Launches an application on Linux."""
    try:
        subprocess.Popen([path])
        return f"Application launched: {path}"
    except Exception as e:
        return f"ERROR: Failed to launch app – {e}"

def open_folder(path):
    """Opens a folder using the default Linux file manager."""
    try:
        subprocess.Popen(["xdg-open", path])
        return f"Folder opened: {path}"
    except Exception as e:
        return f"ERROR: Failed to open folder – {e}"
