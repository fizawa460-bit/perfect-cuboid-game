# Stage36 36-09T Q(i) twist-rankjump proof note

Status: exact internal proof note for the 36-09T preflight. It introduces no receiver or endpoint closure credit.

## 1. Middle quotient and its -1 twist

Write

- `Nminus=p^2-2p-1`,
- `Nplus=p^2+2p-1`,
- `k=Nplus/Nminus`,
- `rho=2*(p^2+1)/Nminus`.

On the retained physical open `p!=0,+/-1`, one has `k!=0,+/-1` and
`rho^2=2*(k^2+1)`.

The middle quotient from 36-09N/36-09O is, after the rational scaling
`x=Nminus^2*U`, `y=Nminus^3*V`,

`E_sigma: V^2=U*(U+1)*(U+k^2)`.

Equivalently before that scaling,

`E_sigma: y^2=x*(x+Nminus^2)*(x+Nplus^2)`.

The 36-09S quotient is

`E_sigma_tau: y^2=x*(x-Nminus^2)*(x-Nplus^2)`.

Hence `E_sigma_tau` is exactly the quadratic twist of `E_sigma` by `-1`.
Over `Q(i)` the isomorphism is

`phi(x,y)=(-x, i*y)`.

Complex conjugation fixes the image of rational `E_sigma(Q)` points and sends
`phi(E_sigma_tau(Q))` to its elliptic negative.

## 2. Fiberwise nontorsion of the retained middle section

36-09M proves on every retained physical fiber

`E_k(Q)[2^infinity] = Z/4 x Z/2`,

with nonzero rational 2-torsion x-coordinates `0,-1,-k^2` and order-4
x-coordinates `+k,-k`.

The Mazur classification source-lock already retained by 36-09S says that a
rational elliptic curve with full rational 2-torsion has torsion
`Z/2 x Z/(2n)` for `n=1,2,3,4`. Since the retained fibers have rational order 4,
`n` must be even. The exact 2-primary group from 36-09M excludes `n=4`, so the
full torsion group is exactly

`E_k(Q)_tors = Z/4 x Z/2`

for every retained physical fiber.

The 36-09N generic section becomes

`P_sigma=(k^2,-rho*k^2)`

on `E_k`. Its x-coordinate `k^2` is not any torsion x-coordinate above on the
retained open: equality with `0,+k,-k` forces `k=0,+/-1`, equality with `-k^2`
forces `k=0`, and `k^2=-1` has no rational solution. Therefore `P_sigma` is
nontorsion on every retained rational physical fiber. In particular

`rank E_sigma,p(Q) >= 1`

fiberwise, not merely generically.

## 3. Generic and specialized rank over Q(i)

Let `K=Q(p)` and `L=K(i)`. On `E_sigma(L) tensor Q`, complex conjugation gives a
`+/-` eigenspace decomposition. The `+` eigenspace is
`E_sigma(K) tensor Q`; via `phi`, the `-` eigenspace is
`E_sigma_tau(K) tensor Q`. This is the elementary quadratic-twist rank
decomposition.

36-09N gives `rank E_sigma(K)=1`. 36-09R/36-09S give
`rank E_sigma_tau(K)=0`. Hence

`rank E_sigma(L)=1`.

Now fix a retained rational specialization admitting a receiver point. 36-09S
proves that the corresponding `E_sigma_tau(Q)` point is nontorsion. Its image
under `phi` is a nontorsion anti-invariant point `Q_minus` in
`E_sigma(Q(i))`, while `P_sigma` is nontorsion and invariant.

They are independent modulo torsion. Indeed, if
`m*P_sigma+n*Q_minus=T` is torsion, conjugation gives
`m*P_sigma-n*Q_minus=conj(T)`. Subtracting gives
`2*n*Q_minus=T-conj(T)`, so n=0 because `Q_minus` is nontorsion; then m=0 because
`P_sigma` is nontorsion.

Therefore every retained receiver point forces

`rank E_sigma,p(Q(i)) >= 2`,

whereas the generic `Q(i)(p)` rank is exactly 1. Thus receiver existence forces
a genuine `Q(i)` rank jump.

## 4. Why this does not double-charge the two quotient conditions

The 36-09O maps are

`R=t+1/t`, `S=t-1/t`, `v=y/t^2`,

with `R^2-S^2=4`. Conversely a compatible pair with common `v` and
`R^2-S^2=4` reconstructs

`t=(R+S)/2`, `1/t=(R-S)/2`, `y=t^2*v`.

Away from the already-excluded boundaries this compatible-pair fiber product is
exactly the original top genus-3 receiver open. Therefore merely requiring
`rank(E_tau)>0` and `rank(E_sigma_tau)>0` does not create a smaller exact
receiver, and requiring compatible points returns to the original receiver.

The `Q(i)` rank-jump formulation is a cleaner single-family gate, not a
candidate-set shrink and not an independence claim between the E_tau and
E_sigma_tau obligations.

## 5. Cycle classification

`36-09T` is `PASS_NEW_GATE_FROM_STRONGER_VIEW`:

- compatible two-quotient point fiber product: `EQUIVALENT` to the top receiver open;
- rank-only S34-W03 intersection: `BLOCKED` because positive ranks do not supply compatible points;
- S34-W02 global MW congruence: `BLOCKED` at present because no complete variable-fiber MW basis is available on the rank-jump locus;
- Q(i) twist-eigenspace rank-jump gate: `LIVE`, selected;
- Gaussian/norm compression on the same Q(i) structure: `UNTESTED` and naturally adjacent;
- variable-prime adelic reciprocity: `UNTESTED`;
- standard Campedelli arithmetic transfer: `UNTESTED`.

No receiver, R29, Q11, endpoint, or perfect-cuboid closure follows here.
