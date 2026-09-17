# Stage32 MB104 — U12 Bolza genus-two spin-passport reduction — 2026-09-17

Status: **NEW PACKET-SENSITIVE GLOBAL REDUCTION / NOT A CLOSURE / NO CREDIT**

## Scope

Assume conditionally that the dangerous balanced equality packet is realized on

```text
Sigma = 000707000f0f,
node-type counts = (7,7,0),
g(E)=1,
d=r_odd=112l,
l>=1.
```

This note uses the smooth Beauville/Stoll--Testa double cover of the cuboid surface, but does **not** return to the archived pointwise conductor-sign problem.

## 1. Stoll--Testa genus-two quotient

Write the genus-five modular curve as

```text
X: u^2=2xy,
   v^2=x^2-y^2,
   w^2=x^2+y^2.
```

Let

```text
G0 ~= (Z/2)^3
```

be the sign-change group in `u,v,w`, and let

```text
G0+ < G0
```

be the order-four subgroup changing an even number of signs.

Stoll--Testa prove that

```text
C2 := X/G0+
```

is the genus-two curve

```text
y^2 = 2(x^5-x),
```

and that

```text
Y := (X x X)/diag(G0+)
```

is smooth and maps two-to-one to the cuboid canonical surface, branched exactly over its 48 nodes.  The two factor quotients give morphisms

```text
rho_1,rho_2 : Y -> C2.
```

The residual quotient `G0/G0+` is the hyperelliptic involution on `C2`; its six fixed points are the six Weierstrass points of `C2`.

This `Y` is the same smooth Beauville double-cover geometry already used in the archived equality-rigidity chain; the new input below is the explicit descent to the genus-two factors.

## 2. The dangerous carrier lift has genus `56l+1`

Let

```text
pi:B -> E
```

be the normalization of the pullback of the hypothetical carrier to `Y`.

Every one of the `112l` supported normalization branches is odd for the Beauville double cover.  Hence `pi` is a connected double cover branched at exactly `112l` points.  Since `g(E)=1`,

```text
2g(B)-2 = 112l,
g(B)=56l+1.                                      (B-GENUS)
```

Let

```text
p_i := rho_i|_B : B -> C2.
```

## 3. Both genus-two projections have exact degree `56l` and are etale

Use the archived equality-rigidity product cover.  Let `Z` be a connected component of the pullback of `B` to `X x X`, and let

```text
e=deg(Z->B) in {2,4}
```

for the current `000707` support.  The two product projections satisfy

```text
deg(Z->X)=14 e l.
```

Since

```text
X -> C2
```

is the free quotient by `G0+` of degree four, commutativity gives

```text
e * deg(p_i)
 = 4 * (14 e l),
```

so independently of `e`,

```text
deg(p_1)=deg(p_2)=56l.                          (DEG56)
```

Now `g(C2)=2`.  Riemann--Hurwitz gives

```text
2g(B)-2
 = deg(p_i)*(2g(C2)-2) + Ram(p_i)
 = 56l*2 + Ram(p_i).
```

By `(B-GENUS)` the left side is `112l`, hence

```text
Ram(p_i)=0.                                     (ETALE-C2)
```

Thus both maps are finite etale covers of exact degree `56l`.

## 4. The joint genus-two pair is birational

The finite etale surface map

```text
Y -> C2 x C2
```

has relative deck group `G0+`: a relative element `r` acts, after choosing product lifts, by `(1,r)` modulo the diagonal `G0+`.

If a nontrivial relative element stabilized `B`, it would descend through the full abelian sign-change quotient to a nontrivial automorphism of the cuboid carrier preserving the support and preserving each node-stabilizer type individually.

The archived exact `000707` support-stabilizer replay gives:

```text
support stabilizer order = 2,
its unique nonidentity element swaps b1=0 <-> b2=0,
type-preserving support stabilizer = 1.
```

Therefore no nontrivial relative element can stabilize `B`.  Consequently

```text
(p_1,p_2): B -> C2 x C2
```

is generically degree one onto its image.  In particular the dangerous packet produces a genuine equal-degree etale self-correspondence of the Bolza genus-two curve, not a repeated common factor.

## 5. Exact factor orientation of the two zero quartics

Use the Stoll--Testa product invariants

```text
U=u1*u2=2b1,
V=v1*v2=2b2,
X=x1*x2=a1+c,
Y=y1*y2=-a1+c,
T=x1*y2=a2+i*a3,
Z=x2*y1=a2-i*a3.
```

The two retained zero-pairing quartics are

```text
Q0: b1=0,  i*a2-a3=0,  a1-c=0,
Q1: b2=0,  i*a3+a1=0,  a2-c=0.
```

For `Q0`, these equations are

