# Stage34 — EXT-C primitive-divisor closure roadmap

## Mission

Stage34 is dedicated to the Stage29 Class-3 kernel

```text
K16-C3-EXT-C-PRIMITIVE-DIVISOR
child: R29-EXT-CHANG-C
parent: J12-PARAMETRIC
```

Stage29 froze the exact wall as follows: finite rank-1/rank-2 windows were
executed and audited, but the all-multiples step remained conjectural. The
required theorem shape is an **effective odd-multiplicity primitive-divisor
result** strong enough to upgrade those windows to every admissible multiple.

The success target is deliberately narrow:

```text
R29-EXT-CHANG-C = CLOSED_ALL_ADMISSIBLE_MULTIPLES
```

This does not by itself close `J12-PARAMETRIC`, Master-Hit coverage, or the
perfect-cuboid problem.

## Operating principle

Stage34 follows the bounded startup model used by Stage32/33. Ordinary MAIN
startup reads only `AGENTS.md`, `MAIN-START-HERE.md`, `MAIN-STATE.json`, the tiny
batch handoff, and `current_leaf_working_set`. Historical Stage29 material is
opened only to import one exact missing interface, then compacted into Stage34.
The roadmap itself is not routine startup input.

The mathematical program separates five layers that must never be conflated:

```text
sequence identity
  -> primitive divisor existence
  -> odd valuation / parity
  -> finite exceptional indices
  -> exact cuboid obstruction adapter
  -> all-multiples family closure
```

A theorem that stops at any earlier arrow does not close the kernel.

---

## 34-01 — Exact EXT-C source reconstruction

**Goal:** turn the Stage29 phrase “odd-multiplicity primitive-divisor theorem”
into a precise theorem target.

Produce three compact locks:

1. `exact-sequence-lock.json`: exact recurrence/closed form, normalization,
   parameters, admissible indices/multiples, nondegeneracy and gcd hypotheses;
2. `finite-window-lock.json`: exact audited ranges, scripts/certificates,
   rank-1/rank-2 split if real, and every surviving exception;
3. `cuboid-obstruction-adapter-lock.json`: the exact edge/gcd/representability
   quantity whose square/parity condition is contradicted by an odd primitive
   divisor.

Do not assume in advance that the object is Lucas, Lehmer, elliptic-divisibility,
or another standard sequence. If old evidence is absent from current main, use
Git history for the exact provenance only; do not replay Stage29.

**Exit gate:** the desired global statement can be written with explicit
quantifiers and no undefined “same family”, “bad multiple”, or “primitive” term.

## 34-02 — Sequence classification and theorem funnel

**Goal:** classify the locked sequence into the strongest valid theorem species.

Route in this order:

- **A — Lucas/Lehmer.** Verify integrality, coprimality/nondegeneracy,
  root-of-unity exclusions, discriminant conditions, and whether the moving
  parameters produce one sequence or a uniform family of sequences. Bilu–Hanrot–
  Voutier is the first primitive-existence candidate, not automatic closure.
- **B — Elliptic divisibility.** Identify the elliptic curve/point, minimal model,
  denominators, bad primes and whether an effective primitive-divisor threshold
  is actually available uniformly in the required family.
- **C — General linear/divisibility recurrence.** Isolate cyclotomic atoms and
  test Stewart/Zsigmondy/Thue/S-unit style effective routes.
- **D — Replacement/vacuity route.** If no usable primitive-divisor theorem
  exists, try to prove directly that primitive-divisor-free offending multiples
  form a finite explicit set, or that residue/sign constraints make persistence
  impossible. This is a legal Stage29 closure alternative.

**Exit gate:** one route is selected with every theorem hypothesis mapped to an
EXT-C source-locked fact or an explicit remaining lemma.

## 34-03 — Primitive-divisor existence theorem, with effective threshold

**Goal:** prove the existence half only.

For the selected route, create a theorem source lock containing exact statement,
bibliographic source, theorem number, definition of “primitive”, exceptional
indices, and explicit threshold `N0`. Prove a hypothesis adapter from the EXT-C
sequence to that theorem. If parameters move, prove uniformity over the exact
parameter domain rather than applying a fixed-sequence theorem pointwise without
control.

For a Lucas/Lehmer identification, the classical `n>30` primitive-divisor theorem
is an obvious candidate, but its applicability and parameter uniformity must be
checked exactly.

**Exit gate:** for every admissible `n>N0`, existence of at least one usable
primitive prime/divisor is certified. Odd multiplicity remains explicitly open.

## 34-04 — Odd-multiplicity / valuation parity theorem

**Goal:** bridge the main gap that ordinary primitive-divisor theorems do not
supply.

Work at the primitive cyclotomic atom rather than the whole term whenever
possible. For a primitive prime `p` at index `n`, determine `v_p(S_n)` using the
appropriate rank-of-apparition and lifting/valuation formula. Separate primes
meeting the discriminant, parameter, index, and bad-reduction sets.

Preferred proof shapes, in order:

