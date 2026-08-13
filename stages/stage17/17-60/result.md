# Stage17-60 - causal decomposition

Status: SUBMITTED_FOR_FRESH_AUDIT

Stage16 and Stage17 have the same primitive/canonical exactly-one population and `R<=B` cutoff. Stage17 adds only integral `R`.

Write the unique integral face as `x^2+y^2=p^2`. For the complementary edge `z`, Stage17 is exactly the extra condition

`p^2+z^2=d^2`.

So the new structural restriction is a second Pythagorean triangle sharing the face diagonal `p`. The complementary edge must extend `p` to an integral right triangle.

The audited laws give

`M_1(B) asymp B^2 log B`,

`N_1(B) ~ (kappa/(24*pi)) B(log B)^3`,

hence

`N_1(B)/M_1(B) asymp (log B)^2/B -> 0`.

Thus the net proved cost is one power of `B`, with `(log B)^2` compensation. The two logarithms are not declared independent probabilities.

Canonical ordering, primitivity, exactly-one multiplicity, and `R<=B` are already charged in Stage16. The adapter `d=R` is an identity. Stage13 also proves extra-face overlaps are lower order, so exactly-one subtraction is not the leading cause.

AR-039 is an explicit survivor family, not the mechanism for the full asymptotic. Intrinsic-versus-interaction classification is deferred to Stage21 with the Stage16S baseline.

```text
STRUCTURAL_MECHANISM=second Pythagorean extension sharing p
CERTIFIED_SURVIVAL=Theta((log B)^2/B)
POLYNOMIAL_COST=one power of B
EXACT_ONE_OVERLAP_IS_LEADING_CAUSE=false
CUTOFF_ADAPTER_CAUSE=false
INTRINSIC_STATUS=DEFER_TO_STAGE21_WITH_STAGE16S
EVIDENCE_LEVEL=PROVED
```

Checkpoint 70 remains blocked pending fresh Stage17-audit.
