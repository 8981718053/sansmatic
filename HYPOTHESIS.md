# Sansmatic — Hypotheses (v0.1)

## Primary Hypothesis (H₀)
Fusing **unambiguous grammar** (Pāṇini-style) with **machine-checkable logic** (dependently typed proofs) yields a language/VM in which every valid statement is both:
1) uniquely parsed, and
2) truth-bound (provable or rejected),
thereby eliminating classes of ambiguity and contradiction present in natural language and typical programming systems.

## Sub-Hypotheses (testable)
H1 — **Parse Determinism:** For all well-formed Sansmatic programs P, `parse(P)` returns exactly one AST (no shift/reduce ambiguities).

H2 — **Proof Binding:** For any `ASSERT φ`, evaluation accepts iff there exists a machine-checkable proof Π such that `check(Π ⊢ φ)`.

H3 — **Bug Reduction:** When code generators are constrained by Sansmatic assertions, runtime class of errors (undefined var, type errors, unmet preconditions) reduces ≥ 80% relative to baseline language X on benchmark Y.

H4 — **Hallucination Suppression (LLM):** When LLM outputs must pass Sansmatic validation, factual error rate on tasks T decreases ≥ 50% at equal coverage.

H5 — **Contract Clarity:** Dispute rate in controlled “smart-contract” simulations drops to near 0 when obligations and remedies are encoded as Sansmatic assertions with executable checks.

H6 — **Cross-Domain Expressivity:** Canonical encodings exist for at least four domains (AI, law, math, physics) without extending core grammar—only libraries.

## Metrics & Evaluation
- Determinism: % unique parses on grammar stress suite.
- Proof Binding: (% asserts proved) / (total asserts) ; rejection rate for invalid proofs.
- Bug Reduction: failing test cases per KLOC before/after Sansmatic constraints.
- Hallucination: factual error rate (E) and abstention rate (A) under validator.
- Contract Clarity: #disputes / #contracts in red-team simulations.
- Expressivity: #domains encoded without core grammar changes.

## Falsifiability
H₀ is falsified if any of the following hold:
- A well-formed program admits multiple parses (counterexample to determinism).
- A contradiction is accepted at run-time.
- Practical tasks show no measurable reduction in ambiguity/error against baselines.
