# Stage35-EX Goal4CF — selected-direction minimal discriminant versus endpoint height

Status: **PROVISIONAL_EXACT_QUANTITATIVE_ADAPTER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT**.

The top-level target is E1, not continuation of Goal4CE. This checkpoint supplies
new quantitative input to the Goal4AW height route. It neither excludes an E1
counterexample nor asserts that a height contradiction now follows.

## 1. Authority and research boundary

- Starting retained head: `70520b10e7db7063b1d7a7b75485533c131fe9f5`.
- PR #1723 is CLOSED without merge; its closure comment is
  <https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1723#issuecomment-5613825355>.
- Mathematical authority remains V74 / Goal4AK, review `5142248509`.
- The independently audited intermediate boundary remains Goal4BS, review
  `5151846948`, exact head `d6f5151c9d95304afe7081c92f40f1d25cc4aa3b`.
- Observed main: `5ca6acba4b591d9e2d40057241c850598c1fa1df`. Compared with
  `42f20e47babdfdda068a605e3fec489eeace460c`, no main-side change occurs in
  root AGENTS.md, docs/research-os, or stages/stage35-ex. This is a scoped
  freshness observation, not merge-ready certification.
- The retained start is 58 commits after the BS audit boundary. A new branch
  does not reset that retained-delta distance. Merge remains forbidden.

Operational authority for the top-level reassessment is the user's explicit
2026-09-10 instruction to choose the research route freely. MAIN-STATE is not
rewritten to pretend that provisional research has been promoted.

## 2. Blind breadth pass, then deduplication

The blind candidate list was recorded before consulting Arsenal recommendations:

| Candidate | Exact comparison or missing input | Status at this checkpoint |
|---|---|---|
| A. Symmetric differentials giving an effective global rational-point height bound | Curve restrictions are not a bound on all isolated rational points; no arithmetic height theorem is supplied | BLOCKED for this proposed import |
| B. Near-square gap against the Master hypotenuse | `T^2-S^2=(U1*U2)^2` is exactly the BS section 3.2 endpoint triangle | EQUIVALENT; no repeat |
| C. Height-decreasing full-endpoint rational correspondence | AY/AZ block the retained derived involution; no different map or fourth-square preservation proof is supplied | BLOCKED with current maps |
| D. Uniform marked elliptic height/discriminant comparison | AW's fixed-direction formulation leaves room for a quantitative selection among the BD cyclic directions | LIVE, selected below |
| E. Uniform simultaneous Pell exclusion | Fixed-source finiteness lacks uniform moving-source bounds; without those bounds it only restates the BS 35EX-02..06 square system | BLOCKED for the proposed fixed-source import |
| F. Infinite distinct-class amplification | AZ requires `rho/kappa>1/2`; no new map with this exponent is supplied | BLOCKED with current maps |

For A, the bounded primary-source check was Bruin--Thomas--Varilly-Alvarado,
*Explicit computation of symmetric differentials and its application to
quasi-hyperbolicity*, <https://arxiv.org/abs/1912.08908>. Its stated cuboid
applications restrict rational and genus-one curves. No all-rational-point
effective height bound is imported. This is not a claim that every future
symmetric-differential arithmetic approach is impossible.

The machine-readable Arsenal registry was queried for the identified height,
elliptic, and fixed-source solver inputs. `S31-W01` is used as an adapter-scope
check: a model change does not grant integral-point completeness. `LIT-PW07`
requires a fixed finite S, an MW basis, and an initial height bound; it supplies
none of the missing uniform moving-family estimates here. No Arsenal card is
promoted or modified. The bounded Stage35-EX source-lock search did not find
the selected-direction quantitative inequality proved below; this is not a
repository-wide or literature-wide novelty claim.

Historical AW, AU, BD, BS, AZ and CE claims remain frozen. In particular,
BD's joint rational-point receiver remains endpoint-equivalent. We use its
forward cyclic point maps, not its joint equations as a purported obstruction.

## 3. Population, height, and selected direction

Assume a positive primitive integer E1 counterexample endpoint:

```text
gcd(A,B,C)=1,
D_AB^2=A^2+B^2, D_AC^2=A^2+C^2, D_BC^2=B^2+C^2,
W^2=A^2+B^2+C^2.
```

The existing audited E1-to-endpoint adapter is retained through Goal4M.
The argument below actually proves its discriminant statement on the larger
population of primitive Euler bricks; W there means the positive real square
root. This larger-population observation supplies nonempty regression examples,
not a rational point on a physical marked elliptic receiver.

Define three *multiplicative* reduced edge-ratio heights:

