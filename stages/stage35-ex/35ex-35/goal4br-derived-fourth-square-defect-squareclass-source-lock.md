# Stage35-EX Goal4BR source lock — derived fourth-square defect, primitive two-square class, and involution reservoir swap

Scope: continue the Goal4BP backup after Goal4BQ. This leaf analyzes the source-fixed fourth-square defect of the classical derived Euler brick from Goal4AY. Audited authority remains V74 / Goal4AK. Goal4BR does not assume the derived brick is itself perfect.

## 1. Six-variable endpoint and derived brick

For the primitive endpoint write

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,
```

with reduced primitive face equations

```text
r_AB^2=(y*a)^2+(z*b)^2,
r_AC^2=(x*a)^2+(z*c)^2,
r_BC^2=(x*b)^2+(y*c)^2,
```

and original space square

```text
W^2=A^2+B^2+C^2.
```

Goal4AY's primitive derived brick has edges

```text
A_D=x*a*b,
B_D=y*a*c,
C_D=z*b*c.
```

Define its fourth-square defect integer

```text
Q_D=A_D^2+B_D^2+C_D^2
   =(x*a*b)^2+(y*a*c)^2+(z*b*c)^2.                 (BR-QD)
```

No source theorem says `Q_D` is a square.

## 2. Exact completion identity

The classical completion identity from Goal4AY becomes, after dividing the raw pair-product identity by `(x*y*z)^2`,

```text
P^2+R^2=W^2*Q_D,                                   (BR-COMP)
```

where

```text
P=r_AB*r_AC*r_BC,
R=x*y*z*a*b*c.                                      (BR-PR)
```

Each reduced Pythagorean hypotenuse is odd, hence `P` is odd. Primitive parity gives `R` even.

Put

```text
G=gcd(P,R),
p=P/G,
r=R/G.                                              (BR-G)
```

Then

```text
gcd(p,r)=1,
p odd,
r even,
[Q_D]=[p^2+r^2] in Q*/Q*^2.                         (BR-CLASS)
```

The last equality follows from `(BR-COMP)` because `(W/G)^2` is a rational square; no divisibility assertion `G|W` is needed.

Consequently every prime in the squarefree support of `Q_D` is congruent to `1 mod 4`. Indeed `p^2+r^2` is odd and, for coprime `p,r`, no prime `ell==3 mod4` can divide their sum of two squares.

Thus

```text
squarefree(Q_D) is an odd product of primes ==1 mod4.  (BR-SUPPORT)
```

This is a genuine source-fixed squareclass restriction, but it is not yet an exclusion.

## 3. Exact gcd reservoir factorization

Retain Goal4AU reservoirs

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB),                                    (BR-h)
```

and define the derived-side reservoirs

```text
j_x=gcd(x,r_AB),
j_y=gcd(y,r_AC),
j_z=gcd(z,r_BC).                                    (BR-j)
```

The primitive six-variable coprimality dictionary implies:

```text
gcd(r_AB,R)=j_x*h_c,
gcd(r_AC,R)=j_y*h_b,
gcd(r_BC,R)=j_z*h_a.                                (BR-face-gcd)
```

Proof for the first identity: a prime dividing `r_AB` and `R` cannot enter through `y,z,a,b`, because in each case the opposite leg in

```text
r_AB^2=(y*a)^2+(z*b)^2
```

remains a unit by the retained coprimalities. Hence it can enter `R` only through `x` or `c`; `gcd(x,c)=1`. If it enters through `x` and also another factor of `R`, the same primitive-face equation rules out divisibility of `r_AB`, so its full `R`-valuation is the `x`-valuation; similarly for `c`. The other two identities are cyclic.

A prime of `R` that divides one reduced hypotenuse cannot divide either of the other two reduced hypotenuses, by the same unit-leg argument. Therefore the six reservoir factors in `(BR-h)` and `(BR-j)` account valuation-exactly for `G`:

```text
G=h_a*h_b*h_c*j_x*j_y*j_z.                          (BR-GFACT)
```

Hence the primitive two-square representative may be written

```text
p=(r_AB/(j_x*h_c))*(r_AC/(j_y*h_b))*(r_BC/(j_z*h_a)),
r=(x/j_x)*(y/j_y)*(z/j_z)*(a/h_a)*(b/h_b)*(c/h_c). (BR-STRIP)
```

No finite prime-support theorem follows: the stripped factors may carry parameter-dependent odd primes.

