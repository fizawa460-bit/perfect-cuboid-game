# Stage29-04 — population host, predicate masks, and condition-cost matrix

```text
TASK_ID=Stage29-04
ROLE=POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
STATUS=AUDITED_PASS_PENDING_MERGE
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
ROADMAP_REVISION=R2_POST_29_02_FOUNDATION_SCREEN_AUDITED
OLD_STAGE_REENTRY_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact common physical host

Let

\[
\mathcal U(B)=\{(a,b,c)\in\mathbf Z_{>0}^3:0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B\}.
\]

Define four exact predicates on every object of `U(B)`:

```text
F_ab = [a^2+b^2 is an integer square]
F_ac = [a^2+c^2 is an integer square]
F_bc = [b^2+c^2 is an integer square]
S    = [R is an integer]
```

There are `2^4=16` **formal Boolean masks**. For each truth assignment define the corresponding labeled fiber in `U(B)`. These fibers are pairwise disjoint and their union is exactly `U(B)`.

Important audit repair: this does **not** assert that all 16 fibers are nonempty. In particular the perfect-cuboid mask is empty for every certified finite cutoff through `10^9`, and global nonemptiness is unknown.

```text
FORMAL_BOOLEAN_MASK_COUNT=16
PAIRWISE_DISJOINT_LABELED_FIBERS=true
UNION_EQUALS_U=true
EMPTY_MASKS_ALLOWED=true
NONEMPTY_BOOLEAN_FIBER_COUNT_CERTIFIED=false
```

## 2. Stage16–20 populations inside the Boolean host

Let

```text
f=F_ab+F_ac+F_bc
E_k={f=k}
E_k^S={f=k and S=1}.
```

Object-for-object under the same primitive/canonical `R<=B` convention,

```text
E1   = M1
E1^S = N1
E2   = M2
E2^S = N2
E3   = M3
E3^S = P.
```

Thus

\[
M_1=(E_1\cap\{S=0\})\sqcup N_1,
\]
\[
M_2=(E_2\cap\{S=0\})\sqcup N_2,
\]
\[
M_3=(E_3\cap\{S=0\})\sqcup P.
\]

The last identity uses no global `P=0` assumption. Stage20 imposes no space-diagonal condition, so a hypothetical perfect cuboid is contained in `M3`.

The `E0` fibers remain part of the exhaustive physical host but are not Stage16–20 target populations.

## 3. Legal nested face-condition ladder

The exact-face strata `M1,M2,M3` are disjoint. They are not an objectwise chain.

The correct nested hosts are

\[
H_{\ge1}=M_1\sqcup M_2\sqcup M_3,
\]
\[
H_{\ge2}=M_2\sqcup M_3,
\]
\[
H_{\ge3}=M_3,
\]

so

\[
H_{\ge3}\subset H_{\ge2}\subset H_{\ge1}\subset U.
\]

Space intersections are

\[
S\cap H_{\ge1}=N_1\sqcup N_2\sqcup P,
\]
\[
S\cap H_{\ge2}=N_2\sqcup P,
\]
\[
S\cap H_{\ge3}=P.
\]

Hence the literal subset ratios are

```text
N1/M1
N2/M2
P/M3
H_ge1/U
H_ge2/H_ge1
H_ge3/H_ge2.
```

The following are matched population-size ratios but are not literal objectwise survival probabilities:

```text
M2/M1
M3/M2
N2/N1
M3/N2.
```

## 4. Current certified theorem surface

Fresh provenance checks retain

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\]

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\]

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge\frac{27}{40\pi^2}>0,
\]

and for every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

For the endpoint,

```text
P(B)=0 for every B<=10^9       # exact finite census
P(B)=0 globally                # NOT PROVED
```

Stage19 also independently proves `N2/M2 -> 0` by its same-measure fixed-finite-set split-prime parity sieve. That theorem species is not multiplied with the separate half-power upper theorem.

## 5. Condition-cost matrix

Because `M2=o(M1)` and `M3=o(M2)`,

\[
H_{\ge1}\sim M_1,
\qquad
H_{\ge2}\sim M_2.
\]

Therefore

\[
\boxed{
\frac{H_{\ge1}}{U}
\sim
\frac{27\zeta(3)}{\pi^3}\frac{\log B}{B}
}
\]

and

\[
\boxed{
\frac{H_{\ge2}}{H_{\ge1}}
\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}.
}
\]

For the third face define

\[
\Phi(B)=\frac{M_3(B)}{M_2(B)+M_3(B)}.
\]

Then

\[
\Phi(B)\to0.
\]

Using the current Stage28 positive-liminf lower theorem rather than the older epsilon-weakened Stage26 form gives

\[
\boxed{
\Phi(B)\gg B^{-2/3}(\log B)^{-5}.
}
\]

For every fixed `0<delta<1/46`, choose `eta` with `delta<eta<1/46`; the upper theorem gives

\[
\boxed{
\Phi(B)=o((\log B)^{-\delta}).
}
\]

The true scale remains unknown.

For the space diagonal after exactly one face,

\[
\boxed{
\frac{N_1}{M_1}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
}
\]

For exactly two faces,

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
\frac{N_2}{M_2}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5},
}
\]

and independently `N2/M2 -> 0`.

For all three faces,

\[
\frac{P(B)}{M_3(B)}
\]

is the literal endpoint survival ratio and its global scale is unknown.

## 6. Exact pointwise bridge to the F7 sign/Kummer squareclasses

The submission correctly separated the physical Boolean `16` from the generic F7 degree `64`, but fresh audit finds an exact pointwise crosswalk already available from the **same F7 map**.

The audited F7 base map is

\[
[x:y:z]=[a^2:b^2:c^2].
\]

On the physical chart `x=a^2!=0`, take the six projective Kummer ratios

\[
\frac yx,\ \frac zx,\ \frac{x+y}{x},\ \frac{x+z}{x},\ \frac{y+z}{x},\ \frac{x+y+z}{x}.
\]

At a physical integer-edge point,

```text
y/x = (b/a)^2             always a Q-square
z/x = (c/a)^2             always a Q-square
(x+y)/x is Q-square       iff F_ab
(x+z)/x is Q-square       iff F_ac
(y+z)/x is Q-square       iff F_bc
(x+y+z)/x is Q-square     iff S.
```

For an integer, being a square in `Q` is equivalent to being an integer square, so there is no rational/integral gap.

Thus

```text
R29-KUM4A=DISCHARGED_POINTWISE_PHYSICAL_TO_F7_COORDINATE_SQUARECLASS_CROSSWALK
```

and the four physical predicates are exactly the triviality tests of the four nontrivial-coordinate candidates after the two edge-ratio squareclasses have become automatically trivial on the physical square-base locus.

## 7. Why 16 still does not equal 64

The preceding exact crosswalk does **not** identify 16 Boolean masks with 16 sheets or 16 fixed subcovers.

A failed predicate means that the corresponding element of `Q*/Q*^2` is nontrivial, but that nontrivial squareclass varies with the point. There is not one universal binary "NO squareclass". Also the generic F7 cover has six independent projective square-root directions and degree 64.

Therefore

```text
BOOLEAN_16_EQUALS_SIGN_COVER_64=false
BOOLEAN_MASKS_ARE_SIGN_SHEETS=false
POINTWISE_KUMMER_SQUARECLASS_CROSSWALK=true
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=false
```

The original receiver is split:

```text
R29-KUM4A = DONE
  PhysicalPredicateToF7CoordinateSquareclassCrosswalk

