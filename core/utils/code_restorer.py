# === FILE: core/utils/code_restorer.py ===

"""
Aurora – Reflexive AI Control Framework
---------------------------------------

Module: core/utils/code_restorer.py
Authors: ChatGPT and Mark
Created: 2025-04-15
Location: Evans, Colorado
Project: Aurora

This module restores human-readable formatting and indentation to flattened Python
code blocks extracted from ChatGPT GUI responses where spaces and newlines have
been stripped.

License:
    This file is part of the Aurora project and is distributed under the terms of
    the MIT License. See the LICENSE file in the project root for details.

WARNING:
    This file may be auto-modified by development tools or AI agents as part of
    the Aurora project workflow. Manual changes should be made cautiously.
    (Meddle if you dare, foolish mortal!)

FLAT Compliance:
    - Registered in: [T02_INITIAL_PROCESSING.txt]
    - This file participates in branch T02-B02_CODE_CAPTURE_CLEAN
    - Versioning and audit history are maintained via flat-file records.

---

Code Restoration Utility

Restores indentation, newlines, and structure to compacted Python code blocks.
"""

import re

# --- Phase 10 patch: spacing and punctuation repair ---
def patch_phase_10_spacing(blob: str) -> str:
    fixes = [
        (r'(?<!\w)(if|for|while|with|as|in|def|class|return|raise|print|except|elif|else|try|not)([A-Za-z_])', r'\1 \2'),
        (r'(?<!\w)(import)([A-Za-z_])', r'\1 \2'),
        (r'(?<!\w)(except)([A-Za-z_]+)(as)([A-Za-z_]+)', r'\1 \2 as \4'),
        (r'(?<!\w)(is|not|and|or)([A-Za-z_])', r'\1 \2'),
        (r'([a-zA-Z0-9_])=([a-zA-Z0-9_])', r'\1 = \2'),
        (r'\bdef ([a-zA-Z0-9_]+) \(', r'def \1('),
        (r'\bclass ([a-zA-Z0-9_]+) \(', r'class \1('),
        (r'([^\s])\(', r'\1 ('),  # space before (
        (r'\)([^\s])', r') \1'),  # space after )
    ]
    for pattern, repl in fixes:
        blob = re.sub(pattern, repl, blob)
        return blob

def preprocess_tokens(blob: str) -> str:
    """
    Phase 9 Preprocessing — Repair severely flattened logic, import spacing, and docstring padding.
    """
    # Ensure triple-quoted docstrings open cleanly after header
    blob = re.sub(r'(# === FILE: .+?===)"""', r'\1\n"""', blob)

    # Break chained import statements like: importyamlimportsys
    blob = re.sub(r'import([A-Z_a-z])', r'import \1', blob)
    blob = re.sub(r'(import [a-zA-Z_]+)(?=import)', r'\1\n', blob)
    blob = re.sub(
        r'(import [a-zA-Z_]+(?:\s+import [a-zA-Z_]+)+)',
        lambda m: '\n'.join(re.findall(r'import [a-zA-Z_]+', m.group())),
        blob
    )

    # Newline before each new class or def block if run-together
    blob = re.sub(r'(class|def)([A-Z_a-z])', r'\1 \2', blob)
    blob = re.sub(r'(?<!\n)(def .+?:)', r'\n\1', blob)
    blob = re.sub(r'(?<!\n)(class .+?:)', r'\n\1', blob)

    # Pad between def blocks if crushed together (def x():def y())
    blob = re.sub(r'(\):)(?=def )', r'\1\n', blob)

    # Ensure closing triple quotes get their own line if packed
    blob = re.sub(r'("""[^"]+)(?=""")', r'\1\n', blob)

    # Fix jammed flow logic (e.g., ifx: → if x:)
    logic_keywords = ['if', 'for', 'while', 'elif', 'except']
    for kw in logic_keywords:
        blob = re.sub(rf'\b{kw}([A-Za-z_])', rf'{kw} \1', blob)

    # Miscellaneous glue and token repairs
    replacements = [
        (r'ifnot', r'if not '),
        (r'elifnot', r'elif not '),
        (r'whilenot', r'while not '),
        (r'([a-zA-Z_])=None', r'\1 = None'),
        (r'=Noneself', r'= None\nself'),
        (r'(except)([a-zA-Z_.]+)(as)([a-zA-Z_])', r'\1 \2 as \4'),
        (r'(\))([a-zA-Z_])', r'\1\n\2'),
        (r'([a-zA-Z_])\(', r'\1 ('),
        (r':([a-zA-Z])', r': \1'),
        (r',([a-zA-Z])', r', \1'),
        (r'print\(', r'\nprint('),
        (r'(?<!\n)(if)__name__', r'\n\1 __name__'),
    ]
    for pattern, repl in replacements:
        blob = re.sub(pattern, repl, blob, flags=re.DOTALL)

    return blob

