# Stage14-AM1 — Azevedo--Moreira prime-power orientation and latest-main refinement

## Status and provenance

`COMPLETE_MERGED_AM_PRIME_POWER_ORIENTATION_ROOT_DICTIONARY_AND_RECENTERING_REFINEMENT`

This stage is a self-contained refinement of merged `Stage14-AM`; it does not overwrite or relabel that result.  It independently rechecks whether the structured/uniform architecture in

> Guilherme Azevedo and Joel Moreira, *Pythagorean triples in level sets of completely multiplicative functions*, arXiv:2607.04903v1 (6 July 2026),

can be used on the current Stage14 square-root packet.  The external theorem is checked against the original paper, not against q11 or merged AM alone.  Relative to merged AM, the new exact content is:

```text
1. the D/A versus rotated m_s/n_s root dictionary;
2. a prime-power Gaussian valuation projector on fixed physical valuation strata;
3. the explicit transfer term between the s7-55 and 4dm pair splits.
```

The merged AM verdict `BLOCKED` is confirmed.

The theorem-source boundary is latest merged main

```text
SOURCE_MAIN_SHA=31762e51ff1ea764a4dbc06fe91656f1a37aaafc
```

and includes, in particular,

```text
Stage14-X15,
Stage14-Work-beX17,
Stage14-4dl,
Stage14-s7-55,
Stage14-t95,
Stage14-t96,
Stage14-q11,
Stage14-s7-56,
Stage14-4dm,
Stage14-Work-bfX18,
Stage14-AM,
Stage14-4dn,
Stage14-s7-57,
Stage14-t97.
```

The post-q11 related results merged at this freeze are `Stage14-s7-56`, `Stage14-4dm`, `Stage14-Work-bfX18`, the first `Stage14-AM` audit in PR #657, and then `Stage14-s7-57`, `Stage14-4dn`, and `Stage14-t97`.  The latter three were initially inspected as advisory, but all are included as theorem sources only after their merge commits on current main.  There is no open related Stage14 PR at this freeze.

```text
UNMERGED_RELATED_STAGE14_RESULTS=NONE
```

The entering theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root saving is proved below.

---

## 1. Current physical receiver

Use the X15 quarter-pair variables

```text
D>A>0,
D,A=B^(1/4+o(1)),
gcd(D,A)=B^o(1),
```

and the rotated Stage14 pair

```text
m_s=D+A,
n_s=D-A.
```

The three physical Pythagorean projections are

```text
X_- = D^2-A^2 = m_s n_s = epsilon_- u_* R J,
X_0 = 2DA      = 2 alpha delta r s,
X_+ = D^2+A^2 = epsilon_+ C_* S T,

X_-^2+X_0^2=X_+^2.                                (1.1)
```

All endpoint, parity, squarefree-cell, primitive/gcd, reciprocal-completion, interval, root-orientation, and charged-once masks remain part of the packet.  After refining the divisor-many X15 weights into physical factorization cells, use bounded selectors on the conditioned cell.  The merged global decomposition is

```text
E[W_+W_-W_k]
 = mu_+mu_-mu_k
 + mu_k Gamma_{+-}
 + mu_- Gamma_{+k}
 + mu_+ Gamma_{-k}
 + Kappa_3.                                       (1.2)
```

Merged s7-54 permits one representative pair.  For `(+,-)`, merged s7-55 gives

```text
Gamma_{+-}=Delta_pair+Err_pair,                    (1.3)
```

where `Delta_pair` is the conditional principal joint-density defect and `Err_pair` is the masked centered inverse-fraction error.  Merged 4dm then makes the exact sign-sensitive recentering

```text
Gamma_{+-}=Z_pair+E_pair,
Z_pair=(1/C_*) Cov(A_+,W_-),
E_pair=Cov(A_+K_{rho_s},W_-),                     (1.4)
```

with `W_+=A_+R_{rho_s}` and `R_{rho_s}=1/C_*+K_{rho_s}`, where `rho_s` is the root in the rotated `(m_s,n_s)` coordinates.  This changes the allocation between the two s7-55 summands, not their sum.  Only `Z_pair^+`, `E_pair^+`, and `Kappa_3^+` obstruct an upper bound.

