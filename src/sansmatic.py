# backup current interpreter
cp sansmatic.py sansmatic.py.bak 2>/dev/null || true

# write fixed interpreter
cat > sansmatic.py <<'PY'
#!/usr/bin/env python3
import re, sys, os

DEFINE_RE = re.compile(r'^DEFINE\s+([A-Za-z_]\w*)\s+AS\s+\{([^}]*)\}\s*$', re.IGNORECASE)
ASSERT_RE = re.compile(r'^ASSERT\s*\(?\s*(.+?)\s*\)?\s*(?:PROOF\s+([A-Za-z_]\w*))?\s*$', re.IGNORECASE)
IF_RE     = re.compile(r'^IF\s*\(?\s*(.+?)\s*\)?\s*THEN\s*\(?\s*(.+?)\s*\)?\s*$', re.IGNORECASE)
EVAL_RE   = re.compile(r'^EVALUATE\s*\(?\s*(.+?)\s*\)?\s*$', re.IGNORECASE)

def normalize(expr: str) -> str:
    if expr is None:
        return ''
    e = expr.strip()
    # remove one or more wrapping parentheses (iteratively)
    while e.startswith('(') and e.endswith(')'):
        e = e[1:-1].strip()
    # collapse whitespace and normalize commas
    e = ' '.join(e.split())
    e = re.sub(r'\s*,\s*', ', ', e)
    return e

def load_proofs(path='proofs.txt'):
    s = set()
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                s.add(line)
    return s

def contra_of(expr: str) -> str:
    e = normalize(expr)
    if e.upper().startswith('NOT '):
        return normalize(e[4:])
    else:
        return normalize('NOT ' + e)

def forward_chain(facts: set, rules: list, max_iters=100):
    facts = set(facts)
    changed = True
    iters = 0
    while changed and iters < max_iters:
        changed = False
        iters += 1
        for cond, cons in rules:
            if cond in facts and cons not in facts:
                facts.add(cons)
                changed = True
    return facts

def run(filename):
    proofs = load_proofs()
    facts = set()
    rules = []
    obligations = []
    outputs = []

    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        sys.exit(1)

    with open(filename) as f:
        lines = [ln.rstrip('\n') for ln in f if ln.strip() and not ln.strip().startswith('#')]

    for ln in lines:
        ln_strip = ln.strip()

        m = DEFINE_RE.match(ln_strip)
        if m:
            name, fields = m.groups()
            outputs.append(f"[DEFINE] {name} = {{{fields.strip()}}}")
            continue

        m = ASSERT_RE.match(ln_strip)
        if m:
            expr_raw, proof_id = m.groups()
            expr = normalize(expr_raw)
            if proof_id:
                if proof_id in proofs:
                    facts.add(expr)
                    outputs.append(f"[ASSERT✔] {expr}  (PROOF {proof_id} ✓)")
                else:
                    obligations.append((expr, proof_id))
                    outputs.append(f"[ASSERT✖] {expr}  (PROOF {proof_id} missing)")
            else:
                obligations.append((expr, None))
                outputs.append(f"[ASSERT✖] {expr}  (no PROOF)")
            # contradiction check
            c = contra_of(expr)
            if c in facts:
                outputs.append(f"[CONTRADICTION] {expr} conflicts with '{c}'")
            continue

        m = IF_RE.match(ln_strip)
        if m:
            cond_raw, cons_raw = m.groups()
            cond = normalize(cond_raw)
            cons = normalize(cons_raw)
            rules.append((cond, cons))
            outputs.append(f"[RULE] {cond} ⇒ {cons}")
            continue

        m = EVAL_RE.match(ln_strip)
        if m:
            target_raw = m.group(1)
            target = normalize(target_raw)
            if obligations:
                outputs.append(f"[HALT] Unmet proof obligations: {len(obligations)}. Cannot EVALUATE '{target}'.")
            else:
                closure = forward_chain(facts, rules)
                if target in closure:
                    outputs.append(f"[EVALUATE✔] {target} is derivable ✓")
                else:
                    outputs.append(f"[EVALUATE✖] {target} is not derivable")
            continue

        outputs.append(f"[INVALID] {ln_strip}")

    print('\\n'.join(outputs))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sansmatic.py program.sans")
        sys.exit(1)
    run(sys.argv[1])
PY

# ensure proofs exist
grep -qxF "proof_001" proofs.txt 2>/dev/null || echo proof_001 >> proofs.txt
grep -qxF "proof_002" proofs.txt 2>/dev/null || echo proof_002 >> proofs.txt

# create a canonical program to test (parentheses allowed or not)
cat > program.sans <<'EOF'
DEFINE Life AS {growth, replication, adaptation}
ASSERT (entity HAS growth) PROOF proof_001
IF (entity HAS growth) THEN (entity IS Alive)
EVALUATE (entity IS Alive)
EOF

# run the test
python sansmatic.py program.sans
