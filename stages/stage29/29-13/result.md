# Stage29-13 — A2 method transfer across surviving routes

```text
STAGE=Stage29
ITEM=29-13_A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN=f7cf3d5e7ff8c4ec4a6baf3e90b8e8c603067338
ATTACK_ROUTE_COUNT_RETAINED=11
NEW_PRIMARY_ROUTE_CREATED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Scope

Gap Scan C changed the pre-29-13 state from `NONE_FOUND` to

```text
GAP_SCAN_C_RESULT=FOUND_EXTERNAL_INPUT_REQUIRED
```

because a recent self-hosted 2026 source set by Lightman Chang contains several family-closure and method claims not yet present in the Stage29 theorem ledger.

29-13 therefore performs two jobs under one source-first firewall:

1. transfer only the **method species** of audited StageA2, never its family-specific conclusion;
2. independently reconstruct the new external A/B/C/D/E claims far enough to decide whether any can become certified Stage29 child receivers.

The StageA2 transferable method species is

```text
exact low-dimensional family/receiver
 -> exact algebraic reduction or squareclass split
 -> explicit cover(s)
 -> genus-one/Jacobian or other complete arithmetic closure
 -> reconstruction/boundary audit.
```

The original StageA2 equation-(6) `-18` exclusion remains family-specific and is not generalized.

## 2. Positive transfer: Saunderson family closes

### 2.1 Exact family and space-diagonal identity

The external Paper A uses the classical Saunderson family

```text
Sa(u,v,w)=
( u(4v^2-w^2), v(4u^2-w^2), 4uvw )
with u^2+v^2=w^2.
```

Independent symbolic reconstruction verifies

```text
a^2+b^2+c^2 = w^2*(w^4+16*u^2*v^2).
```

For the universal Pythagorean parametrization

```text
u=p^2-q^2,
v=2pq,
w=p^2+q^2,
t=p/q,
```

one obtains exactly

```text
w^4+16*u^2*v^2
 = q^8*(t^8+68*t^6-122*t^4+68*t^2+1).
