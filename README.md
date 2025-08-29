# Sansmatic — v0.1

*A universal grammatical–mathematical logical system (theory + code).*  
A theoretical framework: Pāṇini-style grammar + dependently-typed proof kernel → a self-verifying metalanguage/VM.

## Quick links
- [SANSMATIC.md](SANSMATIC.md) — theory and laws
- [examples/](examples/) — demo programs
- [spec/](spec/) — mini grammar spec

## How to contribute
1. Create an issue describing the change.
2. Open a PR with tests and documentation.
3. Use **CC-BY** for docs and **Apache-2.0** for code (see license files).

## Contact
Author: **Raj Mitra**

---

# Prototype Interpreter (v0.1)

This repo contains a minimal prototype interpreter for **Sansmatic**,  
a self-verifying language idea (grammar + proof-binding + VM).

## Run (locally: Termux or Linux)

1. Clone or download the repo.  
2. Run the example:

```bash
python3 src/sansmatic.py examples/program.sans

## Expected output

[DEFINE] Life = {growth, replication, adaptation}
[ASSERT✔] entity HAS growth  (PROOF proof_001 ✓)
[RULE] entity HAS growth ⇒ entity IS Alive
[EVALUATE✔] entity IS Alive is derivable ✓


Proofs are in proofs/proofs.txt.
Examples are in examples/.

License

Code: Apache License 2.0 (see LICENSE)
Documentation: CC BY 4.0 (see LICENSE-DOCS.md)
Alternate License: MIT (see LICENSE-ALT.md)

This means the code under Apache-2.0 OR MIT,
and the documentation under CC BY 4.0.
