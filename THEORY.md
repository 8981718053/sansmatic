# Sansmatic — Theory (v0.1)

## 1. Ontology & Syntax (informal to formal)
Universe 𝕌 of entities. Predicates over 𝕌 denote properties/relations.
Core forms (EBNF sketch):
- `DEFINE Concept C AS {f₁, …, fₙ}`  — introduces predicate C : 𝕌 → Bool and feature symbols fᵢ.
- `ASSERT (φ) [PROOF Π|AUTO_PROVE]`  — registers obligation that φ must be derivable.
- `IF (α) THEN (β)`                   — implication α → β within the logic context Γ.
- `EVALUATE e`                         — execute only when all proof obligations in Γ are discharged.

### Unique Parse Requirement
The grammar `G` is engineered with precedence/associativity and disambiguation filters such that:
> **Determinism (T1):** ∀ program P ∈ L(G), |Parse(P)| = 1.

## 2. Typing & Proof Layer
We interpret Sansmatic in a dependently-typed core (CIC-like).
- Judgments: Γ ⊢ φ : Prop, Γ ⊢ Π : φ.
- Every `ASSERT (φ)` introduces obligation `?k : φ` unless `Π` is provided.

> **Soundness (T2):** If Γ ⊢ Π : φ then φ is valid in the model 𝔐 (relative soundness w.r.t. the proof kernel).

## 3. Denotational Semantics
A translation function ⟦·⟧ maps surface Sansmatic to core logic:
- ⟦DEFINE Concept C AS {f₁…fₙ}⟧ := introduce `C : 𝕌 → Prop` and feature predicates `fᵢ : 𝕌 → Prop`.
- ⟦entity HAS {f₁…fₙ}⟧ := ∧ᵢ fᵢ(entity).
- ⟦IF α THEN β⟧ := ⟦α⟧ → ⟦β⟧.
- ⟦entity IS C⟧ := C(entity).

## 4. Operational Semantics (VM sketch)
Configuration ⟨Γ, Σ, P⟩ where Γ is context/proofs, Σ store (optional), P program.
Rules (selected):
- (Assert-Proof)  If `check(Π ⊢ φ)` then Γ := Γ ∪ {φ}.
- (Assert-Obligation) If no Π, append obligation `?k : φ` to Γ.
- (Eval) Allowed iff all `?k` are discharged; otherwise reject.

> **Preservation (T3):** Execution steps preserve proven facts: if Γ ⊢ φ before a step, then still Γ ⊢ φ after.

> **Progress (T4):** A well-formed program either (i) takes a step, (ii) completes, or (iii) rejects with unmet obligation; never “gets stuck” silently.

## 5. Non-Goals (v0.1)
- General recursion totality is not enforced (can be added later).
- Automated theorem proving is best-effort; manual proofs permitted.
- Performance is secondary to correctness in early prototypes.

## 6. Relationship to Prior Work
- Language theory: unambiguous/LR(1)/PEG grammars.
- Proof assistants: Coq/Lean/Agda (our kernel interface mirrors them).
- SMT/ATP: Z3/CVC5 as `AUTO_PROVE` backends (optional).
- Semantic Web/OWL/RDF: Sansmatic enforces single canonical parse + proof binding, stricter than open-world assumptions.

## 7. Expected Theorems (to be proved as we build)
- T1 Determinism of parse (grammar property).
- T2 Relative soundness (trust base = proof kernel).
- T3 Preservation of proven facts over execution.
- T4 Progress (no silent stuck states).
- 
