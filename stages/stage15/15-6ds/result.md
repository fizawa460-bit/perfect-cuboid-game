# Stage15-6ds — split survivor core: k=1 factor branch and squarefree k>1 Pell branch

Base: merged Stage15-6dr after fresh audit PASS, with the aggregate controller repaired by merged PR #881. The fresh audit of the first Pell draft requires the survivor core to be split before any unit-orbit claim.

Fix one legal cross-gcd cell package `(a,b,c,d)`, one reconstructed base triple `(M,N,U)`, one legal squarefree survivor core `k`, and all already-charged local channel/orientation data. Retain
\[
R\le B,\qquad HMNUV\le B,\qquad (q,H)=1,
\]
all primitivity/positivity/canonical/exactly-two masks, the exact `phi(d_S)phi(e_O)` switched weights, and `kg^2|Delta` with
\[
\Delta=(abM)^4-(cdN)^4>0.
\]
The exact survivor equations are
\[
a^4M^2U^2+d^4N^2V^2=kP^2,
\qquad
b^4M^2V^2+c^4N^2U^2=kQ^2.
\]
Stage15-6df gives the primitive norm coprimalities
\[
\gcd(a^2MU,d^2NV)=1,
\qquad
\gcd(b^2MV,c^2NU)=1.
\]

## 1. Degenerate core k=1: two exact primitive difference-of-squares receivers

Put
\[
C_1=a^2MU,\quad L_1=d^2NV,
\qquad
C_2=c^2NU,\quad L_2=b^2MV.
\]
For `k=1` the two survivor norms are exactly
\[
P^2-L_1^2=C_1^2,
\qquad
Q^2-L_2^2=C_2^2.
\]
Hence
\[
\boxed{(P-L_1)(P+L_1)=C_1^2,}
\qquad
\boxed{(Q-L_2)(Q+L_2)=C_2^2.}
\]
Define positive ordered factor pairs
\[
r_1=P-L_1,\ s_1=P+L_1,
\qquad
r_2=Q-L_2,\ s_2=Q+L_2.
\]
Then
\[
r_1s_1=C_1^2,
\qquad
r_2s_2=C_2^2,
\]
with
\[
P=\frac{r_1+s_1}{2},\quad L_1=\frac{s_1-r_1}{2},
\qquad
Q=\frac{r_2+s_2}{2},\quad L_2=\frac{s_2-r_2}{2}.
\]
The common residual variable is therefore constrained by the exact factor-gap identity
\[
\boxed{
\frac{s_1-r_1}{2d^2N}
=V
=\frac{s_2-r_2}{2b^2M}.
}
\]

Because both triples are primitive, the factor pairs have the usual primitive Pythagorean refinement. If `C_i` is odd then `L_i` is even, `gcd(r_i,s_i)=1`, and
\[
r_i=x_i^2,\qquad s_i=y_i^2,\qquad x_iy_i=C_i.
\]
If `C_i` is even then `L_i` is odd, `gcd(r_i,s_i)=2`, and
\[
r_i=2x_i^2,\qquad s_i=2y_i^2,\qquad 2x_iy_i=C_i.
\]
Thus the `k=1` branch is an exact primitive divisor-pair/factor-gap receiver, not a Pell orbit.

### Multiplicity charge for k=1

