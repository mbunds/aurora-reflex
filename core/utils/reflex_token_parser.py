# === FILE NAME: core/utils/reflex_token_parser.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/utils/reflex_token_parser.py
Authors: ChatGPT and Mark
Created: 2025-04-23
Location: Evans, Colorado
Project: Aurora

This module implements a parser for reflex-style tokens that adhere to the format
/TOKEN/ or /TOKEN: ARGUMENT/ as used by Aurora's reflex protocol. It extracts any tokens
found within a GPT response and returns a structured dictionary including the final
token (which acts as a step finalizer), all tokens encountered, any accompanying arguments,
and the original response text. This functionality is essential for determining if a response
meets the expected completion criteria and for capturing metadata for downstream processing.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of the
    Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: TEMPLATES.txt
    - Conforms to Aurora’s reflex token protocol design.
"""

import re

def parse_reflex_tokens_with_args(response_text, expected=None):
    """
    Parses reflex-style tokens of the format /TOKEN/ or /TOKEN: ARGUMENT/ from response text.

    Args:
        response_text (str): The full GPT response or any string Aurora should parse.
        expected (str, optional): If provided, the parser will check if the final token matches this.

    Returns:
        dict: {
            "matched": bool,           # Whether the final token matched expected.
            "finalizer": str or None,  # The last token found.
            "all_tokens": list of str, # All /TOKEN/ strings found.
            "arguments": dict,         # Mapping of each token to its ARGUMENT (or None if not present).
            "raw": str,                # The original response text.
            "reason": str,             # Explanation if no tokens were found.
        }
    """
    pattern = r"/([A-Z_]+)(?::([^/]+))?/"
    matches = re.findall(pattern, response_text)

    if not matches:
        return {
            "matched": False,
            "finalizer": None,
            "all_tokens": [],
            "arguments": {},
            "raw": response_text,
            "reason": "No tokens found"
        }

    tokens = [f"/{token}/" for token, _ in matches]
    final_token = tokens[-1]
    matched = final_token == expected if expected else True

    return {
        "matched": matched,
        "finalizer": final_token,
        "all_tokens": tokens,
        "arguments": {f"/{token}/": arg.strip() if arg else None for token, arg in matches},
        "raw": response_text
    }
