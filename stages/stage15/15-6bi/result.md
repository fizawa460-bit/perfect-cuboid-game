# Stage15-6bi — complementary Gaussian-product square receiver

Base: Stage15-6bh. This is an exact algebra stage.

Write the odd common norm core as `k^circ=k_S*k_O` using the Stage15-6aa same/opposite Gaussian-orientation split, and put `delta=2^eta` for the finite 2-primary decoration.

Choose the Gaussian core of `alpha_0` primewise as in 6aa. For an odd S-channel prime the same Gaussian prime occurs in both cores; for an O-channel prime conjugate primes occur. Therefore, up to units,

\[
K_\alpha K_\beta
=\delta k_O H_S^2,
\qquad N(H_S)=k_S,
\]

and

\[
K_\alpha\overline{K_\beta}
=\delta k_S H_O^2,
\qquad N(H_O)=k_O.
\]

Since `alpha_0=K_alpha z^2`, `beta_0=K_beta w^2`, we obtain the exact two-product receiver

\[
\boxed{\alpha_0\beta_0=\varepsilon_O\,\delta k_O\,\Xi_O^2},
\qquad \Xi_O=H_Szw,
\]

\[
\boxed{\alpha_0\overline{\beta_0}=\varepsilon_S\,\delta k_S\,\Xi_S^2},
\qquad \Xi_S=H_Oz\overline w.
\]

Both products have norm

\[
N(\alpha_0)N(\beta_0)=S^2,
\qquad S=kN(z)N(w),
\]

hence

\[
\boxed{S=\delta k_O N(\Xi_O)=\delta k_S N(\Xi_S).}
\]

If `alpha_0=x+iy`, `beta_0=p+iq`, the two Gaussian products are

\[
\alpha_0\beta_0=(xp-yq)+i(xq+yp),
\]

\[
\alpha_0\overline{\beta_0}=(xp+yq)+i(yp-xq).
\]

Thus every physical survivor produces two integral Pythagorean triples with the same hypotenuse `S`, carrying complementary S/O squarefree cores.

The endpoint inversion is exact:

\[
2xp=(xp+yq)+(xp-yq),
\quad 2yq=(xp+yq)-(xp-yq),
\]

\[
2yp=(xq+yp)+(yp-xq),
\quad 2xq=(xq+yp)-(yp-xq).
\]

No saving is claimed yet.

```text
STAGE15_6_SUBSTAGE=6bi
STAGE15_6BI_AUDIT_VERDICT=PASS
STAGE15_6BI_COMPLEMENTARY_GAUSSIAN_PRODUCTS=true
STAGE15_6BI_EQUAL_HYPOTENUSE_S=true
STAGE15_6BI_ENDPOINT_INVERSION_EXACT=true
STAGE15_6BI_SUPPORT_SAVING_PROVED=false
STAGE15_6BI_EXIT=EQUAL_HYPOTENUSE_DOUBLE_SQUARE_AUDIT_READY
```
