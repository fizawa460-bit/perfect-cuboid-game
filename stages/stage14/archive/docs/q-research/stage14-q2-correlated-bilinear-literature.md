# Stage14-q2 — Correlated bilinear / quadratic-large-sieve literature pass

## Status

```text
STAGE14_Q2=COMPLETE_FOCUSED_CORRELATED_BILINEAR_LITERATURE_PASS
CHECKED_AT=2026-08-09
TRIGGER_STAGE=Stage14-s5i_and_Stage14-4av
EXACT_OBSTRUCTION=L2_DISPERSION_FOR_EUCLID_INCIDENCE_DISCREPANCY_PLUS_GROWING_AUXILIARY_STATE_AND_SPARSE_LARGE_MODULI
DIRECT_SUBROUTINE_COUNT=2
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
NEXT=Stage14-q3 small-point / first-point height pass
```

## 1. Why q2 changed after q1

The target moved while the literature radar was being rebuilt.

Merged `Stage14-s5i` proves that the pure Euclid divisibility incidence is not an arbitrary two-variable matrix after all. On each coprime state-modulus block its bulk factors into a rank-one local-density product. What remains is a discrepancy term

```text
W(u,v) = W_bulk(u,v) + Delta(u,v),
```

where `Delta` contains finite-box error, primitive Möbius bookkeeping, and sparse large-modulus effects. The next s-stage asks for an `L2` dispersion estimate for `Delta` and divisor switching in the `Q >= XY` regime.

Merged `Stage14-4av` independently proves a fixed-power saving for the bare CRT incidence block after applying the separable quadratic-character bilinear estimate. Its remaining obstruction is the growing auxiliary-state incidence weight, primitive Möbius bookkeeping, and endpoint dyadic ranges.

Therefore q2 is **not** searching for a theorem that handles an arbitrary matrix `W(u,v)`. The actual literature question is narrower:

> Can known character-sum, dispersion, modular-root, or divisor-switching technology control the residual `Delta(u,v)` after the rank-one CRT bulk has already been removed?

## 2. DIRECT subroutine A — Wilson: Jacobi bilinear forms over hyperbolic regions

**Primary source.** Cameron Wilson, *General Bilinear Forms In The Jacobi Symbol Over Hyperbolic Regions*, arXiv:2208.14909, current manuscript dated March 22, 2026.

**Exact source interface.** Wilson studies

```text
sum_{nm <= T} a_n b_m (n/m)
```

with arbitrary bounded separated coefficients `a_n`, `b_m`. The main cancellation theorems are stated for odd square-free `n,m` bounded away from the axes. The proof explicitly reduces the hyperbolic height condition to rectangular character bilinear estimates via Perron/box decompositions, and it records both the standard Heath-Brown rectangular bilinear estimate and the stronger lopsided second-moment inequality needed near thin rectangles.

**Stage14 hypotheses already available.** The reciprocal variables in the s5/4av blocks are odd squarefree divisor pieces, and after the s5i rank-one decomposition the bulk coefficients are separated up to harmless divisor/state factors. Medium dyadic blocks are automatically bounded away from the coordinate axes.

**What can be imported directly.** Once a Stage14 term has genuinely been reduced to separated coefficients, Wilson gives a ready-made way to sum it under a product/hyperbolic cutoff and to handle lopsided rectangular coverings without pretending all dyadic boxes are balanced.

**What it does not do.** Wilson still assumes coefficients of the form `a_n b_m`. It does not turn the present discrepancy `Delta(u,v)` into separated coefficients and does not prove the required `sum |Delta(u,v)|^2` estimate.

**Classification.** `DIRECT` for the **post-separation hyperbolic/endpoint summation subroutine**; not a direct theorem for the full q2 obstruction.

**Handoff.** `Stage14-s5j`, `Stage14-4aw`.

## 3. DIRECT subroutine B — Heath-Brown / Liu quadratic large sieve

**Primary modern source.** Zihao Liu, *Explicit quadratic large sieve inequality*, arXiv:2505.09637, an explicit form of Heath-Brown's real-character large sieve.

