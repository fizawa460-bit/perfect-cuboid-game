# Stage13-7 — final asymptotic snapshot

> **STATUS:** `STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL`
>
> **ROLE:** frozen Stage13-7 theorem snapshot / provenance archive
>
> **NEXT:** `Stage13-8`

This file is a frozen end-of-task snapshot permitted by the Stage13 policy's archive/provenance exception. It consolidates the Stage13-7 theorem chain without replacing the living `stages/stage13/main.md`. Historical intermediate reports remain valid in their stated scope; the supersession ledger below identifies which conditional status flags are no longer current.

## 1. Final theorem

Let

\[
P(B)=\frac{1}{N_1(B)}\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

for the primitive canonical exactly-one-face population with space diagonal at most \(B\).

Let the Stage13-3b chamber integrals be

\[
I_{ab}=0.659705248705705,
\quad
I_{ac}=0.3026997526726076,
\quad
I_{bc}=0.2712955487578571,
\]

with the exact identity

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.
\]

Then the three exactly-one category counts satisfy

\[
\boxed{
N_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

Summing gives

\[
\boxed{
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Consequently

\[
\boxed{
P(B)\longrightarrow
\left(
\frac{8I_{ab}}{\pi^2},
\frac{8I_{ac}}{\pi^2},
\frac{8I_{bc}}{\pi^2}
\right).
}
\]

Numerically,

\[
\boxed{
P_\infty=
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
}
\]

Thus

\[
\boxed{
N_{ab}:N_{ac}:N_{bc}
\longrightarrow
2.431684750178191:1.115756428951881:1.
}
\]

The limiting ratio is therefore **not** \(2:1:1\).

No assumption about nonexistence of perfect cuboids is used.

## 2. Asymptotic deviation

With the Stage13-5 coordinates

\[
\alpha(B)=P_{ab}(B)-\frac12,
\qquad
\beta(B)=\frac{P_{ac}(B)-P_{bc}(B)}2,
\]

we obtain

\[
\boxed{
\alpha(B)\to0.034736933231398814,
\qquad
\beta(B)\to0.01272764444795145.
}
\]

Hence

\[
\Delta(B)=P(B)-\left(\frac12,\frac14,\frac14\right)
\]

has the nonzero limit

\[
\boxed{
\Delta_\infty=
(0.034736933231398814,
 -0.004640822167747971,
 -0.03009611106365087).
}
\]

Its \(L^1\) size is

\[
\|\Delta_\infty\|_1
=0.06947386646279766.
\]

At \(B=100000\), the exact-one data instead have

\[
\alpha\approx0.0007796226864250431,
\qquad
\beta\approx0.007367731952627507,
\]

so \(\beta/\alpha\approx9.45038\). In the proved limit,

\[
\alpha/\beta\approx2.72925.
\]

Thus the accessible near-\(2:1:1\) regime is strongly pre-asymptotically flattened. Stage13-7 proves the limit but does **not** claim monotone convergence or an explicit secondary convergence rate.

## 3. Scale ladder

The same chamber vector survives three major arithmetic reweightings even though their absolute scales are very different.

### 3.1 Preprimitive `m1`

Stage13-7ja gives

\[
M_q(B)\sim C_q B\log B,
\qquad
C_q=\frac{8I_q}{\pi^3},
\]

with

\[
C_{ab}+C_{ac}+C_{bc}=\frac1\pi.
\]

Numerically,

```text
C_ab = 0.17021205235515585
C_ac = 0.07810025196993260
C_bc = 0.06999758185870224
```

and the normalized limit is \(P_\infty\).

### 3.2 Primitive pure-`G`

Stage13-7j gives

\[
G_q(B)\sim K_q B(\log B)^{1/3}
\]

with the numerical prime-product diagnostics

```text
K_ab = 0.1279408373737631
K_ac = 0.05870448947578533
K_bc = 0.05261407234814782
K_total = 0.23925939919769626.
```

The primitive-support transition satisfies

\[
\frac{G_q(B)}{M_q(B)}
\sim
\Lambda(\log B)^{-2/3},
\]

where

\[
\boxed{
\Lambda=\frac{K_q}{C_q}=\pi K_{\rm total}
\approx0.7516555708217902
}
\]

for all three categories. Primitive support changes the logarithmic exponent but not the leading normalized vector.

### 3.3 Primitive raw incidence

Stage13-7jb restores supported-shell richness and obtains

\[
A_q(B)\sim D_q B(\log B)^3,
\qquad
D_q=\frac{\kappa I_q}{3\pi^3}.
\]

Using the Stage12 finite prime-product diagnostic

\[
\kappa\approx0.01855917155586297
\]

only as a numerical diagnostic gives

```text
D_ab = 0.00013162477835561946
D_ac = 0.00006039483228608767
D_bc = 0.00005412904709213402
D_total = 0.00024614865773384115.
```

Exactly,

\[
D_{ab}+D_{ac}+D_{bc}=\frac{\kappa}{24\pi}.
\]

Relative to pure-`G`,

\[
\frac{A_q(B)}{G_q(B)}
\sim
\Omega(\log B)^{8/3}
\]

with common numerical diagnostic

\[
\Omega\approx0.0010287940977836043.
\]

Supported-shell richness therefore also changes the absolute logarithmic scale without changing the leading normalized vector.

### 3.4 Exactly one face

Stage13-7jf proves the pair/triple overlap correction is lower order, hence

\[
N_q(B)=A_q(B)+o(B(\log B)^3).
\]

Therefore the raw and exactly-one leading constants agree categorywise.

## 4. Overlap theorem and the order of limits

The decisive Stage13-7jf argument is a fixed-prime sieve inside the already-counted raw-incidence population.

For a distinguished raw face

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2,
\]

integrality of a chosen second face sharing the tagged leg \(x\) implies

\[
x^2+z^2=\square.
\]

For every sufficiently large inert prime \(p\equiv3\pmod4\), the primitive local raw-incidence acceptance ratio for the necessary condition

\[
x^2+z^2\in QR_0(\mathbf F_p)
\]

satisfies

\[
\rho_p=\frac12+O(p^{-1/2}),
\]

so one may choose an absolute threshold after which

\[
\rho_p\le\frac34.
\]

For any fixed finite set \(S\) of such primes, the frozen Stage12/7jb machinery is refined only by a fixed modulus. Thus the same \(B(\log B)^3\) asymptotic applies with the leading arithmetic constant multiplied by the finite product of local acceptance ratios.

The order of limits is essential:

```text
1. choose k sufficiently large inert primes and hold them fixed;
2. let B -> infinity with that fixed modulus;
3. only afterwards let k -> infinity.
```

Hence no theorem uniform in a modulus growing with \(B\) is required. For every pair overlap,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le D_q\left(\frac34\right)^k
\]

for every fixed \(k\), and therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3).}
\]

