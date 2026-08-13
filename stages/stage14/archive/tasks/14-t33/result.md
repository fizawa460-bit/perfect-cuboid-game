# Stage14-t33 — quadratic Hecke value transfer and Mellin spectral boundary

## Purpose

Stage14-t32 closed the **complete angular correlation** on split auxiliary norm circles and unified the super-square-root visible and invisible states on the Gaussian norm skeleton

\[
N(U)=m,\qquad N(V)=k\delta,\qquad k\mid\varepsilon m,
\qquad \frac{\varepsilon\ell m\delta}{2}\le B.
\]

The remaining task was to transfer the split-torus auxiliary character to a large-sieve framework over \(\mathbf Q(i)\).

Stage14-t33 performs that transfer audit exactly. The result is mixed:

1. at the **value level**, the auxiliary Legendre symbol is exactly a quadratic residue/Hecke symbol over a Gaussian prime ideal;
2. at the **norm-variable level**, the torus trace is not itself a quadratic Hecke character;
3. multiplicative completion of a sparse integral norm circle requires a full Mellin spectrum containing characters of orders larger than two;
4. consequently the Goldmakher--Louvel quadratic Hecke-family large sieve is relevant but is **not by itself sufficient** for the Stage14 norm-index sum;
5. the correct next object is an all-character Mellin/Hecke large sieve, still coupled to
   \(k\mid\varepsilon m\) and \(m\delta\ll B/\ell\).

No global power saving is claimed in t33.

## 1. Value-level quadratic Hecke symbol is exact

Let \(\lambda\equiv1\pmod4\) be a split auxiliary prime and choose

\[
\iota^2\equiv-1\pmod\lambda.
\]

The Gaussian prime ideal

\[
\mathfrak l=(\lambda,i-\iota)
\]

has residue field

\[
\mathbf Z[i]/\mathfrak l\cong\mathbf F_\lambda.
\]

For a rational integer \(F\) coprime to \(\lambda\), its quadratic residue symbol modulo \(\mathfrak l\) is therefore exactly the ordinary Legendre symbol:

\[
\boxed{
\left(\frac{F}{\mathfrak l}\right)_2
=\chi_\lambda(F).
}
\tag{33.1}
\]

Thus the t30--t32 square detector does possess a genuine quadratic-Hecke interpretation **as a value**.

This is the point at which Goldmakher--Louvel becomes structurally relevant. Their Theorem 1.1 gives the number-field analogue of Heath-Brown's quadratic large sieve for a quadratic Hecke family. In particular, for squarefree ideal variables it has the expected \((M+N)(MN)^\varepsilon\) strength.

Reference: L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642, Theorem 1.1.

## 2. The torus trace is not a Hecke character in the norm variable

From t32, after parameterising a split norm circle by

\[
s=x+\iota y,\qquad x-\iota y=R/s,
\]

a one-variable factor of the Stage14 character has the form

\[
A_\lambda(s)
=\chi_\lambda(\alpha s^4-\beta),
\qquad \alpha\beta\ne0,
\tag{33.2}
\]

up to multiplication by a fixed nonzero square.

This is a trace function on the multiplicative torus, but in general it is **not multiplicative**:

\[
A_\lambda(s_1s_2)
\ne A_\lambda(s_1)A_\lambda(s_2).
\]

The frozen audit already supplies a nonzero example in the valid model

\[
A_{13}(s)=\chi_{13}(s^4-4):
\]

\[
A_{13}(2)=1,
\qquad A_{13}(4)=-1,
\]

so

\[
A_{13}(2^2)\ne A_{13}(2)^2.
\]

Therefore (33.1) cannot be reinterpreted as saying that \(U\mapsto A(U)\) or \(V\mapsto A(V)\) is a single quadratic Hecke character.

## 3. Exact multiplicative Mellin decomposition

Let \(\widehat{\mathbf F_\lambda^*}\) be the multiplicative character group. Every torus trace has the exact expansion

\[
\boxed{
A_\lambda(s)
=\frac1{\lambda-1}
\sum_{\psi}
\widehat A_\lambda(\psi)\psi(s),
}
\tag{33.3}
\]