Indeed, in this fixed-root normalization, if

```text
c_pair:=E[A_+K_{rho_s}] mu_-,
```

then direct expansion gives

```text
Z_pair=Delta_pair+c_pair,
E_pair=Err_pair-c_pair.                           (1.5)
```

Thus no s7-55 mass is lost or duplicated.  Merged Work-bfX18 supplies the alternative exact view

```text
Gamma_{ij}=Var(W_i) Resp_{i->j},                  (1.6)
```

which is the same charged-once covariance and cannot be multiplied by (1.4) as another saving.  Merged s7-56 removes only the layers with fixed-power sparse `mu_{+-}`.  The live pair receiver is therefore full-conductor and jointly dense; neither piece in (1.4), nor the connected `Kappa_3` branch, is controlled there.

Merged 4dn specializes the positive zero-mode term further.  With `A=A_+`, `B=W_-`, `mu_A=EA`, and `nu_e=E[B|A=e]`,

```text
Z_pair^+
 = (1/C_*) mu_A(1-mu_A)(nu_1-nu_0)^+.            (1.7)
```

This is an exact conditional-uplift identity, not a multiplicative decomposition or a deficit.  Merged s7-57 additionally proves that exponent-zero positive covariance does not imply near-deterministic coupling.  Merged t97 makes one fixed-U orientation-bit influence an explicit Gaussian conjugate symmetric difference, but proves neither single-congruence localization nor fixed-power boundary sparsity.  None of these three later merges changes the adapter or exponent conclusion below.

---

## 2. Exact dictionary

To avoid the collision between the two papers' letters, write `(M,N)` for the Azevedo--Moreira Euclid parameters.  The exact algebraic dictionary is

| Azevedo--Moreira | Stage14 | Status |
|---|---|---|
| `M` | `D=(m_s+n_s)/2` | exact |
| `N` | `A=(m_s-n_s)/2` | exact |
| `P_x(M,N)=M^2-N^2` | `X_-=epsilon_-u_*RJ` | exact |
| `P_y(M,N)=2MN` | `X_0=2alpha delta r s` | exact |
| `P_z(M,N)=M^2+N^2` | `X_+=epsilon_+C_*ST` | exact |
| equation coefficients `a=b=c=1`, with `a=c` | the X15 cone | exact |
| `M>N>0` | `D>A>0` | exact |
| A--M/Gaussian norm root `rho_AM=M*N^(-1)` | Stage root `rho_s=m_s*n_s^(-1)` | exact Mobius bijection below |
| common multiplier `k` | `k_AM=1` for the raw identity (1.1) | exact; any `gcd(D,A)^2=B^o(1)` decoration stays inside the Stage variables, with no Folner average |
| paper grid `P_w^Q(M,N)=P_w(QM+1,QN)` | none | not the Stage14 conductor |
| paper's fixed `Q` / Folner `Q` | `q=C_*/gcd(h,C_*)` | **not** a dictionary entry |
| fixed phases `f_j in M` | hypothetical multiplicative expansion of physical masks | not constructed |
| `psi(f_j(kP_w))` Bohr acceptance | `W_+,W_-,W_k` exact physical indicators | not equivalent |
| average on `Delta_N` | conditioned dyadic primitive packet `Omega` | different measure |

For every odd component of `C_*`, both `rho_AM +/- 1` and `rho_s +/- 1` are units and

```text
rho_s  = (rho_AM+1)(rho_AM-1)^(-1),
rho_AM = (rho_s +1)(rho_s -1)^(-1).               (2.1)
```

The transform is an involution and carries roots of `-1` to roots of `-1`; hence it preserves the physical prime-by-prime orientation label without identifying the two coordinate ratios.  The exact match (1.1)--(2.1) is real and useful.  The averaging variables and selectors are not matched by that algebraic identity.

---

## 3. Original-paper assumption ledger

The relevant contracts in arXiv:2607.04903v1 are Theorems 1.10/1.12, the concentration Corollaries 2.8/2.10, the aperiodic vanishing Theorem 2.11 and Corollary 2.12, and the pretentious proofs in Theorems 4.3/4.4/4.6/4.8.

