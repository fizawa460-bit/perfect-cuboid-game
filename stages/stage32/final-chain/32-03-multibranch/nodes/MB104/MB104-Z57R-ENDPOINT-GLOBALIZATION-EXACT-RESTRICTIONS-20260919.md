# MB104 Z57R — endpoint globalization exact restrictions — 2026-09-19

Status: **PRE-AUDIT EXACT ENDPOINT GLOBALIZATION REDUCTION / TANGENT BIT STILL OPEN / NO CREDIT**

## Input

On the corrected size48 canonical-cover resolution let

```
D=E_L-C1-C2-C3-C4-C5-E_R,
F=D+Gamma=(1,2,2,2,2,2,1),
Gamma=C1+...+C5.
```

For either elliptic endpoint E with attachment point p, the exact normal bundle is

```
N_E=O_E(E) ~= O_E(-2p).
```

## 1. Restriction of the maximal-ideal bundle

Only the adjacent C1 (or C5) meets E.  Its coefficient in F is two.  Hence

```
O_E(-F)
 = N_E^(-1) tensor O_E(-2p)
 ~= O_E(2p-2p)
 ~= O_E.
```

Thus every maximal-ideal section restricts to a constant on each elliptic endpoint.

This is the endpoint part of the three-dimensional reduced-exceptional section space retained in
Z56.

## 2. Restriction of the first-normal bundle

For F+D the endpoint coefficient is two and the adjacent rational coefficient is three:

```
O_E(-F-D)
 = N_E^(-2) tensor O_E(-3p)
 ~= O_E(4p-3p)
 ~= O_E(p).
```

Hence

```
h0(E,O_E(-F-D))=1.
```

Its unique nonzero section has a simple zero at p.

So the endpoint jet of any first-normal candidate is unique up to scale; there is no additional
endpoint-dimensional family.

## 3. Comparison with m^2

For 2F,

```
O_E(-2F)
 = N_E^(-2) tensor O_E(-4p)
 ~= O_E.
```

The inclusion

```
O_E(-2F) -> O_E(-F-D)=O_E(p)
```

is multiplication by the canonical section of O_E(p), whose divisor is p.

Since both global section spaces are one-dimensional, the induced map on H0 is an isomorphism onto
the unique section of O_E(p).

Therefore the endpoint restriction alone cannot detect whether a section in O(-F-D) survives
modulo O(-2F): the quotient direction is supported in the central A5 strip, not on E.

This corrects the tempting but invalid attempt to read the tangent bit directly from a local
transverse coordinate on E.

## 4. Where the fourth tangent direction actually lives

Cycle comparison gives

```
2F-(F+D)=Gamma.
```

Thus the quotient sheaf

```
O_X(-F-D) / O_X(-2F)
```

is supported on Gamma.

The endpoint restrictions above show that no residual quotient is carried by E_L or E_R.

Consequently the fourth tangent direction of Z56 is a **global section whose nontrivial class modulo
m^2 is detected only on the central A5 chain**, while its endpoint jets are forced by O_E(p).

## 5. Konno source interface

For type (II), m=1, Konno Lemma 5.6 gives:

```
m^n = pi_* O_X(-nF),
embdim=4,
R(Z_K,-F) generated in degree one.
```

The proof uses

```
h0(Z_K,O(-F))=6
```

and a two-dimensional kernel to obtain the four-dimensional tangent image.

Together with the present endpoint calculation, the T0/T1 bit is therefore reduced to identifying
the exact four-dimensional image subspace inside the six-dimensional source space and computing
its degree-two multiplication on Gamma.

No endpoint transition modulus remains to be searched.

## 6. Next leaf

```
MB104-Z58-KONNO-SIX-TO-FOUR-TANGENT-IMAGE-MULTIPLICATION
```

Target:

1. materialize the exact six-dimensional `H0(Z_K,O(-F))` section model;
2. materialize the two-dimensional kernel appearing in Lemma 5.6;
3. quotient to the four tangent generators;
4. compute the two-dimensional kernel of
   `Sym^2(m/m^2)->m^2/m^3`;
5. read whether the second quadric is `yz` or `yz+xw`.

The local A5 equation may be used only to coordinatize the central chain after this global quotient
is fixed.

## Firewalls

```
endpoint_restrictions_exact=true
endpoint_continuous_modulus_remaining=false
fourth_tangent_class_supported_centrally_mod_m2=true
actual_tangent_type_T0=false
actual_tangent_type_T1=false
mixed_coefficient_c_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
