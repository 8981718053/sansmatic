# Sansmatic — Experiments & Evaluation Plan (v0.1)

## E1 — Grammar Determinism Suite
- Goal: Empirically confirm L1/L2 on adversarial inputs.
- Method: Build a corpus of thousands of randomly generated and hand-crafted programs including tricky operator mixes; verify `|Parse(P)| = 1`.
- Metric: determinism rate (%), parser rejection clarity.

## E2 — Proof-Binding on Toy Ontologies
- Goal: Validate L3/L4 on simple domains.
- Method: Examples: `life.sans`, `units.sans` (physics units), `contract.sans` (obligations/remedies).
- Metric: acceptance of valid proofs; rejection of crafted contradictions.

## E3 — LLM Hallucination Gate
- Goal: Reduce factual errors via Sansmatic validator.
- Method: Prompt an LLM to answer factual questions; only accept outputs that compile to Sansmatic and discharge proofs (via SMT/manual).
- Metric: factual error rate vs baseline; abstention rate.

## E4 — Smart-Contract Simulation
- Goal: Show dispute reduction by encoding duties/rights as assertions.
- Method: 100 simulated trades with edge cases; compare disputes vs a comparable Solidity contract without formal assertions.
- Metric: #disputes / 100; time to resolution; violations caught pre-execution.

## E5 — Cross-Domain Encodings
- Goal: Demonstrate expressivity without changing core grammar.
- Method: Encode minimal libraries for AI (types & claims), Math (group theory axioms), Physics (units & conservation), Law (contract template).
- Metric: #domains encoded; #grammar changes required (should be 0); #proof obligations discharged.

## Deliverables
- datasets/, scripts/, and a scoreboard README with metrics.
- A technical report linking results back to HYPOTHESIS.md.
