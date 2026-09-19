# MB104 P6E — hostile full-span survivor nef gate — 2026-09-19

Status: **PRE-AUDIT EXACT GLOBAL NEF REDUCTION / NO CREDIT**

## Target

Use the P6A/P6B hostile support

```
Sigma = 0000093f442e
      = {1,2,3,5,10,14,16,17,18,19,20,21,24,27}.
```

Put

```
P = 7H - 4 sum_(i in Sigma) E_i,
D_l = lP.
```

The retained intersection data are

```
H^2=16,
P^2=336,
H.P=112,
P.E_i=8   for i in Sigma,
P.E_j=0   for j notin Sigma.
```

P6A shows the support spans `P^6`.

The purpose of this leaf is to decide the entire negative-test-curve question for this exact ray, rather than adding another finite curve catalog.

## 1. Local contact input

The retained Z33 local A1 lemma applies to **any** normalization branch over a box node.

If an ambient hyperplane `L` passes through a box node `s`, and a branch over `s` has exceptional multiplicity `m_b`, then

```
ord_b(L) >= m_b.
```

Therefore, for any integral nonexceptional curve `R` not contained in `L`,

```
d := H.R,
m_i := E_i.R >= 0,
sum_(i in Sigma cap L) m_i <= d.              (HC)
```

No low-genus or simple-contact assumption is used here.

## 2. Thirty exact support hyperplanes

The P6E certificate lists 30 subsets of the fourteen support nodes.

For every listed subset:

- its homogeneous node vectors have rank exactly six;
- hence it spans a unique ambient `P^5`, i.e. one hyperplane of `P^6`;
- every support node not listed raises the rank to seven, so the recorded subset is exactly the support incidence of that hyperplane.

Assign the listed positive rational weights with common denominator `609`.

The machine certificate checks exactly:

```
sum_H weight(H) = 1051/609,
for every support node i:
    sum_(H contains i) weight(H) = 655/609,
max_H weight(H) = 46/609.
```

Hence, after deleting **any one** of the thirty hyperplanes, every support node still has weighted coverage at least

```
(655-46)/609 = 1.                              (ROBUST)
```

This one-deletion robustness is the key point.

## 3. Curves spanning P6 or P5

Let `R` be an integral nonexceptional curve and write

```
M_Sigma = sum_(i in Sigma) m_i.
```

### R spans P6

Then `R` is contained in none of the thirty hyperplanes, so every inequality (HC) is valid.

### R spans P5

Then `R` is contained in exactly one ambient hyperplane. Among the selected thirty, at most one inequality can therefore be invalid. Delete it.

In either case, multiply the valid inequalities (HC) by the certificate weights and sum them. By (ROBUST), every `m_i` is covered with coefficient at least one:

```
M_Sigma
 <= (1051/609) d.                              (P6E-MASS)
```

Consequently

```
P.R
 = 7d - 4 M_Sigma
 >= (7 - 4*1051/609)d
 = (59/609)d
 > 0.                                          (P6E-POS)
```

Thus **every integral curve spanning P5 or P6 has strictly positive pairing with P**.

This is population-independent: no assumption on genus, branch count, equal exceptional coefficients, or membership in the known low-degree curve list is used.

## 4. Curves of span at most P4

Use the published Stoll--Testa low-span classification recorded in
`MB104-P6E-STOLL-TESTA-LOW-SPAN-SOURCE-NOTE-20260919.md`.

### Plane curves

Every integral plane curve is a known conic.

P6B replays all 32 conics exactly on the hostile support and finds maximum support incidence three, hence

```
P.Q >= 14 - 12 = 2 > 0.
```

### Curves spanning P3

Every such curve is one of the known genus-one degree-four curves.

P6B replays all 60 such quartics; the worst support incidence is five, hence

```
P.Q >= 28 - 20 = 8 > 0.
```

### Curves spanning P4

Stoll--Testa Theorem 16 says every integral `P^4`-spanning curve has degree eight and geometric genus either three or five.

Assume for contradiction that such an `R` has `P.R<0`.

Then

```
d=8,
M_Sigma > 7d/4 = 14,
so M_Sigma >=15.
```

For fourteen nonnegative integers with total at least 15,

```
sum_i m_i^2 >=17.
```

Hodge projection onto `H` and the exceptional classes gives

```
R^2 <= d^2/16 - (1/2) sum_i m_i^2
    <= 4 - 17/2
    = -9/2.
```

Since `R^2` is integral and adjunction gives the same parity as `d),

```
R^2 <= -6.
```

Therefore

```
p_a(R)
 = 1 + (R^2 + K.R)/2
 = 1 + (R^2 + 8)/2
 <= 2.
```

But arithmetic genus is at least geometric genus, while the published classification gives geometric genus `3` or `5`. Contradiction.

So no `P^4`-spanning integral curve pairs negatively with `P`.

## 5. Exceptional curves

For the 48 exceptional curves:

```
P.E_i = 8 >0  if i in Sigma,
P.E_j = 0     if j notin Sigma.
```

Thus none is negative.

## 6. Nef conclusion

Every irreducible curve on the smooth cuboid resolution is now covered:

- exceptional curves: nonnegative;
- span P2/P3: strictly positive by exact known-curve replay;
- span P4: negative pairing contradicts Stoll--Testa genus classification plus Hodge/adjunction;
- span P5/P6: strictly positive by the robust thirty-hyperplane certificate.

Therefore

```
P is nef,
D_l=lP is nef for every l>=1.
```

Since

```
P^2=336>0,
```

the ray is also big.

The only null curves established by this gate are the unsupported exceptional curves `E_j`, for which `P.E_j=0`.

## 7. Interpretation

This closes the test-curve/effective-cone **negative-pairing** strategy on the hostile P6 survivor in the opposite direction from the original hope:

```
the survivor is not killed by a hidden fixed component;
the exact ray is big and nef.
```

This is stronger than testing a finite curve library and stronger than the seven coordinate-sign K3 root-wall checks.

It does **not** imply that an integral normalization-genus-one member exists. Riemann--Roch effectivity and nefness do not supply irreducibility or the required singularity packet.

The next useful route must therefore attack the genus-one/singularity condition on a big-nef ray, not search for additional negative test curves.

Natural next gate:

```
P6F = BIG-NEF GENUS-ONE SINGULARITY / EQUISINGULAR GATE
```

Start from the retained Lu--Miyaoka requirement

```
n_ordinary_node_or_triple >= max(0,112l-224)
```

and test whether big-nef positivity supplies a source-complete regularity/T-smoothness theorem. Do not use a bare expected-dimension count without controlling the already-retained equigeneric superabundance.

## Source locks

- Z33 hyperplane-contact note at predecessor head
  `b28adadc95776762754e1415a0ecab0da1d4cd8e`,
  blob `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`.
- P6B certificate blob
  `6713ec219456783180bb7966cf3a8420307accff`.
- P6E Stoll--Testa source note blob
  `0959df8849ed0b36e6e57bccda48d11b4ab4eecf`.
- P6E exact certificate blob
  `9579b0c2b909310b426cd4a1539b3d4c2ede0248`.

## Firewalls

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
