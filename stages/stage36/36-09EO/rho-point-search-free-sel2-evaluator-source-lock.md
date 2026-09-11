# Stage36 36-09EO — point-search-free rho Sel2 evaluator and exact 50-box pattern

## Purpose

36-09EL writes `Sel^2(E_rho,p/Q)` as an exact finite F2 localization matrix. 36-09EM gives every odd-prime local Kummer block, and 36-09EN gives the real and dyadic blocks. Thus no local point search remains.

This leaf turns those formulas into a deterministic evaluator, first replays the exact 36-09EJ 62-row box, then evaluates the larger diagnostic box `1<=a,b<=50`. The larger box is **not** an exhaustive physical-parameter ledger; it is used to expose arithmetic structure and to find individually provable fixed-parameter exclusions.

## Closed evaluator

For primitive positive `p=a/b`, `a!=b`, put

```text
N=a^2-b^2,
d=ab,
P=N+2d,
Q=N-2d,
D=P^2-Q^2.
```

Use the translated model

```text
y^2=X(X-P^2)(X-Q^2)
```

and finite support

```text
S_f={2} union {prime divisors of P*Q*D}.
```

The global ambient basis is `[-1]` followed by `S_f` in increasing order, duplicated in the two Kummer coordinates.

At each place use only the closed formulas already proved:

- infinity: `W_infinity=span{(0,1)}`;
- q=2: the shallow/deep 36-09EN formula selected from the exact 2-adic branch criterion;
- odd q|P, q|Q, or q|D: the corresponding 36-09EM formula.

For every place stack `W_v^perp L_v` as in 36-09EL. Then

```text
dim_F2 Sel^2(E_rho,p/Q)=2|G|-rank M_Sel2(a,b).
```

No bounded local witness scan occurs in this evaluator.

## Compatibility with 36-09EJ

On the original ordered primitive box `1<=a,b<=10`, the closed evaluator reproduces exactly

```text
dim 2: 14
dim 3: 14
dim 4: 30
dim 5:  4.
```

It reproduces the same 14 dimension-two rows retained by 36-09EJ. This is a direct compatibility check between the formerly witness-saturated implementation and the new symbolic local formulas.

## Exact diagnostic 50-box

Now evaluate every ordered primitive pair

```text
1<=a,b<=50,
gcd(a,b)=1,
a!=b.
```

There are exactly `1546` rows. The exact Sel2-dimension distribution is

```text
dim 2:  24
dim 3: 136
dim 4: 500
dim 5: 554
dim 6: 280
dim 7:  52.
```

For the canonical row encoding

```text
a,b,semicolon-separated-S_f,ambient_dimension,constraint_rank,sel2_dimension
```

in lexicographic `(a,b)` order with a trailing newline, the SHA-256 digest is

```text
875b813e8af97b34a7fb6d3dab70abb17bc88102beb5523efc751a72352133e7
```

The exact 24 rows with Sel2 dimension two are

```text
(1,2),(1,3),(1,5),
(2,1),(2,3),(2,7),(2,9),
(3,1),(3,2),(3,47),
(5,1),(5,9),
(6,43),
(7,2),(7,11),
(9,2),(9,5),
(11,7),
(22,25),(25,22),
(37,49),(43,6),(47,3),(49,37).
```

## Six exact rho-isomorphism / literal-top-curve orbits

For `p=a/b`, inversion swaps `a,b`, hence

```text
(P,Q) -> (-Q,-P),
```

so the translated rho curve merely swaps the square roots `P^2,Q^2`.

For the physical literal transformation

```text
c(p)=(p+1)/(p-1),
(a,b)->(a+b,a-b),
```

before primitive common-factor removal one has

```text
(P,Q)->(2P,-2Q).
```

After the common square scaling `X=4X'`, `y=8y'`, this is again Q-isomorphic to the same translated rho curve. Thus the full-2 Selmer dimension and rational torsion conditions are invariant on the positive literal orbit

```text
O(p)={p,1/p,|c(p)|,1/|c(p)|}.
```

The 24 dimension-two rows are exactly six such four-point orbits:

```text
O(2)    ={1/3,1/2,2,3},
O(1/5)  ={1/5,2/3,3/2,5},
O(2/7)  ={2/7,5/9,9/5,7/2},
O(2/9)  ={2/9,7/11,11/7,9/2},
O(3/47) ={3/47,22/25,25/22,47/3},
O(6/43) ={6/43,37/49,49/37,43/6}.
```

The first four are exactly the 16-value registry already promoted by 36-09EK. The last two are new.

## Complete 36-09EH criterion on the two new orbits

For the seed `p=3/47`, the closed evaluator gives `Sel2_dim=2`. Direct rational-square testing shows both `+8h` and `-8h` are nonsquares. The translated rho model has good reduction at 13 and

```text
#E_rho,3/47(F_13)=16,
```

which is not divisible by three. Prime-to-13 rational torsion injects under good reduction, so `E_rho,3/47(Q)[3]=0`.

For the seed `p=6/43`, again `Sel2_dim=2`, both `+8h` and `-8h` are nonsquares, and at the good prime 5

```text
#E_rho,6/43(F_5)=8,
```

so `E_rho,6/43(Q)[3]=0`.

Therefore both seeds satisfy the complete exact-green 36-09EH exclusion criterion. Because the other members of each displayed orbit have Q-isomorphic rho curves and the literally identical physical top curve, the same fixed-sector exclusion propagates to all eight values

```text
{3/47,22/25,25/22,47/3,6/43,37/49,49/37,43/6}.
```

After CI consumption the exact fixed-parameter exclusion registry may therefore expand from 16 to 24 values.

## Pattern conclusion and next obligation

The diagnostic data refute any expectation that `Sel2_dim=2` is uniform: dimensions through seven already occur in the 50-box. The useful uniform object is instead the point-search-free matrix evaluator.

The next leaf should extract a sufficient rank criterion from the closed matrix in terms of the support graph / Legendre-symbol data, rather than merely enlarging the box again:

```text
36-09EP_RHO_SEL2_RANK_CRITERION_PREFLIGHT.
```

## Credit firewall

This leaf may grant eight new individually proved fixed-p sector exclusions after exact-head CI. It does not prove that the 50-box is exhaustive or that all positive rational parameters are excluded. Hence all of the following remain false:

```text
uniform_Sel2_dimension_2_theorem,
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```
