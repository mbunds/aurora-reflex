# Folder: `flat/`

## Purpose

This folder contains Aurora’s File-Linked Architecture Tracking (FLAT) documents. These flat files serve as the primary structural memory, audit trail, and module registry for all components in the Aurora reflex system. They define, describe, and document the system's construction — across sessions, modules, and milestones — without relying on traditional memory or embedded metadata.

## Responsibilities

- Maintain persistent, versioned text records of all modules, sessions, and project milestones
- Support FLAT compliance by tracking file creation, purpose, integration status, and authorship
- Provide a non-database, non-volatile reference architecture for reconstructing system state
- Enable Structured Session Engineering (SSE) via trunk/branch/leaf log hierarchies

## Key Files

- `MASTER_INDEX.txt`  
  Global reference index for all FLAT files. Acts as the central routing table and historical record of sessions and structural events.

- `T01_OVERVIEW.txt`, `T02_INITIAL_PROCESSING.txt`, etc.  
  Session-based FLAT files tracking specific trunks and development phases under SSE.

- `FOLDER_TREE.txt`  
  Canonical file and folder structure snapshot, maintained manually or during milestone events.

- `FUTURE_FEATURES.txt`  
  Forward-looking roadmap file capturing feature ambitions, reflex expansions, and architectural evolution.

- `MAGIC_BUSES.txt`  
  Reserved for architectural metaphors and internal messaging constructs within Aurora’s modular bus system.

- `DOCS.txt`, `DEVELOPER_SECURITY.txt`  
  Placeholder or specialized flat files reserved for internal design policy, access notes, or future documentation efforts.

---

## Integration Notes

- Every meaningful Python file, test module, or sequence-defining component must be referenced in at least one FLAT file
- FLAT files use clear section headers and prose-style changelogs to preserve audit-friendly development trails
- Trunks and branches follow naming conventions consistent with SSE methodology (e.g., `T01-B02-L01_HTML_GPT01`)

---

## FLAT Compliance

- This folder **is the compliance layer**
- No code module is considered integrated until referenced and explained within a corresponding FLAT file
- All session files are tracked through `MASTER_INDEX.txt` to preserve cross-module lineage

---

## Notes

FLAT files are not an afterthought — they are Aurora’s **mind**.

No embedded metadata.  
No memory dependency.  
No reliance on ChatGPT’s internal persistence.

FLAT allows Aurora to **remember through structure**.

---

**This is not documentation.  
This is cognition.**