where

\[
\widehat A_\lambda(\psi)
=\sum_{s\in\mathbf F_\lambda^*}
A_\lambda(s)\overline{\psi(s)}.
\]

Since (33.2) depends on \(s^4\),

\[
A_\lambda(\zeta s)=A_\lambda(s)
\qquad(\zeta^4=1).
\]

Hence

\[
\boxed{
\widehat A_\lambda(\psi)=0
\quad\text{unless}\quad
\psi|_{\mu_4}=1.
}
\tag{33.4}
\]

This is a genuine spectral compression, but it is not a quadratic compression.

For the two-torus Stage14 factor

\[
A(s/t)B(st),
\]

substituting (33.3) gives the exact identity

\[
\boxed{
A(s/t)B(st)
=\frac1{(\lambda-1)^2}
\sum_{\psi,\phi}
\widehat A(\psi)\widehat B(\phi)
(\psi\phi)(s)
(\phi\psi^{-1})(t).
}
\tag{33.5}
\]

Thus sparse integral norm circles naturally lead to multiplicative residue characters of \(U\) and \(V\), but their orders are the orders of the Mellin modes \(\psi\) and \(\phi\), not merely two.

## 4. Higher-order modes are unavoidable

The deterministic audit uses the valid square-ratio model

\[
A_\lambda(s)=\chi_\lambda(s^4-4).
\]

For each sampled split prime it computes the full multiplicative discrete Fourier spectrum. Every nonzero Fourier exponent is divisible by four, exactly as predicted by (33.4), but higher-order characters occur in every case:

```text
lambda    largest character order occurring
  13                    3
  17                    4
  29                    7
  37                    9
  41                   10
```

More precisely:

```text
lambda=13: exponents 0,4,8
lambda=17: exponents 0,4,8,12
lambda=29: exponents 0,4,8,12,16,20,24
lambda=37: exponents 0,4,8,12,16,20,24,28,32
lambda=41: exponents 0,4,8,12,16,20,24,28,32,36
```

Thus the sparse norm-circle completion is not contained in the quadratic character subspace.

This also blocks a shortcut through the higher-order corollary of Goldmakher--Louvel: their fixed-order construction assumes the base field contains the required roots of unity. The Gaussian field contains only roots of unity of order dividing four, whereas the Stage14 Mellin spectrum already requires orders 7, 9 and 10 in the frozen sample.

## 5. Why squarefree-kernel aggregation is circular

There is another tempting transfer. Since

\[
\chi_\lambda(F)
\]

depends only on the squarefree ideal kernel of \((F)\), one could aggregate Stage14 points by that kernel and then apply a quadratic Hecke-family large sieve.

Let

\[
a_{\mathfrak b}
=\#\{(U,V):\operatorname{sqfree}((F(U,V)))=\mathfrak b\}.
\]

For an actual square value,

\[
\operatorname{sqfree}((F))=\mathcal O,
\]

so

\[
\boxed{a_{\mathcal O}=N_{\rm square}.}
\]

The large-sieve coefficient energy contains

\[
\sum_{\mathfrak b}|a_{\mathfrak b}|^2
\ge a_{\mathcal O}^2
=N_{\rm square}^2.
\]

Hence this aggregation places the quantity to be bounded directly on the right-hand side. Without an independent collision-energy theorem it is circular and cannot close the square detector.

Therefore

\[
\boxed{
\text{quadratic value-symbol transfer is exact, but quadratic kernel aggregation is not a square-sieve closure.}
}
\]

## 6. Correct all-character Hecke/Mellin object

For a split prime ideal \(\mathfrak l\mid\lambda\), each multiplicative residue character in (33.5) can be viewed, after the finite unit/primary normalisation in \(\mathbf Z[i]\), as a ray-class/Hecke character modulo \(\mathfrak l\).

The correct spectral object is therefore schematically

