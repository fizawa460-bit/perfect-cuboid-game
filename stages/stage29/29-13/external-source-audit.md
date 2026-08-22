# Stage29-13 external source audit — 2026 family/method inputs

## Provenance lock

Primary external repository:

```text
https://github.com/weiqi-kids/perfect-cuboid-problem
```

Source set author: Lightman Chang. These sources are self-hosted 2026 preprints and are not accepted merely by citation. 29-13 uses exact source text plus independent algebra/database checks.

## Paper A — Saunderson

Source files:

```text
paper-a/paper.tex
blob sha 6a4106f553094e88e557d614b2d0b2a6ff668c71
paper-a/paper.pdf
blob sha 048664ee165a168c0a8cfd9854a7b0ab836f406d
```

Load-bearing source locations in `paper.tex`:

- Lemma `lem:body`: `a^2+b^2+c^2=w^2(w^4+16u^2v^2)`;
- Lemma `lem:octic`: exact degree-eight curve after `(u,v,w)=(p^2-q^2,2pq,p^2+q^2)`;
- Lemma `lem:palindrome`: `W=t+1/t` reduction;
- Lemma `lem:lift`: exact converse rational-lift condition `W^2-4=T0^2`;
- Proposition `prop:C0`: every nondegenerate perfect Saunderson brick gives a nonzero finite rational `T0` on `C0`;
- Propositions `prop:jac`, `prop:C0pts`: Jacobian `80a1`, rank zero, four rational points;
- Theorem `thm:main`: family exclusion and degeneracy reconstruction.

Independent checks performed for 29-13:

1. symbolic expansion of the body-diagonal identity gives exact zero;
2. substitution `p=tq` gives exactly
   `t^8+68t^6-122t^4+68t^2+1`;
3. the palindrome and lift substitutions give exactly
   `C0: S^2=T0^4+72T0^2+16`;
4. LMFDB Cremona `80a1` / LMFDB `80.a2` records conductor 80, rank 0, torsion `Z/2 x Z/2`, simplified model `y^2=x^3-7x+6`;
5. `C0` visibly has the four points `(0,±4), infinity_±`; rank-zero Jacobian cardinality four makes this list complete;
6. `T0=0` and `T0=infinity` reconstruct only vanishing-edge Pythagorean parameters.

Verdict:

```text
R29-EXT-CHANG-A=DISCHARGED_INDEPENDENTLY_RECONSTRUCTED
```

Source-quality caveat retained: the introduction incorrectly calls `(240,252,275)` the smallest Euler brick. This historical error is not load-bearing for the proof.

## Paper B — Case B p=1

Source file:

```text
paper-b/paper.tex
blob sha e461b01da3642c4e9fd470d352b58198d00c31e0
```

Load-bearing source locations:

- Definition `def:caseB`;
- Lemma `lem:faces`;
- Lemma `lem:pell`;
- Lemma `lem:lucas`;
- Theorem `thm:main`.

Independent checks performed for 29-13:

1. exact expansion verifies the four polynomial identities in Lemma `lem:faces`;
2. the space condition reduces exactly to `g^2-5Y^2=20`, `Y=q^2`;
3. `5|g`, hence `Y^2-5h^2=-4` after `g=5h`;
4. the classical negative-Pell parametrization gives `Y=L_{2n-1}`;
5. classical Lucas-square results of Cohn imply the only square Lucas values in this sequence are `1` and `4`;
6. these give `q=1,2`, both degenerate.

Verdict:

```text
R29-EXT-CHANG-B=DISCHARGED_PELL_LUCAS_FAMILY_EXCLUSION
```

Source-quality caveat retained: an introductory sentence says the three face conditions hold identically; the formal Lemma correctly shows only two are automatic. The exclusion proof needs only the necessary space condition, so the error does not enter the theorem.

The paper's genus-five Jacobian decomposition is outside the load-bearing closure proof and is not imported in 29-13.

## Paper C — rank-positive fibers

The source and its public explanatory page explicitly restrict the proved computation to finite coefficient windows and state that the all-multiples extension is conjectural. 29-13 therefore preserves:

```text
R29-EXT-CHANG-C=FINITE_WINDOW_COMPUTATIONAL_INPUT_ONLY
GLOBAL_FIBER_CLOSURE_CERTIFIED=false
```

No finite computation is promoted to a universal rank-positive-fiber theorem.

## Paper D — Szpiro/height

The source explicitly does not claim PCP closure and records the absence of the uniform canonical-height lower bound needed for an elementary global closure. 29-13 retains it only as possible later Arsenal input:

```text
R29-EXT-CHANG-D=AMBER_HEIGHT_STRUCTURE_INPUT_NOT_ENDPOINT_DECISIVE
```

## Paper E — Sophie--Germain prime subfamily

Source file:

```text
paper-e/paper.tex
blob sha 1ff42f5a657ab9edafcfd6060f015a19e4322a83
```

The source identifies

```text
Eanom: y^2=x^3-275x+1750
Cremona 800a3 / LMFDB 800.d2.
```

Independent LMFDB data agree with rank `1`, torsion `Z/2`, and an integral-point count of `7` for the elliptic curve.

However the theorem proof itself states:

- the height-difference bound `mu<=2.93` is sampled rather than proved;
- a rigorous `IntegralPoints` certificate would require Magma/Sage or an elliptic-logarithm implementation not run in the reported workflow;
- the text nevertheless *takes* the seven points as complete;
- the proof does not provide, in the load-bearing step, a source-locked explicit integrality-preserving map proving that every integral quartic point maps into exactly the integral points being enumerated on `Eanom`.

Thus the external theorem is not certified as written. LMFDB's elliptic integral-point count is valuable evidence but does not by itself supply the missing quartic integrality/reconstruction adapter.

```text
R29-EXT-CHANG-E=NOT_CERTIFIED_MISSING_RIGOROUS_INTEGRAL_POINT_TRANSFER_AND_COMPLETENESS_CERTIFICATE
```

Repair contract:

```text
1. explicit quartic <-> elliptic birational maps;
2. proof of the required integrality implication;
3. complete IntegralPoints / elliptic-logarithm certificate;
4. exact pullback and cuboid reconstruction ledger.
```

## External import summary

```text
CERTIFIED_EXTERNAL_FAMILY_CLOSURES=2
  A Saunderson
  B Case-B p=1

FINITE_ONLY=1
  C

STRUCTURAL_NONDECISIVE=1
  D

NOT_CERTIFIED_AS_WRITTEN=1
  E

NEW_PRIMARY_ROUTE_CREATED=false
GENERAL_PERFECT_CUBOID_NONEXISTENCE=false
```
