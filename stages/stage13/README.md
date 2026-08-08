# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids.

## Current review state

The R01 review found a genuine circularity in the old raw direction-neutrality argument and an under-derived fixed-modulus overlap step. Stage13-12aa/ab repaired the architecture and Stage13-12ac published the neutral R02 bundle.

R02 has now received three adversarial evaluations:

```text
Grok   = OPEN
Claude = REPAIRABLE
Qwen   = REPAIRABLE
```

All three agree that the R01 circularity was genuinely removed. Their remaining objections split into two groups:

1. quantitative `j=0` Wiener / curved-region / nonzero-harmonic closure;
2. the inert-prime positive-valuation tail and completeness of the local-state overlap refinement.

Stage13-12ad closes group 1 with explicit all-prime/all-harmonic estimates. Stage13-12ae closes group 2 with an exact inert local series and a complete valuation/residue state map.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_EXTERNAL_REVIEW_R02_GROK=OPEN
STAGE13_EXTERNAL_REVIEW_R02_CLAUDE=REPAIRABLE
STAGE13_EXTERNAL_REVIEW_R02_QWEN=REPAIRABLE

STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE

CLAUDE_R02_WEIGHTED_L1_UNIFORMITY=REPAIRED_BY_13_12AD
CLAUDE_R02_NONZERO_HARMONIC_LOWER_ORDER=REPAIRED_BY_13_12AD
GROK_QWEN_R02_CURVED_MIXED_TRANSFER=REPAIRED_BY_13_12AD

P_ADIC_POSITIVE_VALUATION_TAIL=REPAIRED_EXACTLY_BY_13_12AE
LOCAL_STATE_REFINEMENT_COMPLETENESS=REPAIRED_BY_13_12AE

STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
NEXT_STAGE13_TASK=Stage13-12af
```

Stage13 is deliberately **not** self-declared externally `CLOSED`.

## Immutable R02 snapshot

R02 remains frozen as the object actually reviewed:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

Post-R02 repair precedence is

```text
13-12ae/result.md
-> 13-12ad/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical main.md / audit assets
```

A fresh R03, not a mutation of R02, is the next review target.

## 13-12aa — non-circular common-factor architecture

The old 7jb presentation seeded the desired categorywise constants too early. 13-12aa instead derives

\[
A_q(B)\sim\Theta J_q B(\log B)^3
\]

with one unknown common `Theta`, and only afterwards uses the frozen Stage12 total theorem to determine

\[
\Theta=\frac{\kappa}{6\pi^2}.
\]

That removes the R01 circularity structurally.

## 13-12ad — quantitative analytic closure

Fix

\[
\delta=\frac18,\qquad\sigma=\frac58.
\]

For every split prime `q>=13` and every angular phase, 13-12ad proves coefficientwise

\[
\boxed{\|C_{\ell,q}-1\|_{5/8}\le529q^{-5/4}.}
\]

The finite prime `q=5` is separated. The proof also establishes all logarithmic moments needed by the mixed convolution and fixes

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order A = 48
```

with the explicit lower-order ledger

```text
small height                 O(B (log B)^(9/4))
small coordinate             O(B (log B)^(5/2))
mixed log shifts             O(B (log B)^2)
rectangle power tails        B (log B)^C exp(-c (log B)^(1/4))
curved boundary / mesh       O(B (log B)^(-5))
Vaaler excess                O(B (log B)^(-1))
all retained harmonics core  O(B (log B)^(-6))
```

so all are `o(B(log B)^3)`. This is the repair of the Grok/Claude/Qwen R02 objections concerning the mixed Wiener correction, curved-region transfer and nonzero harmonics.

Assets:

```text
stages/stage13/13-12ad/result.md
stages/stage13/scripts/13-12ad/j0_quantitative_closure_audit.py
stages/stage13/data/13-12ad/j0_quantitative_closure_audit_report.json
```

## 13-12ae — exact inert p-adic/local-state closure

For an inert prime

\[
p\equiv3\pmod4,
\]

write

\[
a=v_p(h),\quad b=v_p(r),\quad c=v_p(s).
\]

Primitivity forces `a=0`: if `p|h`, then `p|P,z`, while inertness applied to `x^2+y^2=P^2` forces `p|x,y`, contradicting `gcd(x,y,z)=1`.

Also `(r,s)=1` forces `min(b,c)=0`. Thus the complete allowed valuation states are only

```text
U    (0,0,0)
R_b  (0,b,0), b>=1
S_c  (0,0,c), c>=1
```

and no others.

The exact unrestricted inert local zero-mode series is therefore

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At the main point `Y=Z=1/p`,

\[
L_{p,0}(1,1,1)=\frac{p+1}{p-1}.
\]

The positive-valuation mass is exactly `2/(p-1)`, hence

\[
\boxed{
\frac{T_p^+}{L_{p,0}(1,1,1)}
=\frac{2}{p+1}\le\frac2p.
}
\]

So the previously unspecified absolute constant is explicitly

\[
\boxed{C_0=2.}
\]

On the unit state the exact accepted density is

\[
\alpha_p=\frac{p+1}{2(p-1)}.
\]

Every positive-valuation state is automatically accepted because `p|P` forces `x=y=0 mod p`, while `z` is a unit, so `x^2+z^2=z^2` is a nonzero square.

Therefore the **full** constrained inert local multiplier is

\[
\boxed{
\lambda_p
=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}.
}
\]

Thus

```text
lambda_3 = 1
lambda_7 = 3/4
lambda_p < 3/4 for every inert p>7
```

and the fixed-prime sieve may choose arbitrary distinct inert primes `p>=7`.

The local-state refinement is also made explicit: the unit outer parameter `u=s/r` bijects with the normalized hyperbola `D^2-Z^2=1`, the selected-face residue lies on `X^2+Y^2=1`, and fixed residue restrictions are transferred by fixed-conductor Dirichlet / Gaussian ray-class character orthogonality. `p` is fixed before `B->infinity`, so no growing-modulus uniformity is used. OE/EE is purely 2-adic and factors out at odd `p`.

Assets:

```text
stages/stage13/13-12ae/result.md
stages/stage13/scripts/13-12ae/inert_local_state_audit.py
stages/stage13/data/13-12ae/inert_local_state_audit_report.json
```

## R03 theorem candidate

Combining 13-12ad with the exact 13-12ae overlap factor gives the repaired candidate

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

The normalized candidate limit remains

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

The next step is Stage13-12af: synthesize a fresh neutral R03 single-file bundle, explicitly include the post-R02 repairs, restate the analytic `J_q=2I_q/pi` bridge rather than relying on a numerical check, and request new external review.

## Logical scope

Stage13 does not claim existence or nonexistence of a perfect cuboid, an explicit convergence threshold/rate, monotonicity of directional ratios, publication-grade peer review, or a certified enclosure for `kappa`. Stage12 R09 remains a declared frozen prior input.
