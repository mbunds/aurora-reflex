#   === FILE: core/web/README.md ===

# AURORA – Autonomous File Agent and Reflexive Control Framework

---

**Authors:** ChatGPT and Mark  
**Created:** 2025-04-12  
**Location:** Evans, Colorado  
**Project:** AURORA  
**Milestone:** New SSE/FLAT Compliant "disciplined" project. 
**License:** MIT  
**FLAT Registered In:** MASTER_INDEX.txt  
**WARNING:**  
> This file may be auto-modified by development tools or AI agents.  
> (Meddle if you dare, foolish mortal!)
> (.qtcreator\Python_3_13_2venv\Scripts\activate)
---

## Purpose

This folder implements Aurora’s browser-driven interaction layer with ChatGPT. It contains all modules responsible for launching the GUI session, injecting prompts, capturing DOM output, and parsing assistant responses. This is the layer that allows Aurora to act *reflexively* within a visual interface — without relying on the OpenAI API.

This folder is where **she sees**.

## Responsibilities

- Launch and manage the ChatGPT GUI session in a stable browser context
- Programmatically inject prompts into the DOM
- Monitor GPT-generated output and detect structured response triggers
- Parse and extract assistant response content via BeautifulSoup or WebDriver
- Serve structured DOM data to the reflex and sequencer systems

## Key Files

- `browser_controller.py`  
  Launches Chrome with a persistent profile, stabilizes the interface, and verifies full GPT session readiness.

- `session_driver.py`  
  High-level controller for prompt injection, HTML capture, and DOM-stabilized execution. Integrates with the reflex pipeline.

- `html_parser.py`  
  Extracts key GPT content nodes (e.g., message bubbles, `<pre><code>` blocks, Monaco editor lines) using BeautifulSoup.

- `element_mapper.py`  
  Associates DOM structures with semantic tags and provides a registry-based interface for code block extraction and formatting via `innerText`.

## Subfolder: `html/`

- Logical subdivision for fine-grained DOM parsing tools
- Houses lower-level modules (`html_parser.py`, `element_mapper.py`) and any future formatting/refinement tools

---

## Integration Notes

- Used by the sequencer and reflex dispatcher to manage self-prompt sessions
- Serves as the underlying transport for GUI-based prompt/response interaction
- Requires Chrome with an authenticated ChatGPT session available to launch
- All prompt injection and result parsing are conducted entirely through the GUI — **no API involved**

---

## FLAT Compliance

- All modules here are registered in `T01_OVERVIEW.txt` and `T02_INITIAL_PROCESSING.txt`
- This folder is critical to Aurora’s reflex chain and must be treated as a deterministic black box for DOM I/O
- Key trigger phrases (e.g., `/CODE COMPLETE/`) are detected using logic defined in `session_driver.py` and `reflex_dispatcher.py`

---

## Notes

This layer represents the visual cognition of Aurora —  
She sees, she waits, and she responds based on structure, not memory.

Future additions may include:

- Browser heartbeat and session recovery logic
- Support for alternate GPT UIs or browser targets
- GUI-based visual cue overlays (e.g., action highlights, DOM selectors)

---

**Aurora doesn’t send requests.  
She acts through sight and response.  
This is where the reflex begins.**