For fixed `(a,b,c,d,M,N,U)` enumerate only the first factor pair `r_1s_1=C_1^2`. It determines `L_1`, hence `V`, and then `P`. There are at most
\[
\tau(C_1^2)=B^{o(1)}
\]
choices. The second factor equation, integrality of `Q`, and every physical/local mask are postfilters. We do **not** multiply by a second divisor count. Therefore
\[
\boxed{\#\{V:\ k=1\text{ exact survivor completion for fixed base}\}\le B^{o(1)}}
\]
with the same single completion charge already certified in 6da.

A concrete algebraic survivor witness is
\[
(a,b,c,d)=(1,1,1,1),\qquad(M,N,U,V)=(5,3,7,4).
\]
Then
\[
35^2+12^2=37^2,
\qquad
20^2+21^2=29^2,
\]
so `k=1`, `P=37`, `Q=29`, and
\[
(P-L_1,P+L_1)=(25,49),
\qquad
(Q-L_2,Q+L_2)=(9,49).
\]
The U-eliminant is also exact:
\[
(5^4-3^4)7^2=(5\cdot37-3\cdot29)(5\cdot37+3\cdot29).
\]

## 2. k=1 equivalence to the already-tested factor/double-eliminant geometry

The map
\[
(P,Q,V)\longleftrightarrow(r_1,s_1,r_2,s_2)
\]
subject to the displayed products and factor-gap identity is reversible. Hence it is only a reparametrization of the original two survivor quadrics.

Moreover Stage15-6dg already proved that, because `Delta!=0`, the two normalized double eliminants are Cramer-equivalent to those two survivor quadrics. Specializing `k=1` therefore does not create a third equation or an independent codimension. Eliminating `V` again gives
\[
\Delta U^2
=(b^2MP-d^2NQ)(b^2MP+d^2NQ),
\]
and symmetrically
\[
\Delta V^2
=(a^2MQ-c^2NP)(a^2MQ+c^2NP).
\]

The primitive factor-gap form is useful as a **normal form for a later complementary divisor switch**, but pointwise factorization itself gives no new same-measure fixed-power saving beyond the already-charged `B^{o(1)}` completion fiber.

## 3. Squarefree k>1: exact unit-orbit parametrization

Now assume squarefree `k>1`. Put
\[
C_1=a^2MU,\qquad L=d^2NV.
\]
The first norm is
\[
L^2-kP^2=-C_1^2.
\]
Work in `K=Q(sqrt(k))`. As in 6da, the possible principal-ideal seeds are divisor-many. For one integral-coordinate seed
\[
\xi_{\nu,0}=L_{\nu,0}+P_{\nu,0}\sqrt{k}
\]
and a generator `epsilon_k>1` of the free rank-one unit part, every solution attached to the seed has
\[
\boxed{\xi_{\nu,j}=\pm\xi_{\nu,0}\epsilon_k^j,\qquad j\in J_\nu\subset\mathbf Z.}
\]
The coordinate sequences obey
\[
Z_{j+2}=T_kZ_{j+1}-\eta_kZ_j,
\qquad
T_k=\operatorname{Tr}(\epsilon_k),\quad \eta_k=N(\epsilon_k)\in\{\pm1\}.
\]
Physical polynomial height gives only `O(log B)` admissible exponents per seed, already inside the 6da `B^{o(1)}` charge.

For the second norm set
\[
Y=d^2NQ,
\qquad
C_2=c^2d^2N^2U.
\]
After substituting `L=L_{nu,j}` it becomes
\[
\boxed{(b^2ML_{\nu,j})^2-kY_j^2=-C_2^2.}
\]
Thus for `k>1` the second survivor norm is another norm equation in the **same** real quadratic field. Exact survivors are intersections of two rank-one recurrence orbits, with all physical/local masks retained.

Eliminating `L` gives again
\[
\Delta U^2
=k(b^2MP-d^2NQ)(b^2MP+d^2NQ),
\]
so this is a parametric view of the existing receiver, not independent codimension.

For the certified `k=10` witness
\[
(a,b,c,d)=(1,1,1,1),\quad(M,N,U,V)=(13,1,9,1),
\]
`xi_0=1+37sqrt(10)` lies on the first norm and multiplication by `19+6sqrt(10)` gives `2239+709sqrt(10)`. The first orbit persists while the next term fails the second-square test, confirming that the second norm genuinely filters the orbit without proving a density exponent.

## 4. Unified measure firewall

- `k=1` is charged through one first-factor completion enumeration; its second factor equation is a postfilter.
- `k>1` is charged through one first-norm ideal/unit completion enumeration; its second Pell norm is a postfilter.
- The two branches partition the squarefree-core population and are never multiplied together.
- The 6da `B^{o(1)}` completion multiplicity is charged exactly once in either branch.
- `kg^2|Delta`, exact switched weights, `(q,H)=1`, and all physical survivor masks are preserved.
- No Stage14 exponent is imported.

```text
STAGE15_6_SUBSTAGE=6ds
STAGE15_6DS_CORE_SPLIT_K1_VS_KGT1=true
STAGE15_6DS_K1_RECEIVER=PRIMITIVE_DIFFERENCE_OF_SQUARES_FACTOR_GAP
STAGE15_6DS_K1_TWO_FACTOR_EQUATIONS_EXACT=true
STAGE15_6DS_K1_FACTOR_GAP_COMPATIBILITY_EXACT=true
STAGE15_6DS_K1_EQUIVALENT_TO_SURVIVOR_QUADRICS=true
STAGE15_6DS_K1_DOUBLE_ELIMINANT_EQUIVALENCE=true
STAGE15_6DS_K1_DISTINCT_FIXED_POWER_PROVED=false
STAGE15_6DS_KGT1_FIRST_NORM_UNIT_ORBITS_EXACT=true
STAGE15_6DS_KGT1_SECOND_NORM_SAME_FIELD_PELL=true
STAGE15_6DS_KGT1_RECEIVER=RANK_ONE_RECURRENCE_INTERSECTION
STAGE15_6DS_NEW_INDEPENDENT_CODIMENSION=false
STAGE15_6DS_6DA_MULTIPLICITY_RECHARGED=false
STAGE15_6DS_PHYSICAL_MEASURE_PRESERVED=true
STAGE15_6DS_EXIT=BRANCHWISE_AVERAGING_AND_ARSENAL_AUDIT_READY
```
