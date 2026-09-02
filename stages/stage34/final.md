# Stage34 final — self-contained closure of the Stage29 EXT-C receiver

```text
STAGE=Stage34
STATUS=AUDITED_FINAL_MERGE_NOT_AUTHORIZED
SOURCE_RECEIVER=R29-EXT-CHANG-C
SOURCE_KERNEL=K16-C3-EXT-C-PRIMITIVE-DIVISOR
PARENT_ROUTE=J12-PARAMETRIC
RECEIVER_STATUS=CLOSED
KERNEL_STATUS=DISCHARGED_BY_STAGE34_REPLACEMENT_ROUTE
PARENT_ROUTE_STATUS=OPEN
PERFECT_CUBOID_CONCLUSION=NONE
```

This file is the Stage34 mathematical closeout surface. The algebraic reductions and the finite exclusion predicates needed to identify every closure group are stated here. Repository files, hashes, audit reviews and CI runs at the end are reproducibility provenance, not substitutes for omitted mathematical steps.

## 1. Exact theorem and population

For

```text
q = 20/21, 80/39, 24/7, 84/13, 48/55, 20/99, 60/11
```

put

\[
E_q:\ y^2=x(x+1)(x+q^2).
\]

For the first six fibers the authoritative population is the complete rank-one free lattice modulo all torsion,

\[
Q=nP_q+T,\qquad n\ge1,\qquad T\in E_q(\mathbf Q)_{tors},
\]

and for `q=60/11` it is the complete rank-two lattice

\[
Q=aG_1+bG_2+T,\qquad (a,b)\in\mathbf Z^2\setminus\{(0,0)\},
\qquad T\in E_q(\mathbf Q)_{tors}.
\]

The locked Mordell--Weil generators span the full free parts. Thus this is not a bounded-multiple, selected-ray, or finite-box theorem.

Stage34 proves

\[
\boxed{F_3(Q)\notin\mathbf Q^2}
\]

for every non-torsion point in that full seven-fiber population.

## 2. Exact Face-3 cover

On `E_q`,

\[
F_3(Q)=\left(\frac{2yq}{q^2-x^2}\right)^2+1+q^2.
\]

Using `y^2=x(x+1)(x+q^2)` gives

\[
F_3(Q)=\frac{A_q(x)B_q(x)}{(q^2-x^2)^2},
\]

with

\[
A_q(x)=x^2+q^2,
\]

\[
B_q(x)=(1+q^2)x^2+4q^2x+q^2(1+q^2).
\]

Hence, away from `x=\pm q`, Face-3 is a square exactly when the point lifts to

\[
C_q:\quad
\begin{cases}
y^2=x(x+1)(x+q^2),\\
z^2=A_q(x)B_q(x).
\end{cases}
\]

The eight branch points of the degree-four map `C_q -> P^1_x` are simple and disjoint for `q\ne0,\pm1`, so Riemann--Hurwitz gives `g(C_q)=5`.

## 3. Pole firewall

The points above `x=q` are `(q,\pm q(q+1))`, and those above `x=-q` are `(-q,\pm q(q-1))`. The duplication formula on

\[
y^2=x^3+(1+q^2)x^2+q^2x
\]

shows that every one of these four points doubles to `(0,0)`. Since `(0,0)` is nonzero 2-torsion, every pole point has exact order four. They are therefore outside the non-torsion receiver. The cover equivalence of Section 2 has no receiver exception.

## 4. Exact squareclass reduction: 104 -> 30 -> 22 -> 14

Write `q=a/b` in lowest positive terms and `x=X/Z` with `gcd(X,Z)=1`. Put

\[
A_h=b^2X^2+a^2Z^2,
\]

\[
B_h=b^2(a^2+b^2)X^2+4a^2b^2XZ+a^2(a^2+b^2)Z^2.
\]

Because

\[
B_h-(a^2+b^2)A_h=4a^2b^2XZ,
\]

every odd prime in `gcd(A_h,B_h)` divides `ab`. Thus a square `A_hB_h` forces

\[
A_h=d u^2,\qquad B_h=d v^2
\]

