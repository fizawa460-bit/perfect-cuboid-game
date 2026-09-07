# Stage35-EX Goal4Z source lock — one explicit biquaternion, second Q(i)-cyclic principalization target

Scope: continue the two exact Goal4Y algebraic Brauer classes on the Stage35 open receiver `U={h!=0}`. Goal4Z materializes an explicit rational biquaternion representative for Goal4Y class A modulo `Br_0(U)`, and reduces Goal4Y class B to a single exact `Q(i)/Q` cyclic principal-divisor problem. It does **not** compute the full algebraic Brauer group, local evaluations, verticality, or a Brauer--Manin obstruction.

## Exact parent/source locks

Batch base main: `8a04691d03f8ec17cf2236aab3d0f0d2dbde3fc3`.

- Goal4Y artifact: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json`, blob `9351c92747365838cda92d98854ad136df1847d5`.
- Goal4W proper-surface artifact: `stages/stage35-ex/35ex-35/goal4w-full-picard-h1-algebraic-brauer.json`, blob `f4d09daf2961a9cd2a82bba1ce4ce47939f7fadb`.
- Goal4Q boundary geometry: `stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json`, blob `b1795368ad35e357f7ce5a544c871c665e7b59f9`.
- retained 35EX-22 symbol inventory: `stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json`, blob `537ca589cd45112cca4c8f8091f5c8c77264e70d`.
- Stage33 exact marked Picard source: `stages/stage33/33-09/marked-picard-basis-source.json`, blob `c9eb0e195e95263f6753fb29099ffa6d5d74dc13`.
- pinned upstream divisor equations: `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

