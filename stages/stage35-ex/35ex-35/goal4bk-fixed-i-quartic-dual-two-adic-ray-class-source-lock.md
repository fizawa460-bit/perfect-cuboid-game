# Stage35-EX Goal4BK source lock — fixed-unit quartic dual and the surviving 2-adic ray-class compensator

Scope: continue Goal4BJ after exact-head verification. Audited authority remains V74 / Goal4AK. Goal4BJ constructs the support-cleaned global Gaussian orientation carrier

```text
Xi = Xi_a*Xi_b*Xi_c in Q(i)^*,
```

whose selected-reservoir valuations are `+1,-1,0` according as the Goal4BH status is `sigma=-1`, `sigma=+1`, or nonsecondary. Goal4BK asks whether a single order-four dual character is available and whether quartic reciprocity forces a nontrivial global relation.

The answer is mixed and sharper than the Goal4BJ boundary: an ambient canonical order-four character **does** exist, namely the quartic supplementary character with numerator `i`. It detects the sign of some reservoir valuations. But its global value is not source-fixed: the odd-prime product is exactly compensated by a deeper 2-adic/ray-class value of `Xi`, and the retained source only fixes primary normalization, not the deeper residue needed to make that compensator constant. Natural source cofactor characters have the same problem in a more explicit local form.

## 1. Goal4BJ carrier

Write

```text
Xi = N/D,
N = M_a^-*M_b^-*M_c^-,
D = M_a^+*M_b^+*M_c^+.                              (BK-Xi)
```

All `M_i^+` and `M_i^-` are pairwise-coprime products of source-selected primary Gaussian primes. Hence `N` and `D` are odd primary Gaussian integers, coprime to one another, and all finite divisor support of `Xi` is selected reservoir support.

At a selected primary prime `pi=pi_{i,ell}`,

```text
v_pi(Xi)=+1  for sigma_i(ell)=-1,
v_pi(Xi)=-1  for sigma_i(ell)=+1,
v_pi(Xi)=0   when the secondary orientation is absent.     (BK-val)
```

## 2. The canonical fixed-unit quartic character

For an odd primary Gaussian integer `alpha`, define the standard quartic supplementary character

```text
chi_i(alpha) = (i/alpha)_4.                           (BK-chi)
```

It is multiplicative in the primary denominator, so for `(BK-Xi)` define

```text
chi_i(Xi)=chi_i(N)*chi_i(D)^(-1).                    (BK-chi-Xi)
```

At a selected prime `pi`, the local contribution is exactly

```text
chi_i(pi)^(v_pi(Xi)).                                 (BK-local-dual)
```

Thus inversion of the orientation exponent sends a local value to its inverse. Whenever `chi_i(pi)` has order four, this distinguishes `+1` from `-1` and therefore sees the Goal4BH orientation bit.

This is a genuine order-four dual of the Goal4BJ quartic class. The previous statement "dual character missing" is therefore refined: no **source-fixed-valued** dual had been constructed, but the ambient Gaussian field already supplies a canonical fixed-unit quartic character.

## 3. Standard supplementary law and the free primary residue

For a primary Gaussian integer

```text
alpha=A+B*i,
```

the standard supplementary law is

```text
(i/alpha)_4 = i^((1-A)/2).                            (BK-supp-i)
```

A convenient reference is the standard quartic reciprocity treatment reproduced in Mollin's reciprocity chapter, Lemma 6.5; the same formula appears in modern higher-reciprocity notes.

Primary normalization requires

```text
A odd,
B even,
A+B == 1 mod 4,                                      (BK-primary)
```

but does **not** fix `A mod 8`. Therefore `(BK-supp-i)` is not constant on the primary ray class used in Goal4BF–Goal4BJ.

Three explicit primary Gaussian primes already show the variation:

```text
pi_5  = -1+2*i,   N=5,   chi_i(pi_5)= i,
pi_13 =  3+2*i,   N=13,  chi_i(pi_13)=-i,
pi_17 =  1+4*i,   N=17,  chi_i(pi_17)= 1.             (BK-primary-examples)
```

Each satisfies `(BK-primary)`. These are ambient diagnostics, not claims that all three occur as physical endpoint reservoirs. Their role is precise: the primary condition and the already-proved restriction `ell=1 mod4` do not themselves force a constant value of `chi_i`.

## 4. Why the global quartic product is not yet an obstruction

The odd selected-reservoir contribution of the fixed-unit character is

```text
product_{pi | Xi} chi_i(pi)^(v_pi(Xi)) = chi_i(Xi).  (BK-odd-product)
```

