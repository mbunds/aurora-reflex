# Folder: `docs/`

## Purpose

This folder contains refined documentation, public-facing reference material, and external communication assets for the Aurora Reflexive AI Control Framework. It is distinct from the internal FLAT system, which handles audit trails and structural memory. The `docs/` folder is used to publish, export, or organize knowledge for readers, collaborators, or future maintainers.

## Responsibilities

- Contain formal documentation (e.g., architecture references, user guides, command references)
- Host LaTeX whitepaper sources, generated diagrams, or publish-ready markdown exports
- Support knowledge transfer outside of development sessions
- Provide a place for formatting articles, research materials, and release documentation

## Key Files

- `__init__.py`  
  Empty file retained for Python compatibility and structural consistency.

- *(Future)* `aurora_whitepaper.tex`, `system_reflex_map.md`, `installation_guide.md`  
  These files will define Aurora's theory of operation, reflex structure, and system usage pathways for external audiences.

## Integration Notes

This folder should not be confused with `flat/`, which serves as Aurora’s persistent internal structure.  
Instead, `docs/` may contain cleaned and compiled content *derived from* FLAT entries and runtime interactions, made suitable for public or formal use.

Common sources include:

- Exported markdown or LaTeX from reflex modules or milestone reports
- Captured sequences or screenshots from the `resources/` folder
- Diagrams stored in `graphics/` but referenced from whitepapers or posts

---

## FLAT Compliance

- `docs/` is referenced in `MASTER_INDEX.txt` and `T01_OVERVIEW.txt` as a structured export node
- Files here **do not replace FLAT logs**, but may be derived from or informed by them
- FLAT-to-docs migration may be logged manually in session comments or changelogs

---

## Notes

Future usage may include:

- Article pre-publication drafts
- Whitepaper source structure (LaTeX or markdown)
- Design philosophy records or external methodology briefings
- API or user interface manuals once Aurora reaches general use

---

**Where FLAT remembers,  
`docs/` explains.**
