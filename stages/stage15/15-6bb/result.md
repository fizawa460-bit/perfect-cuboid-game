# Stage15-6bb — minimal rational reciprocal descent normal form

Base: Stage15-6ba. Audit/progress verdict: `PASS` for the exact minimal receiver; no new saving is claimed.

Stage15-6ao gives the unique coordinate squareclass split

\[
f=\kappa_f c^2,\qquad g=\kappa_g e^2,
\qquad (c,e)=1,
\qquad \kappa_f\kappa_g=\kappa,
\]

so `T=ce`. Substituting into the complete descent coordinates yields

\[
V_++V_- = \frac{2\kappa_f c}{\lambda e},
\qquad
V_+-V_- = \frac{2\kappa_g e}{\lambda c}.
\]

Hence

\[
\boxed{(V_++V_-)(V_+-V_-)=\frac{4\kappa}{\lambda^2}.}
\]

The moving denominator from 6ba is therefore exactly one primitive rational ratio `c/e`; it is not an unstructured extra variable.

The remaining norm condition is

\[
\boxed{\kappa_f^2c^4+\kappa_g^2e^4=kZ^2.}
\]

This is precisely the degree-four genus-one quartic already counted pointwise in Stage15-6ao. Thus the rational-ratio support has been reduced to the already-certified quartic receiver, not to a new divisor-many reconstruction.

In particular, applying AR-010 again as a fresh saving would double count the same reconstruction information already consumed in the 6ad--6ao chain.

## Frozen exit

```text
STAGE15_6_SUBSTAGE=6bb
STAGE15_6BB_AUDIT_VERDICT=PASS
STAGE15_6BB_MINIMAL_RATIONAL_RATIO=c/e
STAGE15_6BB_RECIPROCAL_PRODUCT=4*kappa/lambda^2
STAGE15_6BB_REMAINING_QUARTIC=kappa_f^2*c^4+kappa_g^2*e^4=k*Z^2
STAGE15_6BB_NEW_AR010_SAVING=false
STAGE15_6BB_POINTWISE_QUARTIC_COUNT_ALREADY_AVAILABLE=true
STAGE15_6BB_EXIT=GLOBAL_TWIST_PACKET_SECOND_MOMENT_AUDIT
```
