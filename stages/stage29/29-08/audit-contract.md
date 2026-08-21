# Stage29-08 — fresh adversarial audit contract

Audit this submission from `main` plus the PR diff. Do not treat Stage29-08 conclusions as premises.

Required attacks:

1. Independently derive the Peschmann crosswalk from the published edge formulas and verify
   `Master/e^2=f_face` and `H-total/e^2=f_sp` with the exact Stage29-07 choice of shared edge and ratios.
2. Verify that the crosswalk proves Peschmann is an adapted chart of the existing two-face/joint-V4 architecture rather than a ninth independent endpoint surface. Do not infer redundancy of its arithmetic tools.
3. Re-read the 2026 Peschmann source sequence. In particular attack the conflict between the `2604.28072` abstract coverage wording and the later `2605.00573` explicit non-converse statement. Do not certify global Euler-brick coverage unless hypotheses/definitions/versions are reconciled exactly.
4. Verify the genus-3 route direction: endpoint/brick -> rational point is safe; specialized converse must retain its stated square-factor caveat where the source does.
5. Verify that the May `H_mn` quartic is exactly the Master/third-face marginal equation, not the full endpoint. Check the `tau(P)=t^2` lift semantics and exceptional/torsion points.
6. Verify that the exponent-one blocker remains conjectural and finite-verified only. No finite database may become a theorem or density result.
7. Attack `R29-K1` independently: quotient the endpoint by the long-diagonal sign, compare the resulting P5 Euler model to Stage20 `X_face`, and check normal model, resolution, field Q, and physical polarization. Matching `h32` alone is not acceptable proof.
8. Verify the analogous Stage19/K_b model remark is not overgeneralized across the whole three-element orbit.
9. Recheck Saunderson: Stage20 M-degree 6, nonsplit endpoint lift, endpoint canonical degree 12, genus 3; no global coverage promotion.
10. Recheck StageA2 scope: one specific family only.
11. Check Testa--Stoll 28 genus-5 fibrations and 15 Euler-K3 elliptic fibrations for exact field/model wording. Geometric fibration coverage is not rational-section coverage.
12. Reconcile every new receiver with `stages/stage29/29-05/route-registry.json`; no twelfth attack route may be created merely by adding Peschmann receivers.
13. Verify no Stage16--28 backflow, perfect-cuboid existence/nonexistence theorem, or asymptotic transfer is silently introduced.
14. If `R29-K1` or Peschmann coverage needs repair, bounded repair is preferred over forcing a roadmap rewrite unless a materiality certificate is genuinely present.

Expected receiver decisions to audit:

```text
R29-PESCH1 = DISCHARGED or REPAIR/OPEN
R29-PESCH-COV = OPEN unless exact source reconciliation closes it
R29-PESCH2 = OPEN_BOUNDED or exact matched fibration if actually proved
R29-PESCH-E1 = AMBER_CONJECTURAL
R29-K1 = DISCHARGED or REPAIR/OPEN
R29-FIB1 = OPEN
R29-FIB2 = OPEN
```

Allowed final verdicts:

```text
PASS
PASS_AFTER_BOUNDED_REPAIR
FAIL_MATERIAL_REPAIR_REQUIRED
```
