# Stage25-60 R504 Prym/isogeny residual

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

After exact symbolic closure of the full Q-rational extra-involution locus for the normalized generic degree-two family, the only remaining degree-two rank-jump mechanism is a non-bielliptic elliptic factor of the Prym surface of
\[
C_{a,b}\to E_0.
\]

The normalized family is
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1},
\qquad
C_{a,b}: y^2=(a u^2+b)^4+(u^2+1)^4.
\]

The inherited involution gives one `E0` factor. A new independent section requires the dimension-two Prym to admit an elliptic factor Q-isogenous to `E0`.

```text
R504_PRYM_DIMENSION=2
R504_PRYM_TARGET_FACTOR=E0:y^2=x^3-4x
R504_PRYM_E0_FACTOR_LOCUS=OPEN
R504_EXTRA_INVOLUTION_LOCUS=CLOSED
```

The next attack is not another involution ansatz. It must use one of:

1. a Humbert/split-Jacobian invariant for the Prym surface;
2. an explicit degree >=3 map `C_(a,b) -> E0`;
3. a direct endomorphism/isogeny criterion for the Prym in terms of `(a,b)`.

A useful stopping certificate would be either:

- an exact algebraic equation for the Prym-E0 isogeny locus and proof that it has no rational component yielding a Stage19 family; or
- a proof that handling this locus needs a genuinely new external Prym/Humbert theorem not already present in the repository.

No deep-stop claim is made here.
