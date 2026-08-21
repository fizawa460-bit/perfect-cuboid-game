# Stage29-02e audit — global coordinate-K3 eigenspace adapter

```text
ROLE=GLOBAL_COORDINATE_SIGN_K3_TO_NEWFORM_IDENTIFICATION
STATUS=AUDITED_PASS
LOAD_BEARING_FINITE_PRIME_MATCH=false
```

## 1. Canonical eigenspaces of the seven sign quotients

Let

```text
x=(a1,a2,a3,b1,b2,b3,c)
```

be the seven canonical coordinates on the four-quadric cuboid canonical model `Sbar` in `P^6`.

Testa--Stoll prove that `Sbar` has only rational-double-point singularities, that

```text
omega_Sbar ~= O_Sbar(1),
pg(S)=7,
q(S)=0,
h11(S)=64,
rho(S)=64,
```

and that quotienting by the sign change of any one coordinate gives one of the seven K3 quotients

```text
Ka1,Ka2,Ka3,Kb1,Kb2,Kb3,Kc.
```

For a coordinate sign involution `sigma_xj`, all four defining quadrics are invariant and the ambient diagonal linear map has determinant `-1`. In the residue realization of canonical forms, a canonical section represented by a linear coordinate `x_k` therefore has eigenvalue

```text
det(sigma_xj) * sign_sigma(x_k).
```

Hence

```text
H20(S)^(sigma_xj=+1) = <x_j>.
```

The seven coordinate K3 quotients therefore pull back their one-dimensional `H20` spaces to the seven distinct canonical coordinate lines.

## 2. The seven K3 transcendental pieces exhaust the endpoint transcendental part

The Hodge diamond and geometric Picard rank give

```text
rank H2(S)=78,
rho(S)=64,
rank T(S)=14,
T(S)_C = H20(S) + H02(S).
```

There is no residual transcendental `(1,1)` part.

Each generically finite quotient map from `S` to a smooth coordinate K3 induces an injection of transcendental Hodge structures back into `T(S)`. Since `T(S)` has no transcendental `(1,1)` part, each K3 transcendental lattice has rank exactly `2`. Distinct pulled-back `H20` coordinate lines force the seven rank-two pieces to be pairwise disjoint. Their dimensions sum to `14`, so

```text
T(S) = direct_sum_{x in {a1,a2,a3,b1,b2,b3,c}} T(K_x).
```

The quotient maps are defined over `Q`, so the same decomposition is Galois-stable on l-adic realizations after scalar extension.

## 3. Orbit multiplicities force the modular labels

Testa--Stoll give the Q-isomorphism orbits

```text
3 * K_b,
1 * K_c,
3 * K_a,
```

while Horie--Yamauchi Theorem 4.4 gives the semisimple non-Tate endpoint representation

```text
3 * V_h16 + 1 * V_h32 + 3 * V_h8.
```

The three modular representations are pairwise non-isomorphic. Since every coordinate K3 transcendental piece is two-dimensional and the seven pieces exhaust `T(S)`, the unique multiplicity-one orbit must be the unique multiplicity-one modular constituent:

```text
T(K_c) = V_h32.
```

Testa--Stoll further prove `K_a ~= K_c` over `Q(i)`. Horie--Yamauchi identify `h32` as CM by `Q(sqrt(-2))` and `h16` as CM by `Q(i)`, and give

```text
V_h8 ~= chi_2 tensor V_h32.
```

Because a CM representation by `Q(sqrt(-2))` has the self-twist `chi_-2`,

```text
V_h8 ~= chi_2 chi_-2 tensor V_h32
      = chi_-1 tensor V_h32.
```

Thus `V_h8` and `V_h32` become isomorphic over `Q(i)`. By contrast `V_h16` restricts to the CM field `Q(i)` as a reducible induced-CM representation, while `V_h32` remains associated to the distinct CM field `Q(sqrt(-2))`; it cannot be the `K_a` restriction. Therefore

```text
T(K_a) = V_h8,
T(K_b) = V_h16.
```

This is a global semisimple l-adic identification, not a conclusion from finitely many Frobenius traces.

## 4. Stage19 / Stage20 and cross quotient

Using the already-audited Stage29-02b geometric adapter,

```text
Stage19 space-completion K3 = K_b orbit,
Stage20 Euler/third-face K3 = K_c.
```

Hence

```text
Stage19 -> h16,
Stage20 -> h32.
```

For the audited V4 joint-cover diamond over the rational base `Y`, the three nontrivial character pieces are `X_sp`, `X_face`, and `X_cross`. Since `Y` has no transcendental H2,

```text
T(endpoint)
 = T(X_sp) + T(X_face) + T(X_cross).
```

Therefore

```text
T(X_cross)
 = (3*h16 + h32 + 3*h8) - h16 - h32
 = 2*h16 + 3*h8.
```

This has dimension `10`, agreeing with the independently derived `pg_cross=5` Hodge dimension.

## 5. Certification boundary

The result above closes the semisimple non-Tate representation only. It does not identify the complete algebraic Picard character package of `K_a`, `K_b`, or `X_cross`, and it does not compute resolution/boundary corrections or bad-prime local factors for the cross quotient.

```text
R29-L3=DISCHARGED_GLOBAL_EIGENSPACE_ORBIT_ARGUMENT
R29-L2-NT=DISCHARGED_GLOBAL_V4_SUBTRACTION
R29-L2-ALG=OPEN_BOUNDED
R29-L2-BAD=OPEN_BOUNDED
FULL_CROSS_LFUNCTION_COMPLETE=false
LOCAL_TRACE_TO_PHYSICAL_HEIGHT_COUNT=false
PERFECT_CUBOID_CONCLUSION=NONE
```
