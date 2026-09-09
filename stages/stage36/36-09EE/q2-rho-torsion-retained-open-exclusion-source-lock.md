# Stage36 36-09EE Q2 rho-torsion retained-open exclusion source lock

## Purpose

36-09EC proves for the fixed genus-3 curve

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`

that

`T_2 Sel(J)=J(Q)^hat_2`, `J=Jac(C3_2)`.

36-09ED then reduces the infinite Mordell--Weil part to one saturated `Z_2` direction.  The present leaf does not enumerate that direction.  Instead it uses the rank-zero `rho` quotient to show that the completed Abel--Jacobi image of the retained-open curve has **empty intersection already at Q_2** with the localized global 2-adic Mordell--Weil completion.

This is the `S34-W03 RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION` pattern: prove the exact joint receiver/intersection condition empty without classifying a larger auxiliary point set.

## Locked Stage36 inputs

1. 36-09DR fixes the quotient

   `pi_rho:C3_2 -> C_rho`,

   `v=t-1/t`, `Y=z/t^2`,

   `C_rho: Y^2=(v^2+25/4)(v^2+100/9)`.

2. 36-09DS fixes the norm/pushforward map

   `Psi:J -> E_tau x E_sigma x E_rho`,

   with rho component `pi_{rho,*}`.  For the Abel--Jacobi map `iota(P)=[P-P0]`, functoriality gives

   `pi_{rho,*} iota(P)=[pi_rho(P)-pi_rho(P0)]`.

   Only this norm/pushforward identity is used from the historical DS source; the later hostile-audited DS torsion correction remains authoritative for pro-Selmer injectivity claims.

3. 36-09EC proves

   `rank E_rho(Q)=0`

   and `T_2 Sel(J)=J(Q)^hat_2`.

4. 36-09DN fixes the rational reference point

   `P0=(t,z)=(0,1)`

   and the retained-open boundary containing

   `t=0, 1, -1, infinity`.

5. 36-09DQ identifies the full global 2-primary Brauer annihilator with `image(T_2 Sel(J))` in the product of local 2-adic completions and gives the exact orthogonality equivalence for the retained-open adelic curve image.

## A convenient rho Weierstrass model

Write

`A=625/36`, `B=25/3`, `c=2B=50/3`.

Then

`C_rho: Y^2=v^4+A v^2+B^2`.

With the rational point `O_rho=(0,B)` as origin, on `v != 0` set

`X=(Y+B)/v^2`,

`W=v(X^2-1)`.

The quartic identity gives

`W^2=(X^2-1)(cX+A)`.

Set `x=cX`, `y=cW` and finally `x0=36x`, `y0=216y`.  This yields the integral full-rational-2-torsion model

`E_rho^W: y0^2=(x0-600)(x0+600)(x0+625)`.

The transformation extends to the smooth projective curves.  Its four rational 2-torsion points, expressed back on `C_rho`, are

- `O_rho=(0,+25/3)`;
- `(0,-25/3)`;
- the infinity branch `I_+` with `Y/v^2 -> +1`;
- the infinity branch `I_-` with `Y/v^2 -> -1`.

At `P0=(0,1)` one has `v=t-1/t -> infinity` and `Y=z/t^2`, with `Y/v^2 -> +1`. Hence

`pi_rho(P0)=I_+`,

which is the 2-torsion point `(600,0)` on `E_rho^W`.

## Global 2-primary Mordell--Weil completion of E_rho

Because `rank E_rho(Q)=0`, its abstract 2-adic completion is its rational 2-primary torsion subgroup.

The three nonzero rational 2-torsion points on the Weierstrass model are

`T_1=(600,0)`, `T_2=(-600,0)`, `T_3=(-625,0)`.

For a full-rational-2-torsion model `y^2=(x-e1)(x-e2)(x-e3)`, the standard halving criterion says that `(ei,0)` is twice a rational point only if both differences `ei-ej` and `ei-ek` are rational squares.  Here:

- at `600`: the differences are `1200` and `1225=35^2`, and `1200` is not a square;
- at `-600`: one difference is `-1200`, not a rational square;
- at `-625`: the relevant differences are negative.

Thus no nonzero rational 2-torsion point is divisible by 2 in `E_rho(Q)`.  Hence there is no rational point of order 4, and therefore no higher rational 2-power torsion.  Consequently

`E_rho(Q)(2)=E_rho[2](Q) ~= (Z/2)^2`,

and

`E_rho(Q)^hat_2 = E_rho[2](Q)`.

This uses only the 2-primary part; no claim about possible odd rational torsion is needed.

## Q2 completion has no hidden odd-torsion kernel

For a compact p-adic elliptic-curve group, the kernel of

`E(Q_p) -> E(Q_p)^hat_p`

is the maximal prime-to-p torsion subgroup.  This follows from the standard local filtration: an open formal subgroup is a torsion-free `Z_p`-module and multiplication by `p` is an automorphism on the finite prime-to-p torsion.

We therefore show directly that `E_rho^W(Q_2)` has no odd torsion.

For the integral model

`y^2=x^3+625x^2-360000x-225000000`,

the invariants satisfy

`v_2(c4)=4`, `v_2(Delta)=12`, hence `v_2(j)=0`.

Thus the minimal curve is not multiplicative at 2.  If it has good reduction, prime-to-2 torsion injects into `E(F_2)`, whose order is at most 5 by Hasse, so only primes 3 or 5 can occur.  If it has additive reduction, the standard Neron filtration has `E_0/E_1` a 2-group and the additive Kodaira component group has no odd prime divisor other than possibly 3.  Therefore it is enough to rule out Q_2-rational 3- and 5-torsion.

Use the standard division polynomials for a Weierstrass equation with `a1=a3=0`.  For the 3-division polynomial, the ascending coefficient 2-adic valuations are

`[8,8,7,2,0]`.

Its Newton polygon is the single segment from `(0,8)` to `(4,0)`, so every root in an algebraic closure has valuation `2`.  Writing `x=4u` and dividing by `2^8`, the reduction modulo 2 is

`u^4+u^3+1`,

which has no root in `F_2`.  Hence the 3-division polynomial has no root in `Q_2`.

For the 5-division polynomial, the ascending coefficient valuations are

`[24,24,23,18,16,14,12,11,8,8,4,2,0]`.

Again the Newton polygon is one segment of slope `-2`, so a Q_2 root would have `x=4u` with `u` a 2-adic unit.  After dividing by `2^24`, the nonzero mod-2 terms have degrees

`0,3,4,5,6,8,10,11,12`.

The resulting polynomial is nonzero at both elements of `F_2`: its value is `1` at `u=0` and also `1` at `u=1`.  Thus there is no Q_2-rational 5-torsion.

Therefore

`E_rho^W(Q_2)[odd]=0`,

and the natural completion map

`E_rho(Q_2) -> E_rho(Q_2)^hat_2`

is injective.

Standard references for the ingredients are Silverman, *The Arithmetic of Elliptic Curves*, Chapters III and VII (division polynomials, reduction filtration and torsion under reduction), together with the standard Newton polygon theorem for local fields.

## Empty Q2 retained-open intersection

Suppose for contradiction that

`P in U_ret(Q_2)`

has completed Abel--Jacobi image in

`loc_2(J(Q)^hat_2)`.

Apply the rho component of `Psi`.  Since completion and localization are functorial,

`[pi_rho(P)-pi_rho(P0)]`

in `E_rho(Q_2)^hat_2` lies in the localization of

`E_rho(Q)^hat_2=E_rho[2](Q)`.

The local completion map is injective, so the equality already holds in `E_rho(Q_2)`.  Because `pi_rho(P0)=I_+` is itself rational 2-torsion,

`pi_rho(P)`

must be one of the four rational 2-torsion points listed above.

A retained-open point has finite nonzero `t`, so its rho quotient is affine.  The only affine points in that four-point set have

`v=0`.

But `v=t-1/t=0` implies

`t=+1` or `t=-1`,

and both are excluded retained-open boundary values by 36-09DN.  Contradiction.

Hence

`iota_hat_2(U_ret(Q_2)) intersect loc_2(J(Q)^hat_2) = empty`.

Since 36-09EC gives `T_2 Sel(J)=J(Q)^hat_2`, the Q_2 projection of the global retained-open/pro-Selmer intersection is already empty. Therefore

`iota_hat_2(U_ret(A_Q)) intersect image(T_2 Sel(J)) = empty`.

By the exact 36-09DQ Brauer--Manin translation, the retained-open adelic set orthogonal to the full global 2-primary Brauer subgroup is empty.

## Credit boundary

36-09EE may therefore claim, for this fixed `p=2` curve:

- the retained-open curve/pro-Selmer intersection is empty;
- the full global 2-primary Brauer set on the retained-open locus is empty;
- a 2-primary Brauer--Manin obstruction is obtained.

This leaf does **not** by itself promote that obstruction through the Stage36 physical quotient/receiver adapter.  In particular it does not yet claim fixed-parameter exclusion, candidate-set shrink, `R29-CAMP2` closure, `Q11-CAMPEDELLI` closure, endpoint closure, or a Perfect Cuboid result.  Those remain behind a separate promotion/audit boundary.