| Contract | Audit | Reason |
|---|---|---|
| Pythagorean polynomial triple with one irreducible norm and reducible legs | `VERIFIED` | `(P_x,P_y,P_z)=(X_-,X_0,X_+)` exactly. |
| perfect-square/Rado coefficient hypothesis | `VERIFIED` | `a=b=c=1`, hence `a=c`. |
| positivity cone | `VERIFIED` | `D>A>0`. |
| fixed finite family of unimodular completely multiplicative functions | `FAILED` | no fixed family represents the full selectors; the rational fixed-root adapter uses `phi(q)` moving ray characters. |
| `B^o(1)` number of multiplicative/Hecke phases | `UNVERIFIED_FULL_SELECTOR` | Section 4 proves a local `B^o(1)` Gaussian-ideal valuation expansion, but not one for all physical masks.  Staying inside the paper's rational residue-character class costs `B^(chi+o(1))` terms. |
| `B^o(1)` coefficient `L1` cost for the local projector | `VERIFIED_LOCALLY` | both the rational ray expansion and the fixed-valuation-stratum ideal expansion have `L1=1`. |
| fixed functions as the averaging scale tends to infinity | `FAILED` | the required characters and conductors move with `q=C_*=B^(chi+o(1))`. |
| fixed `Q` in the aperiodic theorem / permitted order of limits | `FAILED` | the physical full conductor grows with `B`; no uniform-in-`Q` rate is supplied. |
| multiplicative Folner average over common scale `k` | `FAILED` | Stage14 counts the primitive `k=1` packet (up to the frozen `B^o(1)` peel). |
| unweighted homogeneous convex region | `FAILED` | the conditioned measure retains squarefree allocations, gcd masks, root orientation, reciprocal masks, and charged-once selectors. |
| primitive and opposite-parity restriction | `UNVERIFIED` | Azevedo--Moreira does not impose the primitive Euclid conditions; no uniform Mobius adapter with all other masks is proved. |
| exact root orientation retained | `VERIFIED_LOCAL_IDEAL_MULTIPLICATIVE_ADAPTER_ONLY` | a Gaussian-prime valuation Fourier expansion retains it with divisor-many terms; the paper has no theorem for these ideal phases. |
| Hecke-multiplicative extension of the paper | `FAILED` | the paper's theorems are for completely multiplicative functions on `N`; no Gaussian-ideal/Hecke analogue is stated. |
| pair conditional response/uplift controlled after the 4dm split | `UNVERIFIED` | Work-bfX18 and 4dn prove exact alternative identities, not an arithmetic phase adapter; the views cannot be double charged. |
| fixed-U influential orientation bit transfers to the global selectors | `FAILED` | Work-bfX18 gives a no-cross-promotion witness; t97 only makes that fixed-U edge an explicit symmetric difference and proves no sparsity. |
| connected third cumulant controlled by a Gowers norm under the physical measure | `UNVERIFIED` | no generalized-von-Neumann inequality retaining the conditional masks is proved. |
| quantitative fixed-power aperiodic decay | `FAILED` | the source gives limiting vanishing, not `B^-delta`, and not uniformly in moving phases/conductor. |
| pretentious density deficit or signed anticorrelation | `FAILED` | the source proves positive recurrence/concentration in the structured case. |

Thus the exact polynomial dictionary does not satisfy the theorem's analytic contract.

---

## 4. Exact local expansions and the minimal obstruction

### 4.1 Prime-conductor model

First isolate the transparent local model

```text
p == 1 (mod 4),
```

and choose `iota mod p` with `iota^2=-1`.  On unit pairs `(M,N) mod p`, the A--M/Gaussian norm condition is

```text
p | M^2+N^2
iff M*N^(-1) in {iota,-iota}.                     (4.1)
```

For the complete group `X_p` of multiplicative characters modulo `p`, orthogonality gives the unique exact expansion

```text
1_{M == rho_AM N (mod p)}
 = 1/(p-1) sum_{chi in X_p}
     conjugate(chi(rho_AM)) chi(M) conjugate(chi(N)). (4.2)
```

