# Stage32EX1 EX1-02 — surface-node multibranch residual ledger

Status: candidate only. This note does not grant hostile-audited Stage32EX1 credit, Stage32 MAIN credit, or any endpoint claim.

## 1. Exact local setup

Let `pi:S->X` be the minimal resolution of the singular canonical cuboid surface and let `E_i` be the exceptional curve over the `i`-th A1 node `x_i`. For a hypothetical integral irreducible V6 carrier `Gamma` on the smooth surface `S`, let `nu:N->Gamma` be its normalization.

Because `E_i` is a Cartier divisor on smooth `S` and `Gamma` is not an exceptional component, the pullback to the normalization is an effective divisor

`nu^*E_i = sum_j a_ij q_ij`, with `a_ij >= 1`.

Its degree is the intersection number

`sum_j a_ij = Gamma.E_i = m_i`.

The normalization points `q_ij` are exactly the normalization points mapping, after contraction, to the canonical-model node `x_i`. Hence

`r_i := #(N -> B)^{-1}(x_i) = #supp(nu^*E_i) <= m_i`.

This proves that node-fibre data from the class-level exceptional contacts is an integer-partition problem: the positive orders `a_ij` form a partition of `m_i`, and a nonbijective node fibre requires partition length at least two.

## 2. Zero and unit contacts are completely rigid

For `m_i=0`, the carrier does not meet `E_i`, so `r_i=0`.

For `m_i=1`, there is exactly one intersection point and its local intersection multiplicity is one. Since `E_i` is smooth,

`I_p(Gamma,E_i) >= mult_p(Gamma) * mult_p(E_i) = mult_p(Gamma)`.

Therefore `mult_p(Gamma)=1`. Thus `Gamma` is smooth at that point and meets `E_i` transversely. Consequently a unit-contact node is neither a nonbijective canonical normalization fibre nor a source of strict-transform delta.

For V6 the unit labels are

`[1,2,3,7,15,20,22,24,36]`.

Together with the zero label `6`, only the 38 labels with `m_i>=2` remain in the surface-node residual ledger.

## 3. Exact finite contact-partition envelope

At a labeled node with contact mass `m>=2`, the class-level data permits only partitions `lambda |- m` of length at least two. This is a necessary envelope, not an effectivity statement.

The number of such partitions is `p(m)-1`, where `p(m)` is the ordinary partition number; the omitted partition is the one-part partition `[m]`. Across the actual V6 contact-mass distribution, the labeled node-local multibranch envelopes total exactly `1188`.

This does **not** mean that 1188 geometric local models occur. It means every geometric surface-node multibranch model compatible with the retained contact data must project to one of these 1188 labeled contact-partition envelopes.

The previous global fibre-excess bound remains

`sum_i max(r_i-1,0) <= sum_{m_i>0}(m_i-1)=266-47=219`.

The quantity `219` is still not delta.

## 4. Why contact partitions do not determine delta on the resolution

There are two distinct mechanisms over a surface node.

First, several distinct smooth points of `Gamma` may meet the same exceptional curve `E_i`. Contraction identifies them at `x_i`, so `N->B` is nonbijective there, but `Gamma` itself may be smooth at all those points. This is contraction-only nonbijectivity and contributes zero strict-transform delta at those points.

Second, normalization branches may already coincide at a singular point of `Gamma` lying on `E_i`, or `Gamma` may have a unibranch singularity there. Then positive `delta_E` may occur. The contact partition records the orders of `nu^*E_i`; it does not record which normalization points coincide in `Gamma`, their pairwise tangencies, or a unibranch analytic type.

There is not even a finite local delta upper bound from fixed contact mass alone in the unrestricted smooth-surface local category. In smooth coordinates `(x,y)` with `E={x=0}`, consider

`Gamma_k: y^2 = x^(2k+1)`, `k>=1`.

This is an irreducible unibranch plane curve singularity. Its intersection with `E` has length `2`, while

`delta(Gamma_k)=((2-1)((2k+1)-1))/2=k`.

Thus fixed contact `m=2` allows arbitrarily large delta locally. This example is only a local obstruction to any contact-only delta bound; it is **not** a global V6 carrier construction.

## 5. EX1-02 outcome

The surface-node branch is not excluded. It is, however, exactly reduced at the class-level contact layer to a finite parameterized residual ledger:

- zero/unit contacts are rigid and harmless for multibranch/delta;
- 38 nonunit nodes remain;
- every node-fibre cardinality/contact profile is controlled by an integer partition of the exact `m_i`;
- the labeled local multibranch envelope has 1188 contact types;
- class-level contact data cannot decide intrinsic singularity coincidence/tangency or bound `delta_E` sufficiently for exclusion.

The exact reopen interface is actual-member local equations/jet data, a theorem bounding singularities inside the V6 linear system, or a global constraint coupling the node contact partitions to the total defect budget.

Accordingly EX1-02 routes to EX1-03 while carrying this residual ledger forward to EX1-04/05. No branch-exclusion credit is claimed.
