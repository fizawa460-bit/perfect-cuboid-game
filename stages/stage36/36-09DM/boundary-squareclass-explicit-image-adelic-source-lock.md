# Stage36 36-09DM boundary-squareclass Creutz--Viray explicit-image source lock

## Fixed curve and global reference point

Work on

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`.

Write the four quadratic factors as norms from `E=Q(i)` using

`a=(2,1/2,3,1/3)` and `alpha_j=i*a_j`, so

`t^2+a_j^2 = Norm_{E/Q}(t-alpha_j)`.

The smooth proper curve has the rational point

`P0=(t,z)=(0,1)`,

because the product of the four constant factors is `1`. Stage36 retained-open arithmetic excludes `t=0`, so `P0` is used only as a global Brauer-evaluation reference and is not counted as a retained receiver point.

## Local squareclass-preserving adelic recipe

Choose local t-coordinates

- `t_infinity=2`;
- `t_2=32`;
- `t_3=9`;
- `t_p=p` for every prime `p>3`.

For every branch component set

`u_{v,j}=(t_v-alpha_j)/(-alpha_j)=1+i*(t_v/a_j)`.

The following elementary Hensel criteria are used.

1. For an odd residue characteristic local field, every element congruent to `1` modulo the maximal ideal is a square: apply Hensel to `X^2-u` at `X=1`, since `2` is a unit.
2. In `E_2=Q_2(i)`, normalize the valuation by `v(1+i)=1`, so `v(2)=2`. If `v(epsilon)>2v(2)=4`, then `1+epsilon` is a square by the strong Hensel inequality `v(f(1))>2v(f'(1))` for `f(X)=X^2-(1+epsilon)`.
3. Over the real place, `E tensor_Q R=C`, and every nonzero complex number is a square.

The exact hypotheses are:

- at `p=2`, `v_{E_2}(t_2/a_j)=(8,12,10,10)`, all strictly greater than `4`;
- at `p=3`, `v_3(t_3/a_j)=(2,2,1,3)`, all positive;
- for every `p>3`, every `a_j` is a p-adic unit and `t_p/a_j` is divisible by `p`.

Hence for every place `v` and every `j`,

`[t_v-alpha_j]=[-alpha_j] in (E tensor Q_v)^*/((E tensor Q_v)^*)^2`.

Taking norms shows each rational factor `t_v^2+a_j^2` is a square in `Q_v`. Therefore each displayed t-coordinate lifts to a local point on `C3_2`; choose the product of the four factor square roots for `z_v`. All t-coordinates are different from `0,+/-1,infinity`, so the adelic point lies in the retained open. For all but finitely many primes the chosen point is integral.

## Creutz--Viray evaluation consequence

The 36-09CW source lock freezes the explicit construction

`gamma'(ell)=Cor_{Q(C) tensor L / Q(C)}((ell,t-alpha)_2)`

for `ell in L_1`, with `L=Q(i)^4`.

At the local point `P_v` above, the second-entry squareclass `t_v-alpha` is componentwise the same as at the global rational point `P0`, where it equals `-alpha`. Quaternion symbols depend only on squareclasses. Therefore, for every explicit class represented by `gamma(ell)`,

`gamma(ell)(P_v)=gamma(ell)(P0)` in `Br(Q_v)`

for every place `v`.

The value `gamma(ell)(P0)` is the localization of one global Brauer class in `Br(Q)`. Equivalently, after the Creutz--Viray corestriction expansion it is a finite sum of global quaternion classes. Global Brauer/Hilbert reciprocity gives

`sum_v inv_v(gamma(ell)(P0))=0`.

Adding a constant class from `Br(Q)` also has total invariant zero. Thus the retained-open adelic point is orthogonal to every class in the full Creutz--Viray explicit image, without computing the quotient `L_1/(t-alpha)(Pic^0/2)`.

## Firewalls

This argument proves nonemptiness of the Brauer set for the entire Creutz--Viray explicit image. It does not compute `Pic^0(C3_2)/2`, does not compute the full `L_1` quotient or the rank of the explicit image, and does not identify the Creutz--Viray explicit image with all of `Br(C3_2)[2]/Br(Q)`. The 36-09DD completeness source lock explicitly keeps that possible complement open. Hence no full-Brauer Brauer--Manin obstruction, fixed-p exclusion, receiver closure, endpoint closure, or Perfect Cuboid theorem credit is granted.
