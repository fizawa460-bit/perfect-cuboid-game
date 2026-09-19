# MB104 Z48 — conductor-scheme adjoint adapter on the smooth interior — 2026-09-19

Status: **PARALLEL PRE-AUDIT NEW THEOREM/ADAPTER / EXACT CONDUCTOR-SCHEME REDUCTION / NO CREDIT**

## Purpose

The current Class-3 boundary permits reopening only if a materially new theorem or exact adapter
supplies conductor support/multiplicity control or converts the all-l carrier into a finite
proof-capable object with a reverse adapter.

For a hypothetical surviving integral genus-one carrier

```text
C in |lP|, l>=1,
nu:E -> C,
g(E)=1,
P^2=336,
K_S.P=112,
```

the earlier Z4'/Z3 work gives:

```text
deg Delta = 336l^2+112l = 2 delta(C),
Supp(Delta) is disjoint from the full exceptional locus and the P-null quartics.
```

Z48 replaces the divisor-on-normalization viewpoint by the intrinsic conductor **scheme** on the
smooth surface.

## 1. Conductor ideal and exact quadratic length

Let

```text
c_C = Ann_{O_C}(nu_*O_E / O_C)
```

be the conductor ideal of the normalization.

Because C is an integral Cartier divisor on the smooth surface S, C is Gorenstein.  For a
Gorenstein curve singularity the conductor colength equals the local delta invariant:

```text
length(O_{C,p}/c_{C,p}) = delta_p(C).
```

Equivalently, on the normalization the conductor divisor has degree `2 delta_p`, while the
conductor scheme downstairs has length `delta_p`.

Let `F_C subset O_S` be the inverse image of `c_C` under
`O_S -> O_C`.  Define the zero-dimensional surface conductor scheme

```text
Z_cond := V(F_C) subset S.
```

Then

```text
O_{Z_cond} = O_C/c_C
```

and therefore

```text
length(Z_cond)
 = delta(C)
 = 168l^2+56l.                                  (COND-LENGTH)
```

This is the missing exact quadratic singularity scheme.  By the previous Z4'+Z3 forbidden-locus
result,

```text
Supp(Z_cond)
 subset S \ (all 48 exceptional curves union all P-null elliptic quartics).
```

Hence Z_cond is entirely supported in the smooth interior of the original cuboid surface.

## 2. Surface adjoint exact sequence

For an integral curve on a smooth surface, the conductor is the restriction of the adjoint ideal.
The classical adjunction/conductor sequence is

```text
0
 -> O_S(K_S)
 -> F_C tensor O_S(K_S+C)
 -> nu_* omega_E
 -> 0.                                           (ADJ)
```

Since `g(E)=1`,

```text
omega_E ~= O_E,
h0(E,omega_E)=1.
```

For the cuboid surface, the canonical model is the complete intersection of four quadrics in
P^6 with only A1 singularities.  Its minimal resolution has

```text
K_S=H,
K_S^2=16,
c2(S)=80,
chi(O_S)=8,
q(S)=0,
p_g(S)=7.
```

Thus `H1(S,K_S)=0` by Serre duality.

Taking H0 of (ADJ) gives

```text
h0(S, F_C(K_S+C))
 = h0(S,K_S)+h0(E,omega_E)
 = 7+1
 = 8.                                            (ADJ-H0)
```

## 3. The conductor scheme imposes exactly delta independent adjoint conditions

Because `lP` is big and nef, Kawamata--Viehweg vanishing applies to

```text
K_S+C = K_S+lP.
```

Hence

```text
H^i(S,O_S(K_S+C))=0  for i>0.
```

Riemann--Roch gives

```text
h0(S,O_S(K_S+C))
 = chi(O_S) + ((K_S+C).C)/2
 = 8 + (112l+336l^2)/2
 = 168l^2+56l+8
 = delta(C)+8.                                   (ADJ-DIM)
```

From

```text
0 -> F_C(K_S+C)
  -> O_S(K_S+C)
  -> O_{Z_cond}(K_S+C)
  -> 0
```

and (ADJ-H0), the kernel of evaluation on Z_cond has dimension 8, while the source has dimension
`delta+8` and the target has dimension `length(Z_cond)=delta`.

