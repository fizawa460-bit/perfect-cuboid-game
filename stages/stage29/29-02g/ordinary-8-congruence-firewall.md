# Stage29-02g — audited ordinary 8-congruence firewall and generic level-4 quotient

```text
ROLE=ORDINARY_8_CONGRUENCE_FIREWALL_PLUS_LEVEL4_GENERIC_QUOTIENT
STATUS=AUDITED_PASS_AFTER_BIRATIONAL_SCOPE_REPAIR
```

## 1. Ordinary 8-congruence is abundant

Fisher defines `Z(8,1)` as the moduli surface of symplectically 8-congruent elliptic-curve pairs, up to simultaneous quadratic twist, and works with it only up to birational equivalence. For `N=8, epsilon=1`, this surface is rational over Q; Corollary 1.3 gives infinitely many non-isogenous rational pairs.

Therefore

```text
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED_AUDITED
```

Bare existence of a symplectic 8-torsion isomorphism cannot be used as evidence that cuboid endpoint points are finite or absent.

## 2. Generic level-4 quotient

Over `K=Q(i)`, Testa--Stoll give

```text
Sbar_K ~= (X(8) x X(8))/Delta G0,
G0=ker(PSL2(Z/8)->PSL2(Z/4)),
|G0|=8,
|PSL2(Z/8)|=192,
PSL2(Z/4)~=S4.
```

Forgetting the retained level-4 structure corresponds at the generic moduli/function-field level to enlarging the diagonal group from `G0` to the full `PSL2(Z/8)`. Hence

```text
k((X x X)/Delta G0)
  /
k((X x X)/Delta PSL2(Z/8))
```

has generic degree

```text
[PSL2(Z/8):G0]=192/8=24
```

and generic residual group `S4` on the locus with trivial stabilizer.

The target is the ordinary symplectic 8-congruence moduli surface, birationally represented by Fisher's `Z(8,1)`.

```text
R29-MOD2=EndpointAsLevel4S4GenericQuotientOfOrdinarySymplectic8CongruenceSurface
R29_MOD2=DISCHARGED_GENERIC_BIRATIONAL_QUOTIENT
GENERIC_DEGREE=24
GENERIC_RESIDUAL_GROUP=S4
```

## 3. Scope repair

The audited statement is **not** an assertion that a fixed projective model of `Sbar_K` admits an everywhere finite degree-24 morphism to Fisher's chosen model of `Z(8,1)`. Fisher's surface is only specified birationally, and cusps / extra automorphisms / stabilizers can alter the special fibers.

Thus

```text
EVERYWHERE_FINITE_DEGREE24_COVER=false
R29-MOD2B=BranchCuspAndStabilizerLedgerForGenericDegree24Quotient
```

remains live.

## Interpretation

The contrast

```text
ordinary Z(8,1): rational / abundant rational pairs
endpoint Sbar: general type / retained level4 + Q-conjugation datum
```

locates any useful modular obstruction in the extra level-4 lift, its Q(i)/Q descent, special-locus conditions and physical-open restriction—not in ordinary 8-congruence itself.

```text
ENDPOINT_POINT_SET_COMPUTED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
