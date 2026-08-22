# Stage29-13 — fresh adversarial audit

```text
AUDITED_PR=1321
AUDITED_SUBMISSION_HEAD=da2a4154ccccafeb1295b0421e84e98dc5de7ea2
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
```

## Executive verdict

The two submitted family closures survive hostile reconstruction, with one scope repair on the second family. The StageA2 method firewall is respected. Papers C/D/E remain non-promoted for the reasons stated below. Fresh audit also finds a new theorem not present in the submission: because the audited Stage28 one-third lower bound is produced by an injective Saunderson subfamily and the newly certified Saunderson endpoint exclusion is pointwise on that entire nondegenerate family, the same explicit lower bound holds for `M3-P`.

No overall perfect-cuboid existence/nonexistence statement follows, `P/M3` remains unknown, and the eleven-route portfolio is unchanged.

## 1. StageA2 transfer firewall — PASS

StageA2 closed only the published equation-(6) `-18` family. Its closeout explicitly denies general coverage. Stage29-13 transfers only the method species

```text
source-locked low-dimensional receiver
 -> exact algebraic/squareclass/lift reduction
 -> explicit cover
 -> complete arithmetic closure
 -> reconstruction/boundary audit.
```

The StageA2 family-specific conclusion is not generalized.

## 2. R29-EXT-CHANG-A — Saunderson closure independently reconstructed

For

```text
Sa(u,v,w)=(u(4v^2-w^2), v(4u^2-w^2), 4uvw),
u^2+v^2=w^2,
```

direct expansion gives

```text
a^2+b^2+c^2=w^2(w^4+16u^2v^2).
```

With

```text
u=p^2-q^2, v=2pq, w=p^2+q^2, t=p/q,
```

the square-space condition gives exactly

```text
T^2=t^8+68t^6-122t^4+68t^2+1.
```

The palindromic quotient and the missing rational lift are both required:

```text
W=t+1/t,
S=T/t^2,
S^2=W^4+64W^2-256,
T0=t-1/t,
W^2-4=T0^2,
```

hence every nondegenerate candidate maps to

```text
C0: S^2=T0^4+72T0^2+16.
```

The elliptic identification was independently checked rather than accepted from the source. Scaling

```text
T0=2z, S=4y
```

gives

```text
y^2=z^4+18z^2+1.
```

Its binary-quartic Jacobian is

```text
Y^2=X(X-16)(X-20).
```

The rational change

```text
X=4(x+3), Y=8y
```

gives exactly

```text
y^2=(x+3)(x-1)(x-2)=x^3-7x+6,
```

Cremona `80a1` / LMFDB `80.a2`. The current database data agree with rank `0` and torsion `(Z/2)^2`, so the Jacobian has exactly four rational points. Since `C0` has a rational point, it is a trivial torsor under this Jacobian and therefore has exactly four rational points. The four visible points are

```text
(0,+4), (0,-4), infinity_+, infinity_-.
```

Reconstruction gives

```text
T0=0        -> t=+/-1 -> u=0,
T0=infinity -> t=0/infinity -> v=0,
```

so every point is degenerate.

```text
R29_EXT_CHANG_A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
SAUNDERSON_FAMILY_EXCLUSION_COMPLETE=true
```

The external source's historical sentence calling `(240,252,275)` the smallest Euler brick is false but non-load-bearing.

## 3. R29-EXT-CHANG-B — Pell/Lucas closure passes, taxonomy scope narrowed

For the explicit family

```text
B(q)=(4q,q^2-4,2(q^2-1)), q in Z_{>0},
```

direct expansion gives

```text
a^2+b^2=(q^2+4)^2,
a^2+c^2=(2(q^2+1))^2,
b^2+c^2=5q^4-16q^2+20,
a^2+b^2+c^2=5q^4+20.
```

Thus only two face diagonals are automatic; the stronger introductory sentence in the external paper is false. For any perfect cuboid in this family the necessary space condition gives, with `Y=q^2`,

```text
g^2-5Y^2=20.
```

It forces `5|g`; writing `g=5h` gives

```text
Y^2-5h^2=-4.
```

The positive solutions are exactly

```text
Y=L_{2n-1}, h=F_{2n-1}.
```

Cohn's square-Lucas theorem leaves only `L1=1` and `L3=4`. Since `Y=q^2`, one gets `q=1,2`, and both give degenerate/nonpositive edges. The family closure is therefore valid.

However, the external source calls this family the standard two-adic `Case B at p=1` stratum while also acknowledging that its surrounding taxonomy is not standard published literature. No repository adapter was found proving that this explicit family exhausts a globally defined two-adic stratum of all perfect-cuboid candidates. The audited disposition is therefore deliberately narrower:

```text
R29_EXT_CHANG_B=DISCHARGED_PELL_LUCAS_EXPLICIT_BQ_FAMILY_EXCLUSION
GLOBAL_TWO_ADIC_STRATUM_ADAPTER_CERTIFIED=false
```

