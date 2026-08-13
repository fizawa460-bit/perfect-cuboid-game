# Stage15-6ds — exact Pell/unit orbit and second-norm recurrence correlation

Base: merged Stage15-6dr after fresh audit PASS, with the aggregate controller repaired by merged PR #881. Execute the selected
\[
\boxed{\text{PELL UNIT-ORBIT SECOND-NORM CORRELATION}}
\]
on the same reconstructed physical graph. No Stage14 exponent is imported.

Fix one legal cross-gcd cell package `(a,b,c,d)`, one reconstructed base triple `(M,N,U)`, one legal squarefree survivor core `k`, and all already-charged local channel/orientation data. Retain
\[
R\le B,\qquad HMNUV\le B,\qquad (q,H)=1,
\]
all primitivity/positivity/canonical/exactly-two masks, and the exact core relation `kg^2|Delta` from Stage15-6df.

Put
\[
C_1=a^2MU,\qquad L=d^2NV.
\]
The first survivor norm is
\[
\boxed{L^2-kP^2=-C_1^2.}
\]

## 1. Exact unit-orbit parametrization of one 6da completion fiber

Work in `K=Q(sqrt(k))`. Stage15-6da already partitions the solutions of
\[
N_{K/Q}(\xi)=-C_1^2
\]
into `B^{o(1)}` principal-ideal seeds. Choose one actual integral-coordinate seed
\[
\xi_{\nu,0}=L_{\nu,0}+P_{\nu,0}\sqrt{k}.
\]
Let `epsilon_k>1` generate the free rank-one part of the real quadratic unit group, up to sign and the bounded index needed to remain in the integral-coordinate order relevant to `L+P sqrt(k)`. Every solution attached to this seed ideal is therefore of the exact form
\[
\boxed{\xi_{\nu,j}=\pm\xi_{\nu,0}\epsilon_k^j,\qquad j\in J_\nu\subset\mathbf Z,}
\]
where `J_nu` is the subset for which the resulting coefficients are integral and satisfy `d^2N|L`, positivity, the physical bounds and all survivor masks. Equivalently,
\[
L_{\nu,j}=\frac{\xi_{\nu,0}\epsilon_k^j+\bar\xi_{\nu,0}\bar\epsilon_k^j}{2},
\]
\[
P_{\nu,j}=\frac{\xi_{\nu,0}\epsilon_k^j-\bar\xi_{\nu,0}\bar\epsilon_k^j}{2\sqrt{k}}.
\]
If
\[
T_k=\operatorname{Tr}(\epsilon_k),\qquad \eta_k=N(\epsilon_k)\in\{\pm1\},
\]
then both coordinate sequences obey the exact Lucas/Pell recurrence
\[
\boxed{Z_{j+2}=T_kZ_{j+1}-\eta_k Z_j.}
\]
The physical polynomial height bound implies only `O(log B)` admissible exponents for each seed, recovering the exponent-neutral `B^{o(1)}` completion statement of 6da.

## 2. Substitute the orbit into the second survivor norm

The second survivor equation is
\[
b^4M^2V^2+c^4N^2U^2=kQ^2.
\]
Since `L=d^2NV`, multiply by `d^4N^2` and put
\[
Y=d^2NQ,\qquad C_2=c^2d^2N^2U.
\]
For one Pell-orbit term `L=L_{nu,j}` this becomes exactly
\[
\boxed{(b^2M L_{\nu,j})^2-kY_j^2=-C_2^2.}
\]
Thus the second survivor condition is itself a Pell norm equation in the **same** real quadratic field `K`.

For every second-norm seed
\[
\zeta_{\mu,0}=T_{\mu,0}+Y_{\mu,0}\sqrt{k},\qquad N(\zeta_{\mu,0})=-C_2^2,
\]
write its unit orbit as
\[
\zeta_{\mu,\ell}=\pm\zeta_{\mu,0}\epsilon_k^\ell.
\]
An exact survivor is therefore a correlation of two rank-one recurrence orbits satisfying
\[
\boxed{\operatorname{Re}\zeta_{\mu,\ell}=b^2M\operatorname{Re}\xi_{\nu,j}.}
\]
All local and physical conditions select a subset of these intersections; none is dropped.

## 3. Exact squareclass/eliminant form

The recurrence correlation can also be written
\[
k d^4N^2Q_j^2=b^4M^2L_{\nu,j}^2+c^4d^4N^4U^2.
\]
Using the first norm
\[
L_{\nu,j}^2=kP_{\nu,j}^2-a^4M^2U^2
\]
gives
\[
\boxed{
\Delta U^2
=k\bigl(b^4M^2P_{\nu,j}^2-d^4N^2Q_j^2\bigr),
}
\]
where
\[
\Delta=a^4b^4M^4-c^4d^4N^4=(abM)^4-(cdN)^4.
\]
Factoring the right side recovers exactly
\[
\Delta U^2
=k(b^2MP_{\nu,j}-d^2NQ_j)(b^2MP_{\nu,j}+d^2NQ_j).
\]
Hence the Pell correlation is a new **parametric view** of the survivor receiver, but it does not create a third independent algebraic equation: after eliminating `L`, it returns the already-certified double eliminant.

## 4. Concrete recurrence witness

For the certified survivor
\[
(a,b,c,d)=(1,1,1,1),\quad(M,N,U,V)=(13,1,9,1),\quad k=10,
\]
we have
\[
C_1=117,\qquad \xi_0=1+37\sqrt{10}.
\]
Using the norm-one unit
\[
\epsilon=19+6\sqrt{10},
\]
the next first-norm orbit point is
\[
\xi_1=(1+37\sqrt{10})(19+6\sqrt{10})=2239+709\sqrt{10}.
\]
Both points satisfy `L^2-10P^2=-117^2`. The physical survivor is the `j=0` term: its second norm has `Q=5`. The `j=1` term fails the second-square test because
\[
\frac{13^2\cdot2239^2+9^2}{10}=84721753
\]
is not a square. This is a regression witness that the second norm genuinely filters unit-orbit exponents; it is not evidence for a density exponent.

## 5. Measure firewall

- The outer object remains the reconstructed base `(cells,M,N,U,k,local decorations)` under the original physical measure.
- The 6da seed/ideal and unit multiplicity is charged once as `B^{o(1)}`.
- The second Pell equation is a postfilter on that same fiber, not a second independent count of the core.
- `kg^2|Delta`, exact `phi(d_S)phi(e_O)` switched weights, `(q,H)=1`, and all survivor masks remain available for later averaging.
- No scalar replacement of the reconstructed base is made.

```text
STAGE15_6_SUBSTAGE=6ds
STAGE15_6DS_FIRST_NORM_UNIT_ORBITS_EXACT=true
STAGE15_6DS_PELL_COORDINATES_LINEAR_RECURRENCE=true
STAGE15_6DS_SECOND_NORM_SAME_FIELD_PELL=true
STAGE15_6DS_RECEIVER=RANK_ONE_RECURRENCE_INTERSECTION
STAGE15_6DS_DOUBLE_ELIMINANT_RECOVERED=true
STAGE15_6DS_NEW_INDEPENDENT_CODIMENSION=false
STAGE15_6DS_6DA_MULTIPLICITY_RECHARGED=false
STAGE15_6DS_PHYSICAL_MEASURE_PRESERVED=true
STAGE15_6DS_EXIT=PELL_AVERAGING_AND_ARSENAL_AUDIT_READY
```