The exact Stage13-7jc sandwich then gives

\[
F(B)=o(B(\log B)^3),
\]

and since the triple overlap \(T(B)\le F(B)\),

\[
T(B)=o(B(\log B)^3).
\]

The universal Stage13-3d two-orientation bridge introduces no category-dependent factor here: for each chosen second face, exactly one tagged orientation uses the shared leg as \(x\).

## 5. Supersession ledger

The Stage13-7 substage reports are historical snapshots and retain their stated local truth. Their current interpretation is:

- **13-7j:** the pure-`G` theorem remains active; its old `RAW_DIRECTIONAL_LIMIT_IDENTIFIED=false` and `EXACT_ONE_DIRECTIONAL_LIMIT_IDENTIFIED=false` flags are historical guardrails, superseded by 7jb and 7jf.
- **13-7ja:** active. Primitive support changes `B log B` to `B(log B)^(1/3)` but preserves the chamber vector.
- **13-7jb:** active. Supported-shell restoration changes the scale to `B(log B)^3` and proves the raw directional theorem.
- **13-7jc:** its conditional target `F(B)=o(B(log B)^3)` is now discharged.
- **13-7jd:** its near-linear exponent bound remains valid but is superseded in strength by 7jf.
- **13-7je:** its Kummer surface / congruent-number twist / coupled-height identities remain valid structural information, but they are not needed in the shortest final overlap proof.
- **13-7jf:** active final overlap theorem and exactly-one transfer.
- **13-7jg:** final consistency audit and Stage13-7 completion decision.

## 6. Completion decision

The Stage13-7 research question asked whether the deviation coordinates tend to zero, tend to nonzero limits, remain oscillatory at visible scale, or admit another justified asymptotic description.

It is now resolved:

```text
STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL
ASYMPTOTIC_DEVIATION_RESOLVED=true
ALPHA_LIMIT_IDENTIFIED=true
BETA_LIMIT_IDENTIFIED=true
DELTA_LIMIT_IDENTIFIED=true
ALPHA_LIMIT_NONZERO=true
BETA_LIMIT_NONZERO=true
DELTA_LIMIT_NONZERO=true
LIMIT_EQUALS_2_1_1=false
EXACT_ONE_DIRECTIONAL_LIMIT_UNCONDITIONAL=true
PAIR_OVERLAP_LOWER_ORDER_PROVED=true
TRIPLE_OVERLAP_LOWER_ORDER_PROVED=true
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
NEXT=Stage13-8
```

The completion level is the same project standard used for the frozen Stage12 analytic theorem chain: standard external theorems are invoked in their applicable fixed-parameter form, but no claim of independent publication-level peer review is made.

## 7. What Stage13-8 now needs to do

Stage13-8 was originally planned as the rigorous Stage12-to-Stage13 bridge. Much of the mathematics it anticipated is already proved across Stage13-3d and Stage13-7:

1. universal oriented-to-canonical raw-incidence multiplicity `2` — proved in 13-3d;
2. Stage12 total constant transfer — proved in 13-3d;
3. individual raw directional constants — proved in 13-7jb;
4. overlap removal to exactly-one — proved in 13-7jf;
5. final exact-one directional limit — proved in 13-7jf and audited in 13-7jg.

Accordingly Stage13-8 should primarily consolidate this bridge into the canonical Stage13 exposition, audit notation and local-factor compatibility, and identify any remaining genuinely new bridge lemma before Stage13-9 formulates the main structural theorem.
