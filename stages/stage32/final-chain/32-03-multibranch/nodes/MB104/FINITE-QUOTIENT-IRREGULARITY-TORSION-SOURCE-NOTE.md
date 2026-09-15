# Stage32 MB104 source note — finite quotients, irregularity, and numerical torsion

Status: **EXTERNAL/STANDARD SOURCE ADAPTER / NO CONDUCTOR SIGN / NO CREDIT**

## Scope

This note records only the standard characteristic-zero facts used by the retained MB104 `000707`, `e=2` irregularity/torsion refinement. It does not identify a conductor pair, compute a residual sheet sign, or assert that a numerically trivial line bundle is trivial.

## 1. Finite quotient cohomology

Let a finite group `H` act on a projective complex variety `V`, and let

```text
q:V -> X=V/H
```

be the finite quotient. In characteristic zero the Reynolds averaging operator makes taking `H`-invariants exact. Since `q` is finite,

```text
H^i(X,q_*O_V)=H^i(V,O_V),
O_X=(q_*O_V)^H.
```

Averaging on a finite equivariant Čech resolution therefore gives

```text
H^i(X,O_X) = H^i(V,O_V)^H.                    (QCOH)
```

The same argument for a quotient curve `C -> C/H` gives

```text
H^1(C,O_C)^H = H^1(C/H,O_{C/H}).              (CURVE)
```

No freeness assumption is needed for these coherent-cohomology identities.

## 2. Quotient singularities are rational in characteristic zero

Finite quotient singularities over `C` are rational singularities. One standard route is Boutot's theorem that quotients of varieties with rational singularities by reductive groups in characteristic zero have rational singularities; finite groups are reductive in characteristic zero.

Reference:

- J.-F. Boutot, *Singularites rationnelles et quotients par les groupes reductifs*, Invent. Math. 88 (1987), 65--68.
- Stacks Project, Resolution of Surfaces, Section 54.9 (`0B4V`) for the rational-singularity resolution semantics used here.

Thus for a resolution

```text
rho:Xtilde -> X
```

of a normal projective surface with finite quotient singularities,

```text
rho_*O_Xtilde = O_X,
R^1 rho_*O_Xtilde = 0,
```

and Leray gives

```text
H^1(Xtilde,O_Xtilde)=H^1(X,O_X).              (RES)
```

## 3. Birational irregularity

For smooth projective complex surfaces, irregularity

```text
q(Y)=h^1(Y,O_Y)
```

is a birational invariant. Hence any two smooth projective models of one function field have the same `q`.

## 4. Numerically trivial line bundles when `Pic^0=0`

For a smooth projective variety, the group `Pic^tau` of numerically trivial line bundles contains `Pic^0` as its identity component, and

```text
Pic^tau / Pic^0
```

is the torsion subgroup of the Neron--Severi group. Since the Neron--Severi group is finitely generated, this quotient is finite.

Consequently, if

```text
Pic^0(Y)=0,
```

then every numerically trivial line bundle on `Y` is torsion. This does **not** imply that the line bundle is trivial and supplies no torsion exponent unless that exponent is computed separately.

## Firewalls

- No claim that a finite quotient is smooth.
- No claim that rational singularities imply trivial fundamental group.
- No claim that `Pic(Y)` is torsion-free.
- No claim that a numerically trivial divisor is linearly trivial.
- No conductor sign, weighted-cut bound, `e=2` closure, MB104 credit, or merge authorization.
