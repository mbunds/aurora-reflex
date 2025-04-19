# Folder: `core/web/html/`

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

This folder contains the DOM parsing layer used by Aurora to analyze ChatGPT GUI output at the HTML level. These modules transform raw HTML captured by the browser controller into structured, queryable content for reflex evaluation and code restoration.

This is where **she reads** — line by line, tag by tag.

## Responsibilities

- Parse raw HTML captured from ChatGPT's GUI using BeautifulSoup
- Extract GPT response bubbles, code blocks, and Monaco-based editor lines
- Register semantic mapping keys for extracting specific DOM content types
- Normalize DOM differences across interface updates using stable selectors
- Serve structured content to `session_driver.py` and downstream reflex logic

## Key Files

- `html_parser.py`  
  Parses the captured HTML and exposes access to text bubbles, code blocks, and Monaco editors. Acts as a general-purpose visual DOM interface for assistant output.

- `element_mapper.py`  
  Maintains a registry of canonical DOM extractors. Provides flexible mapping between semantic keys and extraction strategies (e.g., `innertext_code_blocks`).

- `__init__.py`  
  Namespace anchor for `html/` subpackage.

## Integration Notes

- Called by `session_driver.py` after HTML is captured from the browser
- Exposes structured elements for use in:
  - `reflex_dispatcher.py` for trigger string scanning
  - `code_sanitizer.py` for block extraction
  - Visual test modules such as `test_submit_prompt_demo.py`

- Parsing logic uses `BeautifulSoup` and Selenium selectors (depending on entry point)

---

## FLAT Compliance

- Fully tracked in `T01_OVERVIEW.txt` and `T02_INITIAL_PROCESSING.txt`
- DOM field mappings should be documented in FLAT logs when changes occur
- Selector logic updates must be reflected in milestone changelogs and FLAT version history

---

## Notes

This folder is intentionally lightweight and adaptable.

It isolates DOM parsing from reflex logic so that GUI surface changes (e.g., GPT UI updates) can be managed without modifying system flow or sequencer definitions.

Future improvements may include:

- Snapshot preservation of response HTML for debugging or offline replay
- Selector fallbacks or intelligent DOM re-targeting logic
- Structural diffing to detect GPT UI shifts over time

---

**Aurora doesn’t guess what the model said.  
She reads it — from the DOM,  
with precision.**