for a positive squarefree `d` supported on `rad(2ab)`.

The complete raw `d` lists are:

| q | rad(2ab) | raw squareclasses |
|---|---:|---|
| 20/21 | 210 | 1,2,3,5,6,7,10,14,15,21,30,35,42,70,105,210 |
| 80/39 | 390 | 1,2,3,5,6,10,13,15,26,30,39,65,78,130,195,390 |
| 24/7 | 42 | 1,2,3,6,7,14,21,42 |
| 84/13 | 546 | 1,2,3,6,7,13,14,21,26,39,42,78,91,182,273,546 |
| 48/55 | 330 | 1,2,3,5,6,10,11,15,22,30,33,55,66,110,165,330 |
| 20/99 | 330 | 1,2,3,5,6,10,11,15,22,30,33,55,66,110,165,330 |
| 60/11 | 330 | 1,2,3,5,6,10,11,15,22,30,33,55,66,110,165,330 |

This is `104` raw squareclasses.

### 4.1 Sum-of-two-squares filter: 104 -> 30

Since

\[
A_h=(bX)^2+(aZ)^2=d u^2,
\]

any prime `p\equiv3 (mod 4)` occurs in `A_h` to even valuation. Because `d` is squarefree, such a prime cannot divide `d`. The surviving lists are therefore

```text
20/21 : 1,2,5,10
80/39 : 1,2,5,10,13,26,65,130
24/7  : 1,2
84/13 : 1,2,13,26
48/55 : 1,2,5,10
20/99 : 1,2,5,10
60/11 : 1,2,5,10
```

total `30`.

### 4.2 Good-prime projective obstruction: 30 -> 22

For a candidate `(q=a/b,d)`, an eligible obstruction prime is any prime

\[
p\nmid 2ab(a^2-b^2)(a^2+b^2)d.
\]

Define

\[
E_h=XZ(X+Z)(b^2X+a^2Z).
\]

A rational point necessarily reduces to some `[X:Z]\in P^1(F_p)` for which all three quantities

\[
E_h,\qquad A_h/d,\qquad B_h/d
\]

are quadratic residues modulo `p` (zero allowed). Therefore one witness prime with no such projective residue rigorously kills the class; no heuristic prime-selection convention is load-bearing.

The eight exact witness eliminations are

```text
q=20/21, d=5,10      : p=23
q=84/13, d=13,26     : p=31
q=48/55, d=5,10      : p=23
q=20/99, d=5,10      : p=23
```

and the full 22 survivors are

```text
20/21 : 1,2
80/39 : 1,2,5,10,13,26,65,130
24/7  : 1,2
84/13 : 1,2
48/55 : 1,2
20/99 : 1,2
60/11 : 1,2,5,10
```

### 4.3 Exact Q_7 obstruction: 22 -> 14

The remaining eight non-{1,2} classes are

```text
80/39 : 5,10,13,26,65,130
60/11 : 5,10.
```

For each, `d` is a 7-adic unit. Scale a hypothetical `Q_7` point so `X,Z` are integral and not both divisible by 7. Exhausting the eight points of `P^1(F_7)` gives no residue for which `E_h`, `A_h/d`, and `B_h/d` are simultaneously squares. Hence these eight classes are `Q_7`-insoluble.

Thus, on every locked fiber, the only possible squareclasses are exactly

\[
\boxed{d=1,2}.
\]

## 5. The two genus-one auxiliary quartics

For `d=1`, parameterize `x^2+q^2=u^2` by

\[
x=q\frac{t^2-1}{2t},\qquad
u=q\frac{t^2+1}{2t}.
\]

The remaining equation is

\[
K_{q,1}:\quad
W^2=(1+q^2)t^4+8qt^3+2(1+q^2)t^2-8qt+(1+q^2).
\]

For `d=2`, parameterize `x^2+q^2=2u^2` by

\[
x=q\frac{2t^2-4t+1}{2t^2-1},
\qquad
u=-q\frac{2t^2-2t+1}{2t^2-1},
\]

and obtain

