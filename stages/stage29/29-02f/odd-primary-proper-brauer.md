# Stage29-02f — proper-surface odd-primary transcendental Brauer witness

```text
SCOPE=smooth proper cuboid surface S/Q
NOT_YET_SCOPE=nonproper physical open U
STATUS=PASS_CANDIDATE_PENDING_FRESH_AUDIT
```

## Integral odd-prime adapter

Testa--Stoll determine

```text
rank Pic(S_Qbar)=64,
disc Pic(S_Qbar)=-2^28.
```

The smooth surface has `b2=78`, so the transcendental rank is 14.  Because the Picard discriminant is a pure power of two, for every odd prime `ell` the Neron--Severi lattice is `ell`-saturated in `H^2`; there is no odd-index Picard defect contaminating the rank-14 quotient.

The Stage29-02e audited global decomposition of the non-Tate part is

```text
3*h16 + h32 + 3*h8.
```

Each `hN` is a weight-3 two-dimensional representation.  At a good prime `p`, its `H^2` Frobenius polynomial is

```text
X^2-a_p X+p^2.
```

After Tate twist `(1)`, and for `p != ell`, eigenvalue `1 mod ell` implies

```text
2p-a_p == 0 mod ell.
```

For the full 14-dimensional package, a global invariant modulo `ell` would therefore force

```text
ell | D_p
```

for every good `p != ell`, where

```text
D_p=(2p-a_p(h16))^3*(2p-a_p(h32))*(2p-a_p(h8))^3.
```

## Exact witness values

The coefficients extracted from the audited 29-02e trace formulas are

```text
p :   3   5   7   11  13  17  19  23  29  31  37  41  43  47
h16:  0  -6   0    0  10 -30   0   0  42   0 -70  18   0   0
h32:  2   0   0  -14   0   2  34   0   0   0   0 -46 -14   0
h8 : -2   0   0   14   0   2 -34   0   0   0   0 -46  14   0
```

The exact integer checker proves

```text
gcd_p(2p-a_p(h16)) = 2
gcd_p(2p-a_p(h32)) = 2
gcd_p(2p-a_p(h8))  = 2

gcd_p D_p = 128.
```

For every odd `ell` occurring in the test-prime set, the gcd after deleting the forbidden row `p=ell` remains a power of two.  For an odd `ell` not in the set, all rows are allowed.  Thus no odd `ell` can divide `D_p` for every admissible witness prime.

## Brauer consequence

At odd `ell`, Kummer gives the geometric Brauer `ell`-torsion as the quotient of `H^2(mu_ell)` by `Pic/ell`; the Picard saturation above identifies the relevant rank-14 quotient with the reduction of the integral transcendental package.  A `G_Q`-invariant Brauer `ell`-torsion class would be fixed by every good Frobenius, contradicting the determinant witness.

Therefore the candidate conclusion is

```text
Br(S_Qbar)[ell]^{G_Q}=0 for every odd ell.
```

Since

```text
Br(S)/Br_1(S) -> Br(S_Qbar)^{G_Q}
```

is injective and Testa--Stoll Theorem 10 gives `Br_1(S)/Br(Q)=0`, every nonconstant Brauer class on the **proper** surface `S` is 2-primary.

## Firewall for U

This does not kill odd-primary classes on `U=S\D` that fail to extend across `D`.  Such classes are precisely why the boundary Gersten/residue receiver is retained.  The correct narrowed statement is:

```text
odd-primary proper-source Brauer = absent;
odd-primary physical-open Brauer, if any = boundary-residue source only.
```
