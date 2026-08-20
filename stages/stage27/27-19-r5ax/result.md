# Stage27-19-r5ax — exact factor-packet boundary test and r5 upper-lane freeze

```text
TASK_ID=Stage27-19-r5ax
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5aw
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

The audited r5aw route replaced the two survivor-dependent root congruences by exact integer/Gaussian factor packets. The purpose of r5ax is to perform the promised concrete test: substitute those packets into the r5au hyperbolic boundary and determine whether the algebraic factorization itself produces a genuine negative power of the dyadic kernel scale `K`.

It does not. The packet is an exact reparametrization of the same boundary population. Allocation entropy becomes subpower, but a `K^{-eta}` boundary estimate would require a new quantitative lattice/incidence theorem on the same physical measure. Since SR-STR-224 already records that exact transfer gap, this route freezes the present r5 upper lane instead of minting an equivalent theorem gate.

## 1. Difference packet inside the first hyperbolic pair

Retain the residual chart

\[
m=c_0c_s\mu,\qquad n=\delta c_n\nu,
\]

and write

\[
\alpha=c_0c_s,\qquad \beta=\delta c_n,
\qquad \alpha\beta=\delta C,
\qquad C=c_0c_sc_n.
\]

For an actual survivor, r5aw gives the unique odd squarefree allocation

\[
\kappa_-=(\kappa,|m-n|),\qquad
\kappa_+=\kappa/\kappa_-,
\]

with

\[
(\kappa_-,\kappa_+)=1,
\qquad \kappa_-\mid m-n,
\qquad \kappa_+\mid m+n.
\]

Write

\[
m-n=\kappa_-A,\qquad m+n=\kappa_+B.
\]

Then

\[
m=\frac{\kappa_-A+\kappa_+B}{2},
\qquad
n=\frac{\kappa_+B-\kappa_-A}{2},
\]

with the inherited positivity/parity conditions, and therefore

\[
\boxed{
4\delta C\,\mu\nu
=4mn
=\kappa_+^2B^2-\kappa_-^2A^2.
}
\tag{D}
\]

Consequently the r5au pair-product condition `mu*nu <= U` is **equivalent**, not merely implied, to

\[
0<\kappa_+^2B^2-\kappa_-^2A^2\le4\delta C U.
\]

The old modular root choice has disappeared, but the near-cone/hyperbolic boundary has not. The transformation has merely put that boundary into a difference-of-squares strip.

## 2. Gaussian packet inside the second hyperbolic pair

Likewise retain

\[
r=c_0c_n\rho,\qquad s=\delta c_s\sigma,
\]

so

\[
(c_0c_n)(\delta c_s)=\delta C.
\]

For each audited Gaussian allocation choose

\[
\lambda=a+ib,\qquad a^2+b^2=\kappa,
\]

and write

\[
r+is=\lambda\eta,
\qquad \eta=u+iv.
\]

Then

\[
r=au-bv,\qquad s=av+bu,
\]

and hence

\[
\boxed{
\delta C\,\rho\sigma
=rs
=(au-bv)(av+bu).
}
\tag{G}
\]

Thus the r5au condition `rho*sigma <= V` is exactly equivalent to

\[
0<(au-bv)(av+bu)\le\delta C V.
\]

The linear map `(u,v)->(r,s)` has determinant

\[
\det\begin{pmatrix}a&-b\\ b&a\end{pmatrix}=a^2+b^2=\kappa.
\]

This determinant explains the expected `1/kappa` **area** term. It does not, by itself, bound the lattice discrepancy on the curved/thin hyperbolic boundary. That discrepancy is precisely the part which produced the `sqrt(X_R)` term in r5aq-r5av.

## 3. Exact witness check

For the actual Stage19 survivor

\[
(m,n,r,s)=(21,16,27,14),
\quad \delta=2,
\quad (c_0,c_s,c_n)=(3,7,1),
\quad C=21,
\]

one has

\[
(\mu,\nu,\rho,\sigma)=(1,8,9,1),
\qquad \kappa=185.
\]

The difference packet is

\[
\kappa_-=5,\quad \kappa_+=37,\quad A=B=1,
\]

and (D) reads

\[
37^2-5^2=1344=4\cdot2\cdot21\cdot1\cdot8.
\]

The Gaussian packet is

\[
\lambda=11-8i,\qquad \eta=1+2i,
\]

so

\[
27+14i=(11-8i)(1+2i),
\]

and (G) reads

\[
27\cdot14=378=2\cdot21\cdot9\cdot1.
\]

The packet therefore reproduces the physical boundary exactly on a nondegenerate survivor; it does not shrink it by algebra alone.

## 4. Boundary `K`-power test

At fixed `R`, fixed coefficient cell and dyadic `kappa~K`, r5au has

\[
T_R\ll R^{\varepsilon}
\left(\frac{X_R}{K}+\sqrt{X_R}\right),
\qquad X_R=\frac{R}{\delta C}.
\]

Equations (D) and (G) show what the exact packet does to this count:

- the `2^{omega(kappa)}` / Gaussian allocation choices become only `K^{o(1)}` packets;
- within each packet, the counted points are in exact bijection with integer points in the two displayed indefinite quadratic strips;
- the determinant `kappa` controls the bulk area, but no theorem currently controls the boundary discrepancy on the exact physical masks strongly enough to insert a factor `K^{-eta}` into the accumulated square-root term.

Therefore the promised test has the following verdict:

\[
\boxed{
\text{factorization alone does not prove }
\sqrt{X_R}\,K^{-\eta}
\text{ for any fixed }\eta>0.
}
\]

This is a statement about what has been proved, not a theorem that such a saving is impossible. Obtaining it would be genuinely new counting input, not another algebraic rewrite.

## 5. Occupied-diagonal support is now the polynomial-exponent target

The r5aw fixed-`R` theorem gives, uniformly,

\[
N_{2,R}\le48\tau(R^2)^2=R^{o(1)}.
\]

Define the occupied space-diagonal support

\[
\mathcal R_2(B)
=\{R\le B:N_{2,R}>0\},
\qquad S_2(B)=|\mathcal R_2(B)|.
\]

Trivially every occupied `R` contributes at least one cuboid, while the r5aw fiber bound contributes only a subpower number. Hence

\[
\boxed{
S_2(B)\le N_2(B)\le B^{o(1)}S_2(B).
}
\]

So `N_2(B)` and the number of occupied integral space diagonals have the **same polynomial exponent**. In particular, a strict sub-square-root upper bound for `N_2` is equivalent, up to subpower factors, to a strict sub-square-root bound for occupied `R` support.

This is the correct global interpretation of the fixed-`R` collapse. Further local fiber compression cannot lower the whole-family exponent unless it becomes a zero-survivor/support theorem on many diagonals.

## 6. Anti-loop freeze

StructureRadar SR-STR-224 already records the adjacent Ford/divisor-window search and the exact failure to transfer an off-the-shelf theorem through this physical boundary. r5ax therefore does **not** create a renamed external gate and does not restart generic literature search.

The current r5 upper factor-packet lane is frozen. It may reopen only if new input supplies at least one of:

1. an actual same-measure `K^{-eta}` estimate for the exact quadratic boundary packets after all physical coefficient/support masks; or
2. a fixed-power deficit for the occupied physical diagonal support `S_2(B)`.

Neither is proved here.

```text
R5AX_DIFFERENCE_PACKET_BOUNDARY_IDENTITY_PROVED=true
R5AX_GAUSSIAN_PACKET_BOUNDARY_IDENTITY_PROVED=true
R5AX_PACKET_IS_EXACT_REPARAMETRIZATION=true
R5AX_ALLOCATION_ENTROPY=K^o(1)
R5AX_DETERMINANT_KAPPA_AREA_GAIN_RECORDED=true
FACTORIZATION_ALONE_BOUNDARY_K_POWER_PROVED=false
FIXED_R_PHYSICAL_FIBER_SUBPOWER_RETAINED=true
OCCUPIED_R_SUPPORT_EXPONENT_EQUIVALENCE_PROVED=true
OCCUPIED_R_SUPPORT_RELATION=S2(B)<=N2(B)<=B^o(1)*S2(B)
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
R5_UPPER_FACTOR_PACKET_LANE_FROZEN=true
NEW_STRUCTURE_RADAR_GATE_CREATED=false
GENERIC_LITERATURE_SEARCH_RESTARTED=false
NEXT_DERIVED_ROUTE=NONE_R5_UPPER_LANE_FROZEN
NEXT_REOPEN_CONDITION=SAME_MEASURE_BOUNDARY_K_POWER_OR_OCCUPIED_R_SUPPORT_DEFICIT
NEXT_EXPECTED_COMMAND=Stage27-19-r5-audit
```