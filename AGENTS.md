# AGENTS.md

## Cursor Cloud specific instructions

This is a **translation/localization workspace**, not a traditional software project. It contains JAWS screen reader help documentation being translated from English to Hungarian.

### Project structure

- `Help/HTM/` — English source HTM files (JAWS 2026)
- `Help/PO/` — Translation memory PO files (2024)
- `Help/HU/` — Hungarian translated HTM output
- `Help/jaws.po` — Master terminology file (~180k lines)
- `po_stat.py` — PO translation statistics script (Python 3, stdlib only)
- `JAWS_forditas_prompt.md` — Translation rules and AI prompt (Hungarian)

### Running the utility script

```bash
python3 po_stat.py
```

This is the only executable artifact. It uses only Python 3 stdlib (`re`, `os`) — no dependencies to install.

### No services, builds, or tests

There are no services to start, no build steps, no test suites, and no package managers. The development workflow is AI-assisted translation of HTM files following the rules in `JAWS_forditas_prompt.md`.
