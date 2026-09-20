# Stage32 MB-FIB -> MB consumer integration

Status: **ACTIVE ROUTING / PRODUCER-ONLY / NO CREDIT**

This note records the exact consumer target for `stage32mb-fib`. MB-FIB is not allowed to stop at a finite shell census. Its outputs must be assessed against the current MB104 obstruction.

## Current MB consumer obstruction

Current `stage32mb-mainbatch` has retained the ambient chain

```
complete Armstrong fixed-point normal closure
 -> H1(X_H,Z)=0
 -> Pic^tau(Y)=0
 -> w~0
 -> Gamma~tau Gamma on X_H
 -> Zbar~Tdiag(Zbar) on C8 x C8
 -> Phi_Z in End(J(C8))^G.
```

The remaining direct e=2 obstruction is the conductor transition bit. For conductor-identified normalization preimages `x_i,x_j`, the one-coordinate exact-converse receiver is

```
delta_ij = r_z(x_j)/r_z(x_i) in mu_2.
```

It has the exact interpretation

```
delta_ij=+1 <=> same residual sheet,
delta_ij=-1 <=> opposite residual sheet,
```

and the weighted conductor cut is

```
y/2 = sum_p sum_(i<j) I_p(beta_i,beta_j) * (1-delta_(p;i,j))/2.
```

The Hodge obstruction requires `y/2 >= 84*l^2`. The current MB repository does not source-lock the branch-specific normalization-to-product lift needed to evaluate `delta_ij`.

## MB-FIB proof route

### FIB-A: exact low-degree fibration shell census

Run the retained exact Picard64 affine-coset enumeration on support `000707000f0f`:

- shell 0: degree 10, `P.F=30`, mass 10, H-perp norm 400;
- shell 1: degree 10, `P.F=34`, mass 9, H-perp norm 400;
- shell 2: degree 10, `P.F=38`, mass 8, H-perp norm 400;
- shell 3: degree 12, `P.F=36`, mass 12, H-perp norm 144.

Retain only exact Picard64-integral primitive classes nonnegative on the retained known140 set. A zero candidate result is numerical producer evidence only.

### FIB-B1: local consumer bridge to the conductor bit

For every retained shell candidate that can be promoted to an actual fibration/effective pencil, attempt to construct a source-locked local normalization chart at the dangerous supported branches and an explicit specialization of a residual Kummer semi-invariant `r_z`.

Required output shape:

```
(branch / normalization preimage)
 -> fibration-local coordinate
 -> product lift in C8 x C8
 -> residual Kummer coordinate r_z
 -> delta_ij=r_z(x_j)/r_z(x_i).
```

A valid B1 handoff must determine `delta_ij` for actual conductor pairs, or prove a symmetry/monodromy rule that determines a whole certified class of pairs. Numerical fiber totals, support masses, or `eta=0` alone are insufficient.

### FIB-B2: global consumer bridge avoiding pointwise conductor signs

Independently of B1, use the fibration/Picard divisor classes to attack the retained global product-correspondence consequence

```
Zbar ~ Tdiag(Zbar),
Phi_Z in End(J(C8))^G.
```

A valid B2 handoff is an exact contradiction to the existence of the required degree-`28l` etale self-correspondence with the retained support passport. Acceptable forms include:

1. an exact divisor-class calculation of `O_{C8 x C8}(Zbar)` incompatible with `Zbar~Tdiag(Zbar)`;
2. an exact Jacobian decomposition / endomorphism-ring restriction excluding the required integral full-`G` centralizer element;
3. a fibration-induced intersection or residual-geometry identity forcing a contradiction with the retained product-image genus/singularity budget.

B2 is useful specifically because it can close e=2 without evaluating every `delta_ij`.

## Decision tree

- If all FIB-A shells are empty: retain the audited enumeration certificate. Compose separately with the retained degree reduction / degree-8 exhaustiveness to establish the strongest justified global fibration statement. Then test whether that optimum yields a B2 divisor/intersection obstruction. Do not infer e=2 closure from emptiness alone.
- If FIB-A has candidates: send each candidate first to B1 and B2. Degree-10 candidates use residual sextic geometry; degree-12 candidates use `QA+QB+degree4` residual geometry.
- If B1 determines enough conductor signs to prove the weighted cut is strictly below `84*l^2`, hand off the exact conductor table/certificate to MB.
- If B2 proves the required product correspondence cannot exist, hand off that contradiction to MB without conductor-sign reconstruction.
- If neither B1 nor B2 connects the fibration data to the MB consumer obstruction, mark the fibration result as producer-only and do not claim MB progress.

## Handoff requirements

Every consumer handoff must include:

- producer PR and exact head;
- hostile-audit receipt;
- exact certificate/blob identity;
- support/population semantics;
- whether the result is FIB-A, B1, or B2;
- the precise MB statement released;
- explicit firewalls for all stronger claims.

MB-FIB does not close MB104, Stage32-03, MAIN, theorem, endpoint, or Perfect-Cuboid claims by itself.