Therefore the evaluation map is surjective:

```text
H0(O_S(K_S+C)) -> H0(O_{Z_cond}(K_S+C))
```

and Z_cond imposes **exactly delta(C) independent conditions** on the canonical adjoint system.

So the first adjoint/Cayley--Bacharach dimension attack is an exact equality, not an
overdetermination.

## 4. Reverse adapter: Z_cond determines the carrier inside |C|

Twist the defining conductor sequence

```text
0 -> O_S(-C) -> F_C -> c_C -> 0
```

by `O_S(C)`:

```text
0 -> O_S
 -> F_C(C)
 -> c_C tensor O_C(C)
 -> 0.                                           (C-TWIST)
```

On the normalization, the conductor ideal pulls back to the conductor divisor:

```text
nu^* c_C = O_E(-Delta).
```

The retained Z4' identity gives

```text
O_E(C) ~= (H|E)^(3l),
O_E(Delta) ~= (H|E)^(3l+1).
```

Hence

```text
nu^*(c_C tensor O_C(C))
 ~= O_E(C-Delta)
 ~= (H|E)^(-1).
```

Its degree is

```text
- deg(H|E) = -112l < 0.
```

Therefore

```text
H0(C, c_C tensor O_C(C)) = 0.
```

Taking H0 in (C-TWIST) yields

```text
H0(S,F_C(C)) ~= H0(S,O_S),
h0(S,F_C(C)) = 1.                                (UNIQUE-CARRIER)
```

Thus among divisors in `|C|=|lP|`, the only section vanishing on the full conductor scheme
Z_cond is the defining section of C itself.

This is a genuine reverse adapter:

```text
carrier C
 -> finite length conductor scheme Z_cond
 -> unique carrier section in |lP| containing Z_cond.
```

It does not make the set of possible Z_cond finite; it says that once such a scheme is known,
the carrier is uniquely recovered in its linear system.

## 5. Consequence for the Class-3 boundary

Z48 materially improves the missing interface:

Before:

```text
quadratic singularity mass known only as deg Delta on E.
```

After:

```text
Z_cond subset smooth interior of S,
length(Z_cond)=168l^2+56l,
Z_cond imposes exactly delta independent conditions on |K_S+C|,
Z_cond uniquely determines C inside |C|.
```

However, no exact classification of the possible schemes Z_cond is yet available.  Therefore
this is not a finite enumeration and not a carrier exclusion.

The next theorem species is now narrower:

```text
classify/restrict conductor schemes of length 168l^2+56l
arising from integral genus-one divisors in |lP|,
or derive a regularity/Cayley--Bacharach condition stronger than the exact adjoint equality.
```

Any route that merely recounts the delta length or canonical adjoint dimension is now exhausted.

## Source locks

External classical inputs:

- D. Gorenstein, *An Arithmetic Theory of Adjoint Plane Curves*,
  Trans. Amer. Math. Soc. 72 (1952), conductor formulation of adjoints and complete canonical
  series.
- Classical adjoint-system duality: for an integral curve on a nonsingular surface, the inverse
  image of the conductor is the adjoint ideal and gives the adjunction sequence (ADJ).
- For Gorenstein curve singularities,
  `length(O_C/c_C)=delta` and `length(O_E/c_C)=2 delta`.
- Stoll--Testa, *The surface parametrizing cuboids*: the cuboid canonical model is a geometrically
  integral complete intersection of multidegree (2,2,2,2) in P^6 with 48 A1 singularities.

Retained Stage32 inputs:

- Z3/Z40B complete P-null locus;
- Z4'+Z3 conductor support disjointness from the exceptional/null boundary;
- Z4'+Z5' identity
  `O_E(Delta) ~= O_E((3l+1)B_node)`;
- P big and nef, `P^2=336`, `K_S.P=112`.

## Firewalls

```text
quadratic_conductor_scheme_exact=true
conductor_scheme_length_delta_exact=true
conductor_scheme_supported_in_smooth_interior=true
adjoint_conditions_independent_exact=true
carrier_unique_given_full_conductor_scheme=true
possible_conductor_schemes_finitely_classified=false
finite_degree_window_proved=false
carrier_excluded=false
R29_LG2_MB_discharged=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
