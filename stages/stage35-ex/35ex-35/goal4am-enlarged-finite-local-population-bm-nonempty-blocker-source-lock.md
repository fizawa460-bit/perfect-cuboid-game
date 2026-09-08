# Stage35-EX Goal4AM source lock — enlarged finite-local population Brauer–Manin nonemptiness blocker

Scope: consume the provisional exact Goal4AL real evaluation only as a route diagnostic. This leaf tests the enlargement
`U(R)^+ x product_{p finite} U(Q_p)` that was introduced to avoid a primitive-source reverse adapter. It does not promote
Goal4AL, compute finite local images, prove a Brauer–Manin obstruction, prove E1, or close Stage35.

## Exact repo inputs

- Audited authority remains V74 / Goal4AK (PR #1720 hostile-audit PASS review `5142248509`, merge `42f20e47babdfdda068a605e3fec489eeace460c`).
- Goal4Y exact artifact: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json`, retained blob `9351c92747365838cda92d98854ad136df1847d5`.
- Goal4Y certifies the smooth rational point `(x,y,p,q,z,w)=(3/4,0,5/4,1,3/4,5/4)` on `U`.
- Goal4AL provisional exact real certificate: `stages/stage35-ex/35ex-35/goal4al-positive-real-class-b-evaluation.json`, retained blob `abe071018509954ff6572fa29ab927ef537d3135`, canonical `cd0830cf69988b3745eeb0d4725761ffd997696fcf3cb7329727087c1c709d56`.
- The normalized affine equations are `p^2=1+x^2`, `q^2=1+y^2`, `z^2=x^2+y^2`, `w^2=1+x^2+y^2`.

## Exact real path

Let `0 <= t <= 1/4` and define

```text
x(t)=3/4,
y(t)=t,
p(t)=5/4,
q(t)=+sqrt(1+t^2),
z(t)=+sqrt(9/16+t^2),
w(t)=+sqrt(25/16+t^2).
```

These identities satisfy all four normalized surface equations exactly. Since `x=3/4` and `p=5/4` throughout, this path avoids every affine A1 singularity listed in Goal4Q. At `t=0` it is the Goal4Y rational smooth point `P0`. For every `t>0`, all six receiver coordinates `x,y,p,q,z,w` are positive, so `P_t` lies in `U(R)^+`. In particular take

`Pplus=P_{1/4}=(3/4,1/4,5/4,sqrt(17)/4,sqrt(10)/4,sqrt(26)/4)`.

Thus `P0` and `Pplus` lie in the same connected component of `U(R)`.

## Source-bound Brauer facts

1. Tetsuya Uematsu, *Continuity of the Local Evaluation Maps*, Theorem 1.1: for a local field `k`, smooth `k`-scheme `X`, and `A in Br(X)`, the local evaluation map `X(k) -> Q/Z` is locally constant. Canonical PDF: `https://ccmath.meijo-u.ac.jp/~uematsu/paper/Continuity_of_the_local_evaluation_maps.pdf`. Therefore every Brauer evaluation is constant along the connected path from `P0` to `Pplus`.

2. J. S. Milne, *Class Field Theory*, v4.03, Theorem VIII.4.2 (fundamental exact sequence): `0 -> Br(Q) -> direct_sum_v Br(Q_v) -> Q/Z -> 0`, with the last map the sum of local invariants. Canonical PDF: `https://www.jmilne.org/math/CourseNotes/CFTc.pdf`. For any `alpha in Br(U)`, evaluating at the rational point `P0` gives `alpha(P0) in Br(Q)`, hence the diagonal adelic point `(P0)_v` has total invariant sum zero.

## Blocker argument

Start with the diagonal adelic point induced by `P0`. Keep every finite component equal to `P0 in U(Q_p)`, but replace only the real component by `Pplus in U(R)^+`. For every `alpha in Br(U)`, local constancy along the real path gives

`inv_infinity alpha(Pplus) = inv_infinity alpha(P0)`.

All finite evaluations are unchanged, so global reciprocity for `alpha(P0) in Br(Q)` gives

`sum_v inv_v alpha(P_v') = 0`.

Therefore

`(P_v') in ( U(R)^+ x product_{p finite} U(Q_p) ) intersect U(A_Q)^Br`.

The enlarged restricted adelic population is Brauer–Manin nonempty. Consequently it can never yield the desired Brauer–Manin emptiness argument for E1, regardless of how completely class A, class B, or any additional Brauer classes are evaluated on the full sets `U(Q_p)`.

This does not block a Brauer route on a *tighter receiver-admissible finite-local population*. It proves that the earlier enlargement trick is too coarse: a source-bound local population / primitive-integral adapter is now required.

## Credit firewall

Certified provisionally by this leaf:
- exact rational-point-to-positive-real path;
- Brauer–Manin nonemptiness of the enlarged population `U(R)^+ x product U(Q_p)`;
- route decision that full-`U(Q_p)` finite-place evaluation cannot close E1.

Not certified:
- complete local evaluation images at any finite prime;
- full algebraic or transcendental Brauer group;
- Brauer–Manin obstruction on the actual E1 receiver population;
- E1, R29, Stage35, endpoint, or Perfect Cuboid closure.