def restore_code_structure(flat_code: str) -> str:
    """
    Attempt to restore proper indentation and line breaks to a flattened block of Python code.
    """
    flat_code = preprocess_tokens(flat_code)

    keywords = [
        'def ', 'class ', 'if ', 'elif ', 'else:', 'for ', 'while ',
        'try:', 'except ', 'finally:', 'with ', 'return ', 'import ',
        'from ', 'raise ', 'print(', 'input(', '@'
    ]

    pattern = r'(?:(?<=\s)|(?<=^))(?=(?:' + '|'.join([re.escape(k.strip()) for k in keywords]) + '))'
    candidates = re.split(pattern, flat_code)

    raw_lines = []
    buffer = ''
    for chunk in candidates:
        chunk = chunk.strip()
        if not chunk:
            continue
        if any(chunk.startswith(k.strip()) for k in keywords):
            if buffer:
                raw_lines.append(buffer.strip())
            buffer = chunk
        else:
            buffer += ' ' + chunk
    if buffer:
        raw_lines.append(buffer.strip())

    # PHASE 1B: Merge stray 'def' or 'class' lines with their continuations
    final_lines = []
    i = 0
    while i < len(raw_lines):
        line = raw_lines[i]
        if line in ('def', 'class') and i + 1 < len(raw_lines):
            final_lines.append(line + ' ' + raw_lines[i + 1])
            i += 2
        else:
            final_lines.append(line)
            i += 1

    # PHASE 2: Split lines with multiple def/class occurrences
    split_lines = []
    for line in final_lines:
        parts = re.split(r'(?<!^)(?=(?:def |class ))', line)
        for part in parts:
            part = part.strip()
            if part:
                split_lines.append(part)

    # PHASE 3: Indentation logic
    indented_lines = []
    indent = 0
    for line in split_lines:
        line = line.strip()
        indented_lines.append('    ' * indent + line)
        if line.endswith(':'):
            indent += 1
        if re.match(r'^(return|raise|break|continue|pass)\b', line):
            indent = max(0, indent - 1)
        if re.match(r'^(except|elif|else):', line):
            indent = max(0, indent - 1)

    return patch_phase_10_spacing('\n'.join(indented_lines))

    return blob

if __name__ == '__main__':
    example_flat_code = """
#!/usr/bin/env python3importyamlimportargparseimportosimportsysclassConfigLoader:def__init__(self, config_path):self.config_path=config_pathself.required_fields=['app_name','version','database.host','database.port','features.enable_logging']self.config={}defload(self):ifnotos.path.exists(self.config_path):raiseFileNotFoundError(f"Config file not found:{self.config_path}")withopen(self.config_path,'r')asf:try:self.config=yaml.safe_load(f)ifself.configisNone:raiseValueError("YAML file is empty.")exceptyaml.YAMLErrorase:raiseValueError(f"Failed to parse YAML:{e}")defvalidate(self):missing=[]forfieldinself.required_fields:keys=field.split('.')value=self.configforkeyinkeys:ifisinstance(value,dict)andkeyinvalue:value=value[key]else:missing.append(field)breakifmissing:raiseValueError(f"Missing required fields:{', '.join(missing)}")defprint_summary(self):print("=== CONFIG SUMMARY ===")print(f"Application:{self.config.get('app_name')}")print(f"Version:{self.config.get('version')}")db=self.config.get('database',{})print(f"DB Host:{db.get('host')}")print(f"DB Port:{db.get('port')}")features=self.config.get('features',{})print(f"Logging:{features.get('enable_logging')}")print("======================")defmain():parser=argparse.ArgumentParser(description='Load and validate a YAML configuration file.')parser.add_argument('config',metavar='CONFIG_FILE',help='Path to the YAML configuration file')args=parser.parse_args()loader=ConfigLoader(args.config)try:loader.load()loader.validate()loader.print_summary()exceptExceptionase:print(f"[ERROR]{e}",file=sys.stderr)sys.exit(1)if__name__=='__main__':main()
"""
    restored = restore_code_structure(example_flat_code)
    print("\n--- Restored Code ---\n")
    print(restored)