\[
\mathfrak S_L
=
\sum_{\substack{\lambda\sim L\\\lambda\equiv1\ (4)}}
\sum_{\substack{\psi,\phi\\
\psi|_{\mu_4}=\phi|_{\mu_4}=1}}
\frac{\widehat A_\lambda(\psi)\widehat B_\lambda(\phi)}
{(\lambda-1)^2}
\,\mathcal H_{\lambda}(\psi,\phi),
\tag{33.6}
\]

where

\[
\mathcal H_{\lambda}(\psi,\phi)
=
\sum_{m,\delta}
\sum_{k\mid\varepsilon m}
\sum_{\substack{N(U)=m\\N(V)=k\delta}}
(\psi\phi)(U\bmod\mathfrak l)
(\phi\psi^{-1})(V\bmod\mathfrak l)
\]

with the exact physical restrictions

\[
m\delta\ll B/\ell,
\]

the canonical-largest-prime condition, physical interval/reconstruction conditions, and the finite visible/invisible local-state labels retained.

Equation (33.6) is the proper large-sieve transfer object. It requires an **all-character** Gaussian/ray-class large sieve or an equivalent residue-class large sieve, not only a quadratic Hecke family.

Classical algebraic-number-field large-sieve machinery is therefore closer to the corrected target than the quadratic-only theorem, but t33 does not yet prove the necessary sparse split-prime, divisor-coupled hyperbolic estimate.

Reference for the general algebraic-number-field large-sieve setting: M. N. Huxley, *The large sieve inequality for algebraic number fields*, Mathematika 15 (1968), 178--187.

## 7. What remains after t33

The t32 angular theorem remains fully valid:

\[
|C_\lambda(m,n)|\ll\lambda,
\qquad
|C_{\lambda\mu}(m,n)|\ll\lambda\mu.
\]

Stage14-t33 does not retract that saving. It explains why transferring the saving from complete finite-field circles to the sparse integral norm-index family cannot be done by a quadratic Hecke large sieve alone.

The remaining global problem is now:

1. exploit the \(\mu_4\)-restricted all-character spectrum;
2. average the corresponding Gaussian residue characters over split auxiliary primes;
3. preserve
   \[
   k\mid\varepsilon m,
   \qquad m\delta\ll B/\ell;
   \]
4. keep the canonical-largest-prime and local visible/invisible labels;
5. obtain a norm-index correlation saving strong enough to survive projection to active directions.

## 8. Frozen diagnostics

The t33 audit locks the t32 unified total

```text
visible super-sqrt non-torsion       1018
invisible super-sqrt non-torsion    12190
unified cofactor checks             13208
```

and performs the new spectral checks:

```text
split primes spectrally audited                         5
value-level Gaussian residue-map checks              605
primes with higher-order Mellin modes                   5
cases where quadratic/trivial modes alone suffice       0
```

The multiplicativity counterexample is frozen at

```text
lambda=13, A(s)=chi_13(s^4-4)
A(2)=1, A(4)=-1
```

so `A(2*2) != A(2)A(2)`.

These finite computations certify the transfer boundary; they are not asymptotic density claims.

## Boundary

```text
STAGE14_T33=COMPLETE_QUADRATIC_HECKE_VALUE_TRANSFER_AND_MELLIN_SPECTRAL_BOUNDARY
QUADRATIC_HECKE_VALUE_SYMBOL_IDENTIFIED=true
TORUS_TRACE_IS_QUADRATIC_HECKE_CHARACTER_IN_NORM_VARIABLE=false
MU4_MELLIN_SUPPORT_RESTRICTION=true
HIGHER_ORDER_MELLIN_MODES_REQUIRED=true
GOLDMAKHER_LOUVEL_QUADRATIC_LARGE_SIEVE_DIRECTLY_SUFFICIENT=false
SQUAREFREE_KERNEL_AGGREGATION_CLOSES_SQUARE_DETECTOR=false
ALL_CHARACTER_MELLIN_HECKE_SIEVE_OBJECT_DEFINED=true
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t34 build the all-character Mellin/Hecke large-sieve inequality over split Gaussian primes, using mu_4-invariant spectral support and the exact k|epsilon*m, m*delta<<B/ell hyperbola
```