A global quartic Hilbert/reciprocity formulation with second entry `i` includes the ramified place above `2`. The supplementary law `(BK-supp-i)` is exactly the finite odd-prime expression of that 2-adic/ray-class correction.

Goal4BJ proves only the primary congruence

```text
Xi == 1 mod (1+i)^3.                                 (BK-primary-Xi)
```

But `(BK-primary-examples)` shows that primary congruence alone does not make `(BK-odd-product)` constant. Equivalently, the deeper 2-adic residue controlling the fixed-unit quartic character is still free in the retained source package.

Therefore global quartic reciprocity with the canonical dual `i` gives an identity with a **variable 2-adic compensator**, not a contradiction and not a universal sigma cycle.

The complex archimedean place of `Q(i)` contributes no independent real sign capable of closing this gap.

## 5. Natural source cofactor duals expose the same missing datum

Goal4BG/BH also provide natural local complementary Gaussian units. In direction `a`, the BF-selected prime always divides

```text
bar(Phi_BC)=x*b-i*y*c,
```

so the nonvanishing primitive-face cofactor is

```text
C_a^F=Phi_BC=x*b+i*y*c == 2*x*b mod p_a.             (BK-face-cofactor)
```

In a secondary case, the nonvanishing reduced-space cofactor depends on the orientation:

```text
C_a^S=bar(Omega_a)  if sigma_a=-1,
C_a^S=Omega_a       if sigma_a=+1.                   (BK-space-cofactor)
```

Using `lambda_a=sigma_a*iota_a`, the exact residue ratio is

```text
C_a^S/C_a^F == sigma_a * x*(a/ell^m)/c mod p_a.      (BK-ratio-a)
```

Cyclically,

```text
C_b^S/C_b^F == sigma_b * x*(b/ell^m)/c mod p_b,
C_c^S/C_c^F == sigma_c * y*(c/ell^m)/b mod p_c.      (BK-ratio-cyclic)
```

The normalized factors `a/ell^m`, `b/ell^m`, `c/ell^m` depend on the local reservoir prime and valuation. They are not residues of one fixed global source element. Moreover the choice of the nonvanishing space cofactor itself depends on `sigma_i`, so using it as a putative dual character is circular unless a separate global selector is supplied.

Thus the complementary face/space cofactors do not currently produce a fixed source-derived order-four functional with constant local values.

## 6. Hensel leading units are local, not a global second slot

Goal4BH defines primewise Hensel leading units such as

```text
q_a=(x*b-I_a*y*c)/ell^(2*rho).                       (BK-q)
```

These determine the first nonzero local coefficient of the face cancellation, but both `I_a` and the normalization power depend on the selected prime. The retained source has no single global Gaussian integer whose localization is every `q_i` simultaneously.

Therefore the `q_i` do not yet furnish a global quartic second slot either.

## 7. Exact boundary after Goal4BK

Goal4BK obtains a genuine improvement over Goal4BJ:

```text
ambient canonical order-four dual exists = yes;
fixed-unit character chi_i sees some orientation signs = yes;
source fixes chi_i(Xi) to a constant = no;
primary normalization alone kills 2-adic compensator = no;
natural cofactor dual becomes one fixed global unit = no;
Hensel leading units globalize to one second slot = no.
```

Hence the reciprocity route is **not** fail-closed yet. It has been reduced to a concrete next question: can the primitive six-variable parity/source equations determine the deeper 2-adic ray class of the support-cleaned carrier `Xi`, or at least determine the fixed-unit character `chi_i(Xi)`?

## 8. Verdict

Certified provisionally:

```text
CANONICAL_FIXED_I_QUARTIC_DUAL=true;
CHI_I_LOCAL_ORIENTATION_SENSITIVITY=true;
CHI_I_XI_SOURCE_CONSTANT=false;
PRIMARY_CONGRUENCE_SUFFICIENT_FOR_CONSTANT=false;
TWO_ADIC_RAY_CLASS_COMPENSATOR_REMAINS=true;
NATURAL_COFACTOR_FIXED_DUAL_OBTAINED=false;
HENSEL_GLOBAL_SECOND_SLOT_OBTAINED=false;
GLOBAL_QUARTIC_RECIPROCITY_CONTRADICTION=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
universal sigma product;
fixed chi_i(Xi);
quartic obstruction;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Next unit:

```text
35EX-35_GOAL4BL_XI_TWO_ADIC_RAY_CLASS_PARITY_PREFLIGHT
```

Question: compute the source-canonical `2`-adic/ray-class residue of `M_i^-/M_i^+` and `Xi` beyond primary normalization, using the three primitive parity branches and the face/space square-root units. Test whether `chi_i(Xi)` is forced; only then can the fixed-unit quartic reciprocity identity become a nontrivial global sigma relation.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