R29-KUM4B = OPEN
  PhysicalPopulationToSubcoverCountAdapter
```

`R29-KUM4B` must still control

```text
common algebraic host
YES-subcover versus NO-complement semantics
map direction
rational-lift/sign multiplicity
physical R-height
primitivity
canonical ordering
population multiplicity.
```

This is the correct 29-07 target.

## 8. Backflow verdict

The new pointwise crosswalk is Stage29 synthesis and does not alter a frozen Stage16–28 theorem statement.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
OLD_STAGE_CONTRACT_REPAIR_PROVED_NECESSARY=false
```

A later targeted addendum remains allowed only if 29-07 proves that an old certified contract itself must be extended or corrected.

## 9. Handoff to 29-05

29-05 should use the exact host/mask and Kummer-squareclass vocabulary to deduplicate mechanisms and assign one canonical route owner per receiver.

Priority duplicate checks include

```text
face predicate vs Pythagorean-parametrization language
space predicate vs squareclass/Gaussian-norm language
third-face predicate vs K3 double-cover/local-blocker language
joint completion vs V4/cross-character language
physical four-predicate squareclass mask vs F7 coordinate Kummer language.
```

```text
CHECKPOINT29_04_AUDIT=PASS
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
BOUNDED_REPAIR=BOOLEAN_NONEMPTY_SCOPE_PLUS_POINTWISE_F7_CROSSWALK_PLUS_KUM4_SPLIT_PLUS_CURRENT_M3_LOWER_CORRIDOR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
