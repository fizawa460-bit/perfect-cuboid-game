# Stage32 MB104 — population-wide finite-window reduction / coefficient barrier

Status: **RETAINED PARTIAL MB104 / FINITE DEGREE WINDOW NOT YET PROVED / NO RECEIVER CREDIT**.

This checkpoint does not complete MB104. It extracts the strongest population-wide numerical restrictions currently justified by the retained factor-fibration, local branch, Picard/Hodge, and symmetric-tensor interfaces, and isolates the remaining anti-scaling input required for an actual finite degree window.

Let `D` be the strict transform of a nonexceptional integral curve in `R29-LG2-MB`, with normalization genus `g in {0,1}`. Write `n_i=D.F_i`, `d=K_S.D=n1+n2`, `M=sum M_i`, `R=sum r_i`, and `t=M-R=sum_branches(min(A,B)-1)>=0`. Let `s_min` be the number of node branches of the unique FSM-minimal type `(A,B)=(1,1)`.

## 1. Population-wide special-fibre identity

AM source-locks two factor directions, six Satake-boundary elliptics in each direction, and

`F_E = 2E + sum(8 incident exceptional curves)`.

Summing the six fibres in direction `i`, with `q_i` the total intersection with the six boundary elliptics, gives

`6*n_i = 2*q_i + M`, hence `q_i=3*n_i-M/2>=0`.

Therefore `M` is even, `M<=6*n_i` in both directions, and

`M<=6*min(n1,n2)<=3d`.

## 2. Generalized two-factor slack identity

The AR local ramification calculation is degree-independent. For normalization genus `g`, Riemann--Hurwitz gives

`2g-2+2*n_i-q_i = t+q_i_node+eta_i+rho_i =: sigma_i >=0`.

Substituting the special-fibre identity,

`sigma_i=M/2-n_i+2g-2`.

Adding both factor directions gives the exact global identity

`M-d+4g-4 = sigma_1+sigma_2 >=0`.

Hence

`d<=M+4g-4`.

Specializations:

- `g=0`: `d+4<=M<=3d`;
- `g=1`: `d<=M<=3d`.

These are genuine population-wide restrictions, but they do not bound `d` absolutely.

## 3. Population-wide minimal-branch lower bound

Every nonminimal node branch `(A,B)!=(1,1)` consumes at least one unit from `t`, `q_1_node`, or `q_2_node`. If `U` is the number of nonminimal node branches,

`U<=t+q_1_node+q_2_node`.

Since `q_i_node<=sigma_i-t`,

`U<=sigma_1+sigma_2-t = R-d+4g-4`.

Thus

`s_min=R-U >= d-4g+4`.

So

- `g=0`: `s_min>=d+4`;
- `g=1`: `s_min>=d`.

This directly identifies the missing finite-window mechanism: one now needs an **independent upper bound with slope strictly below 1** on `s_min` or `M`, or an independent absolute bound on a factor degree.

## 4. Picard/Hodge exceptional-mass inequality

Stage29 source-locks `H=K_S`, `H^2=16`, and negative-definiteness of `H^perp`. The 48 exceptional curves `E_i` over the ordinary double points are pairwise disjoint rational `(-2)` curves. Adjunction gives `H.E_i=K_S.E_i=0`.

Set

`x = D-(d/16)H in H^perp`.

Since `x.E_i=M_i`, the orthogonal projection of `x` to the exceptional sublattice is

`x_E = -sum_i (M_i/2) E_i`,

with

`x_E^2 = -(1/2) sum_i M_i^2`.

The residual vector `x-x_E` is still in the negative-definite orthogonal complement, so

`D^2-d^2/16 = x^2 <= -(1/2)sum_i M_i^2`.

Adjunction and `Delta_total>=0` give

`D^2 = 2g-2+2*Delta_total-d >= 2g-2-d`.

Therefore

`sum_i M_i^2 <= d^2/8 + 2d - 4g + 4`.

By Cauchy over the 48 exceptional curves,

`M^2 <= 48*sum_i M_i^2 <= 6d^2+96d-192g+192`.

Thus the crude `M<=3d` is sharpened asymptotically to

`M/d <= sqrt(6)+o(1)`.

This is an exact population-wide Picard restriction and can prune fixed-degree profiles substantially, but `sqrt(6)>1`; it still does not supply the sublinear coefficient required to close MB104.

The same argument with `R<=M` or `s_min<=R` does not improve the asymptotic coefficient below one. The existing local feasibility wall also prevents replacing branch multiplicity by delta to manufacture a stronger quadratic penalty.

## 5. Relation to the FSM symmetric-tensor route

The corrected EX6/FSM16 adapter gives positive pole order only for `(A,B)=(1,1)`, with exact pole order `8k`, and the branchwise necessary inequality

`d<=16g-16+4*s_min`.

The new factor-slack lower bound `s_min>=d-4g+4` is much stronger in the opposite direction, so cardinality-only tensor bookkeeping cannot close the population-wide degree direction.

If one insists on combining an upper bound `s_min<=alpha*d+beta` with the FSM inequality alone, `alpha<1/4` is sufficient. But after the new direct lower bound, the sharp closing threshold is simply

`alpha<1`.

Indeed

`d-4g+4 <= s_min <= alpha*d+beta`

implies

`(1-alpha)d <= beta+4g-4`.

The same threshold `alpha<1` applies to an upper bound `M<=alpha*d+beta` because `M>=d-4g+4`.

## 6. Formal scaling witnesses: why the current ledger cannot be finite

The present scalar identities admit arbitrarily large formal solutions.

For genus one and any even `d`, set

`M=d`, `n1=n2=d/2`, `t=0`, `q1=q2=d`, `sigma1=sigma2=0`.

For genus zero and any even `d>=2`, set

`M=d+4`, `n1=n2=d/2`, `t=0`, `q1=q2=d-2`, `sigma1=sigma2=0`.

Both families also satisfy the new Hodge mass inequality for arbitrarily large `d`. These are **formal ledger witnesses only** and do not assert geometric curves. They prove that MB101/102 plus the current two-factor, Picard/Hodge, and Riemann--Hurwitz identities cannot by themselves yield a finite degree cutoff.

## 7. What is finite now

For any fixed `d`, the scalar discrete search is finite: `n1+n2=d`; `M` lies in the finite interval above and also satisfies the quadratic Hodge bound; `q_i=(6*n_i-M)/2` is forced; `R<=M`; and the 48-entry integer exceptional profile can be reduced by the exact MB103 `Aut(S)` canonicalizer. What remains globally infinite is the degree direction itself, together with continuous exceptional landing/tangent data outside the discrete quotient.

## Next MB104 sub-obligation

Find a genuinely independent anti-scaling estimate, preferably one of:

- `s_min <= alpha*d+beta` with `alpha<1`;
- `M <= alpha*d+beta` with `alpha<1`;
- an absolute bound on one factor degree `n_i` or directly on `d`;
- an equivalent local exceptional-landing capacity theorem that forces one of the first two inequalities.

The new Hodge estimate has asymptotic coefficient `sqrt(6)` and therefore does not meet this threshold. Until a subunit coefficient or absolute bound is proved, MB104 remains partial and finite Picard enumeration is forbidden.

## Source locks / firewalls

The checkpoint source-locks MB101/102/103, Stage29 finite-lattice reduction, post1648AL/AM/AR, and the corrected EX6 FSM16 multibranch contract. No unibranch `176/192` cap is imported into the multibranch population. No finite degree window, effectivity, receiver, final-milestone, theorem, endpoint, Stage32 closure, or Perfect Cuboid credit is claimed. Merge remains unauthorized.
