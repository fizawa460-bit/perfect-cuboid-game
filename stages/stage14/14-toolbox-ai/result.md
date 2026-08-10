# Stage14-toolbox-ai — compact torsion denominator and half-angle identities

## Purpose

Package the merged physical compact-torsion machinery into a reusable formula layer for Stage14 main/s.

Earlier toolbox stages already contain the generic witness denominator, Euclid/half-angle normalization, and physical variable dictionary. This stage closes the missing operational chain:

```text
physical elliptic point
 -> compact 2-torsion translate
 -> compact Kummer chamber
 -> physical conjugate/gap coordinate
 -> minus half-angle denominator
 -> complementary plus selector
 -> dual products Q,K
 -> third-face 2x2 gcd-cell routing.
```

No new Stage14 theorem is claimed.

## Canonical merged sources

```text
Stage14-s6-05 / PR #356 / merge c2273d0388b48f8fb51d9dc69d8977efbc83db37
Stage14-s6-06 / PR #360 / merge 42f4315b0659bd402a94adeb8822588ea153305a
Stage14-s6-07 / PR #364 / merge c51992e2373c0f7f265275c211684f6bd5ef9ccf
Stage14-4bl   / PR #365 / merge dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
```

Open PRs are not used as canonical theorem sources.

## Compact physical selector

For

```text
E_{S,X}: W^2=Z(Z-S^2)(Z+X^2),
```

a physical point has `Z>S^2`. Translation by `T0=(0,0)` is

```text
Z -> -S^2X^2/Z,
W -> S^2X^2W/Z^2,
```

and sends the point to `-X^2<Z<0`. The compact point is automatically nonzero modulo `2E(Q)`, preserves the height window and physical reconstruction, and lies in the forced `(--+)` sign chamber with only four physical tau packets.

## Physical conjugate and gap form

For

```text
g=gcd(S,S2),
G=g*d,
R-=H2-S2,
N-=H*G-S^2*H2-X^2*S2,
```

we have

```text
Z_-=-N-/R-.
```

With

```text
U=G-H*S2,
V=H*H2-G,
```

also

```text
Z_-=-U*V/X2^2.
```

The reduced denominator is exact:

```text
D_-^2=(H2-S2)/gcd(N-,H2-S2)
     =X2^2/gcd(X2^2,U*V).
```

## Dual half-angle selectors

Write

```text
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t,
kappa in {1,2}, gcd(s,t)=1.
```

Minus selector:

```text
D_-|t,
k_-=t/D_-,
gcd(N-,H2-S2)=kappa*k_-^2.
```

Plus selector from translation by `(-X^2,0)`:

```text
N+=H*G+X^2*S2-S^2*H2,
Z_+=-N+/(H2+S2),
D_+|s,
k_+=s/D_+,
gcd(N+,H2+S2)=kappa*k_+^2.
```

Define

```text
Q=D_+D_-,
K=k_+k_-.
```

Then exactly

```text
Q*K=X2/kappa,
K^2|N+N-.
```

## Good-odd gcd matrix

After the exact physical transfer to a third primitive face `F3`, let

```text
t2-,t2+,
t3-,t3+
```

be the two half-angle columns of `F2,F3`. On odd prime powers of `X2` coprime to `2H`, define

```text
q--, q-+, q+-, q++
```

as the four corresponding gcd cells. They are pairwise coprime and

```text
q--*q-+*q+-*q++=X2_good.
```

The selector dictionary is

```text
(D_-)_good=q-+,
(k_-)_good=q--,
(D_+)_good=q+-,
(k_+)_good=q++.
```

Thus physical root signs are deterministic divisor allocation, not independent Bernoulli conditions.

## New canonical cards

```text
TB-FORMULA-compact-t0-torsion-translation
TB-LEMMA-physical-compact-class-reduction
TB-FORMULA-physical-conjugate-gap-coordinate
TB-FORMULA-minus-half-angle-denominator
TB-FORMULA-dual-compact-half-angle-selectors
TB-FORMULA-dual-denominator-cancellation-product
TB-DICTIONARY-dual-selector-gcd-matrix
TB-RECIPE-compact-half-angle-prime-routing
TB-WARNING-compact-selector-quantifier-boundary
```

## Maintenance notes

- `D_T` from s6-05/s6-06 is the minus selector `D_-` once the dual notation is introduced.
- `D`, `D_min`, `D_-`, and `D_+` remain different objects.
- The current main whole-family exponent remains `20/21`; this toolbox stage does not alter the exponent ledger.
- The compact torsion translations on `E_{S,X}` must not be identified with the later s7 `j=1728` twist torsion/self-correspondence.

## Boundary

```text
STAGE14_TOOLBOX_AI=COMPLETE_COMPACT_TORSION_DENOMINATOR_AND_HALF_ANGLE_ATLAS
CANONICAL_NEW_CARD_COUNT=9
CANONICAL_TOTAL_CARD_COUNT=57
T0_COMPACT_TORSION_TRANSLATION_FROZEN=true
PHYSICAL_COMPACT_KUMMER_CLASS_REDUCTION_FROZEN=true
PHYSICAL_COMPACT_TAU_PACKET_COUNT=4
PHYSICAL_CONJUGATE_GAP_FORM_FROZEN=true
MINUS_HALF_ANGLE_DENOMINATOR_FROZEN=true
DUAL_COMPACT_HALF_ANGLE_SELECTORS_FROZEN=true
DUAL_PRODUCT_IDENTITY_QK_EQUAL_X2_OVER_KAPPA_FROZEN=true
GOOD_ODD_SELECTOR_GCD_MATRIX_FROZEN=true
ROOT_SIGN_INDEPENDENT_BERNOULLI_MODEL_ALLOWED=false
GENERIC_D_IDENTIFIED_WITH_COMPACT_SELECTOR=false
D_MIN_IDENTIFIED_WITH_DUAL_SELECTORS=false
CURRENT_WHOLE_FAMILY_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-aj quantifier-mismatch and invalid-shortcut warnings
```