```

Hence a nondegenerate perfect Saunderson brick gives a rational point on

```text
C': T^2=t^8+68*t^6-122*t^4+68*t^2+1.
```

### 2.2 Palindromic quotient plus exact lift

Divide by `t^4` and put

```text
W=t+1/t,
S=T/t^2.
```

The exact identity is

```text
S^2=W^4+64*W^2-256.
```

The rational-lift condition is not optional: a rational `t` satisfies

```text
W^2-4=(t-1/t)^2.
```

Write `T0=t-1/t`; substituting `W^2=T0^2+4` gives the genus-one receiver

```text
C0: S^2=T0^4+72*T0^2+16.
```

A nondegenerate Saunderson brick has

```text
t not in {0,+1,-1,infinity}
```

and therefore requires a rational point of `C0` with `T0` finite and nonzero.

This is exactly the StageA2-style move: retain the missing rational lifting condition and pass from a larger curve to a smaller explicit cover whose rational points can be completed.

### 2.3 Complete rational-point closure

`C0` has rational point `(T0,S)=(0,4)` and its Jacobian is

```text
E0: y^2=x^3-7*x+6=(x-1)(x-2)(x+3).
```

Independent LMFDB data for Cremona `80a1` certify

```text
conductor=80
rank=0
torsion=Z/2 x Z/2
E0(Q)={O,(1,0),(2,0),(-3,0)}.
```

Since `C0` is a genus-one curve with a Q-point, `C0 ~=_Q E0` as a pointed genus-one curve and has exactly four rational points. Four rational points are already visible:

```text
(0,+4), (0,-4), infinity_+, infinity_-.
```

Thus these are all rational points of `C0`. They have only

```text
T0=0 or T0=infinity.
```

Reconstruction gives

```text
T0=0       -> t=+/-1 -> u=0 -> vanishing edge
T0=infinity-> t=0/infinity -> v=0 -> vanishing edges.
```

Therefore

```text
R29-EXT-CHANG-A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
SAUNDERSON_PERFECT_CUBOID_POINTS=0
SAUNDERSON_FAMILY_EXCLUSION_COMPLETE=true
```

This closes one thin Euler-brick family only. It does not imply `P=0`, does not determine `P/M3`, and does not provide global Euler-brick coverage.

The external source contains a non-load-bearing historical error in its introduction (`(240,252,275)` is called the smallest Euler brick); the same source later correctly identifies `(44,117,240)` as the smallest Saunderson brick. The family-closure proof above does not use the erroneous historical sentence.

## 3. Positive external child: Case B at p=1 closes by Pell--Lucas

Paper B studies

```text
B(q)=(4q, q^2-4, 2(q^2-1)), q in Z_{>0}.
```

Independent expansion gives

```text
a^2+b^2=(q^2+4)^2,
a^2+c^2=(2(q^2+1))^2,
b^2+c^2=5q^4-16q^2+20,
a^2+b^2+c^2=5q^4+20.
```

The paper's introduction says the three face conditions hold identically; that sentence is false. Its formal Lemma 2.2 states the correct result: only two face diagonals are automatic. This inconsistency does not damage the family exclusion because a perfect cuboid would in particular need the space condition.

If the space diagonal is integral and `Y=q^2`, then

```text
g^2-5Y^2=20.
```

Since `5|g`, write `g=5h`; then

```text
Y^2-5h^2=-4.
```

The positive solutions are

```text
Y=L_{2n-1}, h=F_{2n-1}.
```

Cohn's classical Lucas-square theorem says the only square Lucas numbers in the standard sequence are `L1=1` and `L3=4`. Since `Y=q^2` itself must be square,

```text
q^2 in {1,4}
```

so `q in {1,2}`, both degenerate (`q=1` gives a negative/zero edge; `q=2` gives `b=0`). Therefore

```text
R29-EXT-CHANG-B=DISCHARGED_PELL_LUCAS_FAMILY_EXCLUSION
CASE_B_P1_PERFECT_CUBOID_POINTS=0
```

This is a certified thin-family closure but is not an A2 two-cover transfer: its decisive mechanism is Pell-orbit classification plus a classical recurrence-square theorem.

The genus-five rank calculation in Paper B is **not needed** for this closure and is not promoted here.

## 4. Paper C remains finite-window only

Paper C itself limits its exact computation to

```text
rank-1: 1<=n<=200 with torsion translates
rank-2: |a|,|b|<=12.
```

Its all-multiples extension is explicitly conjectural and requires a new effective odd-multiplicity primitive-divisor theorem for the Face-3 numerator. Therefore

```text
R29-EXT-CHANG-C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY
PESCHMANN_5_2_GLOBAL_CLOSURE_CERTIFIED=false
```

No Stage29 route credit is added for rebranding a finite window as a global theorem.

## 5. Paper D is structural input, not a closure

Paper D advertises minimal-discriminant/conductor/Szpiro structure and explicitly does not prove a perfect-cuboid existence/nonexistence theorem. Its own height discussion does not supply the missing uniform positive canonical-height lower bound needed for a global orbit closure.

```text
R29-EXT-CHANG-D=AMBER_HEIGHT_STRUCTURE_INPUT_NOT_ENDPOINT_DECISIVE
A2_METHOD_TRANSFER_FROM_D=false
```

It remains a possible input to 29-15 Arsenal rematch, not a new attack route.

## 6. Paper E fails certification as written

Paper E reduces its prime-parameter Sophie--Germain branches to a genus-one quartic and identifies the Jacobian

```text
Eanom: y^2=x^3-275*x+1750
Cremona 800a3.
```

Independent LMFDB data agree with

```text
rank=1
torsion=Z/2
number of integral points on Eanom=7.
```

However the paper's load-bearing transfer from integral points of its quartic `Canom` to the integral points of `Eanom`, and back to a complete quartic integral-point list, is not supplied with an explicit integrality-preserving birational map in the theorem proof. More importantly, the source explicitly admits that its height-difference constant `mu<=2.93` is sampled, not proved, and says the rigorous Magma/Sage `IntegralPoints` certificate was not actually run in the reported PARI workflow.

The text then says it nevertheless *takes* the seven points as complete. That is not a proof of the theorem as written.

LMFDB's `7` integral-point count on the elliptic curve does not by itself repair the missing quartic-to-elliptic integrality/reconstruction certificate.

Therefore

```text
R29-EXT-CHANG-E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE
SOPHIE_GERMAIN_PRIME_SUBFAMILY_GLOBAL_CLOSURE_CERTIFIED=false
```

A bounded repair path exists: exhibit and audit the explicit birational maps, prove the needed integrality implication, and source-lock a complete `IntegralPoints` computation or an equivalent elliptic-logarithm proof. Until then this result remains AMBER external input.

## 7. Transfer screen across the eleven routes

The only current route with an explicit receiver satisfying the full StageA2 transfer prerequisites is `J12-PARAMETRIC`.

```text
J12-PARAMETRIC:
  Saunderson family -> SUCCESSFUL_LOW_DIMENSIONAL_COVER_TRANSFER
  Case B p=1       -> CERTIFIED_FAMILY_CLOSURE_DIFFERENT_METHOD
  Peschmann rank-positive fibers -> NO_UNIFORM_COMPLETE_ARITHMETIC_CLOSURE
  Sophie-Germain prime family    -> SOURCE_PROOF_INCOMPLETE
