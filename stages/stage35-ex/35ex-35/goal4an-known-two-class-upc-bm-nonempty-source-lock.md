# Stage35-EX Goal4AN source lock — the two known algebraic Brauer classes do not empty the exact surface-open adelic population

Scope: continue after the exact-head Goal4AM route blocker. Goal4AN tightens the finite-place population from full `U(Q_p)` to the exact algebraic receiver open

```text
U_PC = {p^2=1+x^2, q^2=1+y^2, z^2=x^2+y^2, w^2=1+x^2+y^2, x*y*p*q*z*w != 0}
```

with the positive real component at infinity and the usual restricted-product integrality condition. It tests only the two fixed independent algebraic classes A and B constructed in Goal4Y and explicitly represented by Goal4Z/Goal4AK. It does not compute the full algebraic Brauer group, the transcendental Brauer group, the primitive-source reverse population, E1, or Stage35.

## Exact repo inputs

- Audited authority remains V74 / Goal4AK: PR #1720 hostile-audit PASS review `5142248509`, merged as `42f20e47babdfdda068a605e3fec489eeace460c`.
- 35EX-22 exact surface-open restricted-product construction:
  - source `stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md`, blob `8be8f94accba0253ad1221ce0025eacdb4537a97`;
  - artifact `stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json`, blob `537ca589cd45112cca4c8f8091f5c8c77264e70d`.
- Goal4Y two independent algebraic classes: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json`, blob `9351c92747365838cda92d98854ad136df1847d5`.
- Goal4Z class-A explicit representative source lock: `stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization-source-lock.md`, blob `3a1c2174ee6e45bb693791ae2e974ed2f27fe2a3`.
- Goal4AK audited class-B representative assembly: `stages/stage35-ex/35ex-35/goal4ak-explicit-fb-assembly.json`, blob `5c543b8e5172e19cdb143ba69fcaa55098e5920f`.
- Goal4AL exact real certificate: `stages/stage35-ex/35ex-35/goal4al-positive-real-class-b-evaluation.json`, blob `abe071018509954ff6572fa29ab927ef537d3135`, canonical `cd0830cf69988b3745eeb0d4725761ffd997696fcf3cb7329727087c1c709d56`.
- Goal4AM enlarged-population blocker: `stages/stage35-ex/35ex-35/goal4am-enlarged-finite-local-population-bm-nonempty-blocker.json`, canonical `a04eabc03f1b58f3395d670fc13a81e277d2766b5e80e2b0d5d084dc34d5a5ee`.

The two representatives are

```text
A = (-1,(p+x)(q+y)(w+z)) + (2,(q+y)(w+z)(z+q))       mod Br_0(U),
B = (-1,F_B),  F_B=A31/B31                            mod Br_0(U).
```

Goal4Y certifies that their classes are independent. No assertion that they exhaust `Br_a(U)/Br_0(U)` is made.

## 35EX-22 restricted-product input

35EX-22 provides the smooth rational specialization

```text
P*=(x,y,p,q,z,w)=(272/225,0,353/225,1,272/225,353/225).
```

It is a smooth point of the affine surface and lies outside `U_PC` only because `y=0`.

For any fixed finite set of places, 35EX-22 proves that one may keep `x=272/225`, `p=353/225` and choose nonzero `y_v` sufficiently close to zero so that the three remaining square roots `q_v,z_v,w_v` exist near `1,272/225,353/225`, the resulting point lies in `U_PC(Q_v)`, and it may be chosen inside any prescribed sufficiently small local neighborhood of `P*`.

For every prime `l>=173`, 35EX-22 independently proves existence of an integral smooth open point

```text
P_l in U_PC(Z_l),
```

using the first source conic, the smooth genus-5 fiber, Hasse--Weil, and Hensel lifting. Thus the good-prime components can be chosen integral without imposing one global rational specialization.

## Brauer facts used

### Local constancy

Tetsuya Uematsu, *Continuity of the Local Evaluation Maps*, Theorem 1.1: for a local field `k`, smooth `k`-scheme `X`, and `alpha in Br(X)`, the evaluation map `X(k) -> Br(k) -> Q/Z` is locally constant.
Canonical source: `https://ccmath.meijo-u.ac.jp/~uematsu/paper/Continuity_of_the_local_evaluation_maps.pdf`.

Therefore, for each of A and B and for each place in a fixed finite set, the 35EX-22 deformation can be made sufficiently small that its invariant equals the invariant at `P*`. Since only two classes and finitely many places are involved, one common local neighborhood may be used place-by-place.

