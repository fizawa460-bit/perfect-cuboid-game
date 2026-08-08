# Stage13-13a — claim and dependency ledger

> STATUS: `STAGE13_13A_COMPLETE_CLAIM_DEPENDENCY_LEDGER`
>
> PURPOSE: freeze the exact Stage13 theorem statement and inventory every active proof dependency before canonical resynthesis.
>
> SCOPE: Stage13 R03 (`13-12af`) plus the post-review explicitness supplement (`13-12ag`), with Stage12 R09 treated only as a frozen upstream theorem input.

## 1. Source precedence and active proof boundary

The active mathematical chain is:

```text
Stage12 R09 frozen total theorem
        |
        v
13-12aa  non-circular raw j=0 common-factor architecture
        |
        v
13-12ad  quantitative Wiener / curved-region / harmonic closure
        |
        +-------------------+
        |                   |
        v                   v
13-12ae inert local states   13-12ag explicit coarea / character / theorem crosswalk
        |                   |
        +---------+---------+
                  v
13-12af R03 authoritative proof ordering
                  |
                  v
13-13c future canonical resynthesis
```

R03 itself explicitly gives the precedence

```text
13-12af/current-proof.md
-> 13-12ad/result.md
-> 13-12ae/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical main.md and audit assets
```

with the old `Stage13-7jb` raw direction-neutrality proof and `Stage13-7jf` fixed-prime overlap proof marked superseded.

Stage13-13a strengthens that rule for future resynthesis:

```text
ACTIVE_THEOREM_SOURCE = R03 + 13-12ag
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED = false
R03_IMMUTABLE = true
STAGE12_R09_REOPENED = false
```

Historical files may be cited for provenance or deterministic checks, but no theorem step in the final resynthesis may depend on an argument that R03 itself superseded.

---

## 2. Dependency classifications

Every entry below uses exactly one of the roadmap classes as its **primary** status:

```text
INTERNAL_PROOF
FROZEN_STAGE12_INPUT
STANDARD_EXTERNAL_THEOREM
FINITE_CHECK
REVIEW_RECORD
```

An internally proved claim may still invoke standard external analytic machinery; such secondary dependencies are recorded in the `Depends on` field and are the subject of Stage13-13b.

---

## 3. Frozen theorem statement

Unless a genuine defect is discovered and separately recorded, Stage13-13c must reproduce the following theorem unchanged.

For `q in {ab,ac,bc}`,

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3
}
\]

and

\[
\boxed{
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Here

\[
I_q=\int_{\mathcal R}w_q\,d\omega,
\qquad
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\},
\]

with

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}},
\]

and

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}}.
\]

The normalized direction vector is therefore

\[
\boxed{P_q=\frac{8I_q}{\pi^2}}
\]

with locked numerical validator

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

and ratio validator

