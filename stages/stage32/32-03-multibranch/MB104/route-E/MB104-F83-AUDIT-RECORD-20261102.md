# F83 audit record (2026-11-02)

This file records the external audit of F83 and the notes required by it. **The F83 note itself is kept verbatim**,
byte-identical to the Drive deliverable (file id `1yzURAYgREkQj-UyLPfe-HmlSPj0Nor6s`, same bytes as in the ZIP
`1jJ4aVtUa55cPHU73MaxKYPdPqjruAGfW`). Credit stays 0.

## Files

| File | SHA-256 |
|---|---|
| `MB104-F83-ELLIPTIC-COIMAGE-TORSION-OBSTRUCTION-20261102.md` (research note, by ChatGPT) | `d15944077a964494f28cb9c7f5d1c00a60899687376691d03aed330ea6c9e823` |
| `mb104_f74_f75_window.py` (verifier) | `aee656f8bb44b1fa52a38f666968d114581eaade1d2a086abaaf1fdd959fa0b3` |

Reproduction: `python -I -O mb104_f74_f75_window.py` prints the 10 rows and ends with
`PASS: exact integer arithmetic and expected certificates match`, exit 0. Checked locally on 2026-11-02.

## Audit verdict (integrated audit of F69–F83, audited commit `33ef9d16`)

| Item | Verdict |
|---|---|
| F83 Prop 3.1: the elliptic co-image layer (Y_s of genus 1), for (g,k) ∈ {0,1}×{4,8}: no MB101 carrier with ε > 0 | **limited PASS**, relying on the audited parts of F70–F74 |
| F83 Lemmas 2.1–2.4: E_s has CM by Z[i], B_s = P + E_s[(1+i)³], primitive Gaussian parametrization, \|T₁∩T₂\| ∈ {0, 8} | PASS |
| F83 Prop 4.1: k = 8 ⇒ γ odd and δ_img even, so k = 8, γ = 2 is impossible, also when B_s > 0 | PASS |
| F83 Prop 4.2: Hermitian type, a_i ≥ 2, Δ ≥ 1, and k = 8 parities | PASS (necessary conditions only) |
| F83 §5: the 10 F75 numerical windows | PASS as an integer count (independent recount agrees). Not a curve count, existence result or exclusion |
| F72, F73 | PASS |
| F70, F71, F74 | limited PASS (F70 §5 and F71's large windows depend on F69) |
| F69 analytic bound d ≤ 196416 | HOLD (external-theorem hypotheses not checked by this auditor) |
| MB104 | OPEN |

Must-fix: none. Verifiers verify_f69 … verify_f73 and `mb104_f74_f75_window.py` passed with and without `-O`.

The auditor specifically confirmed that the MB101 multi-branch condition ⇒ I > 0 is **proved** in F74 §6, by
classifying the node branches and using that elliptic subgroup translates do not intersect. It is not assumed.

## Should-fix notes (applied here, without editing the F83 text)

- **SF-1.** F74's h = 4 relies on F72 (étale legs ⇒ ε = 0).
- **SF-2.** "MB101 multi-branch ⇒ I > 0" holds only within F74's elliptic co-image layer and its node classification. It must not be transferred to co-images of higher genus.
- **SF-3.** The numerical enumeration of F83 §5 depends on F75's B_s = 0 windows, which are not fully audited, and counts necessary numerical classes only.

## Relation to route E (E01–E04)

- The F69 HOLD no longer matters for the population.
  - E01 proves directly that C8's group is the principal congruence subgroup PQ¹_B(2). The LMR Def 4.1 and Thm 4.3/4.4 hypotheses were checked against the primary source, and E01 is audited.
  - E01–E04 replace F69's conditional window by the exact statement: the equality face holds only the 80 known curves.
- F83 Prop 3.1 removes F74's window (d ≤ 36) from the ε > 0 cascade. That layer is empty.
