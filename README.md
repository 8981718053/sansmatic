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
