# Stage32 MB104 — `000707000f0f` e=2 research checkpoint — 2026-09-17

Status: **RETAINED RESEARCH CHECKPOINT / NO NEW MATHEMATICAL CREDIT / RESTART-SAFE**

Active leaf:

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP
```

This checkpoint records the exact research boundary reached after the retained conductor-pair receiver work. Its purpose is to prevent later `stage32mb-mainbatch` runs from repeating already-exhausted searches. It does not promote a theorem, receiver, effectivity, endpoint, or Perfect-Cuboid claim.

## 1. Canonical relative-sheet bit is already solved as a receiver

The retained conductor-pair quotient defines

```text
chi_ij := (r_i*r_j)/h,
chi_ij^2=1,
```

for conductor-identified normalization preimages over the residual etale double cover. It gives the exact dictionary

```text
chi_ij=+1 <=> same residual lift <=> [lambda_(p;i,j)]=0,
chi_ij=-1 <=> deck-twisted lift <=> [lambda_(p;i,j)]=[gamma_Q].
```

Thus the missing datum is **not** an absolute square-root label and is **not** a need for a tau-odd coordinate such as an absolute choice of `r_z` or `r_w`. The tau-even relative coordinate `chi_ij` is sufficient in principle.

Load-bearing retained source:

```text
GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-PAIR-INVOLUTION-QUOTIENT.md
blob ff? no — source-locked blob 3344d2f638b8f1373fc660202a5f3307dd30a51b
```

The remaining problem is pointwise evaluation of the actual conductor map

```text
CondPair(C) -> R_U x_U R_U
```

or an equivalent constraint strong enough to bound the weighted cut.

## 2. Downstairs invariant A1 branch data cannot evaluate `chi_ij`

For the local invariant model

```text
A=C[[p,q]],
sigma(p,q)=(-p,-q),
B=A^<sigma>=C[[x,y,z]]/(xz-y^2),
x=p^2, y=pq, z=q^2,
```

the complete downstairs branch germ determines only the unordered pair of product lifts. Two conductor preimages can still be glued by either the identity or the residual deck involution.

Therefore:

```text
exact invariant local branch equation + normalization
  is insufficient to determine
conductor residual-sheet transition.
```

Do not restart a search for an absolute sheet label in invariant tangent/local-branch data alone.

Load-bearing retained source:

```text
GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION.md
blob 7b749f361535031164904bd479fddd69ccc12929
```

## 3. `eta=0`, common-cover and `E[2]` compression are not yet a sign evaluation

The retained e=2 normalization lift and split residual base change give a global normalization-side section, but conductor identification compares trivializations at *distinct normalization preimages*. That comparison is the missing descent/gluing bit.

Existing Abel–Jacobi/common-`H`-cover work compresses the remaining ambiguity to an `E[2]` class (four possibilities), but common-cover existence alone does not select one class. The older relative-V4 odd-degree mechanism is not directly reusable here because the relevant projection degree is `28*l`, hence even.

A useful re-entry would require a concrete character-line divisor/trivialization comparison, not another abstract statement that the difference lies in `E[2]`.

## 4. Cusp-width shortcut remains rejected unless one exact equality is proved

The modular etale-correspondence/cusp-width route cannot be reactivated from the present data. Its required re-entry condition is

```text
f1^{-1}(Cusps) = f2^{-1}(Cusps).
```

The candidate product/Jacobian information controls line-bundle/divisor class data but does not presently prove equality of these effective supports. Do not reuse the cusp-width degree obstruction unless the displayed equality is source-locked.

## 5. Counting-only routes are not the next target

The present retained package has already pushed the following kinds of restrictions without closing the balanced e=2 survivor:

```text
allocation / Hodge-A1 energy,
mod-4 parity,
determinant one-bit,
raw/special-grid Bezout capacities,
ordinary delta bounds,
adaptive-jet dimension bounds,
formal pair-sign cocycle constraints.
```

Formal allocations can still reach the thin-shell/balanced boundary, so another rearrangement of these counts alone should not be treated as a fresh route without genuinely new geometric realizability input.

## 6. Highest-leverage next probe: Armstrong source-completeness

A separate conditional upper route uses the support-specific quotient

```text
X_H=(C8 x C8)/H_diag,
H=<s1,s2> ~= (Z/2)^2.
```

The retained Armstrong source adapter correctly applies the orbit-space theorem to the full fiber-product orbifold/deck group on the simply connected universal cover, not merely to the finite group acting on `C8 x C8`.

For one factor the orbifold presentation has eight order-two branch generators: four of inertia `s1`, four of inertia `s2`. The source adapter reduces fixed elements relevant to abelianization to

```text
2 inertia types
* 4 branch generators
* 4 branch generators
* 4 relative H-cosets
= 128
```

representative fixed-element relations.

The associated integer computation has previously reduced the candidate `H_1` calculation to an exact finite relation matrix and an explicit unimodular minor. The **remaining load-bearing question is source-completeness**, not another numerical rank calculation:

```text
Are those 128 representatives exhaustive for the normal subgroup generated
by all fixed-point elements, at the level needed for the abelianization/H1 computation?
```

Source adapter:

```text
ARMSTRONG-FIBER-PRODUCT-H1-SOURCE-NOTE.md
blob ff1581420337745b1718a0b55b2d8049244277de
```

### Required next work

1. Verify the torsion/fixed-point classification in the fiber product `F=Delta x_H Delta`.
2. Verify that changing conjugators by kernel elements and simultaneous `H`-cosets gives exactly the asserted relative-coset reduction.
3. Verify that the 128 listed representative relations normally generate every fixed-point relation needed after abelianization.
4. Only after (1)–(3), replay/check the exact relation matrix and unimodular minor and decide whether the candidate `H_1(X_H,Z)=0` statement can be promoted under the Stage32 credit/audit rules.
5. If that promotion is valid, revisit the conditional downstream product/Jacobian chain (`Gamma ~ tau Gamma`, diagonal-translation invariance, Rosati-zero correspondence, external-product divisor) without importing any conclusion automatically.
6. If source-completeness fails or cannot be proved, return directly to conductor descent/gluing via normalization-preimage character-line trivializations. Do **not** fall back to the exhausted counting-only routes.

## 7. Firewalls

- No conductor pair is assigned `chi_ij=+1` or `-1` here.
- No conductor loop is assigned `0` or `gamma_Q` here beyond the already-retained exact converse conditional on `chi_ij`.
- No `H_1(X_H,Z)=0` promotion is made by this checkpoint.
- The Armstrong 128-relation completeness remains a research obligation.
- No weighted-cut upper bound below `84*l^2` is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
