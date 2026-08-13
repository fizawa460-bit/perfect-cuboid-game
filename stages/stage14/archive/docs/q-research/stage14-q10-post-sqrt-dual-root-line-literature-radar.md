# Stage14-q10 — post-sqrt dual-root-line literature radar

## Trigger

```text
TRIGGER_STAGE=merged Stage14-X13 + merged Stage14-s7-43 + merged Stage14-4db
FRONTIER_ADVISORY=open Stage14-s7-44
EXACT_OBSTRUCTION=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergy
CURRENT_BEST_BOUND=V(B) << B^(1/2+o(1))
LAST_RADAR_BASELINE=Stage14-q9
```

The q-route was parked after q9 until a stable new obstruction appeared.  X13 changed the global theorem from `23/44` to the square-root bound; s7-43/4db then forced the possible saturation packet to the globally odd-primitive, full-common-core theta-quarter band.  The draft s7-44 frontier makes the remaining issue explicit: two primitive root lines over essentially the same moving common core `C`, one Gaussian (`t^2=-1`) and one endpoint-linear (`t^2=1`), must also admit the original reciprocal physical completion.

This is a genuinely new q10 trigger.  It is not the q9 Gaussian-Hecke / isogeny receiver and it is not the fixed-U t80--t82 projective-ray coefficient space.

## Exact Stage14 packet that literature must respect

At possible square-root saturation:

```text
theta=1/4
5/24 <= phi <= 1/4
chi=2phi-1/4
H=K=B^o(1)
C/J=B^o(1)
C_Cayley/J=B^o(1)
C=J=C_Cayley at fixed-power scale
```

The two root-line objects are:

1. primitive Gaussian pair `(U,V)` with local condition

```text
a U/(b V) = rho_p (mod p^e),
rho_p^2=-1 (mod p^e),
```

2. primitive endpoint column `(A_z,B_z)` with local condition

```text
A_z/B_z = sigma_p (mod p^e),
sigma_p^2=1 (mod p^e).
```

Local orientation count is only `4^omega(C)=B^o(1)`.  Therefore a literature transfer must save on the **joint compatibility / reciprocal completion**, not by charging the same common core a second time.

Required guards:

```text
COMMON_CORE_SECOND_SPACING_CHARGE_FORBIDDEN=true
ORIENTATION_ENTROPY_IS_ONLY_Bo1=true
GLOBAL_ODD_PRIMITIVITY_RETAINED=true
RECIPROCAL_COMPLETION_RETAINED=true
FIXED_U_T_ROUTE_CROSS_PROMOTION_WITHOUT_BRIDGE=false
```

## Literature scan

### A. Reuss — bilinear/trilinear point counting

Thomas Reuss, *Counting points on bilinear and trilinear hypersurfaces*, arXiv:1502.07594.

Classification: `NEAR_HIGH_PRIORITY`.

Reuss proves sharp box bounds for primitive integer points on irreducible bilinear forms on `P^1 x P^1`, with an explicit improvement as the determinant of the coefficient matrix grows.  The proof is lattice-theoretic and therefore unusually compatible with Stage14's primitive anisotropic boxes.  The same paper treats irreducible nonsingular trilinear forms, with dependence on the Cayley hyperdeterminant.

This is the closest deterministic literature weapon if the final reciprocal completion can be eliminated to one fixed-branch equation

```text
x^T A_C y = 0
```

(or a 2x2x2 trilinear analogue) between the two primitive root-line coordinates, with a coefficient determinant/hyperdeterminant carrying a fixed power of `C` after the already-used root-line congruences have been encoded.

Verified compatibility:

- primitive 2-coordinate blocks: yes;
- anisotropic boxes: yes;
- coefficients may vary between packets: yes, provided the determinant parameter is tracked;
- no Fourier cancellation is required: yes.

Missing bridge:

```text
Q10_REUSS_BRIDGE=
  derive the exact reciprocal-completion eliminant after fixing the two legal root-line orientations;
  prove irreducibility/nondegeneracy on every surviving physical branch;
  prove |det A_C| (or hyperdeterminant) has a uniform fixed-power lower bound not already paid for by the root-line count.
```

Without that bridge Reuss is not a direct theorem for the current receiver.

### B. Dong--Robles--Zeindler 2026 — Kloosterman fractions

Anji Dong, Nicolas Robles, Dirk Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.

Classification: `NEAR_HIGH_PRIORITY_ANALYTIC`.

The paper improves bilinear bounds for phases of the form

```text
e(a * inverse(m) / (b n))
```

with arbitrary complex coefficient sequences and also develops related Hermitian/Salié-type estimates.  It improves the older DFI/Bettin--Chandee Kloosterman-fraction technology.

This is potentially relevant only if the Stage14 reciprocal completion, after fixing the two primitive root lines, admits a **zero-loss Fourier/divisor switch** to a genuine Kloosterman-fraction bilinear form with independently controlled dyadic variables.

Missing bridge:

```text
Q10_KLOOSTERMAN_BRIDGE=
  Fourier-detect the exact physical reciprocal completion;
  derive one inverse-fraction phase without replacing the common C by an independent second modulus;
  retain the squarefree-cell, sign and positivity masks in coefficient L2 norms;
  verify the resulting M,N range lies in a power-saving regime of the theorem.
```

