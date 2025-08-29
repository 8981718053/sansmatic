# Sansmatic — Fundamental Laws (v0.1)

**L1. Well-Formedness (Form Law)**  
Only strings in the language L(G) of the sanctioned grammar are admissible.  
_Formal:_ `P ∈ L(G)` is a precondition to any further processing.

**L2. Unique Meaning (Non-Ambiguity Law)**  
Every admissible program has exactly one AST and one canonical denotation.  
_Formal:_ `|Parse(P)| = 1` and `⟦P⟧` is uniquely defined.

**L3. Proof-Binding (Truth Law)**  
Assertions must be accompanied by a proof object Π or an outstanding obligation `?k`. Evaluation is forbidden while any obligation remains.  
_Formal:_ `ASSERT φ ⇒ (∃Π. check(Π ⊢ φ)) ∨ (?k : φ ∈ Γ)` and `EVALUATE` requires `Γ` has no `?k`.

**L4. Consistency Enforcement**  
If Γ entails a contradiction, the program is rejected; no step may introduce `⊥`.  
_Formal:_ If `Γ ⊢ ⊥`, then `reject`.

**L5. Preservation of Invariants**  
Transformations (optimization, compilation) must preserve proven facts and obligations.  
_Formal:_ If `Γ ⊢ φ` and `P ⇓ P'`, then `Γ ⊢ φ` post-transform.

**L6. Total Reference (No “undefined”)**  
All identifiers and concepts must resolve at parse/type time; dangling references are invalid.  
_Formal:_ `lookup(id)` total over declared scope.

**L7. Referential Transparency (Purity for Meaning)**  
Meaning of expressions depends only on their subexpressions and Γ (not hidden global state).  
_Formal:_ If subterms and Γ are equal, denotations are equal.

> **Corollary:** Classes of bugs eliminated: undefined vars, type/arity mismatches, ambiguous parses, unproved claims, hidden state aliasing.

