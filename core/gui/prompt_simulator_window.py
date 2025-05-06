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
    - Registered in: T03_SEQUENCING.txt
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

from PySide6.QtCore import QThread, QObject, Signal, Slot, Qt, QMetaObject

from core.control import simulated_dispatcher

class PromptSimulatorWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Aurora – Prompt Cycle Simulator")
        self.setMinimumSize(700, 500)

        self.layout = QVBoxLayout(self)

        # --- Begin Sequence Button ---
        self.run_button = QPushButton("Run Sequence") # ******************************** "Run sequence" button
        self.run_button.clicked.connect(self.begin_sequence)
        self.layout.addWidget(self.run_button)

        # --- Prompt Preview ---
        self.prompt_label = QLabel("Injected Prompt (Simulated):") # ******************* Injected Prompt (Simulated) listbox
        self.prompt_display = QTextEdit()
        self.prompt_display.setReadOnly(True)

        # --- Simulated GPT Response ---
        self.reply_label = QLabel("Enter Simulated GPT Response:") # ******************* User entry box
        self.reply_input = QLineEdit()
        self.send_button = QPushButton("Send Response") # ****************************** "Send Response" button
        self.send_button.clicked.connect(self.send_response)

        # --- Step History and Response Log ---
        self.step_log = QListWidget()
        self.step_log.setFixedHeight(120)
        self.step_log_label = QLabel("Sequence Step Log:") # ************************** Sequencer Step Log listbox

        self.reply_log = QListWidget()
        self.reply_log.setFixedHeight(120)
        self.reply_log_label = QLabel("Simulated Response Log:") # ******************** Sequencer Response Log listbox

        self.status_label = QLabel("Status: Idle") # ********************************** Sequencer status label
        self.layout.addWidget(self.status_label)

        # --- Layout Assembly ---
        self.layout.addWidget(self.prompt_label) #    Injected Prompt label
        self.layout.addWidget(self.prompt_display) #  Injected Prompt text edit box
        self.layout.addWidget(self.reply_label) #     User entry box label

        hbox = QHBoxLayout()
        hbox.addWidget(self.reply_input) #            User entry box
        hbox.addWidget(self.send_button) #            User entry box send button
        self.layout.addLayout(hbox) #                 Horizonal container

        self.layout.addWidget(self.step_log_label) #  Step Log label
        self.layout.addWidget(self.step_log) #        Step Log listbox

        self.layout.addWidget(self.reply_log_label) # Response Log box label
        self.layout.addWidget(self.reply_log) #       Respons Log listbox

        from core.control.simulated_dispatcher import inject_simulator # Call function inject_simulator
        inject_simulator(self)

    @Slot(str)
    def update_injected_prompt(self, prompt_text: str): # *********************** DISPLAYS SIMULATED GPT RESPONSE BLOCKS IN "prompt_display"
        self.prompt_display.setPlainText(prompt_text)
        #self.step_log.addItem(f"[Injected] {prompt_text[:80]}")
        print(f"[Prompt Injected Display Updated] {prompt_text[:80]}")

    @Slot(str)
    def update_step_log(self, prompt_text: str): # *********************** DISPLAYS STEPS IN "step_log"
        self.step_log.addItem(f"[Injected] {prompt_text[:80]}")
        print(f"[PromptSimulatorWindow Injected] {prompt_text[:80]}")

    @Slot(str)
    def update_response_log(self, prompt_text: str): # *********************** DISPLAYS USER RESPONSES IN "reply_log"
        self.reply_log.addItem(f"[Injected] {prompt_text[:80]}")
        print(f"[PromptSimulatorWindow Injected] {prompt_text[:80]}")

    def send_response(self): # ***************************************** DISPLAYS USER RESPONSE FROM "reply_input"
        response = self.reply_input.text().strip()
        if response:
            #self.reply_log.addItem(f"[User] {response}") # ################################ REPLY LOG ##############################
            print(f"[PromptSimulatorWindow Added User Response:] {response}")
            self.reply_input.clear()
            #self.prompt_display.clear()
            simulated_dispatcher.response_queue.put(response) # ########################## DISPATCHER RESPONSE_QUEUE CRITICAL - USED IN DISPATCHERS ##############

    def begin_sequence(self):
        self.status_label.setText("Status: Running...")
        try:
            seq_id = self.parent().ui.pb_sequence_arm.property("sequence_id") # ******************** Grab sequence id from the arm button, assign to "seq_id"
        except AttributeError:
            print("[PromptSimulatorWindow] Could not access sequence ID.") # ****** If oops
            return

        if seq_id is None:
            print("[PromptSimulatorWindow] No sequence ID armed.") # ************** If oops
            return

        self.thread = QThread()
        self.runner = SequenceRunner(seq_id, self)
        self.runner.moveToThread(self.thread)
        self.thread.started.connect(self.runner.run)
        self.runner.finished.connect(self.thread.quit)
        self.runner.finished.connect(self.runner.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        print(f"[PromptSimulatorWindow] Running sequence {seq_id} in background thread.")
        self.thread.start() # ********************************************************************* Launch sequencer routines

    @Slot()
    def on_sequence_complete(self):
        self.status_label.setText("Status: Sequence complete.")

class SequenceRunner(QObject):
    finished = Signal()

    def __init__(self, sequence_id, simulator_gui):
        super().__init__()
        self.sequence_id = sequence_id
        self.simulator_gui = simulator_gui

    @Slot()
    def run(self):
        import threading
        print(f"[DEBUG] Running in thread: {threading.current_thread().name}")
        from core.control.sequence_controller import SequenceController
        controller = SequenceController(sequence_id=self.sequence_id, simulated=True, simulator_gui=self.simulator_gui)# ************ Assign values to pass to sequence controller
        controller.run() # ************************************************************************ Run sequence controller
        QMetaObject.invokeMethod(
            self.parent(),  # assumes parent is PromptSimulatorWindow
            "on_sequence_complete",
            Qt.QueuedConnection
        )
        self.finished.emit()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = PromptSimulatorWindow()
    window.show()
    simulated_dispatcher.inject_simulator(window)
    sys.exit(app.exec())

