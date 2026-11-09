# Stage35EX row393 — parent-identifier classification and replay gates (2026-11-09)

**Latest verified source count:** 60 newly retained ancestor proof/adoption texts (initial 34 + 5 + 9 + 6 + 5 + 1), distinct from the older 24-text fidelity-check cohort. This is a count of retained documents, **not** mathematical independent new theorems. The first core inventory (56 claim nodes / ~55 primary bodies plus at least seven earlier parents) is not summed as distinct theorems. The exact denominator of required source texts is unknown; percentage complete is **not computable**.

The [source map](ACTIVE-ANCESTOR-SOURCE-MAP.json) enumerates paths, Drive IDs and Git blob SHA. The [dependency map](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md) distinguishes exact logical parents from historical or contextual citations. This file classifies the remaining explicit *identifier names*, not automatically the entire mathematical closure.

| Unmapped identifier | Classification and retained gate | Action for repository self-containment |
|---|---|---|
| `C160` | **Potentially load-bearing coefficient/gcd lemma**, cited by C185 on protected TOP. Multiple unrelated Drive sources carry C160 in their title. | Locate the exact author-side source giving the old gcd/first-entry step actually used by C185; verify scope and provenance; do **not** map by section number alone. |
| `EXTERNAL_BERCZES_THM2_1` | **External superelliptic height input** in [S252](proofs/active-ancestors/S252.md): Bérczes et al., *Explicit bounds for the solutions of superelliptic equations over number fields*, arXiv:2310.09704, Thm 2.1(i), Eq. (2.8). | Transcribe mathematical hypotheses, conventions for `H(f)`, `s` and `Q_S`, and the actual substitution, after checking the primary paper. Do not upload the copyrighted PDF as a substitute. The S252 historical assertion of PDF inspection is **not** a new independent re-check. |
| `EXTERNAL_FERMAT_QUARTIC` | **Classical theorem with a descent already written inside [S196](proofs/active-ancestors/S196.md)** for positive `x^4+y^4=z^2`; likely no separately copied parent body needed. | Review the descent and its domain independently before marking its **mathematical** gate PASS. No need to copy an unrelated historical proof. |
| `S230` | Historical independent *author-side* algebraic cross-check, **not** a hostile audit PASS. | Drive reference to [original S230](https://docs.google.com/document/d/1t2Mf1OgFhJnJkChv_zQTQfGFaLOyd0vMTtc-z6l_Cvo/edit) is enough unless a mathematical step currently uses an exclusive S230 lemma. S231 rederives selected necessary parts. |
| `S242` | Historical fixed-base example/diagnostic candidate. | Retain reference only until a later proof is shown to depend on its exact arithmetic certificate rather than an example. |
| `S250` | Local Legendre/order test possibly inherited and restated within [S251](proofs/active-ancestors/S251.md). | Verify the exact reused lemma and definitions in S251; if self-contained, map to S251 rather than copying duplicate S250. |
| `SECTION16_NONSQUARE` | **Likely load-bearing elementary arithmetic input** cited by [S194](proofs/active-ancestors/S194.md); distinguish the non-square/area-one result from the PLUS fourth-power theorem in S196. | Identify the exact Section16 proof or an equivalent complete GitHub-contained proof, then record the implication and assumptions; no unaudited logical substitution. |

### External paper still blocking a downstream source theorem

[row393 de la Maza Theorem 1 and immediate corollary](ROW393-PRIMARY-THEOREM-GATE.md) require primary-text verification of norm conventions, ideal-class hypotheses, and constants. Formal 181-dimensional quotient must not be conflated with the true Cl/2 dimension or with complete Selmer information.

### Minimal executable evidence checkpoint

- **S316:** [script, expected JSON and literal replay commands](proofs/active-ancestors/S316-replay/README.md) added. The script was actually run, and its **entire 5,384-byte output** matched the original expected JSON. This finite replay PASS does not certify the universal proof.
- **S308 / S193 / S197 / S223 / S225 / S226 / S252 / C185 and other actual calculator-dependent claims:** existing evidence must be deduplicated against [materials](../../materials/README.md), and only essential scripts, inputs, and expected outputs added. No new independent replay PASS is asserted for them here.
- **Original 24-body text fidelity:** historical `24/24` applies only to that cohort. It does not establish text/format/native-table fidelity for all 60 ancestor bodies.

Publication completion is **NOT_COMPLETE**, mathematical independent auditing **NOT_COMPLETE**, branch and downstream global exclusion credits **NOT_PROMOTED**. Research stops at row393; PR #1854 stays draft and unmerged. Google Drive operational files are not edited.
