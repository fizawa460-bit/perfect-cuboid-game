# Stage15-6cz — exact survivor equations in cross-gcd cells

Base: merged Stage15-6cy with fresh audit PASS. This executes the selected route `EXACT_SURVIVOR_RECONSTRUCTION_IN_CELL_NORMALIZED_ROOT_RATIOS`.

Keep
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\qquad H=abcd,
\qquad HMNUV\le B,
\]
with pairwise-coprime cross-gcd cells and `(q,H)=1` for every legal switched odd channel modulus.

Put
\[
X=abM,\quad Y=cdN,\quad Z=acU,\quad W=bdV.
\]
Then `X=m,Y=n,Z=r,W=s`. From `h_alpha=bc` and `h_beta=ad`, the primitive Gaussian coordinates are exactly
\[
\alpha_0=\frac{mr+i ns}{h_\alpha}
=a^2MU+i\,d^2NV,
\]
\[
\beta_0=\frac{ms+i nr}{h_\beta}
=b^2MV+i\,c^2NU.
\]
Hence
\[
A_0=N(\alpha_0)=a^4M^2U^2+d^4N^2V^2,
\]
\[
B_0=N(\beta_0)=b^4M^2V^2+c^4N^2U^2.
\]
The exact integral-space-diagonal survivor condition is
\[
\boxed{\operatorname{sf}(A_0)=\operatorname{sf}(B_0)=k,}
\]
equivalently
\[
\boxed{A_0=kP^2,\qquad B_0=kQ^2}
\]
for one squarefree `k` and positive integers `P,Q`.

The earlier two-channel determinant lock now gives a reconstruction fact that is invisible in the bare quartic. Every odd prime of `k` lies in exactly one channel, so
\[
k_S\mid X^2+Y^2,\qquad k_O\mid X^2-Y^2,
\]
and therefore
\[
\boxed{k^\circ=k_Sk_O\mid |X^4-Y^4|.}
\]
Because `X>Y>0` in the physical toric chamber, the right-hand side is nonzero. The 2-primary part of `k` has only the already-isolated bounded choices. Thus for fixed cells and fixed `(M,N)` the number of possible common squarefree cores is
\[
\#\{k\}\ll \tau(|X^4-Y^4|)B^{o(1)}=B^{o(1)},
\]
since all variables are polynomially bounded by the physical height.

This is the first closure step: fixing three residual variables does **not** leave a polynomial family of unrelated cores. The core belongs to a divisor-many list determined by the already-fixed `(X,Y)` pair. Legal local root/sign orientations only filter that list and do not increase multiplicity.

The toric compatibility condition from 6ak is automatic in these cells:
\[
(a^2MU)(d^2NV)(b^2MV)(c^2NU)
=(abcdMNUV)^2.
\]
Thus the genuinely new reconstruction equation is the common-core norm system above, not the coordinate-product square condition.

```text
STAGE15_6_SUBSTAGE=6cz
STAGE15_6CZ_CELL_GAUSSIAN_COORDINATES_EXACT=true
STAGE15_6CZ_EXACT_SURVIVOR_EQUATIONS=A0=kP^2,B0=kQ^2
STAGE15_6CZ_TORIC_PRODUCT_SQUARE_AUTOMATIC=true
STAGE15_6CZ_ODD_CORE_DIVIDES_FIXED_X4_MINUS_Y4=true
STAGE15_6CZ_FIXED_MN_CORE_CANDIDATES=B^o(1)
STAGE15_6CZ_LOCAL_ORIENTATIONS_INCREASE_MULTIPLICITY=false
STAGE15_6CZ_EXIT=PELL_NORM_COMPLETION_AUDIT_READY
```