\[
K_{q,2}:\quad
W^2=4(q+1)^2t^4-8(q+1)^2t^3+8(1+q^2)t^2-4(q-1)^2t+(q-1)^2.
\]

Both quartics are smooth genus-one curves. Their binary-quartic invariants agree, so they have the same Jacobian, but Stage34 never equates their rational point sets merely from that fact.

## 6. Exact pullback to the receiver

Use homogeneous `[T:S]`.

For `d=1`,

\[
[X:Z]=[a(T^2-S^2):2bTS].
\]

There is no projective base point. The two rational preimages of `x=\infty` are `t=0,\infty`; both map to the elliptic origin and have zero free part. The equations for `x/q=\pm1` have discriminant 8, so there are no rational pole preimages.

For `d=2`,

\[
[X:Z]=[a(2T^2-4TS+S^2):b(2T^2-S^2)].
\]

There is no rational preimage of `x=\infty`, while `t=0,1,1/2,\infty` map to `x=\pm q`; these are exactly the order-four poles of Section 3.

Therefore every non-torsion `C_q(Q)` point maps, without an omitted exceptional case, to a rational matching point on exactly one of `K_{q,1}` or `K_{q,2}` with the same finite non-pole `x`.

## 7. Reconstruction as four square factors

For `d=1`, set

\[
U=T^2-S^2,\qquad V=2TS,
\]

and for `d=2`, set

\[
U=2T^2-S^2,\qquad V=2T^2-4TS+S^2.
\]

In both cases define

\[
A=aU+bV,\qquad B=bU+aV.
\]

The matching elliptic equation becomes a square multiple of

\[
H=UVAB.
\]

Explicitly,

\[
H_1=2TS(T-S)(T+S)
(bT^2+2aTS-bS^2)(aT^2+2bTS-aS^2),
\]

and

\[
H_2=(2T^2-S^2)(2T^2-4TS+S^2)
(2(a+b)T^2-4bTS+(b-a)S^2)
(2(a+b)T^2-4aTS+(a-b)S^2).
\]

Thus every receiver-relevant point lies on a branch

\[
U=\delta_U r_U^2,
\quad V=\delta_V r_V^2,
\quad A=\delta_A r_A^2,
\quad B=\delta_B r_B^2,
\]

where the product squareclass is trivial.

## 8. Complete odd-prime and 2-adic branch patterns

For primitive `[T:S]`, `gcd(U,V)` divides 2 for both `d=1` and `d=2`. Hence no odd prime divides both `U` and `V`.

From

\[
A=aU+bV,\qquad B=bU+aV,
\]

and

\[
aB-bA=(a^2-b^2)V,
\qquad
aA-bB=(a^2-b^2)U,
\]

an odd squareclass prime can occur only in `ab(a^2-b^2)`. Its only parity patterns are

```text
p | a           : none, {U,B}, {V,A}
p | b           : none, {U,A}, {V,B}
p | a^2-b^2     : none, {A,B}.
```

The resulting odd-pattern counts are

```text
20/21 54; 80/39 216; 24/7 36; 84/13 108;
48/55 108; 20/99 216; 60/11 108.
```

### 8.1 The d=2 2-adic pattern

All seven fibers have odd `b` and `v_2(a)>=2`. If `S` is odd, then `U,V,A,B` are all odd. If `S` is even, primitiveness makes `T` odd; writing `S=2s` gives

\[
v_2(U)=v_2(V)=1,
\]

while `aU,aV` have valuation at least 3 and `bV,bU` valuation 1, so

\[
v_2(A)=v_2(B)=1.
\]

Thus the only `d=2` parity patterns are

```text
none, {U,V,A,B}.
```

### 8.2 The d=1 2-adic pattern

Here `U=T^2-S^2`, `V=2TS`.

If `T,S` have opposite parity, then `U` and `B` are odd. Square parity requires `v_2(V)` and `v_2(A)` to have the same parity. For `v_2(a)=2` this gives no 2-squareclass; for `v_2(a)>=3` it gives either `none` or `{V,A}`.

