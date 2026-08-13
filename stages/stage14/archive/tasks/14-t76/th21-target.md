# Stage14-tH21 target emitted by t76

Requested object:

```text
SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
```

Audit only the post-t76 balanced deficient-modulus block. Do not reopen Pell/class-number/regulator, canonical largest-prime detection, t74 fixed `(ell,c)` fibers, t75 large-`g` or highly-unbalanced Type-I branches, or t76 large-clean-`K` root-line spacing.

Condition on the fixed packet

```text
(U,epsilon,k,h,kappa,beta)
```

and dyadic physical scales for canonical `ell` and cover coordinates

```text
A=b-a,
B=b+a,
r=q-p,
t=q+p.
```

Retain exactly

```text
K=odd(kappa),
K_bad=gcd(K,g),
K_clean=K/K_bad,
gcd(K_clean,A*B*r*t)=1,
K_clean < R*T*B^o(1),
t == rho*r (mod K_clean),
```

where the sign of `rho` is fixed primewise by `beta` and only the reciprocal direction choice remains, costing at most `2^omega(K_clean)=B^o(1)`.

Also retain all physical masks

```text
g small on its dyadic scale,
r,t balanced,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell^2>4B,
ell*c<2B,
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
c/odd(h)=R0*T0,
gcd(R0,T0)=1,
ell canonical Gaussian direction prime.
```

The audit question is whether an existing or naturally adaptable bilinear/Type-II dispersion theorem gives a uniform fixed `B`-power saving after summing over the moving canonical direction and balanced short primitive cover pairs with this projective root-line kernel.

In particular inspect, with exact quantifier/range matching rather than name-only citation:

1. DFI-style quadratic-root / prime-modulus dispersion;
2. Kuznetsov/Kloosterman bilinear forms after opening the root-line congruence;
3. spectral large sieve / exceptional Maass estimates;
4. divisor switching plus Cauchy/Poisson in one cover column;
5. bilinear forms with a moving Gaussian-prime direction coefficient;
6. whether the `K_clean`-deficient condition itself supplies enough modulus averaging;
7. whether canonical `ell` and `ell*g*c<2B` create a usable complementary modulus;
8. whether one can keep the fixed `(kappa,beta)` sign rule and both short-cover/hyperbola masks without paying back the desired saving.

Required verdict fields:

```text
STAGE14_TH21=COMPLETE_...
T76_LARGE_CLEAN_KAPPA_BRANCH_REOPENED=false
T75_HIGH_IMBALANCE_BRANCH_REOPENED=false
T75_LARGE_G_BRANCH_REOPENED=false
PROJECTIVE_ROOTLINE_KERNEL_RETAINED=...
CANONICAL_ELL_MASK_RETAINED=...
SHORT_ELLIPSE_MASK_RETAINED=...
SHARP_ELL_G_C_HYPERBOLA_RETAINED=...
OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=...
CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
TH22_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<read latest main>
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=...
NEXT=Stage14-t77
```

Create the dedicated Stage14-tH21 repository area, deterministic audit/frozen boundary where appropriate, dedicated CI, and PR. Do not claim a saving unless every physical mask above survives the theorem adapter.