```text
U=0,
T=0,
Y=0.
```

Since `(x1,y1)` cannot vanish simultaneously on `X`, `T=Y=0` forces

```text
y2=0,
```

and then `u2=0` from `u2^2=2x2y2`.  Thus `Q0` is the image of a **second-factor** fiber of `rho_2` over a Weierstrass point

```text
w0 in C2.
```

For `Q1`, the last two equations are equivalent to

```text
X=Z,
T=Y.
```

Hence

```text
x2(x1-y1)=0,
y2(x1-y1)=0.
```

Since `(x2,y2)` cannot vanish simultaneously,

```text
x1=y1,
```

and therefore `v1=0` from `v1^2=x1^2-y1^2`.  Thus `Q1` is the image of a **first-factor** fiber of `rho_1` over another Weierstrass point

```text
w1 in C2.
```

The two node types are distinct, so `w0` and `w1` belong to distinct Weierstrass-type pairs in the residual hyperelliptic quotient.

## 6. The branch divisor is exactly one Weierstrass fiber from each factor

The current support has

```text
7 nodes on Q0,
7 nodes on Q1,
8l normalization branches at every supported node.
```

Therefore the ramification points of `pi:B->E` split into two reduced divisors

```text
R0, R1,
deg R0 = deg R1 = 7*(8l)=56l.
```

Every point of `R0` lies in the `p_2` fiber over `w0`.  But `p_2` is etale of degree `56l`, so that fiber is reduced of degree `56l`.  Hence equality of effective divisors holds:

```text
R0 = p_2^*(w0).                                 (F0)
```

Likewise

```text
R1 = p_1^*(w1).                                 (F1)
```

All ramification of `pi` occurs on the 14-node packet, so

```text
Ram(pi)=R0+R1.                                  (RAM-SPLIT)
```

This is stronger than the earlier `P1` residual two-fiber capacity statement: at the genus-two level each seven-node zero-quartic block fills one **single** Weierstrass fiber completely.

## 7. Spin-passport equality

Because `E` is elliptic, Riemann--Hurwitz for `pi` gives the canonical divisor identity

```text
K_B ~ Ram(pi) ~ R0+R1.                          (K-RAM)
```

Because `p_1,p_2` are etale,

```text
K_B ~ p_i^* K_C2.
```

Every Weierstrass point `w` on a genus-two hyperelliptic curve satisfies

```text
K_C2 ~ 2w.
```

Using `(F0)/(F1)`,

```text
K_B ~ 2R0,
K_B ~ 2R1.
```

Comparing with `(K-RAM)` gives

```text
R0 ~ R1.                                        (SPIN)
```

Equivalently,

```text
p_2^* O_C2(w0) ~= p_1^* O_C2(w1).              (THETA)
```

Thus the dangerous MB104 correspondence must identify two specified odd theta characteristics after pullback to its common etale cover.

Squaring `(THETA)` is automatic from canonical-bundle functoriality; **triviality of the unsquared difference is the packet-sensitive extra condition** supplied by the exact branch divisor.

## 8. What this does and does not close

This is a new finite-level arithmetic passport on the equal-degree Bolza correspondence:

```text
B -> C2, B -> C2
both etale of degree 56l,
joint map birational,
plus p_2^*O(w0)=p_1^*O(w1).
```

It does not by itself give an upper bound on `l`.  The Bolza curve is arithmetic, so its commensurator contains infinitely many correspondences.  A successful continuation must classify which commensurator/double-coset correspondences satisfy the **specified spin condition** `(THETA)` together with the `000707` node passport.

This is strictly narrower than U10: U10 asked only whether large-degree etale correspondences exist.  U12 asks whether a primitive degree-`56l` correspondence can preserve the exact level-two spin passport forced by the two zero quartics.

Useful next target:

```text
U12-BOLZA-INDEX-SPIN:
  determine the index spectrum of primitive Bolza commensurator double cosets
  satisfying (THETA), and test whether 56l can occur for infinitely many l.
```

If this spectrum is finite or excludes all sufficiently large multiples of 56, U12 becomes a genuine U4 theorem.  If it contains an infinite congruence family, record that arithmetic family and park U12 rather than returning to generic correspondence counting.

## Source boundary

External source:

- Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, Section 4: the product model, `G0+`, the genus-two quotient `C2`, and the smooth double cover `Y`.

Archived exact MB104 inputs at head

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

include:

- `GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md`;
- `GENUS1-SPAN5-BALANCED16-BEAUVILLE-NODE-TYPE-QUOTIENT.md`;
- `GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md`;
- `GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md`;
- `STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md`.

## Firewalls

```text
U12_closes_000707=false
U12_large_l_bound_proved=false
Bolza_spin_passport_proved_conditionally=true
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