If `T,S` are both odd, then `v_2(V)=v_2(A)=1` and `v_2(U)>=3`. Square parity forces `v_2(U)` and `v_2(B)` to have the same parity, hence either `{V,A}` or all four factors. When `v_2(a)=2`, the `{V,A}` option is impossible: if `v_2(U)>3` then `v_2(B)=3`, and in the equality case the required even/even parity also fails. Therefore

```text
v2(a)=2   : none, {U,V,A,B}
v2(a)>=3  : none, {V,A}, {U,V,A,B}.
```

For the seven fibers

```text
v2(a)=2 : 20/21,84/13,20/99,60/11
v2(a)=3 : 24/7
v2(a)=4 : 80/39,48/55.
```

Including at most eight sign patterns with positive total product gives the exact finite over-cover sizes

| q | d=1 | d=2 |
|---|---:|---:|
| 20/21 | 864 | 864 |
| 80/39 | 5184 | 3456 |
| 24/7 | 864 | 576 |
| 84/13 | 1728 | 1728 |
| 48/55 | 2592 | 1728 |
| 20/99 | 3456 | 3456 |
| 60/11 | 1728 | 1728 |

for a total of

\[
\boxed{29952}
\]

branches.

## 9. Finite local and quotient reduction: 29952 -> 92

This section states the actual finite predicates, not merely the internal job names.

### 9.1 Good-prime branch sieve: 29952 -> 1946

For a branch `delta=(δ_U,δ_V,δ_A,δ_B)`, a good-prime witness is a prime outside the coefficient/resultant and squareclass support. A rational branch point would reduce to `[T:S]\in P^1(F_p)` satisfying, for every factor `F_i in {U,V,A,B}`,

```text
if p | δ_i : F_i(T,S)=0 mod p;
otherwise   : F_i(T,S)/δ_i is a quadratic residue mod p, zero allowed.
```

A branch is discarded only when one eligible prime has no projective residue satisfying all four predicates. Thus the mathematical selection rule is existential and witness-based; no choice of a preferred prime is part of the theorem.

The exact survivors are

```text
20/21 : d1 88,  d2 64
80/39 : d1 384, d2 164
24/7  : d1 20,  d2 12
84/13 : d1 48,  d2 12
48/55 : d1 120, d2 72
20/99 : d1 232, d2 184
60/11 : d1 240, d2 306
```

for `1946` total.

### 9.2 Support-prime refinement: 1946 -> 1214

The same projective test is then imposed at the odd support primes themselves, with the necessary zero condition when `p|δ_i`. This leaves

```text
20/21 : 88/24
80/39 : 384/12
24/7  : 20/8
84/13 : 48/4
48/55 : 120/8
20/99 : 232/8
60/11 : 240/18
```

where each pair is `d1/d2`. Total: `1214 = 1132 d1 + 82 d2`.

### 9.3 Reconstruction quotient species: 1214 -> 1024

For each branch define its reconstruction species by

\[
s=\left|\operatorname{sf}(\delta_U\delta_V)\right|,
\]

the positive squarefree representative of the `UV` squareclass. The associated genus-one quotient is the squareclass twist of `Y^2=UV`; a concrete representative is

\[
C^{(1)}_s:\quad Y^2=2sTS(T^2-S^2)
\]

for `d=1`, and

\[
C^{(2)}_s:\quad Y^2=s(2T^2-S^2)(2T^2-4TS+S^2)
\]

for `d=2`.

Eighteen distinct `s`-species occur among the 1214 branches. The six species

\[
\boxed{s=1,2,10,26,66,195}
\]

have unconditional Mordell--Weil rank zero, torsion order four, and complete trivial quotient point sets. Pulling those complete point sets back through all four branch square equations removes exactly `190` branches. No positive-rank species is discarded here.

The result is `1024 = 1004 d1 + 20 d2`; the only remaining d2 cases are

```text
q=20/21 : 16
q=24/7  : 4,
```

all with `|sf(δ_U δ_V)|=7`.

### 9.4 Full support projective test: 1024 -> 92

