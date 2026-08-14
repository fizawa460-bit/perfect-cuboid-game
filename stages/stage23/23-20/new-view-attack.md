# Stage23-20 — Stage17-slice attack ledger

This repair intentionally avoids re-running the Stage14/15 primary machinery. The new viewpoint is to start from the Stage17 Pythagorean chain and add the second-face condition there.

## 1. Stage17 chain coordinates

For the unique integral face write

\[
x^2+y^2=p^2,
\]

and for the already-integral space diagonal write

\[
p^2+z^2=d^2.
\]

Stage23 asks whether a second face, for example

\[
x^2+z^2=q^2
\]

or

\[
y^2+z^2=q^2,
\]

can occur along an infinite primitive Stage17 family.

This reverses the Stage14/15 order of attack: there the two-face geometry is built first and the space diagonal is imposed afterward; here the space diagonal is already solved and the second face is sliced into that solved family.

## 2. Explicit AR-039 source family

Use the audited Stage17 construction AR-039:

\[
x=m^2-n^2,\qquad y=2mn,\qquad p=m^2+n^2,
\]

\[
z=\frac{p^2-1}{2},\qquad d=\frac{p^2+1}{2},
\]

for coprime `m>n` in the frozen congruence class `m=2 mod 14`, `n=1 mod 14`.

The source family is already certified primitive after canonical sorting, exactly-one-face, with integral space diagonal and unbounded height.

## 3. Add the second face symbolically

For the `x-z` face,

\[
4(x^2+z^2)
=
\bigl(p^2+1-4mn\bigr)
\bigl(p^2+1+4mn\bigr).
\]

Equivalently,

\[
4q^2
=
\bigl(m^4+2m^2n^2+n^4-4mn+1\bigr)
\bigl(m^4+2m^2n^2+n^4+4mn+1\bigr).
\]

For the `y-z` face,

\[
4(y^2+z^2)
=
\bigl(p+1-2m\bigr)
\bigl(p+1+2m\bigr)
\bigl(p+1-2n\bigr)
\bigl(p+1+2n\bigr).
\]

Thus Stage23's extra face is converted into an explicit square-value problem on the already-solved Stage17 parameter space.

## 4. One-dimensional slice n=1

Take the genuine infinite AR-039 subfamily `n=1`, `m=t`, `t=2 mod 14`.

Then

\[
x=t^2-1,\qquad y=2t,\qquad p=t^2+1,
\]

\[
z=\frac{(t^2+1)^2-1}{2},\qquad d=\frac{(t^2+1)^2+1}{2}.
\]

The `x-z` square condition becomes

\[
(2q)^2
=
\bigl(t^4+2t^2-4t+2\bigr)
\bigl(t^4+2t^2+4t+2\bigr).
\]

This is a degree-8 hyperelliptic model. If the degree-8 polynomial is squarefree, its smooth projective model has genus 3.

The `y-z` square condition becomes

\[
(2q)^2=t^2(t^2+4)(t^2-2t+2)(t^2+2t+2).
\]

Removing the obvious square factor `t^2`,

\[
Q^2=(t^2+4)(t^2-2t+2)(t^2+2t+2),
\]

which is a degree-6 hyperelliptic model. If squarefree, its smooth projective model has genus 2.

Therefore this Stage17 slice does not collapse to an obvious genus-zero parametrization. It produces higher-genus square-value problems before any Stage14/15 squareclass machinery is invoked.

## 5. Integer test on the certified congruence slice

A direct exact-integer scan was performed on

```text
n=1
m=t=2 mod 14
2 <= t < 200000
```

for both added-face conditions.

Result:

```text
XZ_FACE_HITS=0
YZ_FACE_HITS=0
```

This is finite evidence only. It does not prove that either hyperelliptic curve has no admissible rational/integer points outside the tested range, and it is not a Stage19 nonexistence theorem.

## 6. What this attack establishes

The attack satisfies the controller's demand for a concrete nontrivial candidate family and an ordered test ledger:

```text
CANDIDATE_FAMILY=AR-039 with n=1, m=t=2 mod 14
POSITIVITY=PASS
STRICT_ORDERING=PASS_AFTER_EXISTING_AR039_CANONICAL_SORT
SPACE_DIAGONAL=PASS_IDENTICALLY
PRIMITIVITY=PASS_BY_EXISTING_AR039_CONTRACT
SOURCE_EXACTLY_ONE=PASS_BY_EXISTING_AR039_CONTRACT
HEIGHT_GROWTH=PASS_UNBOUNDED, d~t^4/2
SECOND_FACE_XZ=REDUCED_TO_GENUS3_HYPERELLIPTIC_SQUARE_VALUE_PROBLEM
SECOND_FACE_YZ=REDUCED_TO_GENUS2_HYPERELLIPTIC_SQUARE_VALUE_PROBLEM
EXACTLY_TWO=NOT_REACHED_ON_TESTED_SLICE_BECAUSE_NO_SECOND_FACE_HIT
INFINITE_STAGE19_FAMILY=NOT_FOUND
POSITIVE_POWER_LOWER_BOUND=NOT_FOUND
MATCHING_HALF_POWER_FAMILY=NOT_FOUND
FINITE_SCAN_RANGE=t<200000
FINITE_SCAN_USED_AS_PROOF=false
```

The family fails only at the new second-face gate on the tested slice; all Stage17 source requirements, primitivity and height growth are already live and explicit.

## 7. New-view classification

This is not a re-run of the Stage14/15 route. It yields a distinct Stage23-specific perspective:

```text
NEW_VIEW=STAGE17_FAMILY_SLICING
SOURCE_GEOMETRY=PYTHAGOREAN_CHAIN_ALREADY_SOLVING_SPACE_DIAGONAL
ADDED_CONDITION=SECOND_FACE_SQUARE
RESULTING_GEOMETRY=HIGHER_GENUS_HYPERELLIPTIC_SLICES_ON_AR039
OLD_STAGE14_15_PRIMARY_ROUTE_REUSED=false
```

A stronger theorem would require an actual rational-point analysis of these genus-2/genus-3 curves, or a different Stage17 family/slice that degenerates to genus 0 or genus 1. That is the next mathematically meaningful attack direction; the finite scan alone is not closure.
