# EX1-05F — h=4 local cusp/projection ramification adapter

Status: provisional same-PR candidate. No hostile-audit, Stage32 MAIN, or full-target credit is granted here.

EX1-05E leaves 29 h=4 states `Q=210+2r`, `0<=r<=28`, with descended projection degrees `105` and `81` and total projection ramification

- `R_105=2r`,
- `R_81=48+2r`.

This leaf asks whether the special cusp/node contacts themselves force a positive part of either ramification divisor and thereby remove further Q states.

## Local normalized base change

Use a local cusp parameter `u` on `X(4)` and `v` on the genus-2 quotient `C2`, with `u=v^2`. If a local parameter `t` on the normalization `N` satisfies

`u=t^k * unit`,

then normalization of `v^2=t^k*unit` has `g=gcd(k,2)` points above `t=0`, each mapping to `C2` with ramification index `k/g`. Therefore the total local ramification contribution for the descended projection is

`rho(k)=k-gcd(k,2)`:

- `rho(k)=k-1` for odd `k`;
- `rho(k)=k-2` for even `k`.

At a box node, the resolved modular-fiber formula is `div(u_i)=2L_i+E`. For a normalized branch with exceptional contact `m=I(Gamma,E)` and factor-boundary contact `ell_i=I(Gamma,L_i)`, this gives

`k_i=m+2 ell_i`.

Hence `k_i` has the same parity as `m`, recovering the Beauville odd-contact rule, and

- for odd `m`: `rho_i=m+2ell_i-1`;
- for even `m`: `rho_i=m+2ell_i-2`.

At a smooth point of a factor boundary, `k_i=2ell_i`, so a transverse hit `ell_i=1` has `rho_i=0`.

## Fixed V6 six-cusp bookkeeping

The retained labels `33..44` have V6 pairings

`[11,26,31,22,16,26,25,11,28,40,34,22]`.

The source-locked factor split is

- first factor labels `34,35,38,39,42,43`, boundary sum `182`;
- second factor labels `33,36,37,40,41,44`, boundary sum `110`.

Together with exceptional mass `266`, the six cusp fibers replay exactly:

- `2*182+266=630=6*105`;
- `2*110+266=486=6*81`.

## Why the local cusp adapter does not remove a Q state

For every even `Q` from `26` through `266`, and therefore for every residual `Q=210,212,...,266`, the 48 exceptional totals `M_j` admit the following exact coarse partition. Start with `q_j=M_j mod 2`; their sum is `26`. Increase selected `q_j` by `2` until `sum q_j=Q`; the total available increment capacity is `(266-26)/2=120`. Then split

`M_j = q_j*1 + ((M_j-q_j)/2)*2`.

Thus all node branches have contact `m=1` or `m=2`, with exactly `Q` odd branches. For each such branch choose the source-admissible minimal cusp valuation `a1=a2=4m`. Then `k_1=k_2=m`, `ell_1=ell_2=0`, and both local projection ramification contributions are zero.

Independently, realize each unit of each boundary intersection `C.L` as a distinct smooth transverse boundary hit. Such a point has `k=2` and again contributes zero projection ramification. Consequently the complete fixed class/contact bookkeeping is locally compatible with

`R_105,cusp=R_81,cusp=0`

for every one of the 29 Q states.

This is deliberately only a coarse local valuation noncontradiction. It does **not** construct a global V6 curve or maps. Numerically, the remaining total ramification can be written

- `R_105,off=2r`;
- `R_81,off=48+2r`,

but existence and compatibility of those off-cusp ramification divisors for the same connected h=4 common-cover component are not established.

## Decision

The local special-cusp route removes `0/29` Q states. Its useful output is the exact blocker: class intersections and exceptional contact totals do not couple the two off-cusp ramification divisors strongly enough.

Cycle status: `BLOCKED_NEW_PATTERN_ISOLATED`. The next active route is

`EX1-05G_H4_COMMON_COVER_CORRESPONDENCE_COUPLING`,

which uses the common-cover origin of the two maps rather than attempting to force additional ramification from the six special cusps alone.