**Current Stage14 state.** This weapon is already consumed correctly in s5h and 4av: after true separation, Cauchy-Schwarz plus the quadratic large sieve gives a fixed-power saving on balanced/medium dyadic blocks.

**q2 decision.** Keep this as `DIRECT` only after the incidence/state weight has been separated or controlled in `L2`. It is not evidence that an arbitrary correlated weight is admissible.

**Classification.** `DIRECT` for separated rectangular blocks; already imported.

## 4. NEAR weapon A — Friedlander–Iwaniec character decomposition for rational zeros of ternary quadratic forms

**Primary source.** John Friedlander and Henryk Iwaniec, *Ternary quadratic forms with rational zeros*, J. Théorie des Nombres de Bordeaux 22 (2010), 97–113, DOI 10.5802/jtnb.706.

**Why it matters.** This is one of the classical arithmetic-geometry settings in which local solubility conditions are converted into quadratic-character weights and averaged over two integer parameters. Wilson explicitly points back to this work as the small-modulus character-sum mechanism that complements the large-modulus bilinear estimates.

**Stage14 fit.** After modulus freezing, the growing auxiliary-state system in 4aw/s5j may split into finitely many residue/state patterns plus reciprocal Jacobi characters. The Friedlander–Iwaniec architecture is therefore a realistic template for the **small-modulus/frozen-state side** of the decomposition.

**Mismatch.** Their theorem is for a specific two-parameter family of ternary quadratic forms and does not state an `L2` variance theorem for the Stage14 Euclid-incidence discrepancy. The Stage14 five-factor Pythagorean incidence has to be reduced to their type of separated character sums first.

**Classification.** `NEAR` proof architecture, not a direct import.

## 5. NEAR weapon B — Wilson/Browning/Lyczak/Sarapin: squarefree product parametrisations and multidimensional sieve

**Primary source.** Tim Browning, Julian Lyczak, Roman Sarapin, *Local solubility for a family of quadrics over a split quadric surface*, arXiv:2203.06881.

**Verified interface.** Their analytic section first parameterises a split-quadric family by products of squarefree variables, then applies a multidimensional large sieve to local obstruction sets. In the squarefree coefficient model they obtain logarithmic thinning for a genuinely multi-variable local-solubility problem.

**Stage14 fit.** Structurally this is close to Stage14's product/state bookkeeping: squarefree pieces, local quadratic conditions, and a nontrivial parameter variety rather than independent integer coefficients. It is useful evidence that the state system should be frozen at the residue-vector level before applying analytic cancellation.

**Mismatch.** Their multidimensional sieve exploits forbidden residue sets and yields logarithmic thinning. Stage14 already knows the relevant local images and needs power-saving control of a centered discrepancy/reciprocal-character average. It does not supply the needed `L2(Delta)` theorem.

**Classification.** `NEAR/BACKGROUND` for organisation of state variables; insufficient for the present exponent target.

## 6. NEAR weapon C — modular-square-root bilinear energy

**Primary source.** Alexander Dunn, Bryce Kerr, Igor E. Shparlinski, Alexandru Zaharescu, *Bilinear forms in Weyl sums for modular square roots and applications*, arXiv:1908.10143, Adv. Math. 375 (2020), 107369.

**Verified interface.** The paper proves power-saving estimates for bilinear forms in modular square-root Weyl sums. The mechanism uses weighted additive energy of quadratic residues in a fixed finite field. The authors explicitly frame the result as a bilinear discrepancy/equidistribution tool for modular square roots.

**Stage14 hook.** The norm column `m^2+n^2` produces the exact split-prime root condition

```text
(n/m)^2 = -1 mod p
```

at primes `p = 1 mod 4`. If the s5j discrepancy for state-split norm pieces is Fourier-expanded into root phases modulo a fixed prime/block modulus, the DKSZ energy mechanism is a concrete candidate for gaining cancellation beyond a bare root count.

**Critical mismatch.** DKSZ works with a fixed prime field and separated dyadic weights. Stage14 simultaneously varies squarefree/composite state moduli and still carries primitive/Möbius coupling. No direct theorem in DKSZ averages the exact Stage14 `Delta(u,v)` over those moving composite moduli.

