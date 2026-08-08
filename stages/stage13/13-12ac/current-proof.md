# Stage13-12ac — R02 current proof synthesis

> **ROLE:** authoritative Stage13 R02 review entrypoint
>
> **STATUS:** `CANDIDATE_PENDING_EXTERNAL_R02`
>
> **PRIOR_REVIEW:** R01 returned `OPEN`
>
> **STAGE12_BOUNDARY:** frozen R09 theorem treated as declared prior input

This document is the current proof map for the repaired Stage13 theorem. It does
not ask the reviewer to trust any previous `PASS`, `COMPLETE`, `CLOSED`, hash,
manifest or CI status. Those items are provenance/reproducibility metadata only.
The mathematical argument must be checked from the embedded sources.

The historical exposition in `stages/stage13/main.md` remains useful background,
but its old Stage13-7jb and Stage13-7jf proof steps are superseded by
Stage13-12aa and Stage13-12ab respectively.

---

## 1. Counting target and exact identities

Stage13 counts primitive canonical integer-space-diagonal cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with exactly one integral face diagonal.

Let `A_ab,A_ac,A_bc` denote raw incidences in which the distinguished face is
integral, with the other faces unrestricted. Let

\[
O_{ab,ac},\quad O_{ab,bc},\quad O_{ac,bc}
\]

be pair overlaps and let `T` be the triple overlap. Then exactly

\[
N_{ab}=A_{ab}-O_{ab,ac}-O_{ab,bc}+T,
\]

\[
N_{ac}=A_{ac}-O_{ab,ac}-O_{ac,bc}+T,
\]

\[
N_{bc}=A_{bc}-O_{ab,bc}-O_{ac,bc}+T.
\]

The Stage13-3d projection identity remains active:

\[
C_{\rm prim,q}^{\rm proj}(B)=2A_q(B),
\]

and summing over directions gives

\[
C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).
\]

The factor `2` is the universal swap of the two ordered legs of the selected
integral face; no direction-dependent representation-fiber multiplier remains
once a canonical incidence is fixed.

---

## 2. Declared Stage12 prior input

The Stage12 proof is outside R02. The only theorem-level prior input used in the
Stage13 main-term calibration is the frozen Stage12 R09 primitive oriented
asymptotic

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

Hence the exact factor-2 bridge implies only the total raw statement

\[
A_{ab}(B)+A_{ac}(B)+A_{bc}(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
\]

This total theorem does **not** by itself determine the three directional
constants. R01 correctly identified that the old 7jb presentation effectively
used the desired directional proportions too early. R02 therefore forbids that
route.

---

## 3. Canonical chamber geometry

On the ordered spherical chamber

\[
\mathcal R=\{0<x<y<z,\ x^2+y^2+z^2=1\},
\]

the distinguished-face Gelfand--Leray weights are

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}.
\]

Define

\[
I_q=\int_{\mathcal R}w_q\,d\sigma.
\]

