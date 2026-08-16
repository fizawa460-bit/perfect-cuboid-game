# Stage27-19-r401c — hostile audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401C_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Scope

Hostile audit of PR #1035 / Stage27-19-r401c. This is a lower-reentry intermediate audit only. It does not close checkpoint40, does not advance to checkpoint50, does not improve the global lower exponent above `1/4`, and does not identify the true `N2` exponent.

## 1. Affine-linear receiver and sextic discriminant

Accepted. For `u=a*tau+b` with `a!=0`, the pullback

\[
S^2=H_{a,b}(\tau)=\tau A_{a,b}(\tau)Q_{a,b}(\tau)
\]

has degree six with leading coefficient `a^4`, hence squarefree generic genus two. Independent symbolic recomputation confirms

\[
\operatorname{Disc}(A)=-(4a^2-4ab-1),
\]

\[
\operatorname{Disc}(Q)=-(b-1)^2F(a,b),
\]

\[
\operatorname{Res}(A,Q)=16a^3(a-b)^3,
\]

and therefore

\[
\operatorname{Disc}(H)=1024a^6(a-b)^6(b-1)^6(b^2+1)^2(4a^2-4ab-1)F(a,b).
\]

```text
AFFINE_LINEAR_RECEIVER_ACCEPTED=true
AFFINE_LINEAR_GENERIC_DEGREE=6
AFFINE_LINEAR_GENERIC_GENUS=2
AFFINE_LINEAR_DISCRIMINANT_FACTORIZATION_ACCEPTED=true
```

## 2. Codimension-one degenerations

Accepted. For rational `a!=0`, the only rational discriminant mechanisms are

- `C_R: a=b`,
- `C_0: b=1`,
- `C_A: 4a^2-4ab-1=0`,
- `C_Q: F(a,b)=0`.

The factor `b^2+1` has no rational zero. Away from component intersections, each mechanism removes one square factor of degree two from the sextic squareclass and leaves degree four, hence genus one. No single codimension-one mechanism produces a genus-zero moving family.

The `C_R` specialization was checked for hidden higher gcd: generically `A` and `Q` share only the root `tau=-1`; `A` never divides `Q` for nonzero rational `a`. Thus there is no unrecorded genus-zero escape on `C_R` alone.

```text
AFFINE_LINEAR_SINGLE_DEGENERATION_GENUS=1
AFFINE_LINEAR_CODIM1_GENUS_ZERO_ROUTE=false
```

## 3. Rational simultaneous degenerations

Accepted. Exact pairwise calculations give:

- `C_R cap C_A` empty;
- `C_R cap C_Q` only `a=3+-2sqrt(2)`, hence no rational point;
- `C_R cap C_0` gives `(a,b)=(1,1)`;
- `C_0 cap C_Q` has no rational point because `F(a,1)=4(2a^2-2a+1)^2`;
- `C_0 cap C_A` has discriminant `32`;
- `Res_a(C_A,F)=256(2b-11)^2`, so `C_A cap C_Q` forces `b=11/2`, then `4a^2-22a-1=0` with discriminant `500`, hence no rational point.

Therefore the only rational simultaneous moving degeneration is `(a,b)=(1,1)`, i.e. `u=tau+1`. The parent r401b already proved this line has `z=1` identically and is nonphysical. The `a=0` degree-drop locus is exactly the already-audited constant-u route.

```text
AFFINE_LINEAR_RATIONAL_SIMULTANEOUS_DEGENERATION=(1,1)_ONLY
AFFINE_LINEAR_ONLY_RATIONAL_GENUS_ZERO_MOVING_LINE=u=tau+1
AFFINE_LINEAR_ONLY_RATIONAL_GENUS_ZERO_MOVING_LINE_PHYSICAL=false
AFFINE_LINEAR_PHYSICAL_GENUS_ZERO_ROUTE_EXISTS=false
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=true
```

## 4. Scope firewall

Accepted only for the explicit affine-linear ansatz `u=a*tau+b` in this natural tau-fibration. This does not classify nonlinear degree-two multisections, does not prove the master surface nonrational in all birational models, and does not establish optimality of the quarter-power lower bound.

```text
ALL_DEGREE_TWO_MULTISECTIONS_CLASSIFIED=false
MASTER_SURFACE_RATIONALITY_DISPROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 5. CI / lifecycle

Submission head `e82c5bc1b544cc2f13fe031f48dec15a7bdf6df1` has SUCCESS for the dedicated `Stage27-19-r401c affine-linear multisection classification` workflow and the relevant Stage27 regressions except the older r401a verifier. The r401a failure is a successor-lifecycle assertion: it allowed current stages r401a/r401b but not r401c. That verifier is repaired on this branch to admit the r401c successor state. Historical Stage25 phase10 and Stage15-8 failures remain unrelated lifecycle debt and are not blockers for this mathematics.

```text
DEDICATED_STAGE27_19_R401C_CI_SUBMISSION_HEAD=SUCCESS
R401A_SUCCESSOR_LIFECYCLE_REPAIRED=true
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_LOWER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
NEXT_DERIVED_ROUTE=27-19-r401d
NEXT_EXPECTED_COMMAND=merge PR #1035; then continue Stage27 checkpoint40 exploration
```