Every coefficient in (4.2) is nonzero.  Hence retaining a **fixed root orientation** requires exactly

```text
M_oriented(p)=p-1                                (4.3)
```

multiplicative phases, with coefficient costs

```text
L1=1,
L2=(p-1)^(-1/2).                                  (4.4)
```

If the two roots are unioned before orientation is frozen, then

```text
1_{p | M^2+N^2}
 = 2/(p-1) sum_{chi(-1)=1}
     conjugate(chi(iota)) chi(M) conjugate(chi(N)). (4.5)
```

There are `(p-1)/2` nonzero even-character terms.  After subtracting the trivial-character mean `2/(p-1)`, the centered projector still has `(p-3)/2` nonzero terms and

```text
L1_centered=(p-3)/(p-1),
L2_centered=sqrt(2(p-3))/(p-1).                   (4.6)
```

The coefficients are unique because multiplicative characters form an orthogonal basis on `(Z/pZ)^*`.  Therefore no exact ray-character compression can use fewer nonzero basis phases.

### 4.2 Full physical scale

For a general fixed A--M root `rho_AM mod q`, obtained from the physical `rho_s` by (2.1), the same identity is

```text
1_{M == rho_AM N (mod q)}
 = 1/phi(q) sum_{chi in dual((Z/qZ)^*)}
     conjugate(chi(rho_AM)) chi(M) conjugate(chi(N)). (4.7)
```

All `phi(q)` coefficients are nonzero.  At the merged full-conductor endpoint,

```text
q=C_* B^o(1)=B^(chi+o(1)),
phi(q)=B^(chi+o(1)),                               (4.8)
```

so (4.7) has a fixed-power number of terms.  A rational Dirichlet or residue-ray-class expansion cannot remove this obstruction: on the local unit group it is the same delta function, whose character Fourier support is full.  The different valuation-phase route is treated next.

This proves a fixed-power rank obstruction **inside the rational residue/ray-character adapter compatible with the source's multiplicative-function category**.  It does not yet rule out ideal-multiplicative valuation phases.

```text
RATIONAL_RAY_CHARACTER_FIXED_ROOT_COMPRESSION=FAILED
RATIONAL_RAY_MINIMAL_ORIENTED_PHASE_COUNT=phi(q)=B^(chi+o(1))
MINIMAL_UNORIENTED_PRIME_PHASE_COUNT=(p-1)/2=B^(chi+o(1))
COEFFICIENT_L1_COST=1
RATIONAL_RAY_TERM_COUNT_BO1=false
```

### 4.3 A local fixed-valuation-stratum Gaussian-ideal adapter does exist

The merged packet makes the xi blocks `R,S,T,J` squarefree, but it does not replace the full common core `C_*` by a squarefree modulus.  Prime powers must therefore be retained.  Fix one normalized physical plus-factor valuation stratum and condition the already-allowed `B^o(1)` endpoint/cofactor-overlap decoration.  Write

```text
C_*=product_p p^(e_p),
E_p:=v_p(X_+)=v_p(epsilon_+ C_* S T)>=e_p
```

on the fixed stratum.  For each split `p|C_*`, the physical root chooses one of the conjugate Gaussian prime ideals `pi_p, conjugate(pi_p)`.  Since the primitive/unit condition prevents both conjugate ideals from dividing `M+iN`, the chosen orientation is the exact valuation condition

```text
v_{pi_p}(M+iN)=E_p,
v_{conjugate(pi_p)}(M+iN)=0,
```

with the conjugate alternative for the opposite root.  Using `E_p`, rather than merely `e_p`, retains any prime-power overlap with the remaining norm factors.  Those factors and the frozen overlap decoration stay in `A_+`; they are not silently discarded.

Put `L_p=E_p+1` and define the bounded ideal-multiplicative local phases

```text
lambda_{p,t}(a)
 := exp(2*pi*i*t*v_{pi_p}(a)/L_p),
0<=t<L_p.                                         (4.9)
```

Finite Fourier inversion on `0<=v_{pi_p}<=E_p` gives

```text
1_{v_{pi_p}(a)=E_p}
 = 1/L_p sum_{t=0}^{L_p-1}
     exp(-2*pi*i*t*E_p/L_p) lambda_{p,t}(a).       (4.10)
```