For every odd `p|2ab(a^2-b^2)`, scale a rational branch point to primitive integral `[T:S]`. From `F_i=δ_i r_i^2`, p-integrality of the left side and of `δ_i` forces the auxiliary square roots to be p-integral. Therefore the same four projective residue predicates above are necessary at every support prime.

Exhausting `P^1(F_p)` for the complete support set kills all 20 remaining d2 branches and reduces d1 from 1004 to 92:

```text
20/21 : 24
80/39 : 12
24/7  : 8
84/13 : 8
48/55 : 8
20/99 : 16
60/11 : 16.
```

The surviving d1 `UV` species are

```text
20/21 : 210
80/39 : 390
24/7  : 21
84/13 : 546
48/55 : 330
20/99 : 110 or 30
60/11 : 330.
```

At this point every possible non-torsion receiver point is represented by one of these 92 concrete four-square branches.

## 10. Exact closure of the last 92 branches

The closure chain is

```text
92 -> 76 -> 52 -> 44 -> 30 -> 26 -> 22 -> 12 -> 8 -> 4 -> 0.
```

The mathematical meaning of each arrow follows.

### 10.1 Rank-zero A*B quotients: 92 -> 76

Sixteen branches lie above two rank-zero genus-one `A*B` quotients.

For `q=20/21`, the relevant squareclass is `-105` and the quartic is

\[
Y^2=-44100t^4-176610t^3-88200t^2+176610t-44100.
\]

Its complete rational t-set is

```text
2/5, 3/7, -5/2, -7/3.
```

For `q=80/39`, squareclass `-195`, the quartic is

\[
Y^2=-608400t^4-3089190t^3-1216800t^2+3089190t-608400,
\]

with complete rational t-set

```text
3/13, 5/8, -8/5, -13/3.
```

Both Jacobians have rank zero and torsion order four, and neither quartic has a rational point at infinity. Exact reverse substitution into all four parent equations shows: eight of the sixteen branches have no full rational lift; the other eight lift only to receiver 2-torsion at `x=-1` or `x=-q^2`. Hence no non-torsion receiver lift survives, and `92 -> 76`.

### 10.2 Rank-one Mordell--Weil congruence quotients: 76 -> 52

Twenty-four branches admit a genus-one quotient of exact rank one. For a fixed quotient, write every rational point as

\[
nP+T,
\]

with `T` one of the four torsion classes. Reduction modulo the selected good primes turns each of the omitted parent square equations into a congruence condition on `n`. For each of the 24 branches and for each of its four torsion translates, the admissible residue classes are intersected by generalized CRT. The final integer residue set is empty in all four translates. Therefore the complete Mordell--Weil group has no point satisfying the full four-factor parent conditions. Exactly 24 branches close: `76 -> 52`.

This step is global in `n`; it is not a bounded search on the quotient.

### 10.3 Rank-zero genus-two triple quotients: 52 -> 44

Eight branches have a genus-two quotient obtained by multiplying three of `U,V,A,B`. The corresponding Jacobians have rank zero. Chabauty0 therefore gives the complete rational point set, six projective points on each quotient. Every returned point is then substituted back into all four square equations. Every possible pullback has at least one of

\[
U,V,A,B
\]

equal to zero, so every full lift is receiver-degenerate. There is no nondegenerate full parent lift. Thus `52 -> 44`.

### 10.4 Rank-at-most-one genus-two quotients: 44 -> 30

Fourteen further branches have explicit genus-two triple quotients whose Jacobians have certified rank at most one. Complete rational point sets are obtained by the applicable rank-zero or rank-one Chabauty/elliptic-cover argument, and every rational quotient point is reverse-tested against the four parent square equations. Across all fourteen branches the number of nondegenerate full parent lifts is zero. Hence `44 -> 30`.

### 10.5 Two exact sign orbits: 30 -> 26

The sign involution

\[
[T:S]\longmapsto[-S:T]
\]

pairs the 30 remaining branches and preserves both the four-square parent truth and receiver degeneracy.

One direct representative is `q=20/99`,

\[
\delta=(-1,-55,-5,-11),
\]

