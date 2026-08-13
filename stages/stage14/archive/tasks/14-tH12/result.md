# Stage14-tH12 — generic LD2-transverse twisted-Kummer incidence / dispersion receiver

## Purpose

Stage14-tH11 PARKed the second `tH` support cycle and required a concrete merged live-`t` demand before reopening.  Merged Stage14-t43 supplies that trigger.

After reciprocal quotient, t43 found that all 16 frozen off-direction principal collision blocks are LD2-transverse, while the largest nonprincipal heavy kernels are not explained by the degree-1 / degree-2 isogeny exceptions.  Thus the remaining live object is genuinely the generic LD2-transverse twisted-Kummer incidence

\[
K^{(\tau)}_{\gamma,\gamma'}:
\qquad
Y^2=\tau f_\gamma(x)f_{\gamma'}(y).
\]

Stage14-tH12 does **not** assume any Stage14-t44 theorem.  It asks a narrower infrastructure question:

> after inserting the canonical Gaussian-prime and common-core arithmetic already present in the physical packet, under exactly which additional certificates can this two-dimensional incidence be reduced to a one-dimensional prime-character sum, a one-dimensional common-core character/lattice problem, or a divisor problem?

The output is a reusable receiver plus a list of quantifier traps and counterexamples.  It deliberately stops before claiming a new power saving.

---

## 1. Stable imported state

Only merged inputs are used:

- tH1: primary Gaussian-prime normalization when an oriented Gaussian prime is needed;
- tH9/tH10: squareclass autocorrelation and heavy/light energy receivers;
- t42: reciprocal quotient and common-core key;
- t43: LD2-transverse classification and the fact that generic twisted-Kummer incidence is the present obstruction.

No result from t44 or later is required.

For a reciprocal-quotiented physical state `s`, t42 uses

\[
k=\frac{n}{\delta},
\qquad
h=\frac{\varepsilon m}{k},
\]

and the common-core key

\[
\boxed{
C(s)=(\varepsilon,\delta,h,\mathrm{branch}).
}
\tag{12.1}
\]

The state also has a canonical rational split prime `ell(s)`; when the oriented Gaussian prime is needed, tH1 provides the primary/oriented normalization.

Let

\[
\sigma(s)=\operatorname{sqf}(|F_s|)
\]

be the squareclass kernel and write `xor` for squareclass multiplication modulo squares.

---

## 2. The exact generic LD2 incidence object

Let `LD2(s,t)` mean that the direction pair is classified by t43 as `ld2_transverse`: it is neither degree-1 same-`j` nor degree-2 isogenous.

For a twist `tau`, define the ordered generic incidence set

\[
\mathcal E^{\rm gen}_\tau
=
\{(s,t):
\operatorname{dir}(s)\ne\operatorname{dir}(t),
\ LD2(s,t),
\ \sigma(s)\oplus\sigma(t)=\tau\}.
\tag{12.2}
\]

Its size is

\[
c_{\rm gen}(\tau)=|\mathcal E^{\rm gen}_\tau|.
\]

This is a discrete physical-point incarnation of the twisted-Kummer condition.  Importantly, `LD2-transverse` is only a **low-degree** certificate.  It does not exclude higher-degree isogenies or every special degeneration.

### Exact Fubini partitions

Partition by the common core of the left state:

\[
c_C(\tau)
=
\#\{(s,t)\in\mathcal E^{\rm gen}_\tau:C(s)=C\}.
\]

Then exactly

\[
\boxed{
c_{\rm gen}(\tau)=\sum_C c_C(\tau).}
\tag{12.3}
\]

Likewise, partition by the canonical prime of the left state:

\[
c_\ell(\tau)
=
\#\{(s,t)\in\mathcal E^{\rm gen}_\tau:\ell(s)=\ell\},
\]

so

\[
\boxed{
c_{\rm gen}(\tau)=\sum_\ell c_\ell(\tau).}
\tag{12.4}
\]

There is also the exact joint grid

\[
c_{C,\ell}(\tau)
=
\#\{(s,t)\in\mathcal E^{\rm gen}_\tau:C(s)=C,\ \ell(s)=\ell\},
\]

with

\[
\boxed{
c_{\rm gen}(\tau)=\sum_{C,\ell}c_{C,\ell}(\tau).}
\tag{12.5}
\]

These identities are elementary, but they are the correct quantifier skeleton for every later one-dimensionalization theorem.

---

## 3. Receiver A — fixed common core, moving canonical Gaussian prime

The first desired road is to freeze common-core arithmetic and leave the canonical prime as the analytic variable.

A block is **prime-one-dimensional** only after *all other free variables have been absorbed into fixed data or into coefficients independent of the moving prime*.  Fixing `C(s)` alone does not automatically do this.

### Prime-character certificate

A block `B` may be exported as

```text
CanonicalPrimeCharacterBlock
  tau
  common_core C
  fixed direction / partner cell / dyadic state
  moving primary Gaussian prime varpi
  norm ell=N(varpi)
  coefficient a_B(varpi)
  quadratic conductor/discriminant D_B
  canonical selector weight omega_B(varpi)
  bad-prime set
```

only if the following are proved:

1. **dimension certificate** — after the declared freezes, the only arithmetic summation variable is `varpi`;
2. **phase independence** — `D_B` and every character parameter are independent of the moving `varpi`;
3. **nonprincipal certificate** — the resulting character is nonprincipal, unless the block is explicitly routed to the principal term;
4. **selector accounting** — the canonical-largest-prime / canonical-prime selector is either part of the analytic theorem's weight or has been removed by a proved decomposition;
5. **bad-prime accounting** — primes dividing discriminants, contents, resultants or denominators are removed/charged uniformly;
6. **coefficient separation** — all residual dependence sits in `a_B(varpi)` and does not secretly alter the character conductor.

Under those certificates, the block is reduced to the one-dimensional prime-supported sum

\[
\boxed{
S_B(D_B;L)
=
\sum_{\substack{\varpi\ {m primary}\N\varpi\asymp L}}
 a_B(\varpi)\,\omega_B(\varpi)\,\eta_{D_B}(\varpi),
}
\tag{12.6}
\]

where in the norm-induced case

\[
\eta_D(\varpi)=\chi_D(N\varpi).
\]

This is a genuine one-dimensional character/prime problem.

### What tH12 does **not** infer from (12.6)

Reduction to (12.6) is not itself a power saving.  Uniform cancellation over canonical primes, with conductor and selector ranges of Stage14 size, is a separate analytic theorem.

In particular, `D_B != 1` alone does **not** imply a usable prime-sum saving uniformly when `|D_B|` may be large relative to the prime interval.

The correct tH12 output is therefore

```text
PRIME_ROUTE_REDUCED_TO_1D=true       [only after the certificate]
PRIME_ROUTE_POWER_SAVING_PROVED=false
```

unless a later stage supplies the required prime-character theorem.

---

## 4. Receiver B — fixed canonical prime, moving common core

The second road freezes the canonical prime and attempts to make the common-core variable one-dimensional.

Because

\[
C=(\varepsilon,\delta,h,\mathrm{branch}),
\]

one must not say “the common core moves in one variable” until `epsilon`, `delta`, `branch` and every other residual physical parameter are frozen or parameterized with an accounted multiplicity.  Only then may `h` be treated as the remaining scalar variable.

Three distinct one-dimensional receivers are valid.

### B1. Polynomial-character receiver

Suppose a certified block reduces a local square test to

\[
\chi_q(P_B(h)),
\]

where

- `q` is fixed throughout the block;
- `P_B` is nonzero modulo `q`;
- the squarefree part of `P_B` has bounded degree;
- `P_B` is not a constant times a square modulo `q`.

Then the block is a standard one-variable finite-field/incomplete character-sum problem.  A later stage may insert the appropriate Weil/completion or square-sieve theorem.

But a single condition

\[
\chi_q(P_B(h))=+1
\]

is only a **necessary local filter** for a rational/integer square.  It is not equivalent to the global twisted-Kummer square condition.

Hence one auxiliary prime cannot be used to replace the global square condition exactly.

### B2. Lattice/root-congruence receiver

If the arithmetic gives the stronger condition

\[
P_B(h)\equiv0\pmod q
\tag{12.7}
\]

with a nonzero polynomial of degree `d`, then there are at most `d` residue classes modulo `q`.  For an interval of length `H`,

\[
\boxed{
N_B\le d\left(\frac Hq+1\right).
}
\tag{12.8}
\]

This is an elementary one-dimensional lattice incidence bound.

It is **not** valid if the condition is merely `chi_q(P_B(h))=+1`, where roughly half the residue classes may survive.

### B3. Divisor receiver

If the physical block proves

\[
h\mid M_B
\tag{12.9}
\]

for an integer `M_B` that is fixed inside the block and polynomially bounded in `B`, then

\[
\boxed{
\#\{h:h\mid M_B\}\le\tau(M_B)=B^{o(1)}.
}
\tag{12.10}
\]

This is the cleanest common-core one-dimensionalization.

The word **fixed** is essential.  A relation `h | M(h)` does not give a divisor bound by `tau(M)`; that is a quantifier mistake.

### Optional curve fallback

If freezing the canonical prime leaves an actual equation

\[
Y^2=P_B(h)
\]

with cubic/quartic squarefree `P_B`, the problem has become one-dimensional but is now a genus-one bounded-height problem rather than a lattice/divisor problem.  Such a route is allowed only with a uniform theorem whose dependence on the varying coefficients is explicitly controlled.

---

## 5. Receiver C — heavy/light kernel mass

Stage14-tH10 gives, for the reciprocal-quotiented population of size `H`,

\[
E_4
\le
A_1^2+T(H^2-A_1)+(R_{\rm non}-T)M_T,
\tag{12.11}
\]

where

\[
M_T=\sum_{\substack{\tau\ne1\\c(\tau)>T}}c(\tau).
\]

Stage14-t43 shows that low-degree exceptions do not explain the observed heavy tail, so tH12 provides a receiver for the **generic LD2 mass inside the heavy kernels**.

For a disjoint block partition `B`, define

\[
M^{\rm gen}_{T,B}
=
\#\{(s,t)\in B:
LD2(s,t),\ \tau(s,t)\in\mathcal H_T\}.
\]

Then exactly

\[
\boxed{
M_T^{\rm gen}=\sum_B M^{\rm gen}_{T,B}.
}
\tag{12.12}
\]

For each block, a later stage may supply any certified bound obtained from

- fixed-core / moving-prime route;
- fixed-prime / moving-core route;
- a direct incidence theorem.

If two valid bounds `U_B^(prime)` and `U_B^(core)` apply to the **same block**, one may use

\[
M^{\rm gen}_{T,B}
\le
\min(U_B^{\rm prime},U_B^{\rm core}).
\tag{12.13}
\]

and sum over disjoint blocks.

One may not take minima of incompatible partitions without first refining them to a common disjoint partition.

### Higher-degree isogenies

`LD2-transverse` does not mean “non-isogenous in every degree”.  Higher-degree isogenies may later be split out as exceptional heavy blocks.  tH12 therefore does not require their full classification in advance: the heavy/light receiver only needs their **aggregate mass** controlled if they become heavy.

---

## 6. The combined generic incidence receiver

A future live stage can hand tH12 records of the form

```text
LD2KummerIncidenceBlock
  tau
  reciprocal_quotiented: true
  ld2_transverse: true

  fixed_common_core:
    eps
    delta
    h            [fixed on prime route]
    branch

  canonical_prime:
    ell / oriented primary varpi

  residual_free_dimension
  disjoint_block_id

  prime_route_certificate:
    phase_independent_of_varpi
    nonprincipal
    selector_accounted
    bad_primes_accounted
    coefficient_separated
    one_dimensional_bound

  core_route_certificate:
    scalar_core_variable
    fixed_auxiliary_modulus
    nonsquare_polynomial
    root_congruence       [optional]
    fixed_dividend_M      [optional]
    one_dimensional_bound

  heavy_kernel:
    threshold T
    kernel_tau
    pair_mass_bound
```

The adapter accepts a route only when its certificate is complete.

For a common disjoint partition `mathcal B`,

\[
\boxed{
I^{\rm gen}
\le
\sum_{B\in\mathcal B}
\min\{U_B^{\rm certified}\},
}
\tag{12.14}
\]

where the minimum ranges only over certified bounds for that same block.

This is the reusable incidence/dispersion receiver requested by t44.

---

## 7. Quantifier mistakes explicitly forbidden

Stage14-tH12 freezes the following failure modes.

### Q1. Per-block subpolynomial is not global subpolynomial

If there are `B^alpha` blocks and each has `B^o(1)` points, the aggregate may still be `B^(alpha+o(1))`.

Therefore every block theorem must be accompanied by a block-count / coefficient-energy / aggregate summation ledger.

### Q2. One Legendre symbol does not detect a global square

A nonsquare integer can be a quadratic residue modulo a chosen prime.  Thus

```text
chi_q(N)=+1
```

is a local filter, not the statement “N is a square”.  Exact square detection needs the actual square equation or a multi-prime/square-sieve argument.

### Q3. Adaptive auxiliary moduli destroy the claimed cancellation

Choosing a different auxiliary prime `q=q(h)` or `q=q(varpi)` point-by-point does not create one fixed character sum.  Variation of the modulus must be dyadically/family averaged by an actual theorem.

### Q4. LD2-transverse does not imply every specialization is nondegenerate

It excludes degree-1 same-`j` and degree-2 isogeny only.  It does not prove:

- absence of higher-degree isogeny;
- nonvanishing of every resultant/discriminant;
- that a specialized polynomial is nonsquare modulo every auxiliary prime;
- that a moving-prime phase is nonprincipal.

Each of those needs its own certificate.

### Q5. Fixing the common core may still leave dimension two

If the partner state or another coordinate is still moving independently, the block is not a one-dimensional prime sum.  `residual_free_dimension=1` must be proved, not assumed.

### Q6. Fixing the canonical prime may not make the common core scalar

The common core is `(eps,delta,h,branch)`.  Treating it as just `h` is valid only after the other fields and residual state have been frozen/accounted.

### Q7. Root bounds cannot be applied to residue conditions

`P(h)=0 mod q` has at most `deg P` residue classes.  `chi_q(P(h))=+1` may have about `q/2` classes.

### Q8. Divisor bounds require a fixed dividend

`h | M_B` with fixed polynomial-size `M_B` gives `B^o(1)` choices.  `h | M(h)` does not.

### Q9. Canonical-prime selection can correlate with the character

A theorem for all split primes does not automatically apply to a physically selected canonical-largest-prime subsequence.  The selector must be part of the weight or removed by a valid decomposition.

### Q10. Heavy exceptional masses must be disjointified

Low-degree, higher-isogeny, bad-prime, common-core-degenerate and prime-degenerate labels may overlap.  Their masses cannot simply be added unless a disjoint partition or inclusion-exclusion bound is stated.

### Q11. Principal and nonprincipal kernels are different receivers

`tau=1` contributes to the principal `A1` problem.  The heavy/light nonprincipal term uses `tau!=1`; one must not feed principal collisions into `R_non` or `M_T`.

---

## 8. Counterexamples kept with the receiver

The deterministic audit contains small explicit models for the main logical failures:

1. **many-block countermodel** — every fixed-core block has one incidence while the number of cores grows; local `O(1)` does not imply global `O(1)`;
2. **local-square false positive** — `6` is not a square over the integers but is `1 mod 5`, hence passes the Legendre `+1` test modulo 5;
3. **square-polynomial degeneration** — `P(h)=h^2` gives no nontrivial quadratic-character cancellation and demonstrates why a nonsquare-polynomial certificate is needed;
4. **root/residue separation** — `P(h)=h mod q` has one zero residue but approximately half of nonzero residues have character `+1`;
5. **moving-dividend trap** — `h | h` holds for every `h` and gives no divisor sparsity.

These are logical stress tests, not models of the exact Stage14 geometry.

---

## 9. Frozen t43 regression

The audit reuses the merged t42/t43 deterministic population and checks:

```text
reciprocal quotient states                    560
A1                                             592
principal LD2-transverse blocks                16
ordered off-direction LD2 pair mass        308846
heavy threshold                                20
heavy kernels                                  72
heavy pair mass                              1834
max nonprincipal multiplicity                   40
```

It additionally verifies, for the actual frozen LD2 pair set, that the fixed-common-core, fixed-canonical-prime and joint `(core,ell)` partitions all reconstruct exactly the same generic pair mass, globally and twist-by-twist.

Those finite counts are diagnostics only.

---

## 10. What has and has not been achieved

### Proved / frozen as reusable infrastructure

- exact generic-LD2 incidence set and Fubini partitions;
- exact common-core key from t42;
- prime-route one-dimensionalization certificate;
- common-core character/lattice/divisor certificates;
- elementary lattice/root bound;
- heavy/light generic mass handoff compatible with tH10;
- common-partition rule for combining prime/core bounds;
- explicit quantifier and degeneration failure catalogue.

### Not proved

- a prime-character saving for the actual canonical-prime selector;
- a polynomial-character or divisor reduction for every actual t44 common-core block;
- a global generic Kummer incidence power saving;
- a subpolynomial bound for every nonprincipal twist multiplicity;
- a bound for all higher-degree isogeny exceptions;
- the critical square-root-strip saving;
- `A_{1,1}` power saving;
- `T=o(sqrt(B))`;
- perfect-cuboid nonexistence.

The point of tH12 is to tell live t44 exactly what extra statement must be proved before a two-dimensional Kummer incidence may legally be treated as one-dimensional.

---

## Boundary

```text
STAGE14_TH12=COMPLETE_LD2_KUMMER_CANONICAL_PRIME_COMMON_CORE_RECEIVER
TH_REOPEN_TRIGGER=T43_GENERIC_LD2_TWISTED_KUMMER_PRIMARY_OBSTRUCTION
TH_REQUIRES_T44_RESULT=false
GENERIC_LD2_INCIDENCE_FUBINI_PARTITIONS_PROVED=true
FIXED_CORE_MOVING_CANONICAL_PRIME_RECEIVER_DEFINED=true
FIXED_PRIME_MOVING_COMMON_CORE_RECEIVER_DEFINED=true
ONE_DIMENSIONAL_PRIME_CHARACTER_CERTIFICATE_DEFINED=true
ONE_DIMENSIONAL_COMMON_CORE_CHARACTER_CERTIFICATE_DEFINED=true
ONE_DIMENSIONAL_LATTICE_ROOT_RECEIVER_PROVED=true
ONE_DIMENSIONAL_DIVISOR_RECEIVER_DEFINED=true
HEAVY_LIGHT_GENERIC_KERNEL_MASS_RECEIVER_DEFINED=true
COMMON_REFINEMENT_REQUIRED_TO_COMBINE_ROUTE_BOUNDS=true
SINGLE_LEGENDRE_SYMBOL_IS_GLOBAL_SQUARE_DETECTOR=false
LD2_TRANSVERSE_IMPLIES_ALL_DEGREE_NONISOGENOUS=false
CANONICAL_PRIME_SELECTOR_CANCELLATION_PROVED=false
GENERIC_KUMMER_INCIDENCE_POWER_SAVING_PROVED=false
NONPRINCIPAL_TWIST_MULTIPLICITY_SUBPOLY_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH13 only if live t exposes a concrete certified prime/core specialization needing a sharper adapter; otherwise hand tH12 receiver to t44 and PARK
```
