# Stage36 36-09DP global Q2 2-primary Weil--Chatelet localization source lock

## Sources

1. Brendan Creutz, *A Grunwald--Wang type theorem for abelian varieties*, Acta Arith. 154 (2012), 353--370, DOI 10.4064/aa154-4-2, arXiv:1009.3546v3. Theorem 1.3 is the weak-approximation theorem for the full Weil--Chatelet group.
2. Stage36 36-09DN source lock `stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md`, which freezes the rational-point identification of the nonconstant Brauer quotient with the Weil--Chatelet group for the Stage36 curve.
3. Stage36 36-09DO source lock `stages/stage36/36-09DO/full-2primary-q2-formal-neighborhood-boundary-source-lock.md`, which freezes the dyadic Mattuck/local-duality structure used below.

## Frozen weak-approximation theorem

Let `A/k` be an abelian variety over a number field and `S` a finite set of primes. Creutz Theorem 1.3 states that

`H^1(k,A) -> product_{v in S} H^1(k_v,A)`

is surjective.

This is the full Weil--Chatelet group, not a fixed finite-level subgroup. Creutz explicitly distinguishes this from finite-level questions: the map on `H^1(k,A)[n]` can fail to be surjective for some `n` (including examples with `n=2`). Therefore Stage36 must not replace Theorem 1.3 by a claim of fixed-`2^n` surjectivity.

## 2-primary consequence

Take `k=Q`, `A=J=Jac(C3_2)`, and `S={2}`. Let

`eta in H^1(Q_2,J)(2)`

be any 2-primary local class. By Creutz Theorem 1.3 there is some

`xi in H^1(Q,J)`

with `loc_2(xi)=eta`.

The Weil--Chatelet group is torsion, hence decomposes as the direct sum of its primary components. Write

`xi = xi_(2) + sum_{ell != 2} xi_(ell)`.

Localization is a group homomorphism and respects primary decomposition. Since `eta` is 2-primary, the `ell`-primary component of `loc_2(xi)` is zero for every odd `ell`. Consequently

`loc_2(xi_(2)) = eta`.

Therefore

`H^1(Q,J)(2) -> H^1(Q_2,J)(2)`

is surjective.

This conclusion is compatible with finite-level failure: the global preimage `xi_(2)` of a local class of order `2^n` need not itself have order dividing `2^n`.

## Brauer translation for C3_2

For the smooth projective Stage36 curve

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`

there is the rational point `P0=(0,1)`. The DN source lock freezes the standard consequence that the nonconstant Brauer quotient is identified with the Weil--Chatelet group of the Jacobian, compatibly with localization. Thus on 2-primary components,

`(Br(C3_2)/Br(Q))(2) ~= H^1(Q,J)(2)`

and

`(Br(C3_2 x Q_2)/Br(Q_2))(2) ~= H^1(Q_2,J)(2)`.

Hence the global 2-primary Brauer localization image at `Q_2` equals the entire local nonconstant 2-primary Brauer group.

## Unbounded dyadic depth

The DO source lock freezes an open torsion-free subgroup

`M ~= Z_2^3`

inside `J(Q_2)` and the local Tate/Lichtenbaum duality pairing between `J(Q_2)` and `H^1(Q_2,J)`. The Pontryagin dual of `Z_2^3` has characters of order `2^n` for every `n>=1`. Therefore `H^1(Q_2,J)(2)` has unbounded 2-power exponent.

Combined with the surjectivity above, the global 2-primary localization image is also unbounded: arbitrarily deep dyadic local characters do globalize, though generally by global classes of larger 2-power order than a prescribed finite level.

## Consequence for the P0 formal neighborhood

DO proved that every nonzero sufficiently small Abel--Jacobi displacement from `P0` is detected by some local 2-primary character. DP globalizes that detecting character. Therefore there is no punctured `Q_2`-analytic neighborhood of `P0` on which every **global** 2-primary Brauer class has the same evaluation as at `P0`.

This closes the bounded-image/common-neighborhood alternative left open by DO.

## Global adelic firewall

The preceding statement concerns the projection of global Brauer classes to the single place `Q_2`. It does **not** imply that the retained-open adelic Brauer--Manin set for the full global 2-primary Brauer group is empty. A global class that realizes a chosen `Q_2` character may have nonzero localization/evaluation at other places, and the Brauer--Manin condition is the sum of local invariants over all places.

Thus DP proves neither

`U_ret(A_Q)^{Br(C3_2)(2)} = empty`

nor its nonemptiness. The next exact problem is the adelic annihilator of the global 2-primary localization image under the sum of local Tate pairings. This is where the Cassels--Tate/Poitou--Tate/Mordell--Weil closure interface becomes relevant.

## Firewalls

DP does not prove a Brauer--Manin obstruction, fixed `p=2` exclusion, candidate shrink, receiver emptiness, endpoint closure, or Perfect Cuboid nonexistence. It also does not claim fixed-level `H^1(Q,J)[2^n]` surjectivity.