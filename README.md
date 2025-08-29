Sansmatic: A universal grammatical-mathematical logical system (theory + code).

# Sansmatic — v0.1

A theoretical framework: Pāṇini-style grammar + dependently-typed proof kernel → a self-verifying metalanguage/VM.

## Quick links
- SANSMATIC.md — theory and laws (root)
- examples/ — demo programs
- spec/ — mini grammar spec

## How to contribute
1. Create an issue describing the change.
2. Open a PR with tests/documentation.
3. Use CC-BY for docs and Apache-2.0 for code (see license files).

## Contact
Author: Raj (or your chosen author name)

_____________

# SANSMATIC v0.1 — Prototype

Author: Raj Mitra — 28 Aug 2025

This repo contains a minimal prototype interpreter for Sansmatic (v0.1),
a self-verifying language idea (grammar + proof-binding + VM).

## Run (locally, Termux or Linux)

1. Download or clone the repo.
2. Run the example:
```bash
python3 src/sansmatic.py examples/program.sans
Expected output:

pgsql
Copy code
[DEFINE] Life = {growth, replication, adaptation}
[ASSERT✔] entity HAS growth  (PROOF proof_001 ✓)
[RULE] entity HAS growth ⇒ entity IS Alive
[EVALUATE✔] entity IS Alive is derivable ✓

Proofs are in proofs/proofs.txt. Examples are in examples/.


4. Commit message: `Add README with usage` → **Commit new file**.

---

# 6 — Create `.gitignore` (optional but helpful)
1. **Add file → Create new file**.  
2. Filename: `.gitignore`  
3. Paste:


pycache/
*.pyc
.env


4. Commit: `Add .gitignore` → **Commit new file**.

---

# 7 — Create `LICENSE` (MIT recommended)
1. **Add file → Create new file**.  
2. Filename: `LICENSE`  
3. Paste MIT license text, replacing `<YEAR>` and `<OWNER>` with `2025` and `Raj Mitra` (or your preferred
 name):

MIT License

Copyright (c) 2025 Raj Mitra

Permission is hereby granted, free of charge, to any person obtaining a copy
... (rest of MIT license) ...


*(If you want, I can paste the full MIT text for you — tell me and I’ll give the full block to paste.)*

4. Commit message: `Add MIT license` → **Commit new file**.

---

# 8 — Verify the files exist
After the commits, refresh your repo page. You should see folders `src/`, `proofs/`, `examples/` and the files you added. Tap `src/sansmatic.py` to view the file contents on GitHub — that confirms upload success.

---

# 9 — Create a release (optional, anchors v0.1)
1. On the repo page tap **Releases** (right side or under “Code” drop-down) → **Draft a new release**.  
2. Tag version: `v0.1`  
3. Release title: `v0.1 Prototype`  
4. Description: short note like: `Initial public prototype: Sansmatic v0.1 interpreter + examples (Raj Mitra, 28 Aug 2025)`  
5. Click **Publish release**.

This creates a permanent snapshot and makes it citable.

---

# 10 — If you later want to run files from this repo to test in Termux
- On the repo page open **Code → Download ZIP** to download the whole repo to your phone, then unzip it in Termux.  
- Or open a file (e.g. `src/sansmatic.py`), click **Raw**, then copy its raw text and paste into a Termux file.

---

## Final notes & next step
- Do the steps above **in this exact order**. For each file: Add file → Create new file → set path → paste content → commit.
- If any step gives an error or something looks different in your mobile UI, paste a screenshot or copy the error text here and I’ll tell you exactly what to tap next.
- If you want, I’ll paste the **full MIT license block** right now so you can copy it exactly — say “MIT text please” and I’ll paste it.
