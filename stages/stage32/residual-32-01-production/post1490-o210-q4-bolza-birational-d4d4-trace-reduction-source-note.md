# Stage32 post-1490 O210 Bolza birational correspondence / D4+D4 trace reduction

Scope: fixed recovered V6 class `g1-d186` only, at `O=210`, `q'=4`.
This note starts from the exact Bolza principal Rosati lock
`8d828cdf6d1f5cb1d790c46292535dc252e503356e1047ce972c41e61f524529`.
It derives a new necessary constraint on the simultaneous `(105,81)`
correspondence and performs the required lightweight enumeration preflight.
It does not claim geometric realization of any lattice point and does not
exclude O210.

## 1. The pair map is birational

Retain the exact quotient notation

- `Z=X(8)`;
- `H=Gamma'[4]/Gamma[8] ~= V4`, acting freely on `Z`;
- `P=Z x Z`;
- `X=P/H_diag`;
- `C0=Z/H`.

Because `H` is abelian, `H_diag` is normal in `H x H`, and

`(H x H)/H_diag ~= H ~= V4`.

The free action of `H x H` on `P` therefore gives a finite etale Galois map

`q : X -> C0 x C0`

of degree four with deck group V4.

For a hypothetical carrier, the retained Beauville pullback `Y` is the
normalization of its image curve in `X`. The two retained maps
`f1,f2:Y->C0` are exactly the two components of `q|_Y`, with degrees
`105` and `81`.

Let `e` be the generic degree of the pair map

`F=(f1,f2):Y -> Gamma subset C0 x C0`.

For a curve in a V4-Galois cover, this generic degree is the order of the
deck stabilizer of its generic image curve, so

`e in {1,2,4}`.

On the other hand, after normalizing `Gamma`, both `f1` and `f2` factor
through the degree-`e` map, hence `e` divides both 105 and 81. Thus

`e | gcd(105,81)=3`.

Consequently `e=1`. The pair map is birational onto the integral
correspondence curve `Gamma`, whose normalization is `Y` and whose
geometric genus is 106.

## 2. Correspondence self-intersection and Rosati trace

For the standard correspondence intersection identity use Igor Dolgachev
and Yuri G. Zarhin, *Endomorphisms of Complex Abelian Varieties*,
April 8, 2025 manuscript, Chapter 10, Section 10.1, equations (10.3) and
(10.4) and the paragraph identifying switch of factors with the Rosati
involution:

`https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1467/2025/10/Endomorphisms_April_2025.pdf`

The exact imported identity for a correspondence `D` of bidegree
`(d1,d2)` on `C x C` is

`Sigma(D)=2*d1*d2-D^2
         =2*d1*d2+(2g(C)-2)(d1+d2)-2*p_a(D)+2`,

and under `Corr(C) ~= End(J(C))` this is the rational trace of the
Rosati product of the associated endomorphism with its adjoint.

For `Gamma`, write

`p_a(Gamma)=106+delta`,  `delta>=0`.

With `g(C0)=2` and `(d1,d2)=(105,81)`,

`Tr_Q(T^dagger*T) = 17172 - 2*delta`.

Here switching the factors replaces the correspondence endomorphism by
its Rosati adjoint, so the formula applies to the retained
`T=(f1)_*(f2)^*` without an orientation ambiguity.

In `End(E^2)=M_2(Q(sqrt(-2)))`, a Rosati-symmetric matrix has rational
trace twice its ordinary 2-by-2 matrix trace. Hence define

`Q(T)=tr_2(H^{-1}*bar(T)^t*H*T)`.

Then every geometric survivor satisfies the exact identity

`Q(T)=8586-delta <= 8586`.

## 3. Exact rank-eight lattice is D4 + D4

Write each entry of `T` as `a+b*r`, `r^2=-2`, in coordinate order

`(t11.a,t11.b,t12.a,t12.b,t21.a,t21.b,t22.a,t22.b)`.

Exact expansion of `Q(T)` gives Gram matrix

```
A =
[ 4,  0, -2, -4,  2, -4, -3,  0]
[ 0,  8,  4, -4,  4,  4,  0, -6]
[-2,  4,  4,  0,  1,  4,  2, -4]
[-4, -4,  0,  8, -4,  2,  4,  4]
[ 2,  4,  1, -4,  4,  0, -2, -4]
[-4,  4,  4,  2,  0,  8,  4, -4]
[-3,  0,  2,  4, -2,  4,  4,  0]
[ 0, -6, -4,  4, -4, -4,  0,  8]
```

Its determinant is 16. The verifier source-locks an explicit determinant-one
integral change of basis whose transformed Gram matrix is two copies of

```
D4 =
[ 2,-1, 0, 0]
[-1, 2,-1,-1]
[ 0,-1, 2, 0]
[ 0,-1, 0, 2].
```

Therefore the exact trace lattice is `D4 direct-sum D4`. In particular
`Q(T)` is always even, so the geometric singularity defect `delta` is
necessarily even.

## 4. Exact preflight count: materialization is impossible

For `D4={x in Z^4 : sum x_i is even}` with the usual Euclidean norm,
a vector of even norm automatically has even coordinate sum. Jacobi's
four-square theorem gives

`r_4(n)=8*sum_{d|n, 4 not-divides d} d`.

Thus the number of `D4` vectors of norm `2m` is

`a(0)=1`,
`a(m)=24*sum_{d|m, d odd} d` for `m>=1`.

Convolving two copies gives an exact count for the trace ellipsoid
`Q(T)<=8586` (`m<=4293`):

`5,516,362,054,085,041`

integral matrices, including zero.

For a positive semidefinite `T^dagger*T`, the old operator bound
`T^dagger*T <= 8505 I` is automatic whenever
`tr_2(T^dagger*T)<=8505`. Since `Q(T)` is even, every point with
`Q(T)<=8504` automatically survives both the new trace bound and the old
Rosati operator bound. Their exact count is

`5,309,821,812,906,193`.

The remaining trace shell `8506<=Q(T)<=8586` contains

`206,540,241,178,848`

points before the determinant/operator filter.

For reference, in the shell the 2-by-2 positive Hermitian operator
condition is equivalently

`Norm(det T) >= 8505*Q(T) - 8505^2`;

for `Q(T)<=8505` the right side is nonpositive, which is the automatic
case above.

Source for the counting formula: M. D. Hirschhorn,
*A simple proof of Jacobi's four-square theorem*,
J. Austral. Math. Soc. (Series A) 32 (1982), 61-67, formula (1.1).

## Verdict and next leaf

The requested lightweight preflight is decisive: exact materialization of
the Rosati-only frontier is neither storage-safe nor mathematically useful.
There are already more than 5.3 quadrillion integral endomorphisms satisfying
the current trace and operator inequalities.

Therefore the correct next step is not brute-force enumeration. It is to
consume an independent geometric constraint (the retained common-cover /
six-Weierstrass structure, or an equivalent exact invariant) in the
`D4 direct-sum D4` coordinates before any survivor materialization.

Firewalls:

- O210 remains OPEN.
- The count is a count of integral endomorphism candidates, not geometric
  correspondences.
- No carrier existence/effectivity is inferred.
- O186/O188 and the Abel-Jacobi-zero closure remain closed.
- FULL178 remains inactive.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
