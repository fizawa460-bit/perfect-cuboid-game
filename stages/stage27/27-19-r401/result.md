# Stage27-19-r401 — Stage19 lower-bound reentry

```text
TASK_ID=Stage27-19-r401
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
ROUTE_LABEL=STAGE19_LOWER_FAMILY_ARCHAEOLOGY
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Purpose

Stage27 upper exploration has isolated several strict-sub-half reopen contracts but has not proved `mu<1/2`. This route re-enters the current Stage19 lower interface instead. Its first obligation is narrower than proving a new exponent: determine exactly why the known positive-power constructions stop at `1/4`, and state a quantitative crossing condition for any future lower family.

The authoritative current Stage19 receiver is

\[
N_2(B)\gg B^{1/4},
\qquad
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

The historical Stage19 constant floor is superseded; this route starts from the post-Stage25 quarter-power lower.

## 2. Known quarter-power families are internally saturated

The audited R501 construction has two-dimensional reduced rational-parameter count

\[
\#\Omega_{501}(T)\gg T^2,
\]

and homogeneous physical height degree eight. Stage25-r507 proves the primitive gcd is uniformly bounded and therefore proves the reverse bound as well:

\[
N_{R501}(B)=\Theta(B^{1/4}).
\]

The audited R502 construction has the same exponent ledger: `T^2` reduced parameters, primitive physical height of degree eight, uniformly bounded primitive gcd, bounded parameter multiplicity, and

\[
N_{R502}(B)=\Theta(B^{1/4}).
\]

Therefore re-estimating primitive gcds or taking a fixed finite union of these known degree-eight rational families cannot raise the polynomial exponent above `1/4`. This statement is scoped only to the audited R501/R502 lineages; it is not a claim that every possible Stage19 parametrization has this form.

## 3. Lower-family exponent calculus

Let a candidate Stage19 construction be indexed by a parameter set `Omega(T)` satisfying, after all physical filters required for a lower theorem,

\[
\#\Omega(T)\gg T^{\kappa-o(1)},
\]

and suppose every retained parameter gives primitive physical space height

\[
R\ll T^{h+o(1)}.
\]

Assume also that the map from retained parameters to primitive canonical exactly-two Stage19 objects has fibers `T^{o(1)}` and that discarded exceptional parameters cost only `T^{o(1)}` relative to the fixed-power count. Choosing `T=B^{1/h-o(1)}` yields

\[
\boxed{N_2(B)\gg B^{\kappa/h-o(1)}}.
\]

Thus the exact fixed-power progress gate is

\[
\boxed{\kappa/h>1/4.}
\]

For R501/R502, `(kappa,h)=(2,8)`, giving `2/8=1/4` exactly.

Two immediate special cases are:

- with quadratic parameter count `kappa=2`, one needs physical height degree `h<8`;
- with height degree `h=8`, one needs effective parameter-count exponent `kappa>2`.

More generally, if a future outer parameter thickens an R501/R502-type base count from `T^2` to `T^(2+lambda)` while increasing the physical height from `T^8` to `T^(8+q)`, then

\[
\frac{2+\lambda}{8+q}>\frac14
\iff
\boxed{4\lambda>q}.
\]

This is bookkeeping, not a proof that such an outer family exists.

## 4. Exact Stage19 master space receiver

Return to the exact Stage19 toric coordinates

\[
A=m^2r^2+n^2s^2,
\qquad
B=m^2s^2+n^2r^2,
\]

for which integral space diagonal is equivalent to `AB` being a square, equivalently `sf(A)=sf(B)`.

Set

\[
x=m/n,\qquad y=r/s.
\]

After division by `n^2s^2`,

\[
\frac{A}{n^2s^2}=x^2y^2+1,
\qquad
\frac{B}{n^2s^2}=x^2+y^2.
\]

For positive rational `A,B`, `AB` is a rational square if and only if `A/B` is a rational square. Hence there is a positive rational `z` such that

\[
\boxed{x^2y^2+1=z^2(x^2+y^2)}.
\]

This biquadratic rational-point surface is an exact receiver for the Stage19 **space-diagonal condition** in the two-face toric host. It does not by itself enforce every remaining physical filter: positivity/nondegeneracy, primitive/canonical normalization, parity/coprimality decorations, and exclusion of the third integral face must still be checked by any lower construction.

No dominant rational parametrization of this surface is claimed here.

## 5. What can actually beat one quarter

The current audited repository boundary from R505 is consistent with the calculus above. A lower improvement must supply at least one of the following theorem species:

1. **lower-height explicit family:** polynomially many Stage19 objects with effective `kappa/h>1/4`, for example `kappa=2,h<8`;
2. **genuinely thicker family:** an additional polynomial parameter direction whose count gain beats its added height cost, e.g. `4 lambda>q` in the coupled model above;
3. **moving-core / moving-fiber mass theorem:** a uniform theorem producing polynomially many rational points in the exact physical measure, with subpolynomial parameter-to-object fibers and the full Stage19 adapter;
4. another exact support theorem giving a polynomially large admissible set with primitive/canonical/exactly-two control.

Fixed finite collections of the already-audited quarter-power families cannot satisfy this gate merely by union.

## 6. Result of r401

This route does **not** improve the lower exponent yet. It does remove a false target: the known R501/R502 quarter-power lower is not weak because of an unexamined primitive-gcd loss. Within those audited families the exponent is genuinely saturated.

The new actionable object is the exact master receiver

\[
x^2y^2+1=z^2(x^2+y^2),
\]

together with the quantitative family gate `kappa/h>1/4`. A subsequent lower route should search this receiver for lower-height rational curves, polynomially many distinct leaves with controlled overlap, or a moving-core small-point theorem. None of those is asserted to exist in r401.

```text
R501_QUARTER_SATURATION_USED=true
R502_QUARTER_SATURATION_USED=true
FIXED_FINITE_UNION_OF_KNOWN_QUARTER_FAMILIES_UPGRADES_EXPONENT=false
LOWER_FAMILY_EXPONENT_CALCULUS_PROVED=true
LOWER_PROGRESS_GATE=kappa/h>1/4
R501_R502_LEDGER=kappa=2,h=8
COUPLED_OUTER_PARAMETER_GATE=4*lambda>q
MASTER_SPACE_RECEIVER_DERIVED=true
MASTER_SPACE_RECEIVER=x^2*y^2+1=z^2*(x^2+y^2)
MASTER_SURFACE_DOMINANT_RATIONAL_PARAMETRIZATION_PROVED=false
MOVING_CORE_POLYNOMIAL_MASS_THEOREM_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```