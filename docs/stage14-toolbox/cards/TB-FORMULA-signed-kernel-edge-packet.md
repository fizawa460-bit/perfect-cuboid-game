# Signed squarefree kernel edge packet

```yaml
ID: TB-FORMULA-signed-kernel-edge-packet
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact signed squarefree kernel factorization on the three Pythagorean edges
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

An integral non-torsion witness with

```text
Gi=di*ui^2
```

and the exact pairwise gcd-support restrictions from toolbox-af.

## OUTPUT

There are positive odd squarefree `a,b,c` and `tau_i in {+1,-1,+2,-2}` such that

```text
d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c

a | rad_odd(S)
b | rad_odd(X)
c | rad_odd(H)

gcd(a,b)=gcd(a,c)=gcd(b,c)=1.
```

The product-square condition leaves exactly 16 admissible ordered `(tau0,tau1,tau2)` packets:

```text
product of signs = +1
number of even tau_i is even.
```

## VARIABLE DICTIONARY

- `a` = odd kernel on the `G0/G1` edge, supported on `S`.
- `b` = odd kernel on the `G0/G2` edge, supported on `X`.
- `c` = odd kernel on the `G1/G2` edge, supported on `H`.
- `tau_i` = finite sign/2-primary factor.

## USED BY

- Fixed-packet arithmetic.
- Composite edge-kernel incidence.
- Full-radical congruence derivation.
- Later two-quadrics geometry.

## DO NOT USE FOR

- Do not treat `a,b,c` as the full odd radicals of `S,X,H`; they are selected squarefree edge kernels.
- Do not infer a full-family saving from the fact that there are only 16 `tau` packets.
- Do not drop the sign/2-primary data when reconstructing the exact quadratic equations.

## PROVENANCE NOTES

Merged PR #345 proves the exact edge factorization and the sixteen-state sign/2-adic classification.