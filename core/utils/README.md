# Folder: `core/utils/`

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

This folder contains Aurora’s reflex support utilities and output refinement tools. These modules perform formatting, cleanup, token repair, and style normalization for flattened or damaged code extracted from GUI-based ChatGPT responses.

While not part of the reflex dispatch chain directly, these utilities are essential to restoring **human-readable structure** and ensuring that Aurora's outputs maintain clarity, determinism, and developer-grade formatting.

This folder is where **she polishes her voice**.

## Responsibilities

- Restore proper indentation and structure to flattened or malformed code blocks
- Apply logic-aware spacing, punctuation repair, and class/function detection
- Normalize prompt-generated code into readable, testable output
- Support visual or CLI-based reflex execution with readable final outputs
- Provide beautification post-processing compatible with FLAT systems and visual review

## Key Files

- `code_restorer.py`  
  Reconstructs flattened code into logical structures with indentation, spacing, and syntax cues. Handles token reassembly and structural breaks caused by GUI rendering.

- `code_formatter.py`  
  Final pass beautifier. Normalizes spacing, import line formats, and aesthetic consistency for restored code blocks.

- `code_sanitizer.py`  
  High-level entry point for GUI-captured output. Wraps both restoration and beautification into a single pipeline. Called directly by reflex sequences or test capture routines.

- `__init__.py`  
  Included for namespace completeness.

## Integration Notes

- Used by:  
  - `session_driver.py` – to post-process captured GPT output  
  - `reflex_dispatcher.py` – for reflex code validation  
  - `tests/test_submit_prompt_demo.py` – for flattened block restoration

- Output is generally returned as `str` for display, logging, or module writeback

- These utilities are **modular** and can be extended to support other languages or prompt styles in future sequences

---

## FLAT Compliance

- Registered in: `T02_INITIAL_PROCESSING.txt`
- FLAT files referencing output capture or code cleaning must identify which utility stage was used
- Token restoration must be traceable through sequencer logs or milestone records

---

## Notes

This folder is not about logic.  
It’s about **presentation**, **readability**, and **developer trust**.

Aurora doesn’t just act —  
**she shows you what she did.**

Future expansions may include:

- Jupyter-style code block postprocessors
- Reflex-specific comment overlays for generated code
- Automated code comparison and version-aware formatting

---

**When Aurora speaks,  
this is how she ensures  
you’ll understand her.**