with the genus-two `U*V*B` quotient. Its Jacobian has rank zero and its complete rational set consists of six projective points. Only one satisfies all four parent square predicates, and that point has `V=0`; all six are receiver-degenerate.

The second direct representative is on `q=60/11`. Its degree-two quotient over `Q(i)` is elliptic of exact rank one with torsion `C2 x C2`. A fixed infinite-order point is 2-saturated. Elliptic Chabauty with obstruction integer `R=4` gives the complete rational quotient-X set `0,-1320`; reverse reconstruction gives only

```text
x = 1, -1, 1/11, -11,
```

plus separately checked quotient `x=0` and infinity exceptions. Every one is receiver-degenerate. The two direct closures and their two sign partners close four branches: `30 -> 26`.

### 10.6 Two alternate rank-zero triple quotients: 26 -> 22

Two more direct representatives admit rank-zero genus-two triple quotients:

```text
q=20/99, delta=(-11,5,517055,-9401), triple=U*V*A
q=48/55, delta=(-6,110,1442,-237930), triple=U*V*B.
```

Their integral sextic models have coefficients

```text
[-94010,-930699,188020,930699,-94010] with zero end coefficient pattern,
[39655,69216,-79310,-69216,39655] with zero end coefficient pattern,
```

respectively; both Jacobians have rank zero. Chabauty0 returns six projective rational points on each. Exact four-factor pullback leaves one full-parent point per curve, but it has respectively `A=0` and `B=0`. Thus both direct branches are receiver-degenerate; their audited sign partners are also closed. Hence `26 -> 22`.

### 10.7 Candidate A, defined mathematically: 22 -> 12

The next ten branches are five sign orbits. A direct representative of each orbit is completely specified by `(q,delta,triple)`:

| q | delta=(δU,δV,δA,δB) | triple quotient | rank bound |
|---|---|---|---|
| 60/11 | (-11,15,-11715,71) | V*A*B | 0 |
| 60/11 | (30,-22,142,-23430) | V*A*B | 0 |
| 60/11 | (-1,-165,-15,-11) | U*V*B | <=1 |
| 84/13 | (546,2,26,42) | U*A*B | 0 |
| 84/13 | (1,273,21,13) | V*A*B | 0 |

This five-orbit set is what Stage34 called **Candidate A**; the name carries no extra mathematics.

For the five direct quotients, the complete rational quotient point set has six projective points in every case. Their projective `[T:S]` sets are, respectively,

```text
60/11 #1 : (-11:1),(-6:5),(0:1),(1:11),(5:6),(1:0)
60/11 #2 : (-11:1),(-6:5),(0:1),(1:11),(5:6),(1:0)
60/11 #3 : (0:1),(-1:1),(1:0),(1:11),(-11:1),(1:1)
84/13 #1 : (1:13),(-1:1),(-13:1),(6:7),(-7:6),(1:1)
84/13 #2 : (1:13),(0:1),(1:0),(-13:1),(6:7),(-7:6).
```

Each point is substituted into

\[
U/\delta_U,\ V/\delta_V,\ A/\delta_A,\ B/\delta_B.
\]

In every orbit exactly one quotient point can satisfy all four square predicates, and that lift has `UVAB=0`; hence the number of nondegenerate full-parent lifts is zero. The sign involution closes the five partners. Therefore Candidate A closes exactly ten branches and `22 -> 12`.

### 10.8 Candidate B, defined mathematically: 12 -> 8

Four of the twelve remaining branches are the two `q=20/99` sign orbits

```text
(-6,10,510,-34)  <->  (6,-10,-510,34)
(-5,3,17,-255)   <->  (5,-3,-17,255).
```

This four-branch set is **Candidate B**. Unlike Candidate A, the claim here is not that the factor covers have no rational points. The only claim needed is that they have no point in the receiver intersection.

For `q=20/99`,

\[
U=T^2-S^2,\quad V=2TS,\quad A=20U+99V,\quad B=99U+20V.
\]

A receiver point on the d=1 split must additionally satisfy the exact `K_{20/99,1}` condition

\[
A^2+B^2=w^2.
\]

