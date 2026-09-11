# Stage32 MB104 — population-wide finite-window reduction / coefficient barrier

Status: **RETAINED PARTIAL MB104 / FINITE DEGREE WINDOW NOT YET PROVED / NO RECEIVER CREDIT**.

This checkpoint does not complete MB104. It extracts the strongest population-wide numerical restrictions currently justified by the retained factor-fibration, local branch, and symmetric-tensor interfaces, and isolates the remaining coefficient gap required for an actual finite degree window.

## Scope

Let `D` be the strict transform on the minimal resolution `S` of a nonexceptional integral curve in the residual `R29-LG2-MB` population. Let

- `g in {0,1}` be the geometric genus of the normalization;
- `d=K_S.D` be the canonical/projective degree;
- `n1,n2` be the two factor-fibration degrees, so `n1+n2=d`;
- `M=sum_i M_i` be total exceptional intersection mass;
- `R=sum_i r_i` be the number of normalization branches over box nodes;
- `t=M-R=sum_branches(min(A,B)-1)>=0`;
- `s_min` be the number of node branches of the unique FSM-minimal type `(A,B)=(1,1)`.

Boundary-elliptic components themselves are already-known curves and are not part of the unknown residual carrier population considered below.

## 1. Population-wide special-fibre identity

AM source-locks two factor directions, six Satake-boundary elliptics in each direction, and for every one of those special fibres

`F_E = 2 E + sum(8 incident exceptional curves)`.

Distinct fibres in one direction are disjoint. Six fibres times eight node incidences gives all 48 exceptional curves exactly once in that direction. If `q_i` is total intersection of `D` with the six boundary elliptics in direction `i`, then summing the six fibre identities gives

`6*n_i = 2*q_i + M`.

Hence

`q_i = 3*n_i - M/2 >= 0`,

so in particular

- `M` is even;
- `M <= 6*n_i` for both directions;
- `M <= 6*min(n1,n2) <= 3*d`.

These are genuine population-wide intersection restrictions, but the coefficient `3` does not bound `d`.

## 2. Generalized two-factor slack identity

AR proves the local ramification accounting for a genus-one V6 test. The local identities do not use the V6 degree; replacing the genus-one Riemann--Hurwitz total `2*n_i` by the general normalization formula `2g-2+2*n_i` gives, direction by direction,

`2g-2 + 2*n_i - q_i = t + q_i_node + eta_i + rho_i =: sigma_i`,

where `q_i_node, eta_i, rho_i` are all nonnegative and retain exactly the AR meanings.

Substituting `q_i=3*n_i-M/2` yields

`sigma_i = M/2 - n_i + 2g - 2 >= 0`.

Adding the two directions and using `n1+n2=d` gives the exact global slack identity

`M - d + 4g - 4 = sigma_1 + sigma_2 >= 0`.

Therefore every residual low-genus multibranch carrier necessarily satisfies

`d <= M + 4g - 4`.

Specializations:

- `g=0`: `M >= d+4`;
- `g=1`: `M >= d`.

Together with the special-fibre upper bound:

- `g=0`: `d+4 <= M <= 3d`;
- `g=1`: `d <= M <= 3d`.

This is not a finite degree window.

## 3. Population-wide minimal-branch lower bound

Call a node branch nonminimal when `(A,B)!=(1,1)`. As in AR, every nonminimal branch consumes at least one unit from

`t`, `q_1_node`, or `q_2_node`.

Thus, if `U` is the number of nonminimal node branches,

`U <= t + q_1_node + q_2_node`.

Since `sigma_i=t+q_i_node+eta_i+rho_i`, one has `q_i_node <= sigma_i-t`. Therefore

`U <= sigma_1 + sigma_2 - t`
`  = (M-d+4g-4) - (M-R)`
`  = R-d+4g-4`.

As `s_min=R-U`, this gives the exact population-wide lower bound

`s_min >= d - 4g + 4`.

Hence

- `g=0`: `s_min >= d+4`;
- `g=1`: `s_min >= d`.

In particular `R>=s_min`, so the same lower bounds hold for the total node-branch count.

## 4. Exact relation to the FSM symmetric-tensor route

In the proof of Freitag--Salvati Manni Theorem 3.1 a node branch has

`a1=4A`, `a2=4B`, `A,B>0`, `A+B` even.

The `(dzdw)^(8k)` term contributes pole order `16k`, while `Delta(z)^k Delta(w)^k` contributes zero order `4(A+B)k`. Therefore the positive pole order on a branch is

`max(0,16-4(A+B))*k`.

Since `A+B` is even and at least two, positive poles occur **only** for `(A,B)=(1,1)`, with pole order exactly `8k`. If `s_min` is the number of such branches, the same zero/pole count gives the branchwise necessary inequality

`d <= 16g - 16 + 4*s_min`.

The new factor-slack result is much stronger in the needed direction:

`s_min >= d-4g+4`.

Thus the FSM branch-cardinality inequality is automatically compatible and cannot by itself produce the missing finite degree window. This generalizes the previously retained fixed-V6 dominance diagnosis to the whole `g=0/1` multibranch receiver.

## 5. What is finite now, and what is not

For a **fixed** degree `d`, the retained scalar numerical search is finite:

- `n1,n2` are positive integers with `n1+n2=d` outside known factor-fibre components;
- `M` is an even integer in the interval above;
- `R` lies between `s_min` and `M`;
- `q_i=(6*n_i-M)/2` is forced;
- the 48-entry integer exceptional-mass profile has total `M` and can be reduced by the exact MB103 `Aut(S)` canonicalizer.

This does **not** make the whole receiver finite because `d` itself is still unbounded, and continuous exceptional landing/tangent data remain outside the MB103 discrete quotient.

## 6. Exact remaining coefficient gap

Any one of the following types of genuinely new population-wide input would close the numerical degree direction:

1. `s_min <= alpha*d + beta` with `alpha < 1/4`; combined with `d <= 16g-16+4*s_min` this gives an absolute degree bound.
2. `M <= alpha*d + beta` with `alpha < 1`; combined with `d <= M+4g-4` this gives an absolute degree bound.
3. An independent absolute bound on one factor degree `n_i`, or directly on `d`.

Current exact retained inequalities give only `s_min<=R<=M<=3d`, so none reaches a closing coefficient. Reusing the EX6 fixed-V6 tensor/cardinality route cannot supply this missing upper coefficient; its retained contract already marks that route nonexcluding/dominated.

## Firewalls

- MB104 is **not complete**.
- No unibranch `176/192` cap is imported.
- No absolute multibranch degree bound is claimed.
- No finite Picard enumeration is released.
- No effectivity, receiver, final-milestone, theorem, endpoint, or Perfect Cuboid credit.
- No merge authorization.

Next MB104 sub-obligation: obtain a genuinely independent upper coefficient on `s_min`, `M`, or a factor degree; otherwise record MB104 as blocked rather than silently enumerating an unbounded degree family.