**Classification.** `NEAR`, specifically for the norm-column Fourier/root component after modulus freezing.

## 7. NEAR weapon D — roots of quadratic congruences / spectral Weyl sums

**Primary source.** Hieu T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301, Bull. London Math. Soc. 56 (2024), 2886–2910. Ngo builds on the Duke–Friedlander–Iwaniec theory of Weyl sums for quadratic roots and obtains strong estimates for positive-discriminant quadratics; the negative-discriminant case is the classical DFI setting.

**Stage14 hook.** State-split `m^2+n^2` congruences are a particularly rigid quadratic-root problem (`x^2 = -1 mod q`). Thus the root-spacing/spectral machinery is more structurally faithful to the norm column than treating it as a generic divisor constraint.

**Mismatch.** These theorems control Weyl sums/equidistribution of modular roots as the modulus varies. Stage14's target is a covariance of Euclid incidence counts with extra linear columns and Möbius/state weights. A Fourier transform must first show that the Stage14 second moment is dominated by one of these Weyl linear forms.

**Classification.** `NEAR`. This is the preferred deep fallback if elementary CRT/geometry-of-numbers dispersion fails specifically on the norm column.

## 8. NEAR weapon E — general BDH variance as a model for the desired L2 step

**Primary source.** Adam J. Harper, *Simple Barban–Davenport–Halberstam type asymptotics for general sequences*, arXiv:2412.19644.

**Verified interface.** Harper gives elementary variance estimates for a general complex sequence in arithmetic progressions, with useful asymptotics when the sequence is sparse or sufficiently integer-like in divisibility by small moduli.

**Stage14 hook.** The desired `sum |Delta(u,v)|^2` is conceptually a Barban–Davenport–Halberstam variance: exact congruence counts minus local-density main terms, squared and averaged over moduli/state pieces.

**Mismatch.** Harper's object is a one-dimensional sequence in arithmetic progressions. Stage14 counts primitive two-dimensional Euclid lattice points simultaneously satisfying divisibility conditions in several binary forms. A nontrivial encoding/reduction is required before the theorem applies.

**Classification.** `NEAR` as an `L2` proof template, not a direct theorem.

## 9. NEAR weapon F — divisor switching for `Q >= XY`

**Primary source example.** Daniel Fiorilli, *On a theorem of Bombieri, Friedlander and Iwaniec*, arXiv:1108.0439, which develops Hooley's variant of divisor switching in a mean-value problem.

**Stage14 hook.** s5i explicitly isolates a sparse large-modulus regime `Q >= XY`. In such a regime, a divisibility relation `q | F(m,n)` often has a small complementary quotient because the polynomial value is bounded by the physical box. Re-indexing by that quotient rather than by `q` is exactly the structural purpose of divisor switching.

**Mismatch.** The BFI/Fiorilli setting is arithmetic progressions/divisor problems, not the five simultaneous Euclid factors. The switch has to be derived separately for each relevant Stage14 factor, and the norm column may behave differently from the linear columns.

**Classification.** `NEAR` method transfer. This is the preferred first attack on the sparse `Q >= XY` block before invoking deeper spectral machinery.

## 10. BLOCKED / do-not-misuse results

### 10.1 Quadratic large sieve with arbitrary `Delta(u,v)` — BLOCKED

No source found in q2 permits replacing the residual two-variable discrepancy by separated coefficients without proving an additional norm/low-rank statement. Heath-Brown/Liu and Wilson remain separated-coefficient theorems.

### 10.2 Modular-root energy as a theorem for all five Euclid columns — BLOCKED

DKSZ/Ngo/DFI machinery is naturally attached to polynomial-root phases, especially the norm column. It does not automatically control simultaneous linear-factor state incidence.

### 10.3 Multidimensional local sieve as the missing power saving — BLOCKED

The Browning–Lyczak–Sarapin sieve is structurally informative but its logarithmic residue-exclusion mechanism is not the power-saving centered-character estimate required by the Stage14 exponent budget.

