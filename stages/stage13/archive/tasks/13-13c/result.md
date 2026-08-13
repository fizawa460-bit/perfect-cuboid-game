# Stage13-13c — result

> STATUS: `STAGE13_13C_COMPLETE_CANONICAL_PROOF_RESYNTHESIS`

## Decision

The Stage13 proof has been resynthesized into one canonical document:

```text
stages/stage13/13-13c/stage13-final-proof.md
```

The resynthesis preserves the exact theorem contract frozen by 13-13a and the minimal external-theorem boundary fixed by 13-13b.

```text
THEOREM_CHANGED=false
R03_REWRITTEN=false
STAGE12_R09_REOPENED=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
```

## Canonical proof order

The new proof no longer requires the reader to follow the historical repair sequence. Its logical chain is:

```text
definitions / exact inclusion-exclusion
  -> exact Stage12 factor-two projection bridge
  -> canonical chamber and Gelfand--Leray weights
  -> exact J_q = 2 I_q / pi bridge
  -> primitive j=0 local coefficient system
  -> uniform weighted-Wiener mixed correction
  -> special Perron/residue pole-order lemma
  -> curved zero-mode main + Vaaler/nonzero-harmonic error
  -> one common raw arithmetic constant Theta
  -> Stage12 total calibration of Theta
  -> exact inert-prime local state and character sum
  -> lambda_p = (p+5)/(2(p+1))
  -> fixed-S overlap squeeze
  -> exactly-one directional theorem.
```

## Frozen theorem reproduced

For `q in {ab,ac,bc}`,

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

The proof also reproduces

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8},
\qquad
J_q=\frac{2I_q}{\pi},
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3),
\]

and

\[
\lambda_p=\frac{p+5}{2(p+1)}
\qquad(p\equiv3\pmod4).
\]

Hence

\[
\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}.
\]

## Non-circularity lock

The proof explicitly preserves the required ordering:

```text
1. prove A_q(B) ~ Theta J_q B(log B)^3 with one q-independent Theta;
2. only then import Stage12 R09 total mass;
3. solve Theta = kappa/(6 pi^2);
4. derive A_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3.
```

Thus the Stage12 directional proportions are never assumed or used to manufacture direction-neutrality.

## External boundary lock

The canonical proof imports only:

```text
Stage12 R09 primitive-oriented total theorem
Dirichlet/Hecke analytic continuation + functional equation + polynomial strip/conductor growth
Vaaler periodic interval majorant/minorant
```

The historical general Selberg--Delange black box and Gaussian-Hecke zero-free region remain valid context, but are not required as final logical gates.

The special integer-pole-order Perron/residue step is written directly into the canonical proof.

## Uniformity and order-of-limits lock

The raw analytic choices remain

```text
H0=U=exp((log B)^(1/4))
eta=(log B)^(-8)
L=(log B)^4
A=48
```

and every displayed error is `o(B(log B)^3)`.

For the overlap squeeze the order is explicit:

```text
fix k and S_k
-> B -> infinity
-> take limsup
-> k -> infinity.
```

No modulus depending on `B` occurs.

## Supersession lock

The canonical proof does not depend on:

```text
Stage13-7jb old raw direction-neutrality proof
Stage13-7jf old fixed-prime overlap presentation
R01/R02 bundles as mathematical dependencies
finite-B directional fits as asymptotic proof
finite-field enumeration as proof of alpha_p
categorywise D_q/K_q numerical equality as proof of commonness
```

R03 remains immutable historical reviewed evidence.

## Handoff

The next stage is deterministic consistency/reproducibility auditing of the new canonical proof. It must verify constants and exact identities independently of prose and detect any stale superseded formula before R04 is generated.

```text
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
THEOREM_CHANGED=false
R03_REWRITTEN=false
CANONICAL_PROOF_PATH=stages/stage13/13-13c/stage13-final-proof.md
MINIMAL_EXTERNAL_BOUNDARY_PRESERVED=true
NEXT=13-13d
```