### Integral good-prime vanishing

Each fixed Brauer class on the finite-type Q-variety `U` is represented by finite algebraic data and therefore spreads out after inverting finitely many rational primes. Hence there is a finite set `S_ext` such that A and B extend to Brauer classes on a smooth integral model over `Z[1/S_ext]` on the relevant smooth open.

J. S. Milne, *Etale Cohomology*, Chapter IV, Corollary 2.13 states that for a Henselian local ring `R`,

```text
Br(R) ~= Br(R/m).
```

Canonical source: `https://www.jmilne.org/math/Books/ECpup4.pdf`.
For `R=Z_l`, the residue field is finite and its Brauer group is zero. Consequently, outside `S_ext`, evaluation of either extended class at any integral `Z_l` point is zero in `Br(Q_l)`.

Enlarge a finite set `S` to contain `S_ext`, all primes `<173`, and all denominator/bad-model primes needed so that `P*` itself is integral on the same model outside `S`.

### Global reciprocity at P*

For either `alpha=A` or `B`, the rational evaluation `alpha(P*)` lies in `Br(Q)`. Global Brauer reciprocity therefore gives

```text
sum_v inv_v(alpha(P*)) = 0.
```

We use the global Brauer exact sequence in J. S. Milne, *Class Field Theory*, v4.03, with the final map the sum of local invariants. Canonical source: `https://www.jmilne.org/math/CourseNotes/CFT.pdf`.

## Restricted adelic construction

Choose a modified adelic point `(Q_v)` as follows.

1. At infinity, choose a positive `y_infinity>0` sufficiently close to zero in the 35EX-22 local deformation. Then `Q_infinity` lies in `U_PC(R)^+` and, by local constancy, both A and B have the same real invariants as at `P*`.
2. For every finite `l in S`, choose the 35EX-22 nonzero-`y_l` local deformation sufficiently close to `P*` that both A and B retain their `P*` invariants.
3. For every finite `l notin S`, use an integral point `P_l in U_PC(Z_l)` supplied by 35EX-22. Both A and B evaluate to zero there. The diagonal point `P*` is also integral outside `S`, so its A/B evaluations are zero there as well.

Thus for either `alpha=A` or `B`, every local invariant of `(Q_v)` agrees with the corresponding local invariant of the diagonal `P*` adelic point. Global reciprocity therefore gives

```text
sum_v inv_v(alpha(Q_v))=0.
```

The point `(Q_v)` is a genuine restricted-product adele because all but finitely many finite components lie in `U_PC(Z_l)`. Therefore

```text
(U_PC(R)^+ x product'_l U_PC(Q_l))^{<A,B>} != empty.
```

In particular, Goal4AL's exact value `inv_infinity(B)=1/2` on `U_PC(R)^+` is not itself an obstruction: on the constructed adelic point it is compensated by finite-place invariants, exactly as global reciprocity requires.

## Route consequence

The two currently explicit independent algebraic classes A and B cannot, by themselves or by any F2-linear combination of them plus constants, empty the exact algebraic surface-open adelic population `U_PC(A_Q)` with positive real component.

This is stronger than Goal4AM's full-`U(Q_p)` enlargement blocker, because the finite components now lie in the exact smaller surface-open `U_PC` and satisfy restricted-product integrality. It is still not a statement about the actual primitive/canonical Stage35-EX source population: 35EX-21 explicitly leaves that reverse population adapter unproved.

The next useful leaf must therefore do at least one of:

- construct a genuinely tighter primitive/source-admissible finite-local population and evaluate against it;
- prove that A and B exhaust the relevant algebraic Brauer quotient and then investigate whether additional transcendental classes exist;
- or switch to a preserved non-Brauer route.

## Credit firewall

Certified provisionally by Goal4AN only:
- one restricted-product adelic point on `U_PC` with positive real component orthogonal to the span of the two known classes A and B;
- the exact real `1/2` value of B is not a standalone obstruction on this population;
- the known two-class Brauer span cannot close E1 through `U_PC` alone.

Not certified:
- `Br_a(U)/Br_0(U)=<A,B>`;
- any statement about the transcendental Brauer group;
- Brauer--Manin nonemptiness of the actual primitive/canonical E1 source population;
- complete finite local evaluation images;
- E1, R29, Stage35, endpoint, or Perfect Cuboid closure.
