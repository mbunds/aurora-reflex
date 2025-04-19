# Folder: `tests/`

## Purpose

This folder contains test modules for validating Aurora’s reflexive control systems, including GUI integration, sequence execution, DOM parsing, and internal reflex trigger mechanisms. These tests provide assurance that Aurora's procedural logic and automation routines operate as expected under various scenarios.

## Responsibilities

- Validate DOM-based response parsing from ChatGPT sessions
- Confirm correct prompt injection and response stabilization cycles
- Test execution of step-driven reflex sequences
- Ensure integration between UI components, sequence controller, and browser interface
- Provide regression detection for core reflex and prompt I/O subsystems

## Key Files

- `test_session_driver.py`  
  Validates prompt submission to ChatGPT via GUI, response capture via DOM, and completion detection.

- `test_element_mapper.py`  
  Tests the `ElementMapper` system used to extract meaningful code/data blocks from ChatGPT responses.

- *(Planned)* `test_sequence_execution.py`  
  Will simulate and validate step-by-step sequence execution logic driven by database-loaded definitions.

## Integration Notes

Tests are executed manually or via CI-compatible runners. GUI-based tests may require a visible browser (non-headless mode) and may invoke live prompts to OpenAI’s ChatGPT interface. Ensure rate limits and automation timing are handled with care.

To run all tests: (If we're lucky; project is in flux...)

```bash
python -m unittest discover tests/
