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

## Use of FLAT files in a ChatGPT Project

The named text files are to be uploaded and attached to a project
created within the OpenAI web or desktop app GUI.

Once uploaded, seed the session by asking GPT to examine the attachments,
particularly your main index document which will inform the main trunk
session (SSE methodology) about the project and available files stored in
FLAT .txt documents.

Maintaining these is often more work than coding and debugging, but keeping
the AI updated with regular re-uploads of freshly updated FLAT files will
keep the session focused on the main goal, and will progress through creating,
debugging, testing, and improving functions across many, many modules, but
with caveats; as you widen the attention requirements of the model, it can
become more focused on code and tracking changes than it is on looking into
freshly updated FLAT files.

While the work is "smaller", it is easier for the model to track its session
tokens and keep a wide range of topics "within view", including instructions
to "always examine FLAT files". But as a project grows, it will be up to the
developer to explicitly instruct the session to examine SPECIFIC related flat
files to ensure it has the context of your most recently updated files, and
when doing so, ask it to report about the contents, then ask it to re-center
its focus on the current goal, which you may refine at any time. This causes
a lot to happen in the GPT "background", but suffice it to say that from there
you can be virtually assured that the session will be synchronized with the
task and your goals for continually adding functionality.

Be advised though, that auto-generated code is no subststute for deep coding
experience, as the GPT can, and will create "perfectly funtional routines"
which don't match your ideas. Avoid "polluting context" in sessions by
digressing into other topics. This is tolerable early in a session, but can
confuse context if expaneded session attention is being leveraged by the FLAT
method, and the AI is more than willing to go off the rails if it thinks you
asked it to; keep your prompts focused on YOUR goal, and avoid its suggestions
as you force the session to progress; it won't mind, and in fact will help it
refocus and centered on a topic. For some reason, the FLAT method causes the
model to appear "eager", and quite so, overzealous at times, an illusion I
noticed emerging as the methods were refined. Ignore it, until YOU are ready
to prodeed. It doesn't "mind" this either, and the illusion stems from the
deterministic focus provided to it from the FLAT files.

Never go rogue in a project session. The AI isn't your assistant — it’s your
pair-programming partner. Break context, and you'll break the contract.

When aligned, the AI keeps a tight focus on your context, and develops certain
"expectations" for your style and intent. When I went "proactive" offline of
a session and created a datbase "out of partnership" with my project sessions,
I created a chain of misunderstandings that rippled through the project under
development which I am debugging even today. This process met negative resistance
during the OpenSIM DCS project because the AI was involved in the creation of
the databse and naming of tables and columns in parallel with support code
generation, but my "rogue" contribution after the fact, when critical modules
were already developed with intent shared by myself and the session, mis-matched
the AI context, and caused it to start "guessing" (not hallucinating) about my
goal for the DB, which ALMOST sounded plausible, but it never complained, and
instead happily helped me embed my self-sabotage deeply into code loaded with
misaligned intent.

I finally got the session more "aligned", but this required days, and even now
it suggests tearing down the whole procedure and starting over.

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
