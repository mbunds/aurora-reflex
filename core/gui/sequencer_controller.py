# === FILE NAME: core/gui/sequencer_controller.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/gui/sequencer_controller.py
Authors: ChatGPT and Mark
Created: 2025-04-17
Location: Evans, Colorado
Project: Aurora

This module manages the GUI control layer for the Sequence Runner subsystem.
It bridges database-loaded sequence definitions with user-facing list views,
and manages enabling logic for RUN/EDIT operations based on selection state.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: T02_INITIAL_PROCESSING.txt
    - Category: GUI Controller
    - Interfaces with: ui_form.py, db_interface.py
    - Exposes callable functions for list model population and user interaction
"""

# === PATH PATCH (MANDATORY BEFORE BOOT IMPORTS) ===
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from core.boot.pathfix import patch_path
patch_path()
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import sqlite3
from data.db_interface import load_sequence_steps, DB_PATH
#print("[DEBUG] sys.path =", sys.path)
#print("[DEBUG] Attempting to open DB_PATH:", DB_PATH)

def load_sequences_from_db():
    """Fetch all sequences from the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, name, description, sequence_type FROM sequences")
    results = cur.fetchall()
    conn.close()
    return results

def populate_sequence_listview(view):
    """Populate a QListView with available sequences."""
    sequence_data = load_sequences_from_db()
    model = QStandardItemModel()

    for seq in sequence_data:
        label = f"{seq['name']} | {seq['description']} [{seq['sequence_type']}]"
        item = QStandardItem(label)
        item.setData(seq['id'], Qt.UserRole)
        model.appendRow(item)

    view.setModel(model)
    return model

def populate_steps_for_sequence(step_data, view):
    """Populate a QListView with steps (pre-fetched)."""
    model = QStandardItemModel()

    for step in step_data:
        label = f"{step['step_order']:02d} – {step['instruction']}"
        item = QStandardItem(label)
        model.appendRow(item)

    view.setModel(model)
    return model

def handle_sequence_selection(index, view, ui):
    """Called when a sequence is selected. Loads steps and updates buttons."""
    model = view.model()
    item = model.itemFromIndex(index)
    sequence_id = item.data(Qt.UserRole)

    # Load steps directly
    step_data = load_sequence_steps(sequence_id)

    # Populate the view with them
    populate_steps_for_sequence(step_data, ui.lv_steps)

    # Enable ARM button
    ui.pb_sequence_arm.setEnabled(True)

    # Disable RUN and EDIT initially
    ui.pb_sequence_run.setEnabled(False)

    # EDIT should only be enabled if steps are present *and* RUN is enabled later
    ui.pb_sequence_edit.setEnabled(True if step_data and ui.pb_sequence_run.setEnabled == True else False)

    # Store metadata on the button
    ui.pb_sequence_arm.setProperty("sequence_id", sequence_id)
    ui.pb_sequence_arm.setProperty("has_steps", bool(step_data))

def arm_selected_sequence(ui):
    """Handles the arming logic when 'Select' is clicked."""
    seq_id = ui.pb_sequence_arm.property("sequence_id")
    has_steps = ui.pb_sequence_arm.property("has_steps")
    if seq_id is not None:
        ui.pb_sequence_run.setEnabled(True if has_steps else False)
        ui.pb_sequence_edit.setEnabled(True)