```

Other surviving routes do not currently expose a source-locked one-dimensional family/cover with complete reconstruction on which the A2 closure chain can be executed without inventing a new adapter:

```text
G10-FULL-ENDPOINT       surface-level, no A2 family cover
G10-LOWGENUS-PICARD     finite numerical classes but no point-coverage theorem
G10-K3-SIGN             K3 quotient structure, no complete endpoint carrier
Q11-CAMPEDELLI          quotient arithmetic remains Q-form/descent level
Q11-BEAUVILLE           infinite twist family, no finite twist closure
Q11-MODULAR             arithmetic defect action unresolved
Q11-BRAUER              open-boundary/two-primary evaluation unresolved
J12-JOINT-V4            generic joint surface, final conditional P/M3 unknown
J12-LOCAL-SQUARECLASS   local-to-global adapter absent
J12-POP-INTERACTION     already GREEN counting route; no rational-point cover receiver.
```

Thus 29-13 is a **positive but bounded transfer stage**, not a general propagation of StageA2 across all routes.

## 8. Portfolio consequence

Two new certified family exclusions are added to the parametric theorem ledger:

```text
CERTIFIED_NEW_FAMILY_CLOSURE_COUNT_29_13=2
A2_STYLE_SUCCESSFUL_TRANSFER_COUNT=1
```

They do not change the primary parent route colors:

```text
J12-PARAMETRIC=AMBER_GLOBAL_COVERAGE_WITH_CONJECTURAL_DECISIVE_BLOCKER
J12-POP-INTERACTION=GREEN
TOTAL_ROUTE_COLORS=1_GREEN_10_AMBER
```

Why `J12-PARAMETRIC` remains AMBER:

- Saunderson is a thin family, not all Euler bricks;
- Case B at `p=1` is one one-parameter stratum;
- Master-Hit global coverage is already known, but the universal exponent-one blocker remains conjectural;
- Paper C is finite-window only;
- Paper E is not certified as written.

The literal final endpoint survival remains

```text
P(B)/M3(B)=UNKNOWN_GLOBAL_SCALE.
```

## 9. Routing

No frozen Stage16--28 theorem changes and no new primary mechanism appears.

```text
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
ATTACK_ROUTE_COUNT_RETAINED=11
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-14_NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