No such bridge is currently proved on the global s/main receiver.  The fixed-U t80--t82 route already contains inverse-fraction phases, but that coefficient space remains separate.

Related older baseline: Bettin--Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.  It is weaker quantitatively but gives the same transfer diagnostic.

### C. Baier 2026 / modular-square-root energy

Stephan Baier, *On certain bilinear sums with modular square roots and applications*, arXiv:2601.15448; and *A note on bilinear sums with modular square roots*, arXiv:2605.01635.

Classification: `NEAR_SECONDARY`, not direct.

The January paper gives unconditional bilinear estimates and additive-energy bounds for modular square roots for arbitrary integer modulus.  A representative kernel has

```text
k^2 = j m (mod r),
```

and the unconditional bilinear bound becomes nontrivial in specified ranges (for a simple corollary, both main lengths are above roughly `r^(1/3+epsilon)`).  It also gives restricted second/fourth energies of modular square roots.

Why direct import fails here:

- the Stage14 Gaussian line has fixed local RHS `-1` after coefficient normalization, not a moving `j m` family;
- the endpoint line has the trivial `+1` root family;
- the hard object is the compatibility of **two** primitive points plus reciprocal completion, not the additive energy of one modular-root family;
- `C` moves with the physical packet and has already been charged once.

A useful transfer would require first producing a moving modular-root argument from the reciprocal eliminant itself.  Until then this literature does not yield a certified `B^{-delta}`.

### D. Ngo / DFI/Toth quadratic-root equidistribution

Hieu T. Ngo, *On roots of quadratic congruences*, Bull. LMS 56 (2024), arXiv:2107.13301; Duke--Friedlander--Iwaniec and Toth are the underlying spectral precedents.

Classification: `BACKGROUND_NEAR`, direct import blocked.

These results control Weyl sums/equidistribution of roots of a single irreducible quadratic congruence as the modulus varies (with strong arithmetic-progression refinements in Ngo).  They do not contain the second primitive root line, the full common-core charged-once restriction, or the reciprocal physical completion.  Replacing the Stage14 packet by one quadratic-root sequence would discard the current obstruction rather than bound it.

### E. General determinant method

Browning--Heath-Brown--Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117, and the global determinant-method literature.

Classification: `BACKGROUND` for q10.

Uniform bounded-degree point counts are available, but the present packet is already much thinner than a generic bounded-degree variety.  A generic determinant-method embedding loses the exact common-core root-line density unless one first produces an irreducible low-degree eliminant with a useful coefficient determinant.  At that point Reuss's specialized bilinear/trilinear lattice theorem is the sharper first test.

## 2026 delta relative to q9

The important new literature since the original q shelf is not a direct solution, but there are now stronger analytic weapons close to the two current Stage14 frontiers:

```text
GLOBAL_S/MAIN:
  Reuss bilinear/trilinear determinant-sensitive lattice count = best first transfer test
  Dong--Robles--Zeindler Kloosterman fractions = best analytic fallback after exact Fourier bridge

FIXED_U_T:
  Dong--Robles--Zeindler 2026 is materially closer to t80--t82 inverse-fraction phases
  Baier 2026 modular-root bilinear/energy bounds are relevant secondary input
```

The second line is **not** cross-promoted to the global receiver.

## Verdict

No external theorem found in this pass directly proves

```text
sum_C I_C << B^(1/2-delta+o(1))
```

for any certified fixed `delta>0` while retaining the complete Stage14 packet.

```text
STAGE14_Q10=COMPLETE_POST_SQRT_DUAL_ROOT_LINE_LITERATURE_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
REUSS_BILINEAR_TRILINEAR_TRANSFER=NEAR_HIGH_PRIORITY
DONG_ROBLES_ZEINDLER_2026_KLOOSTERMAN_TRANSFER=NEAR_HIGH_PRIORITY_ANALYTIC
BAIER_2026_MODULAR_ROOT_ENERGY_TRANSFER=NEAR_SECONDARY
NGO_DFI_SINGLE_ROOT_EQUIDISTRIBUTION_DIRECT_IMPORT=false
GENERIC_DETERMINANT_METHOD_DIRECT_IMPORT=false
FIXED_U_T82_CROSS_PROMOTED_TO_GLOBAL=false
```

## Falsifiable handoff

The smallest useful next proof task is **not** another broad literature search.  On one fixed physical sign/orientation branch in the theta-quarter band, eliminate the reciprocal completion between the primitive Gaussian pair and primitive endpoint pair and classify the resulting equation.

```text
Q10_HANDOFF_TEST:
  if eliminant is irreducible bilinear with determinant carrying C^eta:
      test Reuss immediately;
  else if it Fourier-divisor-switches to a true inverse-fraction bilinear form:
      test Dong--Robles--Zeindler / Bettin--Chandee ranges;
  else:
      retain SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergyPowerSaving
      as a genuinely new incidence theorem target.
```

Recommended receivers:

```text
HANDOFF_S=Stage14-s7-45 after the s7-44 H decision
HANDOFF_MAIN=next post-4db/4dc exact eliminant stage
HANDOFF_T=keep t80--t82 literature mapping separate
NEXT_Q_STAGE=NONE_UNTIL_THE_ELIMINANT_SHAPE_IS_KNOWN_OR_A_NEW_STABLE_OBSTRUCTION_APPEARS
```