```text
ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

The decimal values are validators only. The symbolic integral formulas are authoritative.

---

## 4. Claim ledger

### C01 — exact inclusion-exclusion for exactly-one counts

**Claim.** For distinct face labels `q,r,s`,

\[
N_q=A_q-O_{qr}-O_{qs}+T,
\]

and

\[
N_1=\sum_qA_q-2\sum_{q<r}O_{qr}+3T.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `stages/stage13/13-12af/current-proof.md`, §1
- Depends on: definitions only
- Status: exact finite identity; no asymptotic input

### C02 — exact Stage12/Stage13 factor-two projection bridge

**Claim.** Directionwise and in total,

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B),
\qquad
C_{\rm prim}(B)=2\sum_qA_q(B).
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §1; frozen bridge provenance in Stage13-3d / Stage13-8
- Depends on: Stage12/Stage13 object convention and projection multiplicity
- Status: exact finite representation identity
- Note: the factor `2` is not an asymptotic fit

### C03 — canonical chamber Gelfand--Leray weights

**Claim.** On `R={0<x<y<z} subset S^2`, the three directional weights are

\[
w_{ab}=1/\sqrt{x^2+y^2},\quad
w_{ac}=1/\sqrt{x^2+z^2},\quad
w_{bc}=1/\sqrt{y^2+z^2}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §2
- Depends on: Jacobian calculation for the two quadratic constraints
- Status: active

### C04 — chamber integral partition

**Claim.** With `I_q=int_R w_q dω`,

\[
I_{ab}+I_{ac}+I_{bc}=\pi^2/8.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §2 and Stage13 chamber geometry
- Depends on: chamber partition/coarea geometry
- Status: symbolic identity authoritative; decimals are checks

### C05 — analytic bridge between zero Fourier kernel and chamber integral

**Claim.** If `J_q` is the outer-angle zero-mode kernel integral, then

\[
\boxed{J_q=\frac{2I_q}{\pi}},
\qquad
\sum_qJ_q=\frac\pi4.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §3, expanded independently in `13-12ag` §1
- Depends on: explicit spherical coordinates, coarea/Fubini, `psi=2phi-pi/2`
- Status: active analytic derivation
- Supersedes: any wording that treats the earlier quadrature comparison as the proof

### C06 — non-circular raw common-factor form before Stage12 calibration

**Claim.** There exists one arithmetic constant `Theta>0`, independent of `q`, such that

\[
A_q(B)\sim\Theta J_qB(\log B)^3.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12aa`, with quantitative closure by `13-12ad`; summarized in R03 §§4--6
- Depends on: primitive `j=0` Euler-factor system, weighted mixed correction, zero-mode pole structure, curved-region transfer, nonzero-harmonic lower order
- Standard external dependency: finite-order Selberg--Delange/Tauberian and Gaussian-Hecke zero-free input
- Status: active and explicitly obtained **before** use of Stage12 total mass
- Supersedes: old `7jb` categorywise constant check

### C07 — primitive split-prime local `j=0` coefficient system

**Claim.** For split primes the primitive local subtraction gives the `Z_0` and `Z_ell` coefficient systems in `13-12aa`, with pure-axis factors having zero-mode pole pattern `(1,2,2)` and nonzero harmonics losing the `h`-axis zeta pole.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12aa` §§1--3
- Depends on: Gaussian representation formulas and primitive support subtraction
- Status: active local algebra

### C08 — quantitative weighted-Wiener mixed correction

**Claim.** For every split prime `p>=13` and every retained angular phase,

\[
\boxed{\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ad` §§2--5; R03 §5
- Depends on: explicit coefficientwise Wiener norm estimates
- Status: active; `p=5` is separated as a finite factor

### C09 — logarithmic moments of the global correction

**Claim.** For each fixed `m`,

\[
\sum_{u,v,w}\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty
\]

uniformly over retained harmonics.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ad` §6; R03 §5
- Depends on: C08 and elementary comparison of logarithms with `(uvw)^{3/8}`
- Status: active; controls anisotropic convolution log shifts

### C10 — curved-region and harmonic remainder is lower order

**Claim.** With the frozen choices

```text
H0=U=exp((log B)^(1/4))
eta=(log B)^(-8)
L=(log B)^4
A=48
```

all small-height, wing, mesh/boundary, Vaaler and retained nonzero-harmonic errors are `o(B(log B)^3)`.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ad` §§7 onward; R03 §6
- Depends on: C08--C09 plus standard finite-order analytic inputs
- Status: active quantitative error ledger

### C11 — OE/EE parity split is a finite 2-adic radial variant only

**Claim.** The OE/EE branches alter only finite 2-adic radial constants and do not introduce a direction-dependent odd-prime leading factor.

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §6.1, with inherited parameterization from Stage12/earlier Stage13
- Depends on: locked parity parameterization and branchwise analytic estimates
- Status: active; exact external-hypothesis mapping deferred to 13-13b

### C12 — frozen Stage12 R09 total theorem

**Claim imported from Stage12.**

\[
\boxed{
C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3
}
\]

for the Stage12 bundle-defined primitive oriented count.

