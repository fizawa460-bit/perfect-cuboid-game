# Stage29-13 external source audit — 2026 family/method inputs

```text
STATUS=AUDITED_AFTER_FRESH_ADVERSARIAL_RECONSTRUCTION
PRIMARY_EXTERNAL_REPOSITORY=https://github.com/weiqi-kids/perfect-cuboid-problem
SOURCE_SET_AUTHOR=Lightman Chang
SELF_HOSTED_SOURCE_SET=true
AUTOMATIC_THEOREM_IMPORT=false
```

The 2026 sources below are self-hosted preprints. Stage29 accepts a claim only after the load-bearing algebra/arithmetic/reconstruction chain is independently checked.

## Paper A — Saunderson

Primary source: `paper-a/paper.tex` (source-set blob recorded in the submission ledger).

Load-bearing chain independently checked:

```text
Sa(u,v,w)=(u(4v^2-w^2),v(4u^2-w^2),4uvw)
u^2+v^2=w^2

a^2+b^2+c^2=w^2(w^4+16u^2v^2)
```

With `u=p^2-q^2`, `v=2pq`, `w=p^2+q^2`, `t=p/q`:

```text
T^2=t^8+68t^6-122t^4+68t^2+1.
```

The rational lift omitted by the mere palindromic quotient is retained:

```text
W=t+1/t,
T0=t-1/t,
W^2-4=T0^2,
C0: S^2=T0^4+72T0^2+16.
```

The Jacobian was independently reconstructed. Scaling `T0=2z`, `S=4y` gives `y^2=z^4+18z^2+1`, whose Jacobian is `Y^2=X(X-16)(X-20)`. The rational change `X=4(x+3)`, `Y=8y` yields exactly

```text
y^2=x^3-7x+6,
```

Cremona `80a1` / LMFDB `80.a2`. Current database data agree with rank `0`, torsion `(Z/2)^2`. Since `C0` has a rational point, it is a trivial genus-one torsor and has four rational points, exactly `(0,+/-4)` and the two rational points at infinity. Reconstruction sends them only to `t=+/-1,0,infinity`, hence vanishing-edge inputs.

```text
R29-EXT-CHANG-A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
SAUNDERSON_FAMILY_EXCLUSION_COMPLETE=true
```

Source-quality warning: the introduction incorrectly calls `(240,252,275)` the smallest Euler brick. This statement is non-load-bearing.

## Paper B — explicit B(q) family

Primary source: `paper-b/paper.tex`.

For

```text
B(q)=(4q,q^2-4,2(q^2-1)), q in Z_{>0},
```

direct expansion verifies

```text
a^2+b^2=(q^2+4)^2,
a^2+c^2=(2(q^2+1))^2,
b^2+c^2=5q^4-16q^2+20,
a^2+b^2+c^2=5q^4+20.
```

Only two face conditions are automatic; a stronger introductory sentence in the source is false. The necessary space condition gives, with `Y=q^2`,

```text
g^2-5Y^2=20
5|g
g=5h
Y^2-5h^2=-4.
```

The positive solutions are `Y=L_(2n-1)`, `h=F_(2n-1)`. Cohn's square-Lucas theorem leaves only `Y=1,4`; therefore `q=1,2`, both degenerate/nonpositive.

The family closure is certified. The external name “Case B at p=1” is retained only as a source label: no repository adapter was found proving that this explicit family exhausts a globally defined two-adic stratum of all candidates.

```text
R29-EXT-CHANG-B=DISCHARGED_PELL_LUCAS_EXPLICIT_BQ_FAMILY_EXCLUSION
GLOBAL_TWO_ADIC_STRATUM_ADAPTER_CERTIFIED=false
```

The paper's genus-five Jacobian decomposition is unnecessary for this closure and is not imported.

## Paper C — rank-positive fibers

Direct source inspection confirms that the actual theorem is finite-window only:

```text
rank one: 1<=n<=200 with torsion translates
rank two: |a|,|b|<=12.
```

The all-multiples extension is explicitly not proved; the source identifies the missing input as effective primitive-divisor control for the Face-3 numerator with odd multiplicity.

```text
R29-EXT-CHANG-C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY
GLOBAL_FIBER_CLOSURE_CERTIFIED=false
```

## Paper D — Szpiro/height

Direct source inspection confirms a structural theorem package about the family `E_q`: minimal models, conductor/discriminant, multiplicative reduction, Szpiro behavior and the `Q(sqrt(2))` factorization. It explicitly makes no perfect-cuboid closure claim and records the absence of the uniform Szpiro-free canonical-height lower bound that would be needed for a simple global orbit closure.

```text
R29-EXT-CHANG-D=AMBER_HEIGHT_STRUCTURE_INPUT_NOT_ENDPOINT_DECISIVE
```

It remains eligible for a later Arsenal rematch.

## Paper E — Sophie--Germain prime subfamily claim

Primary source: `paper-e/paper.tex`; scripts under `paper-e/scripts/`.

The elliptic data are consistent with current databases:

```text
Eanom: y^2=x^3-275x+1750
Cremona 800a3 / LMFDB 800.d2
rank=1
torsion=Z/2
elliptic integral-point count=7.
```

However, the committed proof does not certify the claimed prime-family closure. The file `paper-e/scripts/04_height_completeness.gp` explicitly says its height-difference constant is sampled and that a fully rigorous constant/completeness certificate requires Cremona--Prickett--Siksek / Magma/Sage `IntegralPoints`-type machinery not supplied in the workflow. `03_integral_points.gp` performs bounded Mordell--Weil and `ellratpoints` searches, not a complete Baker/elliptic-logarithm enumeration.

No hidden Magma/Sage certificate was found in the committed script tree. The workflow also identifies the quartic Jacobian via `ellfromeqn` but does not give the required load-bearing explicit birational map proving the relevant quartic-integral -> elliptic-integral implication and complete pullback/reconstruction.

Therefore the source's statement “we take the seven points as complete” is not accepted as a proof.

```text
R29-EXT-CHANG-E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE
```

Repair contract:

```text
1. explicit quartic <-> elliptic birational maps;
2. proof of the required integrality implication;
3. complete IntegralPoints / elliptic-logarithm certificate;
4. exact pullback and cuboid reconstruction ledger.
```

## Population interaction discovered by audit

The audited Stage28-50-r2 lower theorem counts an injective primitive/canonical positive-density cone inside the same Saunderson family and proves

```text
liminf M3(B)/B^(1/3) >= 27/(40*pi^2).
```

Because Paper A's exclusion has now been independently certified pointwise on every nondegenerate Saunderson member, the entire counted cone lies in `M3-P`. Hence Stage29-13 also certifies

```text
R29-POP-SAUND-NONENDPOINT=DISCHARGED_EXPLICIT_NONENDPOINT_M3_LOWER
liminf (M3(B)-P(B))/B^(1/3) >= 27/(40*pi^2).
```

This does not imply `P/M3->0` and requires no Stage28 backflow.

## Final external import summary

```text
CERTIFIED_EXTERNAL_FAMILY_CLOSURES=2
  A Saunderson
  B explicit B(q) family

A2_STYLE_SUCCESSFUL_TRANSFER_COUNT=1
  A Saunderson

FINITE_ONLY=1
  C

STRUCTURAL_NONDECISIVE=1
  D

NOT_CERTIFIED_AS_WRITTEN=1
  E

NEW_PRIMARY_ROUTE_CREATED=false
GENERAL_PERFECT_CUBOID_NONEXISTENCE=false
```