This is a scope repair, not a mathematical failure of the Pell/Lucas exclusion.

## 4. Papers C and D — submitted dispositions confirmed

Paper C explicitly restricts its rank-positive computations to finite windows (`1<=n<=200` in rank one and `|a|,|b|<=12` in rank two) and explicitly states that an all-multiples closure is not proved. The missing input is an effective odd-multiplicity primitive-divisor theorem for the Face-3 numerator.

```text
R29_EXT_CHANG_C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY
```

Paper D proves structural information about the elliptic family (minimal models, conductor/discriminant/Szpiro behavior) and explicitly does not close a cuboid family. It also records the lack of a uniform Szpiro-free positive canonical-height lower bound.

```text
R29_EXT_CHANG_D=AMBER_HEIGHT_STRUCTURE_INPUT_NOT_ENDPOINT_DECISIVE
```

## 5. Paper E — attempted repair fails

The elliptic data are consistent with the current database:

```text
Eanom: y^2=x^3-275x+1750,
Cremona 800a3 / LMFDB 800.d2,
rank=1,
torsion=Z/2,
elliptic integral-point count=7.
```

But the external proof does not certify the claimed quartic closure. Its own `paper-e/scripts/04_height_completeness.gp` says the height-difference constant is sampled and explicitly states that a fully certified constant requires Cremona--Prickett--Siksek / Magma/Sage `IntegralPoints`-type machinery not supplied. The accompanying PARI script performs bounded Mordell--Weil and `ellratpoints` searches, not a complete Baker/elliptic-logarithm enumeration. No hidden Magma/Sage certificate was found in the committed `paper-e/scripts` tree.

Moreover the committed workflow uses `ellfromeqn` to identify the Jacobian but does not supply a load-bearing explicit birational map proving that every relevant integral quartic point maps into the enumerated integral points of `Eanom`, followed by a complete pullback/reconstruction ledger.

Therefore

```text
R29_EXT_CHANG_E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE
```

is retained.

## 6. Material positive repair — non-endpoint M3 lower theorem

Stage28-50-r2 already has an independent audited theorem on the same Saunderson construction. On the primitive opposite-parity cone

```text
1/8<=s/r<=4/5
```

the physical map is injective, `R<=8r^6`, and

```text
#C(T)=27/(20*pi^2)T^2+O(T log T).
```

Hence it proved

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}\ge\frac{27}{40\pi^2}.
\]

Every counted lower-family object is a nondegenerate primitive canonical Saunderson Euler brick. By the newly certified pointwise Saunderson endpoint exclusion, none lies in `P`. Therefore the exact same count lies in `M3-P`, giving the new Stage29 theorem

\[
\boxed{
\liminf_{B\to\infty}\frac{M_3(B)-P(B)}{B^{1/3}}
\ge\frac{27}{40\pi^2}>0.
}
\]

```text
R29_POP_SAUND_NONENDPOINT=DISCHARGED_EXPLICIT_NONENDPOINT_M3_LOWER
```

This does not imply `P/M3->0`, because the true growth scale of the full `M3` population remains unknown. It also does not repair a false Stage28 statement, so no targeted backflow is required.

## 7. Portfolio / ownership

The two certified family closures are new endpoint exclusions for thin explicit families and were not found as already closed by a stronger audited repository family theorem. They belong primarily to `J12-PARAMETRIC`; the new `M3-P` corollary is a secondary `J12-POP-INTERACTION` consumer. This does not create a twelfth route and does not produce duplicate primary attack credit.

The global Master-Hit route remains AMBER because `R29-PESCH-E1` is still conjectural. The population route remains the one existing GREEN route, now with an additional certified non-endpoint lower child.

```text
CERTIFIED_NEW_FAMILY_CLOSURE_COUNT_29_13=2
A2_STYLE_SUCCESSFUL_TRANSFER_COUNT=1
J12_PARAMETRIC=AMBER
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

## Final verdict

```text
AUDIT_REQUIRED=false
CHECKPOINT29_13_AUDIT=PASS
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
MATERIAL_POSITIVE_REPAIR=SAUNDERSON_NONENDPOINT_M3_LOWER_PLUS_CASE_B_TAXONOMY_SCOPE_NARROWING
R29_EXT_CHANG_A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
R29_EXT_CHANG_B=DISCHARGED_PELL_LUCAS_EXPLICIT_BQ_FAMILY_EXCLUSION
R29_EXT_CHANG_C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY
R29_EXT_CHANG_D=AMBER_HEIGHT_STRUCTURE_INPUT_NOT_ENDPOINT_DECISIVE
R29_EXT_CHANG_E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE
R29_POP_SAUND_NONENDPOINT=DISCHARGED_EXPLICIT_NONENDPOINT_M3_LOWER
CERTIFIED_NEW_FAMILY_CLOSURE_COUNT_29_13=2
A2_STYLE_SUCCESSFUL_TRANSFER_COUNT=1
J12_PARAMETRIC=AMBER
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-14_NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
