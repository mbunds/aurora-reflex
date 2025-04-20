# === FILE NAME: core/gui/prompt_simulator_window.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/gui/prompt_simulator_window.py
Authors: ChatGPT and Mark
Created: 2025-04-20
Location: Evans, Colorado
Project: Aurora

This module implements the Prompt Cycle Simulation Utility. It replaces live browser
interaction with a GUI mock environment for testing step-based prompt sequences without
launching ChatGPT or consuming tokens. Prompts intended for the browser are intercepted,
and a manual response may be entered to simulate GPT output.

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

Prompt Simulation Utility

Displays prompts that would be issued by the reflex dispatcher,
allows user to supply simulated responses, and provides UI feedback
for step flow and interaction without launching a browser.
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QListWidget, QTextEdit, QLineEdit, QPushButton
)

from PySide6.QtCore import QThread, QObject, Signal, Slot

from core.control import simulated_dispatcher

class PromptSimulatorWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Aurora – Prompt Cycle Simulator")
        self.setMinimumSize(700, 500)

        self.layout = QVBoxLayout(self)

        # --- Prompt Preview ---
        self.prompt_label = QLabel("Injected Prompt (Simulated):")
        self.prompt_display = QTextEdit()
        self.prompt_display.setReadOnly(True)

        # --- Begin Sequence Button ---
        self.run_button = QPushButton("Run Sequence")
        self.run_button.clicked.connect(self.begin_sequence)
        self.layout.addWidget(self.run_button)

        # --- Simulated GPT Response ---
        self.reply_label = QLabel("Enter Simulated GPT Response:")
        self.reply_input = QLineEdit()
        self.send_button = QPushButton("Send Response")
        self.send_button.clicked.connect(self.send_response)

        # --- Step History and Response Log ---
        self.step_log = QListWidget()
        self.step_log.setFixedHeight(120)
        self.step_log_label = QLabel("Sequence Step Log:")

        self.reply_log = QListWidget()
        self.reply_log.setFixedHeight(120)
        self.reply_log_label = QLabel("Simulated Response Log:")

        # --- Layout Assembly ---
        self.layout.addWidget(self.prompt_label)
        self.layout.addWidget(self.prompt_display)
        self.layout.addWidget(self.reply_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.reply_input)
        hbox.addWidget(self.send_button)
        self.layout.addLayout(hbox)

        self.layout.addWidget(self.step_log_label)
        self.layout.addWidget(self.step_log)

        self.layout.addWidget(self.reply_log_label)
        self.layout.addWidget(self.reply_log)

        from core.control.simulated_dispatcher import inject_simulator
        inject_simulator(self)

    def inject_prompt(self, prompt_text: str):
        self.prompt_display.setPlainText(prompt_text)
        self.step_log.addItem(f"[Injected] {prompt_text[:80]}")

    def send_response(self):
        response = self.reply_input.text().strip()
        if response:
            self.reply_log.addItem(f"[User] {response}")
            self.reply_input.clear()
            self.prompt_display.clear()
            simulated_dispatcher.response_queue.put(response)

    def begin_sequence(self):
        try:
            seq_id = self.parent().ui.pb_sequence_arm.property("sequence_id")
        except AttributeError:
            print("[PromptSimulatorWindow] Could not access sequence ID.")
            return

        if seq_id is None:
            print("[PromptSimulatorWindow] No sequence ID armed.")
            return

        self.thread = QThread()
        self.runner = SequenceRunner(seq_id)
        self.runner.moveToThread(self.thread)
        self.thread.started.connect(self.runner.run)
        self.runner.finished.connect(self.thread.quit)
        self.runner.finished.connect(self.runner.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        print(f"[PromptSimulatorWindow] Running sequence {seq_id} in background thread.")
        self.thread.start()

class SequenceRunner(QObject):
    finished = Signal()

    def __init__(self, sequence_id):
        super().__init__()
        self.sequence_id = sequence_id

    @Slot()
    def run(self):
        import threading
        print(f"[DEBUG] Running in thread: {threading.current_thread().name}")
        from core.control.sequence_controller import SequenceController
        controller = SequenceController(sequence_id=self.sequence_id, simulated=True)
        controller.run()
        self.finished.emit()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = PromptSimulatorWindow()
    window.show()
    simulated_dispatcher.inject_simulator(window)
    sys.exit(app.exec())