Multiplying (4.10) over the oriented Gaussian prime powers in this fixed valuation stratum gives exact phase count and coefficient cost

```text
M_ideal = product_{p|C_*}(E_p+1) <= tau(X_+),
L1_ideal=1.                                        (4.11)
```

Thus `M_ideal=B^o(1)` by the standard divisor bound.  Conjugate-prime valuations retain the root orientation.  This proves a subpolynomial Gaussian-ideal multiplicative expansion for the **local fixed-valuation-stratum divisibility/orientation part** of `W_+`.  The exact stratum is essential: using packet-wide maxima instead of the fixed physical exponents would not justify the divisor-bound cost.

When every selected exponent is `E_p=1`, (4.10) is the two-point Fourier/Walsh projector and (4.11) becomes the `2^omega(q)` squarefree formula recorded in merged Stage14-AM.  Thus (4.9)--(4.11) are a prime-power extension of that merged local adapter, with the precise scope restriction needed for the divisor bound.

The phases (4.9) are completely multiplicative on Gaussian principal ideals/elements.  They are **not** claimed here to satisfy the global idele-class/ray normalization of a Hecke Groessencharacter.  Consequently this is a local ideal-multiplicative adapter, while a genuine Hecke-character adapter remains unverified.

```text
LOCAL_GAUSSIAN_IDEAL_VALUATION_ADAPTER_PROVED=true
LOCAL_ADAPTER_SCOPE=FIXED_NORMALIZED_VALUATION_STRATUM_ONLY
MERGED_AM_SQUAREFREE_WALSH_EXTENDED_TO_PRIME_POWER_STRATA=true
LOCAL_ORIENTATION_PHASE_COUNT=Bo1
LOCAL_ORIENTATION_COEFFICIENT_L1=1
```

This does not complete the requested selector decomposition:

1. Azevedo--Moreira has no theorem for the phases (4.9), which live on oriented Gaussian ideals rather than on the rational side values `P_x,P_y,P_z`.
2. The prime set, exact exponents, conductors and phase family move with the physical valuation stratum and with `B`; the paper fixes one finite family before taking its limits.
3. The dyadic atomic allocation, cross-gcd, reciprocal completion, conditional root label, and charged-once coupling of `W_+,W_-,W_k` have not been assembled into one common phase system on the same measure.

Therefore the accurate decomposition ledger is

```text
W_PLUS_LOCAL_DIVISIBILITY_ORIENTATION_ADAPTER=PROVED_ON_FIXED_NORMALIZED_VALUATION_STRATUM
GENUINE_HECKE_CHARACTER_ADAPTER_PROVED=false
W_PLUS_FULL_PHYSICAL_PHASE_DECOMPOSITION=UNVERIFIED
W_MINUS_FULL_PHYSICAL_PHASE_DECOMPOSITION=UNVERIFIED
W_K_FULL_PHYSICAL_PHASE_DECOMPOSITION=UNVERIFIED
FULL_THREE_SELECTOR_BO1_PHASE_DECOMPOSITION=UNVERIFIED
```

The smallest **selector-level** obstruction is now precise: in the source variables, an oriented root is a delta function on the rational unit ratio and has full ray-character support `phi(q)`; compressing that mask to at most `tau(X_+)=B^o(1)` on a fixed valuation stratum uses valuations of the Gaussian linear factor `M+iN`, which is not one of the rational side values `P_x,P_y,P_z` covered by the theorem.  Thus orientation visibility itself forces either fixed-power in-category rank or an out-of-category Gaussian-ideal phase.  Either route also lacks uniform quantitative estimates, and the remaining physical masks are still unassembled.

The smallest **overall AM-transfer obstruction**, agreeing with merged Stage14-AM, occurs even earlier and survives if the orientation adapter is supplied for free:

```text
AM:      average the common multiplier k over a multiplicative Folner sequence;
Stage14: retain the primitive physical fibre k_AM=1 with its gcd masks.
```

The AM Folner sets eventually contain every fixed divisor and give no positive-density or quantitative projection to the single primitive fibre.  Hence

