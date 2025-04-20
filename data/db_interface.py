# === FILE NAME: core/data/db_interface.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/data/db_interface.py
Authors: ChatGPT and Mark
Created: 2025-04-16
Location: Evans, Colorado
Project: Aurora

This module interfaces with Aurora’s sqlite3 database (aurora.db) to load
sequence definitions and step instructions from the `sequences` and
`sequence_steps` tables. It provides runtime access for step execution logic.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T02_INITIAL_PROCESSING.txt
    - This file participates in the T02-B04_SEQ_CONT branch of development.
    - All session behaviors are tracked and logged through flat file modules.

---

Database Interface

Exposes methods for loading sequences, steps, and metadata for use in
reflex-driven execution controllers.
"""

import sqlite3
from typing import List, Dict

#DB_PATH = r"C:\Users\MBUNDS\Documents\QtDesignStudio\AURORA\data\aurora.db"
import os
DB_PATH = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'aurora.db')))
DB_PATH = os.path.normpath(DB_PATH)
print("[DEBUG] DB_PATH resolved to:", DB_PATH)

def get_sequence_id_by_name(name: str) -> int:
    """
    Look up the ID of a sequence by its name from the 'sequences' table.

    Args:
        name (str): The human-readable name of the sequence.

    Returns:
        int: The ID of the sequence, or None if not found.
    """
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id FROM sequences WHERE name = ?", (name,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def load_sequence_steps(sequence_id: int) -> List[Dict]:
    """
    Load all steps for a given sequence from the database.

    Args:  sequence_id (int): The ID of the sequence to load.

    Returns: List[Dict]: Ordered list of step dictionaries.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    query = """
    SELECT id, sequence_id, step_order, instruction, expected, reflex_action, repeat, jump, jmp_rpt
    FROM sequence_steps
    WHERE sequence_id = ?
    ORDER BY step_order ASC
    """
    cur.execute(query, (sequence_id,))
    rows = cur.fetchall()
    conn.close()

    steps = []
    for row in rows:
        steps.append({
            "id": row["id"],
            "sequence_id": row["sequence_id"],
            "step_order": row["step_order"],
            "instruction": row["instruction"],
            "expected": row["expected"],
            "reflex_action": row["reflex_action"],
            "repeat": row["repeat"],
            "jump": row["jump"],
            "jmp_rpt": row["jmp_rpt"],
        })

    print(f"[DB] Loaded {len(steps)} steps for sequence {sequence_id}")
    return steps

def resolve_key_phrase(key_id: int) -> str:
    """
    Lookup a key phrase by its ID from the 'keys' table.
    Args: key_id (int): The key ID to resolve.
    Returns: str: The associated phrase from the keys table, or '(UNRESOLVED)' if not found.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    query = "SELECT id, type, direction, is_phrase, long_phrase FROM keys WHERE id = ?"
    cur.execute(query, (key_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return "(UNRESOLVED)"

    # Resolve phrase: use long_phrase if is_phrase is True, else use id (or future lookup strategy)
    if row[3]:  # is_phrase
        long_id = row[4]
        return resolve_long_phrase(long_id)  # Delegated to next helper
    else:
        return str(row[0])  # fallback to raw ID string or future mapping

def resolve_long_phrase(long_phrase_id: int) -> str:
    """
    Lookup a long phrase string by its ID from the 'long_phrases' table.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    query = "SELECT phrase FROM long_phrases WHERE id = ?"
    cur.execute(query, (long_phrase_id,))
    row = cur.fetchone()
    conn.close()

    return row[0] if row else "(UNRESOLVED-LONG)"

# === FUNCTION: resolve_reflex_action ===
def resolve_reflex_action(reflex_id: int) -> str:
    """
    Look up a reflex_action ID in the 'keys' table and return the associated key string.
    """
    import sqlite3
    from data.db_interface import DB_PATH

    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT key FROM keys WHERE id = ?", (reflex_id,))
        row = cur.fetchone()
        return row[0] if row else ""
    finally:
        conn.close()

if __name__ == "__main__":
    name = "SHOW MODE"
    seq_id = get_sequence_id_by_name(name)
    if seq_id is None:
        print(f"[db_interface] Sequence '{name}' not found.")
    else:
        steps = load_sequence_steps(seq_id)
        for i, step in enumerate(steps):
            print(f"Step {i} (order {step['step_order']}): {step['instruction']}")