Reduce modulo 13. The branch equations alone have only two projective residue possibilities,

```text
(T:S)=(5:1): (U,V,A,B)=(11,10,1,2),  A^2+B^2=5
(T:S)=(8:1): (U,V,A,B)=(11,3,10,5),  A^2+B^2=8.
```

The square residues mod 13 are

```text
0,1,3,4,9,10,12.
```

Both `5` and `8` are nonsquares. Exhaustion of all 14 points of `P^1(F_13)` therefore gives zero branch+K survivors for each of the four delta tuples. Hence these four branches contribute no Face-3-square receiver point, even though the factor branches themselves may have rational points. This is the precise Candidate-B firewall. Thus `12 -> 8`.

### 10.9 q=80/39 Gaussian quotient orbits: 8 -> 4

Four of the eight branches form two sign orbits on `q=80/39`. One representative is

\[
\delta=(-1,-195,-5,-39).
\]

Its Q(i)-elliptic quotient has exact rank one and torsion `C2 x C2`. The fixed generator is 2-saturated; elliptic Chabauty with `R=4` gives complete finite rational quotient-X set

```text
1521, 6400.
```

Reverse reconstruction gives exactly

```text
5/8, -8/5, 3/13, -13/3.
```

At `5/8,-8/5`, `A=0`; at `3/13,-13/3`, `B=0`. The second q=80/39 representative is treated by the same exact Gaussian quotient mechanism and likewise has zero nondegenerate full-parent lifts. The sign involution transfers both closures to their partners. Therefore all four q=80/39 branches close and `8 -> 4`.

### 10.10 q=84/13 torsion quotients: 4 -> 0

The last four branches are two sign orbits on `q=84/13`. For each direct representative the Q(i)-elliptic quotient has rank zero. Good reduction at two primes bounds the torsion order by four, while an explicit `C2 x C2` subgroup already has order four; therefore the complete quotient group is exactly `C2 x C2`.

For the first representative, the complete torsion quotient-X values are

```text
infinity, 0, 89531, -578508 i.
```

The rational X values are `0,89531`; inverse reconstruction gives

```text
x=-1,1,-7/6,6/7.
```

Testing all four parent square conditions leaves only one full-parent lift, at `x=-7/6`, and it has `A=0`.

For the second representative, the complete torsion quotient-X values are

```text
infinity, 0, -1157016, 179062 i.
```

The rational X values are `0,-1157016`; inverse reconstruction gives

```text
x=-1,1,-13,1/13.
```

The only full-parent lift is at `x=-13`, and it has `B=0`.

Quotient infinity is also receiver-degenerate. Thus both direct representatives have zero nondegenerate full-parent lifts. The sign involution closes their two partners. Therefore

\[
\boxed{4\to0}.
\]

Combining Sections 9 and 10 gives the complete finite chain

\[
29952\to1946\to1214\to1024\to92\to76\to52\to44\to30\to26\to22\to12\to8\to4\to0.
\]

Every arrow now has an explicit input class, quotient or residue predicate, and exact reason for exclusion in this file.

## 11. Receiver implication

Assume, for contradiction, that a non-torsion point in the authoritative Stage34 population has square Face-3.

1. It is not a pole, by Section 3.
2. By Section 2 it lifts to `C_q(Q)`.
3. Section 4 forces its squareclass to `d=1` or `d=2`.
4. Sections 5--7 place it on a matching reconstruction branch satisfying all four square conditions.
5. Section 8 places that branch among the 29,952 exact finite over-cover branches.
6. Sections 9--10 exclude every receiver-relevant branch; the final residual is zero.

Contradiction. Hence

\[
\boxed{\text{no non-torsion rational point in the seven locked fibers has square Face-3}.}
\]

Equivalently,

```text
all_multiples_closed=true
R29_EXT_CHANG_C_closed=true
receiver_face3_square_points_remaining=0.
```

## 12. Audit boundary

The receiver-level hostile audit explicitly authorized

```text
all_multiples_closed=true
R29_EXT_CHANG_C_closed=true.
```