```text
MINIMAL_AM_TRANSFER_OBSTRUCTION=PRIMITIVE_K1_VS_MULTIPLICATIVE_FOLNER_K_AVERAGE
```

---

## 5. Conditional pair/cumulant adapter and coefficient cost

For clarity, suppose hypothetically that each physical selector had a valid expansion on the same conditioned measure,

```text
W_j=sum_{a<=M_j} c_{j,a} F_{j,a},
L_j=sum_a |c_{j,a}|,
j in {+,-,k}.                                     (5.1)
```

Then exact multilinearity would give

```text
Gamma_{ij}
 = sum_{a,b} c_{i,a}c_{j,b}
   ( E[F_{i,a}F_{j,b}]-E[F_{i,a}]E[F_{j,b}] ),    (5.2)

Kappa_3
 = sum_{a,b,c} c_{+,a}c_{-,b}c_{k,c}
   E[(F_{+,a}-EF_{+,a})
     (F_{-,b}-EF_{-,b})
     (F_{k,c}-EF_{k,c})].                         (5.3)
```

The coefficient costs would be at most `L_iL_j` and `L_+L_-L_k`.  Thus `B^o(1)` phase counts and `B^o(1)` `L1` costs would indeed be the correct adapter target.

Equations (4.2)--(4.8) show why that target is not met inside the paper's rational character category: the canonical full-conductor expansion has good `L1` cost but `B^(chi+o(1))` moving phases.  Equations (4.9)--(4.11) compress the local fixed-valuation orientation only by moving to Gaussian-ideal phases not covered by the paper.  Moreover (5.2)--(5.3) are expectations on the physical conditional measure, whereas Azevedo--Moreira's vanishing theorem is on its unweighted averaging scheme.  No source theorem identifies the two expectations.

Consequently

```text
PAIR_ZERO_MODE_COFACTOR_COVARIANCE_MULTIPLICATIVE_ADAPTER_PROVED=false
CENTERED_INVERSE_FRACTION_AM_ADAPTER_PROVED=false
CONNECTED_THIRD_CUMULANT_GOWERS_ADAPTER_PROVED=false
CONDITIONAL_RESPONSE_AM_ADAPTER_PROVED=false
ZERO_CENTERED_AND_RESPONSE_VIEWS_DOUBLE_CHARGED=false
```

---

## 6. Aperiodic/Gowers-uniform branch

Azevedo--Moreira Corollary 2.12 yields a limiting zero when its precise fixed-function, fixed-grid, unweighted hypotheses hold and at least one eligible phase is aperiodic.  It supplies no rate uniform in the phase, its conductor, or the number of phases.  Frantzikinakis--Host likewise supplies the higher-order structured/uniform architecture and limiting Gowers uniformity of aperiodic multiplicative functions, not the uniform fixed-power estimate required here.

Even under a hypothetical legal selector expansion, the imported conclusion would therefore be only

```text
B^(1/2) * o(1)=B^(1/2+o(1)),                      (6.1)
```

not `B^(1/2-delta)` for a fixed `delta>0`.

There is a stronger local warning: every rational character in the exact root projector (4.2) is a Dirichlet/ray character and hence lies in the **pretentious/structured** class.  The Gaussian-ideal phases (4.9) have no aperiodic/pretentious classification theorem in the cited source.  Thus the mandatory orientation mask supplies no legally controlled aperiodic term.

```text
APERIODIC_BRANCH_QUALITATIVE_VANISHING_AVAILABLE=true
APERIODIC_BRANCH_UNIFORM_IN_MOVING_CONDUCTOR=false
APERIODIC_BRANCH_FIXED_POWER_SAVING_PROVED=false
RATIONAL_ROOT_PROJECTOR_APERIODIC_PHASE_COUNT=0
IDEAL_PHASE_APERIODIC_CLASSIFICATION_AVAILABLE=false
```

---

## 7. Pretentious/structured branch

The structured branch cannot be discarded.  The trivial character in (4.5) is exactly the local principal density.  Merged s7-49/s7-50 give its charged-once ledger:

```text
ambient complete coordinate exponent : 1/2,
C_* support                            : +chi,
root-line density                      : -chi,
total                                  : 1/2.       (7.1)
```