The exact coordinate adapter is

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`.

The affine equations on `h=1` are

`p^2=1+x^2`, `q^2=1+y^2`, `z^2=x^2+y^2`, `w^2=1+x^2+y^2`.

## The three global units

Set

`u1=p+x`, `u2=q+y`, `u3=w+z`.

Then on `U`

`u1(p-x)=1`, `u2(q-y)=1`, `u3(w-z)=1`.

Thus `u1,u2,u3` are actual global units on `U`, not merely functions on the smaller old 35EX-22 open locus.

Relative to the four boundary types

`(strict infinity conic, eps-edge exceptional, delta-edge exceptional, eta-edge exceptional)`, their divisor parities are

- `u1 : (1,0,1,1)`;
- `u2 : (1,1,0,1)`;
- `u3 : (1,1,1,0)`.

Here `eps` means the eight rational infinity nodes `x=p=0`, `delta` the eight rational infinity nodes `y=q=0`, and `eta` the eight `Q(i)` infinity nodes `z=w=0`. The zero parity on the matching exceptional follows because the numerator and denominator vanish with the same exceptional order; the other cases have an odd pole from `h`.

Therefore

`u1*u2*u3 : (1,0,0,0)`.

For the quadratic character `Q(i)/Q`, this produces exactly the `cc` part of Goal4Y class A: `-1` on all eight strict components and zero on all infinity exceptional components.

## A new Q(sqrt(2))-split rational factor

Set

`r=z+q`.

On the affine receiver, `r=0` implies

`z=-q`, hence `z^2=q^2`, hence `x^2=1`, and then `p^2=2`.

Thus the geometric zero divisor is the union of the four components

`x=+/-1`, `p=+/-sqrt(2)`, `z=-q`,

which are defined over `Q(sqrt(2))`. Under the Stoll adapter these are exactly the `C3s` first-block curves with fixed `e3=+1`:

`a1+e1*a2=0`, `sqrt(2)*a1+e2*b3=0`, `b1+b2=0`.

The factor `r` does not vanish at any affine A1 node from Goal4Q:

- `x=y=z=0` has `q=+/-1`;
- `x=0,q=w=0` has `z^2=-1`, so `z!=0`;
- `y=0,p=w=0` has `z^2=-1` and `q=+/-1`, so `z+q!=0`.

Consequently `(2,r)` has no nontrivial residue on any divisor lying inside `U`: on the four strict zero components, `2` is a square in the constant field `Q(sqrt(2))`, and there is no affine exceptional contribution.

At every component of the infinity boundary, `r/h` has odd exceptional parity. At a generic strict component the numerator is nonzero. At an infinity node where `z+q` vanishes, use

`(z+q)(z-q)=x^2-h^2`.

The complementary factor is a unit there and the defining A1 relation forces `z+q` to vanish to exceptional order two; subtracting the order-one denominator `h` leaves odd parity. At nodes where the numerator is nonzero, the denominator contributes odd parity directly. Hence

`r : (1,1,1,1)`.

It follows that

`u2*u3*r : (1,1,0,0)`.

This is exactly the `ct` / squareclass-`2` residue pattern of Goal4Y class A.

## Explicit Goal4Y class A

Define the algebraic Brauer class on `U`

`A_exp = (-1, u1*u2*u3) + (2, u2*u3*r)`

or, expanded,

`A_exp = (-1,(p+x)(q+y)(w+z)) + (2,(q+y)(w+z)(z+q))`.

Both quaternion summands are unramified on `U` by the unit and `Q(sqrt(2))`-split divisor checks above.

Its boundary characters are exactly:

- strict known indices `1..8`: `(-1)+(2)=(-2)`;
- eps exceptional known indices `93..100`: `(2)`;
- all remaining boundary orbits: zero.

This is the exact Goal4Y class-A residue representative. The difference between `A_exp` and the Goal4Y cohomological class A has zero residues on every component of `S\U`, so purity extends the difference to the smooth proper `S`. Goal4W gives `Br_1(S)/Br_0(S)=0`; hence `A_exp` equals Goal4Y class A modulo `Br_0(U)`.

This explicit representative is not contained in the old 35EX-22 seven-linear-factor presentation because the load-bearing factor `z+q` is new and 35EX-22 was defined on the smaller locus `x*y*p*q*z*w!=0`.

## Goal4Y class B: exact cyclic reduction, literal function still missing

For Goal4Y class B (Smith position 13), the exact V4 cocycle has

`f_B(ct)=0` literally.

Therefore its restriction to `Gal(Q(i,sqrt(2))/Q(i))=<ct>` is zero, and the remaining class is a `Q(i)/Q` cyclic/quaternion problem. In particular the next literal target may be taken in the form

`B_exp = (-1,F_B)`

modulo constants, provided one constructs the exact rational function `F_B`.

An exact Picard lift of `f_B(cc)` in the pinned upstream INDLIST divisor basis is the divisor-class combination

`10:5, 11:-1, 12:5, 13:9, 14:2, 15:6, 18:6, 19:6, 21:-1, 22:6, 23:5, 25:-8, 26:-10, 29:-2, 34:-11, 35:-13, 37:-13, 38:13, 109:-2, 110:1, 111:-1, 113:2, 125:7, 126:1, 127:-2, 133:1, 135:1`.

Call this divisor class `D_B`. The V4 cocycle relation makes `D_B+cc(D_B)` trivial in `Pic(Ubar)`, hence it differs from zero in `Pic(Sbar)` by an explicitly computable integral combination of the 32 boundary components. Therefore the remaining task is a literal principalization:

find `F_B in Q(U)^*` and an integral boundary divisor `E_B` such that

`div_S(F_B)=D_B+cc(D_B)-E_B`,

with the parity of `E_B` matching the Goal4Y B residues:

- strict indices `1..8`: `-1` character;
- exceptional indices `94,96,98,100,101,103,105,107`: `-1` character;
- all other boundary orbits: zero.

Goal4Z does not invent `F_B`. The old seven-factor 35EX-22 presentation is not enough: its simple affine factors do not materialize the resolution-sensitive doubled-edge selection in B while remaining unramified on the full open receiver. The exact next leaf is therefore the `Q(i)` cyclic principal-divisor adapter for this one remaining class.

## Firewall

Certified by Goal4Z:

- one of the two Goal4Y classes has an explicit evaluable rational biquaternion representative modulo constants;
- the second class is reduced from V4 to a single `Q(i)/Q` cyclic/quaternion principalization problem with an exact Picard divisor-class target;
- the old 35EX-22 seven-factor layer is not by itself the missing full adapter.

Not certified:

- an explicit `F_B`;
- explicit rational symbols for both independent classes;
- the full group `Br_a(U)`;
- local evaluation maps;
- verticality relative to the genus-5 fibration;
- a Brauer--Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.