The promoted receiver state independently records zero remaining Face-3-square receiver points. The proof is deliberately receiver-restricted. It does not assert

```text
direct_cover_rational_points_complete=true
factor_cover_rational_points_complete=true
Candidate-B factor-cover Q-pointset empty
J12-PARAMETRIC closed
parent route closed
perfect cuboid existence or nonexistence.
```

Candidate B is especially important: its four factor branches may possess rational points; mod 13 proves only that none simultaneously satisfies the required d=1 K-condition, which is exactly the receiver intersection needed here.

## 13. Stage29 compatibility writeback

The exact downstream writeback is

```text
R29-EXT-CHANG-C = CLOSED_ALL_ADMISSIBLE_MULTIPLES_BY_STAGE34_RECEIVER_RESTRICTED_ROUTE_D
K16-C3-EXT-C-PRIMITIVE-DIVISOR = DISCHARGED_BY_STAGE34_REPLACEMENT_ROUTE.
```

The frozen historical Stage29 ledgers are not rewritten. The live frontier changes

```text
active kernels : 13 -> 12
Class 3        : 9 -> 8
Class 2        : 4 -> 4.
```

`J12-PARAMETRIC` remains open with

```text
K16-C3-PESCH-EXPONENT-ONE
K16-C3-MOVING-FIBER-ARITHMETIC
K16-C2-EXT-E-INTEGRAL-CERTIFICATION.
```

## 14. Reusable theorem and anti-loop rule

Downstream work may use the single implication

```text
full seven-fiber non-torsion MW population
+ exact Face-3 cover equivalence
+ pole=order-4-torsion firewall
+ exact d={1,2} split
+ exact four-factor reconstruction
+ complete finite squareclass/local/quotient closure to residual 0
=> no Face-3-square point in R29-EXT-CHANG-C.
```

Do not reopen the audited q=80/39 or q=84/13 terminal orbits, the 92-branch closure, the receiver implication, or the Stage29 writeback unless an audit is revoked, a source-lock mismatch is found, or materially new evidence changes the premises.

## 15. Provenance and replay

The load-bearing source locks remain reproducibility records for the statements written above. Principal frozen identifiers are:

```text
population contract blob       f38d74862655b206b66f09105c4f5be481bc6444
Face-3 reduction blob          c023d3ad8567faa280f23e28e0300acfcc61e6a2
pole torsion blob              04334c55124e4c2d61a685bd53a930ee5798f0aa
receiver pullback blob         101181f7575c1e559cd0438abd37e627b7bf984c
reconstruction blob            a357a6691e0be4abd4965b3f822c829864d814bf
odd squareclass blob           a053c32a8dbda15c909b7cddc241e8534d4399f9
two-adic blob                  a27621570e79e045a47bc27aec7ecbabb2ebd5f1
all-factor promotion blob      4c50fa4361071fa09b307a7e3c3f01f220701591
receiver promotion blob        fb3a79542088362973e1355bdc75e10433ccc12a
```

Receiver hostile audit: review `5088591887`.

Exact receiver replay:

```text
run=33620807240
job=100217139651
conclusion=SUCCESS
```

Stage29 writeback replay:

```text
run=33622578539
job=100222778353
conclusion=SUCCESS
```

These identifiers permit byte-for-byte reproduction; they are not required to determine what mathematical assertion each transition proves, because those assertions and their finite exclusion predicates are stated above.

## 16. Final handoff

```text
STAGE34_ALL_MULTIPLES_CLOSED=true
R29_EXT_CHANG_C_CLOSED=true
K16_C3_EXT_C_PRIMITIVE_DIVISOR_DISCHARGED=true
J12_PARAMETRIC_CLOSED=false
PARENT_ROUTE_CLOSED=false
POST_STAGE34_ACTIVE_KERNELS=12
POST_STAGE34_CLASS3_KERNELS=8
POST_STAGE34_CLASS2_KERNELS=4
NEXT_EXACT_LEAF=NONE_STAGE34_COMPLETE
NEXT_OWNER=POST_STAGE29_RESEARCH_OS
AUDIT_STATUS=PASS
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