Nontrivial Dirichlet characters in (4.2)--(4.5) are pretentious as well.  The pretentious part of Azevedo--Moreira is a positive recurrence/concentration theorem; it does not give a density deficit or a signed upper-bound cancellation.  Frantzikinakis--Mountakis independently confirms that pretentious multiplicative systems can sustain positive generalized-Pythagorean recurrence.

No merged Stage14 result proves that the full physical masks exclude the trivial/ray-character sector, force a fixed-power loss in `Z_pair` (equivalently in the positive conditional uplift), or make the structured contribution anticorrelate with the principal term.  Merged s7-56 proves only that `mu_{+-}=B^-delta` layers are cheap; its survivor has `mu_{+-}=B^-o(1)` and may still carry (7.1).  Work-bfX18/4dn are explicit identities, not multiplicative factorizations.  Merged s7-57 supplies the interior witness `a=b=1/2`, `p=3/8`, whose normalized positive covariance is `eta=1/2`: exponent-zero correlation can stay bounded away from deterministic equality.  Thus neither conditional normalization nor Bernoulli extremality removes the structured square-root sector.

```text
PRETENTIOUS_BRANCH_CAN_MAINTAIN_SQRT_SATURATION=true
PHYSICAL_PRETENTIOUS_CLASS_EMPTY_AT_SQRT=false
PHYSICAL_PRETENTIOUS_FIXED_POWER_DENSITY_DEFICIT_PROVED=false
PRETENTIOUS_SIGNED_ANTICORRELATION_PROVED=false
```

---

## 8. Exponent ledger

| Branch | Imported/current bound | New fixed `delta` from AM? |
|---|---:|---:|
| already-peeled conductor loss `d=B^lambda` | `1/2-lambda` | no; merged s7-50 |
| already-peeled sparse pair occupancy `mu_{+-}=B^-eta` | `1/2-eta` | no; merged s7-56 |
| hypothetical legal aperiodic term | `1/2+o(1)` via qualitative `o(1)` | `0` |
| rational full-conductor fixed-root ray-character family | `1/2+o(1)` | `0` |
| local fixed-valuation Gaussian-ideal adapter | no applicable source bound | `0` |
| pretentious/trivial principal sector | `1/2+o(1)` | `0` |
| dense positive `Z_pair` / conditional response (same branch) | `1/2+o(1)` | `0` |
| masked positive `E_pair`, connected positive `Kappa_3` union | `1/2+o(1)` | `0` |

Therefore

```text
AM_CERTIFIED_DELTA=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FINAL_EXPONENT_LEDGER=V(B)<<B^(1/2+o(1))
```

---

## 9. Final verdict and one next adapter lemma

The final transfer classification is

```text
FINAL_VERDICT=BLOCKED
DIRECT=false
NEAR_WITH_PROVED_ADAPTER=false
NEAR_ADAPTER_INCOMPLETE=false
BLOCKED=true
```

There is a genuine proved local fixed-valuation Gaussian-ideal multiplicative adapter, so the geometry is closer than a superficial analogy.  Nevertheless the **Azevedo--Moreira transfer** is `BLOCKED`: that adapter is outside the theorem (and is not yet a genuine Hecke-character theorem), the in-category rational adapter has fixed-power moving rank, the available vanishing is qualitative, and the structured trivial mode still carries exponent `1/2`.

The next task is narrowed to one bespoke statement, not another literature citation:

```text
PrimitivePhysicalHeckeAdapterLemma.
```

Required statement: uniformly for `1/6<=chi<=1/4`, `q=C_*=B^(chi+o(1))`, every fixed physical root, and every merged full-conductor/interior-dense/primitive/charged-once cell, first project the AM common-dilation average exactly to the primitive fibre `k_AM=1`; then express each centered physical selector `W_j-EW_j`, `j in {+,-,k}`, on one common conditional measure as at most `B^o(1)` bounded Gaussian Hecke-multiplicative phases with total coefficient `L1=B^o(1)`, retaining every range, parity, squarefree, gcd, reciprocal, root-orientation, and charged-once mask.  Equivalently, (5.2)--(5.3) must become legal identities for the full physical pair defects, centered inverse-fraction error, and connected third cumulant.

