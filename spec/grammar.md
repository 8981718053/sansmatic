# Sansmatic mini grammar (spec/grammar.md) — v0.1

This is a compact EBNF sketch for the core forms used in v0.1.

S -> StatementList
Statement -> DefineStmt | AssertStmt | IfStmt | EvalStmt
DefineStmt -> "DEFINE" IDENT "AS" "{" FieldList "}"
AssertStmt -> "ASSERT" "(" Expr ")" ["PROOF" ProofRef]
IfStmt -> "IF" "(" Expr ")" "THEN" "(" Expr ")"
EvalStmt -> "EVALUATE" Expr
Expr -> Predicate | Compound
Predicate -> IDENT | IDENT "(" ArgList ")"
ProofRef -> PROOF_ID | AUTO_PROVE

Notes:
- Panini-style production rules will later be expanded into prioritized rewrites with markers.
- This mini-spec is intentionally small for prototyping the parser.
- 