The independently audited values are

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8
```

and pointwise on the chamber

\[
w_{ab}>w_{ac}>w_{bc}.
\]

The Stage13-7j outer-angle kernels `k_q` satisfy

\[
J_q:=\int k_q(t(\phi))\,d\phi=\frac{2I_q}{\pi},
\qquad
J_{ab}+J_{ac}+J_{bc}=\frac\pi4.
\]

These geometric identities are logically prior to the repaired arithmetic
common-factor argument.

---

## 4. R01 FATAL finding and the 13-12aa repair

### 4.1 What was wrong

The old Stage13-7jb validator formed

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

from the Stage12 total and chamber proportions and then checked that `D_q/K_q`
was common across directions. Since Stage13-7j already had `K_q` proportional
to `I_q`, equality of those ratios was algebraic and was not an independent
proof of direction-neutral arithmetic amplification.

R02 accepts that criticism. The old 7jb constant check is provenance only.

### 4.2 Exact raw `j=0` local coefficient

Stage13-12aa returns to the Stage12/Stage13 outer coordinates

\[
p=hrs,\qquad
z=\frac{h(s^2-r^2)}2,\qquad
d=\frac{h(r^2+s^2)}2,
\qquad (r,s)=1.
\]

At a split prime `q=1 mod 4`, put

\[
a=v_q(h),\qquad b=v_q(rs),\qquad e=a+b.
\]

Because `(r,s)=1`, positive base valuation occurs in at most one of `r,s`.
The raw primitive zero-mode local coefficient is

\[
Z_0(a,b)=
\begin{cases}
2b+1,&a=0,\\
2,&a\ge1.
\end{cases}
\]

For a nonzero Gaussian angular phase `theta`, with

\[
H_e(\theta)=1+2\sum_{m=1}^e\cos(m\theta),
\]

the primitive harmonic coefficient is

\[
Z_\ell(a,b;\theta)=
\begin{cases}
H_b(\theta),&a=0,\\
2\cos((a+b)\theta),&a\ge1.
\end{cases}
\]

These are direct primitive differences

\[
G_{a+b}-1_{a\ge1}G_{a+b-1},
\qquad
H_{a+b}-1_{a\ge1}H_{a+b-1}.
\]

No categorywise asymptotic constant or value of `kappa` enters here.

### 4.3 Pure factors and mixed correction

For a split prime, the zero-mode pure factors are

\[
A_0(x)=\frac{1+x}{1-x},
\qquad
B_0(y)=\frac{1+y}{(1-y)^2},
\]

while nonzero harmonics have

\[
A_\ell(x)=\frac{1-x^2}{1-2\cos\theta\,x+x^2},
\qquad
B_\ell(y)=\frac{1+y}{1-2\cos\theta\,y+y^2}.
\]

After standard split/inert/2-adic factors are collected, the singular pieces
have the schematic form

\[
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s),
\]

\[
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s),
\]

whereas for every nonzero Gaussian harmonic

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s),
\]

\[
B_\ell(s)=\zeta(s)L(s,\xi_{8\ell})E_{b,\ell}(s).
\]

Thus the zero mode has the extra scale-variable zeta pole that is absent in
nonzero harmonics.

The full split-prime three-variable series `D_ell(x,y,z)` is divided by the
three pure factors to define a mixed correction

\[
C_\ell(x,y,z)=\frac{D_\ell(x,y,z)}
{A_\ell(x)B_\ell(y)B_\ell(z)}.
\]

The exact axis identities imply every nonconstant monomial of `C_ell-1`
contains at least two positive coordinate exponents. In the same weighted
Dirichlet/Wiener algebra used in Stage13-7h this yields, for fixed
`delta>0`,

\[
\|C_{\ell,q}-1\|_\delta\ll_\delta q^{-1-2\delta},
\]

uniformly in the retained polylogarithmic harmonic range. Hence the global
mixed correction converges absolutely in the required half-plane.

The R02 reviewer should independently verify that this weighted-`l1` step and
its claimed uniformity are sufficient for the subsequent curved-region
transfer.

### 4.4 Common factor before calibration

Using the `j=0` factorization, the zero angular mode has one common arithmetic
multiplier; the canonical category enters through the real kernel `J_q` only.
The repaired theorem shape is therefore obtained **before** Stage12 calibration:

\[
\boxed{
A_q(B)\sim \Theta J_q B(\log B)^3
}
\]

with one unknown `Theta>0` for all three directions.

Selberg--Vaaler bracketing with polylogarithmic degree and the same
polylog-uniform Gaussian-Hecke input used in the earlier Stage13 harmonic
analysis give lower order for the retained nonzero harmonics because their
scale factor has no zeta pole. The bracketing and small-height boundary terms
are also required to be `o(B(log B)^3)`.

Only after commonness is established do we use

\[
\sum_qA_q(B)\sim\frac{\kappa}{24\pi}B(\log B)^3
\]

and

\[
\sum_qJ_q=\frac\pi4.
\]

Therefore

\[
\Theta=\frac{\kappa}{6\pi^2},
\]

and since `J_q=2I_q/pi`,

\[
\boxed{
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

This is the repaired raw directional theorem.

---

## 5. R01 MAJOR finding and the 13-12ab repair

### 5.1 What was missing

The old Stage13-7jf computed finite-field local acceptance factors for a
second-face necessary condition, but it moved too quickly from that local
calculation to the assertion that a fixed finite set of congruence conditions
multiplies the global Stage13 main constant by the corresponding factors.
R02 does not accept “same machinery” as a proof of that transfer.

### 5.2 Fixed-local-factor lemma

Work inside the explicit Stage13-12aa Fourier-channel Euler product. For one
fixed prime `p`, refine the local state by the finite unit residue data needed
to evaluate the second-face quadratic-residue condition `W_p`. The constrained
local factor is `L^W_{p,ell}` and the unconstrained factor is `L_{p,ell}`.

For a fixed finite set `S`, multiplicativity gives

\[
\boxed{
\mathcal D_{\ell,S}
=\mathcal D_\ell
\prod_{p\in S}
\frac{L^W_{p,\ell}}{L_{p,\ell}}.
}
\]

Because `S` is fixed while `B->infinity`, this is a finite replacement of
Euler factors, not a growing-modulus theorem. The replacement does not alter
the zeta pole orders, the archimedean category kernel, or the previously used
polylog-uniform nonzero-harmonic cancellation. At zero mode it multiplies the
main constant by the finite product of local acceptance factors

\[
\lambda_p=L^W_{p,0}(1,1,1)/L_{p,0}(1,1,1).
\]

The R02 reviewer should verify that the refined local state genuinely captures
the imposed condition in every local valuation stratum and that the fixed
factor replacement preserves all analytic hypotheses used in 13-12aa.

### 5.3 Inert-prime acceptance

For an inert prime `p=3 mod 4`, on the unit-hypotenuse stratum the necessary
condition has exact acceptance

\[
\lambda_p^\times
=\frac{p+1}{2(p-1)}
=\frac12+\frac1{p-1}.
\]

The positive-valuation part of the normalized local Euler factor is
`O(1/p)` with an absolute constant. Thus

\[
\lambda_p\le\frac12+O(1/p).
\]

Consequently there exists `p0` such that every inert prime `p>p0` satisfies

\[
\lambda_p\le\frac34.
\]

### 5.4 Fixed-k squeeze and order of limits

Choose any fixed `k` sufficiently large inert primes satisfying the previous
bound and call the set `S_k`. Every pair-overlap object satisfies the necessary
second-face condition at all primes in `S_k`, so for an appropriate tagged raw
population

\[
O_{qr}(B)\le \text{constrained tagged raw count}.
\]

The fixed-local theorem gives, with `S_k` held fixed as `B->infinity`,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le C_q\prod_{p\in S_k}\lambda_p
\le C_q\left(\frac34\right)^k
\]

for a finite direction-dependent raw constant `C_q` (a harmless universal
tagging multiplicity may be absorbed into it).

Now, and only now, let `k->infinity`. Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

No uniform asymptotic for a modulus growing with `B` is used. Since the triple
overlap is a subset of every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

---

## 6. Exactly-one transfer

Insert the lower-order pair/triple estimates into the exact
inclusion-exclusion identities. For every direction

\[
N_q(B)=A_q(B)+o(B(\log B)^3),
\]

so the repaired raw theorem implies the repaired exactly-one theorem

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

Summing and using `sum I_q=pi^2/8` gives

\[
\boxed{
N_1(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

After normalization,

\[
\frac{(N_{ab},N_{ac},N_{bc})}{N_1}
\longrightarrow
\left(
\frac{8I_{ab}}{\pi^2},
\frac{8I_{ac}}{\pi^2},
\frac{8I_{bc}}{\pi^2}
\right),
\]

numerically

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

or normalized by `bc`,

```text
2.431684750178191 : 1.115756428951881 : 1.
```

---

## 7. Finite near-2:1:1 interpretation

At `B=100000` the exactly-one count is

```text
(84146, 43180, 40704)
```

with ratio approximately

```text
2.0673 : 1.0608 : 1.
```

The Stage13 finite diagnostics attribute much of the flattening relative to the
asymptotic chamber vector to supported-shell richness, with additional
parity/pure-`G`/primitive-support cancellations. This is a finite structural
interpretation, not an effective convergence theorem. R02 claims neither a
monotone approach nor a numerical threshold at which the asymptotic ratio must
be visible.

---

## 8. Required R02 audit targets

The reviewer is specifically asked to challenge, rather than assume, all of the
following.

1. Exact canonical definitions, projection factor `2` and inclusion-exclusion.
2. Chamber/Gelfand--Leray weights and `J_q=2I_q/pi`.
3. The 13-12aa raw `j=0` primitive local coefficient formulas.
4. The 13-12aa pure-factor singularity ledger and mixed-correction
   weighted-`l1` bound, including uniformity in the retained harmonic range.
5. The zero-mode curved-region transfer and the assertion that direction enters
   only through `J_q`.
6. The nonzero-harmonic, bracketing and boundary lower-order bounds at raw
   `B(log B)^3` scale.
7. The rule that Stage12 total calibration is used only after the common
   `Theta` theorem has been established.
8. The 13-12ab finite local-state refinement and exact Euler-factor replacement
   for every fixed prime condition.
9. The inert-prime unit acceptance formula and the `O(1/p)` positive-valuation
   tail with an absolute constant sufficient for eventual `lambda_p<=3/4`.
10. The order-of-limits argument: fixed `k`, then `B->infinity`, then
    `k->infinity`, with no hidden growing-modulus uniformity.
11. Pair/triple lower order and the final exactly-one transfer.
12. All stated non-claims and the declared Stage12 R09 input boundary.

---

## 9. Review neutrality and evidence rules

For R02:

```text
PREVIOUS_R01_VERDICT_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false
```

Hashes and CI establish source identity and deterministic regeneration only.
They do not establish mathematical correctness. A reviewer may return `OPEN` or
`REPAIRABLE` whenever the mathematical chain warrants it, even if every local
script reports `PASS`.

---

## 10. Scope and non-claims

Stage13 R02 does **not** claim:

- existence or nonexistence of a perfect cuboid;
- an explicit convergence rate;
- an effective threshold for closeness to the limiting vector;
- monotonicity of directional ratios;
- publication-grade peer review;
- a certified numerical enclosure for `kappa`.

A perfect cuboid, if one exists, lies in the triple-overlap population. The
statement `T(B)=o(B(log B)^3)` is a density statement and does not imply that
`T(B)` is empty.

---

## 11. Current candidate decision

The project-side repaired theorem is the boxed exactly-one asymptotic above, but
its external status remains deliberately unresolved:

```text
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_R02_CANDIDATE_READY=true
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
```

The R02 reviewer, not this document, determines whether the final verdict is
`CLOSED`, `REPAIRABLE`, `OPEN` or `UNREADABLE_SOURCE`.
