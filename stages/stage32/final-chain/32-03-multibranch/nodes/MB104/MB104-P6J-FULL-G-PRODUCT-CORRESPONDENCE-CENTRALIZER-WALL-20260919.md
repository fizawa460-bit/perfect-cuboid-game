# MB104 P6J — full-G product-correspondence centralizer wall — 2026-09-19

Status: **PRE-AUDIT EXACT COMPLEX CENTRALIZER / INTEGRAL ENDOMORPHISM INTERFACE WALL / NO CREDIT**

## Target

P6D2 forces a connected full-deck product pullback

```text
Z -> C8 x C8
```

with both factor maps etale of degree `56l` and with the diagonal action of

```text
G ~= (Z/2)^3
```

stabilizing `Z`. Therefore the product correspondence induced on `J(C8)` commutes with `G`.

This leaf computes the exact complex-linear `G`-centralizer and asks whether the retained source inventory upgrades it to a restrictive integral/algebraic endomorphism ring.

## 1. Character of H^0(C8,K)

The retained product/source geometry gives

```text
g(C8)=5.
```

There are exactly three singular involutions `s1,s2,s3`, each with eight fixed points. Riemann--Hurwitz for an involution gives quotient genus one. Hence on

```text
V=H^0(C8,K_C8)
```

each `s_j` has invariant dimension one and trace

```text
1-4 = -3.
```

The other four nonidentity elements of `G` are fixed-point-free; their quotient genus is three, so their trace on `V` is

```text
3-2 = +1.
```

The full quotient `C8/G` is `P1`, so the trivial character is absent.

Take `s1,s2,s3` as an F2-basis of `G`. Fourier inversion gives the exact character multiplicities:

```text
weight 0:  m=0,
weight 1:  m=0,0,0,
weight 2:  m=1,1,1,
weight 3:  m=2.
```

Thus

```text
V ~= chi_12 + chi_13 + chi_23 + 2 chi_123.
```

This is the same weight pattern already visible in P6H through the quadratic building-line degrees.

## 2. Complex-linear centralizer

Therefore

```text
End_C(V)^G
  ~= C direct_sum C direct_sum C direct_sum M_2(C),
dim_C = 1+1+1+4 = 7.
```

Any algebraic correspondence commuting with `G` maps into this seven-dimensional algebra on holomorphic differentials.

Diagonal `G`-stability of the current full-deck product curve is enough to obtain this centralizer condition; the historical support-specific e=2 candidate relation `Phi_Z=0` is neither used nor imported.

## 3. Why this does not close P6

The complex centralizer is not small enough to force a contradiction. In particular, the weight-three isotypic component already allows an arbitrary `2 x 2` block.

The retained archive contains support-specific computations of `J(C8)^G[2]` and candidate e=2 Rosati/product reductions, and a CM adapter for the elliptic quotients `C8/<s_j>`. None of the bounded retained assets inspected here supplies a source-complete identification of

```text
End(J(C8))^G
```

as an integral order together with the degree/Rosati constraints for the present full-deck e=4 common correspondence.

Therefore the exact complex character calculation cannot be promoted to a finite algebraic correspondence classification by assumption.

## 4. Disposition

```text
full-G complex centralizer = EXACT, dimension 7,
integral/algebraic centralizer classification = MISSING INTERFACE,
correspondence excluded = false.
```

P6J is parked at the integral endomorphism-ring interface. This is not a repository-wide claim that no such description exists; it records only the retained source boundary checked for the current lane.

## 5. Next exact invariant

The common-cover structure has a stronger function-field statement that does not require the full endomorphism ring. For each of the three generating quadratic characters of `G`, the two factor maps must pull back the same quadratic subextension of `k(Z)/k(E)`.

The next leaf is therefore

```text
MB104-P6K-FULL-G-CHARACTER-SQUARE-CLASS-COUPLING.
```

Target: source-lock the three quadratic branch functions on `C8/G=P1` and prove exact square-class equalities

```text
q_j(psi_1) / q_j(psi_2) in k(E)^{*2},  j=1,2,3.
```

Then determine whether their divisors/Abel--Jacobi classes add information beyond P6H.

## Source locks

Historical archive exact head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md` blob `a29161602c0b38f0607794e56e61068b8cb9735d`;
- `GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY.md` blob `cb05a7a187c9dd7495ee1f4af3b92fb776900422`;
- historical product-correspondence comparison only: blob `2c2db567db6a3c33762b2ff3d7f39f885a95b974`;
- elliptic-quotient CM adapter only: blob `24d48dfc50aca285d8808b95b2685b196511c666`.

## Firewalls

```text
complex_G_centralizer_dimension=7
integral_End_JC8_G_classified=false
historical_e2_PhiZ_zero_imported=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