```text
h_AB=max(A,B)/gcd(A,B),
h_AC=max(A,C)/gcd(A,C),
h_BC=max(B,C)/gcd(B,C).
```

Choose a pair attaining `h*=max(h_AB,h_AC,h_BC)`, breaking ties in the fixed order
AB, AC, BC. Its opposite edge selects the C-, B-, or A-orientation of BD,
respectively. This selection uses the edges alone, with no rank, conductor,
discriminant factorization, or E1 square-root oracle.

**Primitive height lemma.** Put `M=max(A,B,C)`. Then

```text
(h*)^2 >= M >= W/sqrt(3).                              (CF-1)
```

Proof: suppose A=M. Set x=gcd(A,B), y=gcd(A,C). Since a common divisor of x,y
would divide A,B,C, gcd(x,y)=1. Thus xy divides A and

```text
h_AB*h_AC=A^2/(xy) >= A.
```

The other choices of the largest edge follow by permutation. Finally
`W^2<=3M^2`. No pairwise-coprimality assumption on the raw edges is made.

## 4. Explicit global minimal model on every reduced face

For the chosen pair, let b,c be its positive coprime reduced legs. Because its
face diagonal is rational, the reduced face is a primitive integer right
triangle. Hence b,c have opposite parity and b!=c. Write h=max(b,c)>=2.

The AT/BD parameter (possibly negated, which leaves E unchanged) has

```text
r=c^2-b^2, s=2bc, t=b^2+c^2,
q=r/s, r^2+s^2=t^2,
gcd(r,s)=gcd(r,t)=gcd(s,t)=1,
r,t odd, 4|s.
```

Thus this is already a reduced q; there is no hidden common-content division.
The AW integral model is

```text
E: y^2=x(x-s^2)(x+r^2),
a2=r^2-s^2, a4=-r^2*s^2,
Delta_raw=16*r^4*s^4*t^4,
c4_raw=16*(r^4+r^2*s^2+s^4).
```

Make the **explicit rational isomorphism**

```text
x=4u, y=8v+4u.
```

The resulting integral equation is

```text
E_min: v^2+u*v = u^3 + ((r^2-s^2-1)/4)*u^2
                         - (r^2*s^2/16)*u.             (CF-2)
```

Both coefficients are integers: r odd gives r^2=1 mod 8, and 4|s.
Its invariants are

```text
c4_min=r^4+r^2*s^2+s^4,
Delta_min=(r*s*t)^4/256.                               (CF-3)
```

To prove global minimality, at 2 the displayed c4 is odd. At any odd prime
ell|rst, reduce the bracket: if ell|r it is s^4; if ell|s it is r^4; if ell|t,
use r^2=-s^2 to obtain s^4. In each case it is a unit. At every other prime
Delta is a unit. An integral Weierstrass model with c4 or Delta a local unit
is minimal: an integral model of smaller discriminant would require a
positive-valuation change scale and would make c4 or Delta nonintegral.

The invariant change formulas are source-checked against Silverman,
*The Arithmetic of Elliptic Curves*, second edition, Chapter III, Table 3.1,
printed p.45 (PDF p.63): `u^4*c4'=c4`, `u^12*Delta'=Delta`.
Primary monograph: <https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf>.
The repository verifier independently expands the displayed model change and
its invariants; no output from a numerical minimal-model routine is assumed.

This strengthens AW's odd-prime-only statement on the **source-derived
subfamily r odd, 4|s**. It does not classify every alternate AW r/s convention.

## 5. Pair-height discriminant bound

Put k=min(b,c), so 1<=k<=h-1. The exact factorization

```text
k*(h^2-k^2)-(h^2-1)
  =(k-1)*(h^2-k^2-k-1) >= 0                           (CF-4)
```

follows since
`h^2-k^2-k-1 = (h-k-1)*(h+k+1)+k >= 1`.
Consequently

```text
|r*s*t| = 2*h*k*(h^2-k^2)*(h^2+k^2)
         >= 2*h^3*(h^2-1)
         >= (3/2)*h^5,
```

where the last step uses h>=2. Combining with (CF-3),

```text
|Delta_min(E)| >= (81/4096)*h^20.                     (CF-5)
```

Use the direction selected in section 3. Equations (CF-1) and (CF-5) give

```text
|Delta_min(E_*)| >= (81/4096)*M^10
                 >= W^10/12288.                      (CF-6)
```

All three curves are the relabeled BD/Goal4L receivers. Under the hypothetical
endpoint assumption each carries its physical marked non-torsion point, so
the selected curve retains that hypothesis. We do not infer non-torsion points
from Euler-brick regression examples with nonsquare W^2.

## 6. Exact quantifiers and what AW receives