### 10.4 Spectral/Kuznetsov escalation before elementary dispersion is tested — DEFER

The root-Weyl literature shows a viable deep route for the norm column, but the current s5i decomposition has already exposed an elementary rank-one bulk. First test the covariance of the explicit CRT/Möbius errors. Escalate to spectral root sums only if the norm-column covariance survives that reduction.

## 11. Concrete receiving-stage proof architecture extracted from q2

q2 does not deliver a single theorem that closes the current obstruction. It does deliver a much sharper proof order for `s5j` / `4aw`.

### Step A — freeze state and common gcd data

Expand the primitive Möbius condition only to a controlled truncation and freeze the finite local-state labels. On each frozen block, preserve the exact s5i rank-one main density and define the centered remainder `Delta`.

### Step B — square before taking characters

For the target

```text
sum_{u,v} |Delta(u,v)|^2,
```

expand the square first. The inner object becomes a covariance of two Euclid congruence systems. Separate pairs according to common factors/gcd of the two modulus systems. The independent CRT part should reproduce the product density and cancel against the centered main term; only diagonal/shared-factor configurations should remain large.

This is the exact point at which a persistent diagonal can be identified honestly rather than hidden inside an arbitrary coefficient matrix.

### Step C — medium modulus

For linear-linear and linear-norm blocks, use geometry-of-numbers/CRT to bound the covariance error. Once a remaining reciprocal-character factor has separated coefficients, apply Heath-Brown/Liu; if the region is product/hyperbolic or lopsided, use Wilson's hyperbolic theorem/covering rather than summing balanced-box estimates naively.

### Step D — norm-column residue roots

If the `m^2+n^2` shared-factor covariance remains too large after Step B, rewrite it through roots of `x^2 = -1 mod q`. Test first a classical root-spacing/large-sieve formulation; only then escalate to DKSZ additive-energy or DFI/Ngo spectral Weyl-sum technology.

### Step E — sparse large modulus

For `Q >= XY`, switch from the large divisor to the complementary quotient of the bounded Euclid factor. Split the four linear columns and the norm column, because their quotient geometry differs. The goal is to return the new modulus to a medium range where Steps B–D apply.

### Step F — only then restore the full character polynomial

After `L2(Delta)` and sparse blocks are controlled, reinsert the finite character expansion/state multiplicity and use the direct separated Jacobi tools. Do not prove cancellation mode-by-mode before controlling the common incidence discrepancy.

## 12. q2 decision

The literature search found **no existing theorem that directly proves the Stage14 discrepancy second moment**. That is important negative information: the current proof workers should not waste time searching for a magical "quadratic large sieve with arbitrary correlated coefficients" theorem.

However, q2 found two directly usable subroutines and three credible escalation routes:

```text
DIRECT:
  Heath-Brown/Liu  -> separated rectangular reciprocal blocks
  Wilson           -> separated hyperbolic/lopsided reciprocal blocks

NEAR, medium/norm discrepancy:
  Friedlander-Iwaniec small-modulus character architecture
  DKSZ modular-square-root additive energy
  DFI/Ngo quadratic-root Weyl/spectral machinery

NEAR, variance/sparse architecture:
  Harper BDH-style variance template
  Hooley/Fiorilli divisor switching
```

The most important practical result is that `s5i` has already done the hard conceptual reduction: the pure incidence bulk is rank one. The remaining problem should now be attacked as an explicit **centered congruence covariance / dispersion calculation**, not as a generic two-variable bilinear-form problem.

## 13. Handoff

```text
TO=Stage14-s5j
ACTION=expand sum|Delta|^2 as a covariance of two frozen Euclid congruence systems; isolate shared-factor diagonals; use divisor switching for Q>=XY; invoke root-Weyl technology only on a surviving norm-column obstruction

TO=Stage14-4aw
ACTION=freeze growing auxiliary states, separate their CRT bulk from centered discrepancy, and use Wilson for hyperbolic/lopsided endpoint summation after true separation

NEXT_Q=Stage14-q3
TOPIC=small-point / first-point height literature pass
```