- Primary class: `FROZEN_STAGE12_INPUT`
- Source: Stage12 R09 freeze, merge commit recorded by PR #84
- Frozen scope: total primitive oriented count only
- Additional frozen ledger: `eta=pi*kappa`
- Status: Stage13-13a does not reopen its proof

### C13 — calibration of `Theta` after commonness is proved

**Claim.** Using C02, C05, C06 and C12 only after C06 is established,

\[
\boxed{\Theta=\frac{\kappa}{6\pi^2}}
\]

and therefore

\[
\boxed{A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 §7; `13-12aa` §6
- Depends on: C02, C05, C06, C12
- Status: active and non-circular by ordering

### C14 — inert-prime scale valuation is zero by primitivity

**Claim.** For every inert odd prime `p=3 mod 4`, in the outer variables

\[
a=v_p(h)=0.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §2; R03 §8
- Depends on: inertness of `-1`, primitive cuboid gcd
- Status: active exact local fact

### C15 — complete inert valuation state table

**Claim.** With `(r,s)=1`, the only primitive inert-prime valuation states are

```text
U   = (0,0,0)
R_b = (0,b,0), b>=1
S_c = (0,0,c), c>=1
```

and the positive-base-valuation states automatically pass the tagged second-face residue condition.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §3
- Depends on: C14 and coprimality `(r,s)=1`
- Status: active and exhaustive

### C16 — exact unrestricted inert local series and positive-valuation mass

**Claim.** At `Y=Z=1/p`,

\[
L_{p,0}(1,1,1)=\frac{p+1}{p-1},
\qquad
T_p^+=\frac2{p-1},
\]

so

\[
\boxed{\frac{T_p^+}{L_{p,0}(1,1,1)}=\frac2{p+1}\le\frac2p}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §4; R03 §8
- Depends on: C15
- Status: active; fixes absolute constant `C0=2`

### C17 — exact unit-state acceptance at inert primes

**Claim.** The unit-state acceptance for the tagged second-face square condition is

\[
\boxed{\alpha_p=\frac{p+1}{2(p-1)}}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §5; explicit symbolic character-sum derivation in `13-12ag` §2
- Depends on: finite-field circle/hyperbola counts and quadratic character identities
- Status: active; finite enumeration is validator only

### C18 — exact constrained inert local multiplier

**Claim.**

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}
\]

and for inert `p>=7`,

\[
\lambda_p\le3/4.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §7
- Depends on: C16 and C17
- Status: active; supersedes the softer `13-12ab` `1/2+O(1/p)` bound

### C19 — fixed-prime residue-state transfer

**Claim.** For a fixed finite set `S` of primes, adjoining the finite local residue predicates changes only finitely many Euler factors; the leading zero-mode constant is multiplied by the product of local acceptances, while nonprincipal fixed-conductor character combinations remain lower order.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ab` §2, sharpened/completed in `13-12ae` §6
- Depends on: fixed-conductor character orthogonality, CRT, the same Selberg--Delange/Hecke theorem boundary as the raw proof
- Standard external dependency: fixed-conductor analytic estimates
- Status: active; **order is fixed `S`, then `B->infinity`**

### C20 — pair-overlap fixed-set squeeze

**Claim.** For each pair overlap,

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ae` §§8--9; R03 later overlap sections
- Depends on: C18, C19, tagged injection, and order of limits `B->infinity` before `k->infinity`
- Status: active; no modulus grows with `B`

### C21 — triple overlap is lower order

**Claim.**

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ab` §4 / `13-12ae` fixed-set closure / R03
- Depends on: C20 and the exact inclusion `T subset O_{qr}`
- Status: active; no perfect-cuboid nonexistence assumption

### C22 — exactly-one directional theorem

**Claim.**

\[
\boxed{N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 theorem synthesis; `13-12ab` §5 after repairs
- Depends on: C01, C13, C20, C21
- Status: **frozen theorem statement for 13-13c**

### C23 — exactly-one total theorem

**Claim.**

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 theorem synthesis
- Depends on: C01, C04, C13, C20, C21
- Status: **frozen theorem statement for 13-13c**

### C24 — normalized directional limit

**Claim.**

\[
\boxed{\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}}.
\]

- Primary class: `INTERNAL_PROOF`
- Active source: R03 / Stage13 roadmap theorem candidate
- Depends on: C04, C22, C23
- Status: symbolic formula frozen; decimal vector only a validator

### C25 — finite numerical chamber/integral checks

**Claim type.** Numerical quadrature and finite census reproduce the symbolic chamber constants, direction vector and exact bridge identities at audited cutoffs.

- Primary class: `FINITE_CHECK`
- Sources: Stage13-3/7/8 audit assets and roadmap summaries
- Depends on: deterministic scripts/data
- Status: validation only; never used to prove the asymptotic theorem

### C26 — standard finite-order Selberg--Delange/Tauberian input

**Imported statement class.** The zero-mode one-variable Dirichlet factors with their locked pole orders admit the finite-order summatory expansions and remainders used in `13-12ad`.

- Primary class: `STANDARD_EXTERNAL_THEOREM`
- Active source of use: `13-12ad` §7 and `13-12ag` §3 crosswalk
- Exact bibliographic theorem/hypothesis mapping: **deferred to 13-13b**
- Status: mapped dependency, not internally reproved

### C27 — Gaussian-Hecke zero-free / harmonic cancellation input

**Imported statement class.** Nonzero angular characters in the retained range `ell<=(log B)^4` have sufficient uniform cancellation to make the complete retained harmonic contribution lower order.

- Primary class: `STANDARD_EXTERNAL_THEOREM`
- Active source of use: `13-12ad`, R03 §6, `13-12ag` §3
- Exact source/hypotheses/conductor bounds: **deferred to 13-13b**
- Status: mapped dependency, not internally reproved

### C28 — fixed-conductor character orthogonality / CRT transfer

**Imported statement class.** For each fixed local set, residue restrictions can be decomposed into fixed-conductor character combinations and tensor across primes by CRT; principal terms preserve the pole structure and nonprincipal terms are controlled by the same analytic framework.

- Primary class: `STANDARD_EXTERNAL_THEOREM`
- Active source of use: `13-12ab` §2 and `13-12ae` §6
- Exact source/hypothesis map: **deferred to 13-13b**
- Status: mapped dependency

### C29 — R03 reviewer records

**Record.** Supplied project records state:

```text
Grok R03  = CLOSED
Qwen R03  = CLOSED
Claude R03 = not recorded
```

- Primary class: `REVIEW_RECORD`
- Source: Stage13 roadmap and `13-12ag` header
- Status: review evidence only; not mathematical proof

### C30 — no perfect-cuboid nonexistence assumption

**Claim about scope.** The pair/triple lower-order argument and exactly-one asymptotic do not assume that a perfect cuboid does not exist.

- Primary class: `INTERNAL_PROOF`
- Active source: `13-12ab`, `13-12ae`, R03 scope statements
- Depends on: overlap estimates rather than setting `T=0`
- Status: active scope lock

---

## 5. Drift and duplication audit

### D01 — R03 status header is stale bookkeeping

`13-12af/current-proof.md` still carries the historical header

```text
STATUS: PENDING_EXTERNAL_R03
```

while the later project record has Grok and Qwen `CLOSED` on R03.

Classification:

```text
MATHEMATICAL_DEFECT=false
BOOKKEEPING_DRIFT=true
```

Action: do not mutate R03. The future canonical proof/freeze files will carry the current review state.

### D02 — `J_q=2I_q/pi` proof source drift

`13-12aa` says Stage13-7j “independently checked” the bridge. R03 and `13-12ag` now contain the explicit analytic derivation.

Classification:

```text
THEOREM_CHANGED=false
PREFERRED_FINAL_SOURCE=13-12ag explicit derivation
NUMERICAL_QUADRATURE_ROLE=validator_only
```

### D03 — inert local multiplier was sharpened after 13-12ab

`13-12ab` proves only

\[
\lambda_p\le1/2+O(1/p)
\]

through a soft positive-valuation tail. `13-12ae` replaces it with the exact formula

\[
\lambda_p=(p+5)/(2(p+1)).
\]

Classification:

```text
13_12AB_SOFT_BOUND=historical_intermediate
13_12AE_EXACT_FORMULA=active
THEOREM_CHANGED=false
```

### D04 — character-sum proof was expanded after R03

R03/12ae state the exact unit acceptance. `13-12ag` supplies the full symbolic decomposition

```text
S0=0
S1=p-1
S2=p+1
S3=-2
```

and hence `(p+1)^2/2` accepted unit states.

Classification:

```text
R03_RESULT=unchanged
13_12AG_ROLE=proof_explicitness
FINAL_RESYNTHESIS_SHOULD_INLINE_13_12AG_DERIVATION=true
```

### D05 — external theorem boundary is identified but not yet publication-grade

R03/12ad/12ag clearly identify the standard finite-order Selberg--Delange/Tauberian and Gaussian-Hecke zero-free inputs, but the exact theorem/source/hypothesis table is intentionally assigned to `13-13b`.

Classification:

```text
UNMAPPED_DEPENDENCY_FOUND=false
FULL_HYPOTHESIS_CROSSWALK_COMPLETE=false
NEXT_STAGE=13-13b
```

This is not a 13-13a blocker because every external dependency has been located; 13-13b exists specifically to audit its precise hypotheses.

---

## 6. Superseded arguments explicitly excluded

The following historical proof routes are **not required** by the active theorem chain:

```text
Stage13-7jb old raw direction-neutrality proof
Stage13-7jf old fixed-prime overlap proof
R01 proof bundle as a mathematical dependency
R02 proof bundle as a mathematical dependency
supported_richness_raw_asymptotic.py categorywise D_q/K_q equality as proof
finite-field enumeration as proof of alpha_p
finite B directional fits as proof of limiting proportions
```

They remain provenance, diagnostics, or review history only.

Therefore

```text
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
```

is locked for Stage13-13a.

---

## 7. Frozen resynthesis contract for 13-13c

Unless 13-13b discovers a genuine theorem-level failure of an external hypothesis, Stage13-13c must preserve all of the following exactly:

```text
COUNTING_CONVENTION=primitive canonical exactly-one-face count with integer space diagonal
STAGE12_INPUT=C_prim(B) ~ kappa/(12*pi) B(log B)^3
RAW_DIRECTIONAL=A_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
PAIR_OVERLAP=O_qr(B)=o(B(log B)^3)
TRIPLE_OVERLAP=T(B)=o(B(log B)^3)
EXACT_ONE_DIRECTIONAL=N_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
EXACT_ONE_TOTAL=N1(B) ~ kappa/(24*pi) B(log B)^3
DIRECTION_LIMIT=P_q=8*I_q/pi^2
CHAMBER_SUM=sum I_q=pi^2/8
JQ_BRIDGE=J_q=2*I_q/pi
INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2*(p+1))
NO_PERFECT_CUBOID_NONEXISTENCE_ASSUMPTION=true
```

The decimal direction vector is retained only as a deterministic validator of the symbolic formulas.

---

## 8. Stage13-13a decision

No theorem-level contradiction was found while inventorying the active R03 + `13-12ag` chain. The only discrepancies found are provenance/bookkeeping drift or later explicit sharpening of an unchanged theorem.

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
CLAIM_COUNT=30
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
THEOREM_LEVEL_DEFECT_FOUND=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
EXTERNAL_DEPENDENCY_CATEGORIES_IDENTIFIED=true
FULL_EXTERNAL_HYPOTHESIS_AUDIT_DEFERRED_TO_13_13B=true
R03_IMMUTABLE=true
STAGE12_R09_REOPENED=false
NEXT=13-13b
```