With natural logarithms, the new statement is

```text
for every positive primitive endpoint P,
  for the deterministic edge-selected direction i(P),
  log|Delta_min(E_i(P))| >= 10*log W(P)-log(12288).       (CF-C2*)
```

It is not AW-C2 for one fixed preselected direction. Nor is it a lower bound
in an arbitrary cutoff B_cut for every point of height <=B_cut: keeping one
point fixed while increasing B_cut would invalidate that quantifier pattern.
On the dyadic shell B_cut/2<W<=B_cut it instead yields the uniform statement

```text
log|Delta_min(E_*)| >= 10*log B_cut-log(12582912).        (CF-shell)
```

Thus the quantitative discriminant-growth obstruction can be removed from a
**selected-direction, actual-height or dyadic-shell** version of AW. The old
certificate's fixed-direction flags are not rewritten or retroactively marked
true. The new proof supplies the selector and quantifier adapter explicitly.

Petsche, *Small rational points on elliptic curves over number fields*,
NYJM 12 (2006), Theorem 2, printed p.259, remains applicable to the selected
non-torsion point. The primary source was rechecked at
<https://nyjm.albany.edu/nyjm/j/2006/12-16.pdf>. If one also proved
`sigma(E_*)<=Sigma` and a uniform numerical bound
`hhat(P_*)<=C_up*log W+C0`, the remaining coefficient gate would be

```text
10/(10^15*Sigma^6*log^2(104613*Sigma^2)) > C_up.         (CF-win)
```

Neither auxiliary bound nor this strict win is proved here. In particular,
the exact discriminant records prime powers and does not control their
radical or the Szpiro ratio. No ABC/Szpiro conjecture is assumed.

## 7. Verification and bounded evidence contract

The companion verifier recomputes the general symbolic polynomial identities,
the invariant scaling, exact local-unit reductions, the positive-factor
inequalities, and the selector's primitive gcd proof obligations. It also runs
deterministic integer/rational regressions on:

- all unordered positive primitive triples with largest edge <=60 for (CF-1);
- all coprime opposite-parity pairs 1<=k<h<=500 for (CF-2)--(CF-5);
- nonempty primitive Euler-brick examples for the final selector bound;
- a scaled nonprimitive negative control, showing why primitive height matters.

The symbolic and written arguments establish the general lemma; the finite
panels only detect regressions. No perfect-cuboid search or UNKNOWN-based census
claim is made. Certificate dependencies use UTF-8/LF source commitments to
avoid platform-only CRLF hash drift. The checker verifies the locked parent
blobs and current source content separately from the new artifact digest.

## 8. Checkpoint and next single research obligation

```text
CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_ACTIVE_RECEIVER=SELECTED_PHYSICAL_MARKED_HEIGHT_COMPARISON_AFTER_CF_C2_STAR
CYCLE_LIVE_CANDIDATES=1
CYCLE_UNTESTED_CANDIDATES=0
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true
CYCLE_BLIND_REDISCOVERY=true
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false
CYCLE_NEW_VIEW=SOURCE_SELECTED_GLOBAL_MINIMAL_DISCRIMINANT_HEIGHT_ADAPTER
CYCLE_NEW_VIEW_SOURCE=INTERNAL_DERIVATION
```

The next single bounded obligation is a **selected physical marked-point local
height comparison preflight**: derive an explicit upper comparison under the
same selector and actual W; inspect whether source-marked local contributions
can give a lower comparison without an unproved uniform Szpiro bound. If that
does not give a coefficient win or a new invariant, freeze the precise blocker
and broaden again. Do not merely rerun the old Petsche/AW comparison, increase
local prime depth, or describe (CF-6) as an E1 sieve.

The six generated candidates were accounted for; no claim of exhausting all
possible E1 methods is made. This is a research checkpoint with a live next
obligation, not a parking declaration or automatic future-run authorization.

```text
EXPLICIT_SOURCE_FAMILY_GLOBAL_MINIMAL_MODEL=true
SELECTED_DIRECTION_DISCRIMINANT_HEIGHT_ADAPTER=true
FIXED_DIRECTION_AW_C2_DISCHARGED=false
EXPLICIT_MARKED_CANONICAL_HEIGHT_UPPER_CONSTANT=false
UNIFORM_SZPIRO_BOUND=false
STRICT_CANONICAL_HEIGHT_COEFFICIENT_WIN=false
FINITE_HEIGHT_REDUCTION=false
E1_proved=false
R29_PESCH_E1_closed=false
stage35_closed=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
HOSTILE_AUDIT_PASS=false
```

No merge. MAIN-STATE remains V74 / Goal4AK.
