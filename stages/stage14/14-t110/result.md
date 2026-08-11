# Stage14-t110 — lift the projective prime class to Gaussian residue classes

## Status

`COMPLETE_PROJECTIVE_CLASS_TO_GAUSSIAN_RESIDUE_CLASS_UNION`

Consumes Stage14-t109 on the same batch branch and merged Stage14-t90/t87 projective-selector structure.

On a live primitive cofactor ray, t109 reduces the moving prime-side acceptance to

```text
[pi_ell]=c in
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x,
d=B^o(1),
gcd(d,ell)=1.
```

Choose any representative `rho in (Z[i]/dZ[i])^x` of the projective class `c`.  By the definition of the quotient,

```text
[pi_ell]=[rho]
```

is equivalent to the existence of a rational unit

```text
s in (Z/dZ)^x
```

such that

```text
pi_ell == s*rho (mod d).
```

Therefore one projective class is exactly the union

```text
C(c,d)
 = {s*rho mod d : s in (Z/dZ)^x}
```

of invertible Gaussian residue classes.  Its cardinality is at most

```text
phi(d)<=d=B^o(1).
```

Changing the representative `rho` only permutes this union.  The canonical Gaussian unit/orientation convention changes the lift by at most an `O(1)` factor and creates no polynomial family.

Hence the accepted dominant primes on one core ray are exactly those canonical split Gaussian primes whose residue lies in the subpolynomial union `C(c,d)` and whose rational norm lies in

```text
I_B(n)=
(max(2*sqrt(B),2*h*k0*n), 2B/(h*k0*n)].
```

Equivalently, the t109 persistent-ray problem is a finite/subpolynomial union of ordinary Gaussian prime progression/ray-class occupancy problems with growing modulus `d=B^o(1)`.

This is an exact reformulation only.  No prime ideal theorem, Chebotarev estimate, Siegel--Walfisz statement, or lower/upper density estimate is imported here.  In particular, the general subpolynomial growth of `d` is not silently replaced by a fixed or polylogarithmic modulus.

```text
PROJECTIVE_CLASS_LIFT_TO_GAUSSIAN_RESIDUES_EXACT=true
PROJECTIVE_CLASS_RESIDUE_UNION_SIZE=Bo1
GAUSSIAN_RESIDUE_CLASSES_INVERTIBLE=true
CANONICAL_UNIT_ORIENTATION_COST=O1
RAY_OCCUPANCY_REDUCED_TO_GAUSSIAN_PRIME_PROGRESSIONS=true
UNIFORM_GAUSSIAN_PRIME_PROGRESSSION_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUSubpolynomialGaussianProjectivePrimeClassOccupancyAlongPrimitiveCofactorRays
NEXT=Stage14-t111
```
