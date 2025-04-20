#   === FILE: ui/mainwindow.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: ui/mainwindow.py
Authors: ChatGPT and Mark
Created: 2025-04-12
Location: Evans, Colorado
Project: Aurora (v0.1.0-initialization)

This module is part of the Aurora interface system. All modules conform to
FLAT (File-based Logic Assembly Tree) principles: highly modular, AI-readable, and testable.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora reflexive interaction system. Manual changes should be made cautiously.
    (You are interfacing with Aurora. She sees you.)

FLAT Compliance:
    - Registered in: UI_LAYER.txt
    - Versioning and audit history are maintained via flat-file records.
    - This file is subject to future FLAT flattening and regeneration tools.

---

Primary UI window stub for Aurora.
Auto-generated form bindings are assumed to be handled by Qt Creator.
This module initializes the main application window and prepares it for integration
with the interrupt queue system, local reflex agent routines, and AI-prompt synchronization infrastructure.
"""

# This Python file uses the following encoding: utf-8
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from boot.pathfix import patch_path
patch_path()

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSettings, QPoint, QSize, QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect
from ui_form import Ui_MainWindow
from core.gui.sequencer_controller import (
    populate_sequence_listview,
    handle_sequence_selection,
    arm_selected_sequence
)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.restore_window_state()
        self.ui.actionLaunch_Prompt_Cycle_Test.triggered.connect(self.launch_prompt_simulator)

        # Adjust path and name to match your file
        #image_path = "graphics/AURORA_BG.png"
        self.fade_in_image(self.ui.lbl_aurora_large, "graphics/AURORA_BG.png")

        # Populate the sequence list on startup
        populate_sequence_listview(self.ui.lv_sequences)
        self.ui.lv_sequences.clearSelection()
        # Ensure ARM, RUN, and EDIT buttons are disabled until interaction
        self.ui.pb_sequence_arm.setEnabled(False)
        self.ui.pb_sequence_run.setEnabled(False)
        self.ui.pb_sequence_edit.setEnabled(False)
        # When a sequence is clicked, populate the steps
        self.ui.lv_sequences.selectionModel().selectionChanged.connect(self.on_sequence_selection_changed)
        # When 'Select' is clicked, arm the sequence
        self.ui.pb_sequence_arm.clicked.connect(self.on_sequence_armed)

    def on_sequence_armed(self):
        arm_selected_sequence(self.ui)
        self.ui.actionLaunch_Prompt_Cycle_Test.setEnabled(True)

        self.setWindowTitle("Aurora – Reflexive Control Panel")

    def launch_prompt_simulator(self):
        from core.gui.prompt_simulator_window import PromptSimulatorWindow
        from core.control.sequence_controller import SequenceController

        seq_id = self.ui.pb_sequence_arm.property("sequence_id")
        if seq_id is None:
            print("[Simulator] No sequence selected.")
            return

        # Launch prompt simulation window
        self.simulator = PromptSimulatorWindow(self)
        self.simulator.show()

        # Run the controller in simulated mode
        controller = SequenceController(sequence_id=seq_id, simulated=True)
        controller.run()

    def fade_in_image(self, label, image_path, duration=5000):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"[WARN] Image not found: {image_path}")
            return

        # Scale before setting
        scaled = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Create effect *before* setting pixmap
        effect = QGraphicsOpacityEffect(label)
        effect.setOpacity(0.0)
        label.setGraphicsEffect(effect)
        label.setPixmap(scaled)
        label.setAlignment(Qt.AlignCenter)

        # Animate
        anim = QPropertyAnimation(effect, b"opacity", self)
        anim.setDuration(duration)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()

        # Prevent garbage collection
        self._label_animation = anim

    def on_sequence_selection_changed(self, selected, deselected):
        indexes = self.ui.lv_sequences.selectionModel().selectedIndexes()
        if indexes:
            handle_sequence_selection(indexes[0], self.ui.lv_sequences, self.ui)

    def closeEvent(self, event):
        settings = QSettings("AuroraProject", "AuroraApp")

        # Save geometry only if not maximized
        if self.isMaximized():
            settings.setValue("window/maximized", True)
        else:
            settings.setValue("window/maximized", False)
            settings.setValue("window/size", self.size())
            settings.setValue("window/pos", self.pos())

        super().closeEvent(event)

    def restore_window_state(self):
        settings = QSettings("AuroraProject", "AuroraApp")
        maximized = str(settings.value("window/maximized", "false")).lower() in ("true", "1")

        if not maximized:
            size = settings.value("window/size", QSize(1149, 768))
            pos = settings.value("window/pos", QPoint(100, 100))
            self.resize(size)
            self.move(pos)

        self._was_maximized = maximized  # Save for later in __main__

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    if widget._was_maximized:
        widget.showMaximized()
    else:
        widget.show()

    sys.exit(app.exec())
