# Stage28-60-r2 — geometric meaning of the log-squared normalizer

```text
ROUTE=R17_GEOMETRIC_LOG2_NORMALIZER
STATUS=CAUSAL_EXPLANATION_WITH_FIREWALL
```

The new interaction-curvature theorem contains the normalizing factor `(log B)^2` because

\[
\frac{M_2}{N_1}
\sim \frac{24\pi C_{M_2}}{\kappa}(\log B)^2.
\]

This ratio already has an audited geometric interpretation in `S25-W06`.

The Manin ledgers are

```text
N1_MANIN_INVARIANTS=(1,4)
M2_MANIN_INVARIANTS=(1,6)
```

so the two populations have the same polynomial `a=1` order while the target has a `b`-invariant larger by two.  At the theorem interface this is exactly the relative `(log B)^2` factor between `M2` and `N1`.

Hence the critical scale

\[
\mathcal I_{face}/\mathcal I_{sp}\asymp (\log B)^{-2}
\]

is not an arbitrary normalization invented at Stage28.  It is the already-certified intermediate-population log gap between `N1` and `M2`.

This gives a useful causal interpretation of the bridge identity:

```text
M3/N2
= relative face-vs-space interaction
  x known N1-to-M2 intermediate-population compensation.
```

However this is a bookkeeping/geometry explanation, not an independent probability factor.  The `(log B)^2` compensation is already contained in `M2/N1` and must not be charged again.

There is also a strict boundary on the geometric interpretation.  `S25-W06` explicitly forbids extending the toric Manin `(a,b)` subtraction through the Stage20 K3 cover as a fake Picard-rank calculation.  Therefore Stage28 may use the `N1 -> M2` `(1,4)->(1,6)` ledger to explain the normalizer, but it may not infer a value of `I_face`, `I_sp`, `K_28`, or `M3/N2` from a K3 Picard-rank difference.

```text
LOG2_NORMALIZER_HAS_AUDITED_GEOMETRIC_ORIGIN=true
GEOMETRIC_ORIGIN=N1_TO_M2_B_INVARIANT_GAP_4_TO_6
LOG2_CHARGED_AS_NEW_INDEPENDENT_FACTOR=false
K3_PICARD_SUBTRACTION_FORBIDDEN=true
BRANCH_PROFILE_COMPARISON_STILL_REQUIRED=true
AUDIT_REQUIRED=true
```