1. prove some primitive `p` has `v_p(S_n)=1`;
2. more generally prove some primitive `p` has odd `v_p(S_n)`;
3. show the primitive part cannot be a square, forcing an odd valuation somewhere;
4. prove a local squareclass/cyclotomic norm contradiction equivalent to odd
   multiplicity;
5. reduce failure of all four to a finite effective exceptional set.

Do not infer odd valuation merely because `p` is primitive. Explicitly audit
Wieferich-type or repeated-root phenomena if they can raise valuation.

**Exit gate:** every admissible `n>N1` has a primitive divisor usable with odd
multiplicity, with a finite explicit exception set.

## 34-05 — Exceptional-prime and bad-parameter cleanup

**Goal:** remove theorem-side exceptional sets before cuboid-side promotion.

Partition and close:

- `p=2` and other small primes;
- primes dividing sequence discriminant/parameters;
- primes dividing the index `n` where valuation formulas change;
- degenerate/root-of-unity parameter values;
- bad-reduction primes if an elliptic route is used;
- primitive-divisor theorem defective indices;
- odd-multiplicity exceptional indices/parameters.

Use congruences, exact factorization, Thue/S-unit equations, finite CAS, or
certified enumeration as appropriate. Every finite computation must output a
small deterministic certificate, not only a log.

**Exit gate:** the union of all exceptions is explicit and finite.

## 34-06 — Cuboid obstruction adapter proof

**Goal:** prove that the number-theoretic divisor result kills the exact EXT-C
bad multiple.

Starting from `cuboid-obstruction-adapter-lock.json`, prove every arrow:

```text
primitive p at multiple n
  -> p enters the exact EXT-C parent edge / gcd factor for the first time
  -> v_p of the relevant factor is odd
  -> required square / representability / gcd condition fails
  -> this multiple cannot be a spec-admissible EXT-C endpoint candidate
```

Audit sign, normalization, gcd cancellation, scaling, primitivity and any
coordinate permutation. No “morally the same factor” transfer is accepted.

**Exit gate:** the adapter is an exact implication for the same population and
index normalization used by Stage29.

## 34-07 — Certified finite-window and small-index closure

**Goal:** join the new asymptotic theorem to the old audited finite work without a
gap or overlap ambiguity.

Re-run only if necessary for reproducibility. Otherwise source-lock the audited
Stage29 finite certificates, then extend them only through the maximum of all
new thresholds and exceptional indices. Record exact coverage as a union of
intervals/index classes and verify there is no missing admissible multiple.

**Exit gate:** every admissible index below the global theorem threshold is
closed by deterministic finite evidence.

## 34-08 — All-multiples synthesis

**Goal:** state and prove the Stage34 kernel theorem.

The synthesis certificate must contain:

```text
FOR EVERY admissible EXT-C parameter and multiple n:
  if n is in the finite region -> 34-07 certificate closes it;
  if n is beyond the threshold -> 34-03 + 34-04 + 34-06 close it;
therefore no uncontrolled bad multiple survives.
```

Alternative route-D closure is accepted only if it proves the same universal
family conclusion.

**Exit gate:** `promotion_gates.all_multiples_closed=true` and
`R29_EXT_CHANG_C_closed=true`, while endpoint/global firewalls remain false.

## 34-09 — Hostile audit and Stage29 receiver writeback

Audit specifically for the historical failure modes:

- finite evidence silently promoted to all multiples;
- a primitive divisor theorem cited without odd multiplicity;
- a fixed-sequence theorem used uniformly over moving parameters without proof;
- theorem definition of “primitive” mismatched to the cuboid gcd factor;
- missed small indices/defective terms;
- cancellation destroys the claimed odd valuation;
- EXT-C thin-family closure overstated as a global cuboid theorem.

After PASS, write a compact cross-stage certificate that closes only
`R29-EXT-CHANG-C` / `K16-C3-EXT-C-PRIMITIVE-DIVISOR`. Do not rewrite Stage29
history unless an explicit compatibility pointer is useful.

---

## Research priority and likely bottleneck

The highest-risk mathematical leaf is **34-04**, not primitive existence. If the
EXT-C sequence is Lucas/Lehmer, primitive existence may already be close to a
standard theorem, whereas forcing an odd valuation uniformly is a stronger
statement and may encounter rare repeated-prime/Wieferich behavior. Therefore
Stage34 should spend early effort on identifying exactly what parity is needed
and whether a squarefree primitive factor, a cyclotomic atom argument, or a
finite exceptional-set theorem is enough. This avoids proving a beautiful
primitive-divisor theorem that still does not close the receiver.

## Closure definition

Stage34 is complete only when all of the following are true:

```text
exact sequence + index set source-locked
finite Stage29 window source-locked
primitive existence effective and source-locked
odd multiplicity/parity proved
all exceptional indices/parameters finitely discharged
cuboid obstruction adapter proved
all admissible multiples covered
hostile audit PASS
R29-EXT-CHANG-C closed
```

The following remain forbidden conclusions from Stage34 alone:

```text
J12-PARAMETRIC globally closed
all Master-Hit fibers closed
perfect cuboid nonexistence proved
```