This is the minimum adapter because the primitive-radial quantifier mismatch remains even when the local orientation expansion is granted for free.  Proving it would still not supply the separate uniform fixed-power aperiodic estimate or eliminate the structured/trivial sector; it would only make those analytic questions legally posed on the physical packet.

No new auxiliary H is useful yet: no surveyed theorem states this physical collective dichotomy.

```text
STAGE14_AM1=COMPLETE_MERGED_AM_PRIME_POWER_ORIENTATION_ROOT_DICTIONARY_AND_RECENTERING_REFINEMENT
SOURCE_MAIN_SHA=31762e51ff1ea764a4dbc06fe91656f1a37aaafc
MERGED_AM_CONSUMED=true
MERGED_AM_OVERWRITTEN=false
MERGED_Q11_CONSUMED=true
MERGED_X15_CONSUMED=true
MERGED_WORK_BEX17_CONSUMED=true
MERGED_4DL_CONSUMED=true
MERGED_S7_55_CONSUMED=true
MERGED_S7_56_CONSUMED=true
MERGED_4DM_CONSUMED=true
MERGED_WORK_BFX18_CONSUMED=true
MERGED_T96_CONTEXT_CONSUMED=true
MERGED_T97_CONSUMED=true
MERGED_4DN_CONSUMED=true
MERGED_S7_57_CONSUMED=true
UNMERGED_RELATED_STAGE14_USED_AS_THEOREM_SOURCE=false
EXACT_PYTHAGOREAN_DICTIONARY_PROVED=true
ROTATED_ROOT_MOBIUS_DICTIONARY_PROVED=true
S7_55_TO_4DM_RECENTERING_TRANSFER_PROVED=true
LOCAL_GAUSSIAN_IDEAL_VALUATION_ADAPTER_PROVED=true
LOCAL_ADAPTER_SCOPE=FIXED_NORMALIZED_VALUATION_STRATUM_ONLY
MERGED_AM_SQUAREFREE_WALSH_EXTENDED_TO_PRIME_POWER_STRATA=true
LOCAL_ORIENTATION_PHASE_COUNT=Bo1
LOCAL_ORIENTATION_COEFFICIENT_L1=1
GENUINE_HECKE_CHARACTER_ADAPTER_PROVED=false
FULL_PHYSICAL_SELECTOR_BO1_PHASE_DECOMPOSITION_PROVED=false
MINIMAL_AM_TRANSFER_OBSTRUCTION=PRIMITIVE_K1_VS_MULTIPLICATIVE_FOLNER_K_AVERAGE
RATIONAL_RAY_FIXED_ROOT_CHARACTER_RANK_OBSTRUCTION_PROVED=true
RATIONAL_RAY_MINIMAL_ORIENTED_PHASE_COUNT=phi(q)=B^(chi+o(1))
COEFFICIENT_L1_COST=1
APERIODIC_BRANCH_FIXED_POWER_SAVING_PROVED=false
PRETENTIOUS_BRANCH_CAN_MAINTAIN_SQRT_SATURATION=true
PHYSICAL_PRETENTIOUS_FIXED_POWER_DENSITY_DEFICIT_PROVED=false
PRETENTIOUS_SIGNED_ANTICORRELATION_PROVED=false
AM_CERTIFIED_DELTA=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FINAL_VERDICT=BLOCKED
DIRECT=false
NEAR_WITH_PROVED_ADAPTER=false
NEAR_ADAPTER_INCOMPLETE=false
BLOCKED=true
NEXT_ADAPTER_LEMMA=PrimitivePhysicalHeckeAdapterLemma
AM_AUXILIARY_H_NEEDED=false
```

## External sources checked

- Azevedo--Moreira, arXiv:2607.04903v1: <https://arxiv.org/abs/2607.04903>
- Frantzikinakis--Host, arXiv:1403.0945v2: <https://arxiv.org/abs/1403.0945>
- Frantzikinakis--Mountakis, arXiv:2508.09778v2: <https://arxiv.org/abs/2508.09778>