## 4. Conditional square receiver versus actual endpoint condition

If one additionally imposed

```text
Q_D=S^2,                                             (BR-extra)
```

then `(BR-CLASS)` would become a genuine primitive Pythagorean square condition

```text
p^2+r^2=t^2,
```

with `p` odd and `r` even, hence `r` divisible by four and the usual primitive Euclidean parametrization applies.

But `(BR-extra)` is **not** a consequence of the original perfect endpoint. It means the derived Euler brick is also a perfect cuboid. Goal4AY proves only three-face preservation under the derived operator; it explicitly does not prove fourth-square preservation.

Therefore S34-W01 cannot be triggered by treating `Q_D` as a required square. Doing so would replace the original endpoint population by the strictly smaller, unsupported population

```text
{perfect endpoint whose derived brick is also perfect}.
```

The exact squareclass restriction `(BR-SUPPORT)` is valid on the full original endpoint population; the Pythagorean square equation is only conditional on the extra unsupported hypothesis `(BR-extra)`.

## 5. Exact two-cycle reservoir swap

Goal4AY gives the six-variable involution

```text
D:(x,y,z ; a,b,c) -> (a,b,c ; x,y,z),               (BR-D)
```

and the reduced hypotenuse permutation

```text
r'_AB=r_BC,
r'_AC=r_AC,
r'_BC=r_AB.                                        (BR-rD)
```

For the derived brick, its Goal4AU-type reservoirs are therefore

```text
h'_a=gcd(x,r_AB)=j_x,
h'_b=gcd(y,r_AC)=j_y,
h'_c=gcd(z,r_BC)=j_z,                                (BR-swap1)
```

while its `j`-reservoirs are

```text
j'_x=gcd(a,r_BC)=h_a,
j'_y=gcd(b,r_AC)=h_b,
j'_z=gcd(c,r_AB)=h_c.                                (BR-swap2)
```

Thus the two triples swap exactly under the derived involution:

```text
(h_a,h_b,h_c) <-> (j_x,j_y,j_z).                    (BR-RES-SWAP)
```

The fourth-square defects also form the tautological two-cycle

```text
space_norm(P)=W^2,
space_norm(D(P))=Q_D,
space_norm(D^2(P))=W^2.                              (BR-DEFECT-CYCLE)
```

Since `D^2=id`, this is not a strict descent and does not force `Q_D` square.

## 6. S34-W01 applicability boundary

The exact output available on the full endpoint population is:

```text
[Q_D]=[p^2+r^2],
gcd(p,r)=1,
p odd,
r even,
squarefree support(Q_D) subset {ell: ell==1 mod4}.
```

This is not a finite exhaustive squareclass family. The allowed set of `1 mod4` primes is unbounded, and no bounded low-degree factorization with finite shared-prime support has been obtained. Therefore

```text
S34-W01_TRIGGERED=false.                              (BR-S34)
```

The card remains a router only if a future source theorem further bounds the squareclass support.

## 7. Verdict

Certified provisionally:

```text
DERIVED_DEFECT_Q_D_EXPLICIT=true;
COMPLETION_P2_PLUS_R2_EQUALS_W2_QD=true;
PRIMITIVE_TWO_SQUARE_CLASS_REPRESENTATIVE=true;
G_FACTOR_EQUALS_HA_HB_HC_JX_JY_JZ=true;
Q_D_SQUAREFREE_SUPPORT_ONLY_ODD_1MOD4=true;
DERIVED_RESERVOIR_TRIPLES_SWAP_UNDER_INVOLUTION=true;
ORIGINAL_ENDPOINT_FORCES_Q_D_SQUARE=false;
S34_W01_TRIGGERED=false;
FINITE_SQUARECLASS_FAMILY_OBTAINED=false;
STRICT_DESCENT_OBTAINED=false;
BRANCH_PRUNING=false.
```

This closes the Goal4BP backup as a useful exact invariant but not an endpoint exclusion route.

## 8. Next leaf

With the Goal4BP live route blocked at rational realization (Goal4BQ) and its distinct backup now fail-closed as non-obstructive, run a fresh parking/breadth audit rather than silently recycling either route:

```text
35EX-35_GOAL4BS_POST_BOUNDARY_DERIVED_BACKUP_PARKING_AUDIT
```

Preserve the exact missing objects: a global rational realization/height adapter for boundary depth, or a new source-fixed invariant distinct from the Gaussian carrier and derived defect squareclass.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
