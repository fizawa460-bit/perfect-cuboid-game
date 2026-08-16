# Stage27-40ad — fixed-U subpolynomial class-averaging attack

```text
TASK_ID=Stage27-40ad
OWNER_STAGE=Stage27
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_ONLY
ROUTE_LABEL=T_SUBPOLY_CLASS_AVERAGING
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## Target

Stage27-40ab left one possible T-side escape hatch: replace the unavailable pointwise super-Kai theorem by an averaged theorem plus a chargeable physical pushforward bound. This task asks whether averaging over the **ordinary Gaussian residue / projective-class labels already present inside one fixed-U Stage14 packet** can supply that fixed-power charge.

The answer is no: the exact frozen class universe is only subpolynomial.

## 1. Exact fixed-U class universe

Stage14-t135 freezes

```text
R_d=(Z[i]/dZ[i])^x,
H_d=image((Z/dZ)^x),
h_d=|H_d|,
```

and explicitly records `h_d=B^o(1)`. The same terminal T chain retains `d=B^o(1)`. Hence

\[
|R_d|\le d^2=B^{o(1)},
\]

and every projective/residue label family obtained from `R_d`, `H_d`, or `G(d)` also has cardinality `B^o(1)`.

Thus the number of ordinary Gaussian residue classes available for an averaged theorem at one fixed-U packet is not polynomial in `B`.

## 2. Why a fixed-power exceptional-class fraction collapses to pointwise

Let `C_U` be any such fixed-U target-class family, so

\[
|C_U|=B^{o(1)}.
\]

Suppose an averaged theorem claimed an exceptional family `E_U` with a genuine fixed-power class-count saving

\[
|E_U|\le B^{-\eta+o(1)}|C_U|
\]

for some fixed `eta>0`.

Because `|C_U|=B^{o(1)}`, the right-hand side tends to zero. Since `|E_U|` is an integer, for all sufficiently large `B` one has

\[
|E_U|=0.
\]

So a **fixed-power exceptional fraction over this subpolynomial fixed-U class universe is asymptotically equivalent to a uniform pointwise theorem on every class**. It is not an intermediate averaged substitute for the missing Stage14-t157/tH33 individual-residue theorem.

## 3. Collision energy does not rescue fixed-U averaging

Stage27-40ab introduced the physical class weight

\[
w(c)=\#\{p\in P:\pi(p)=c\}
\]

and the sufficient energy condition

\[
\sum_c w(c)^2\le B^{o(1)}\frac{(\sum_c w(c))^2}{|C_U|}.
\]

Even if this optimal anti-concentration bound were proved, the denominator `|C_U|=B^o(1)` yields only a subpolynomial gain. It cannot by itself create the fixed `B^{-delta}` deficit needed to cross the half-power host.

This is distinct from Stage27-40aa's witness-moment closure: here the second moment is taken on the **target-class pushforward**, not on reciprocal-witness multiplicity. The obstruction is instead the subpolynomial size of the class space.

## 4. Exact surviving averaged-theorem gate

Therefore an averaged T-route can still matter only if its averaging variable ranges over a genuinely polynomial-size **outer physical family**, before or across the fixed-U localization, and the theorem is weighted in that physical measure strongly enough to survive the Stage14 capacity ledger.

A legal reopen must provide both:

1. an outer label/packet family `A(B)` with `|A(B)|>=B^{kappa-o(1)}` for some fixed `kappa>0` on the relevant critical-wall mass; and
2. a weighted exceptional-preimage or mean-square theorem across that actual outer family giving a fixed-power deficit after all localization multiplicities are charged.

Averaging only over `beta mod d`, projective classes, `H_d`, `G(d)`, or other fixed-U residue labels is closed as a standalone fixed-power mechanism.

## Outcome

This route removes one ambiguity left by 40ab: ordinary class averaging inside the frozen fixed-U modulus cannot be the missing adapter unless it is already strong enough to become pointwise. Any future averaged rescue must move to a polynomial-size outer physical parameter family and carry the true packet weights.

```text
T_FIXED_U_CLASS_AVERAGING_ATTACK_EXECUTED=true
FIXED_U_CLASS_UNIVERSE_SUBPOLYNOMIAL=true
FIXED_POWER_EXCEPTION_FRACTION_IMPLIES_EVENTUAL_ZERO_EXCEPTIONS=true
FIXED_U_CLASS_ENERGY_GAIN_FIXED_POWER=false
T_AVERAGED_ROUTE_REQUIRES_POLYNOMIAL_OUTER_PHYSICAL_FAMILY=true
OUTER_PHYSICAL_WEIGHTED_AVERAGING_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=Stage27-audit
```
