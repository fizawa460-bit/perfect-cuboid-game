# Stage32 post-B16 literature/receiver exact reconciliation

Status: **MAIN EVIDENCE COMPLETE — PENDING FRESH HOSTILE AUDIT**.

This checkpoint reconciles the hostile-audited D16/B16 bounded numerical close with the frozen Stage29 low-genus receiver contracts and the currently available literature. It does not grant receiver, theorem, route, endpoint, or B18 credit.

## Locked repository inputs

- PR `#1450` repaired B16 hostile audit review: `5055088574`
- audited PR head: `d1f888978481eb93e240c1369d1436df251ee9b2`
- audited B16 state: `stages/stage32/audits/32-18BG.json`
- repaired B16 close evidence: `stages/stage32/32-18BG/D16_B16_REPAIRED_CLOSE_EVIDENCE.md`
- Stage29 LG2 route contract: `stages/stage29/29-02c-LG2/route-contract.json`
- Stage29 LG2 finite-search contract: `stages/stage29/29-02c-LG2/finite-search-contract.md`
- Stage29 LG2 audit: `stages/stage29/29-02c-LG2/audit.md`

The Stage29 receiver completion criterion remains authoritative: a complete numerical orbit list over the full unibranch genus-0 degree `<=176` and genus-1 degree `<=192` windows is required, and every numerical survivor must then be disposed by ineffectivity, known boundary/degenerate status, or an explicit effective carrier. Numerical enumeration alone is not effectivity.

## Literature source locks and exact usable statements

### FSM16 — unibranch degree cap

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691; preprint `https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`.

Theorem 3.1 assumes that the normalization map of the irreducible curve to its image in the box variety is **bijective** and proves

`d <= 176 + 16g`.

Thus the frozen Stage29 windows `g=0: d<=176` and `g=1: d<=192` are correctly restricted to the unibranch/bijective-normalization population. This theorem does not cover multibranch-at-node curves.

### GFU20 — symmetric-differential constraints

Natalia García-Fritz and Giancarlo Urzúa, *Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Math. Z. 296 (2020), 573–593, DOI `10.1007/s00209-019-02439-x`.

For the cuboid surface, Theorem 1.2 gives in particular:

- every geometric-genus 0 or 1 curve contains at least two of the 48 singularities;
- if the curve is smooth at the singular points, `deg(C) <= 4g(C)+44`;
- a rational curve on the resolution that is neither exceptional nor contained in the coordinate boundary has exceptional-divisor intersection at least 8.

The stronger degree inequality has an extra smooth-at-singular-points hypothesis and therefore cannot replace the FSM16 `176/192` cap for the whole frozen unibranch receiver population.

### BTVA22 — explicit symmetric differentials

Nils Bruin, Jordan Thomas and Anthony Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), no. 6, 1377–1405, DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908`.

For the cuboid surface their explicit differential constraints imply that, apart from the known exceptions, rational curves must pass through at least seven singularities; the rational-curve singularities span the ambient `P^6`, and genus-1 curves must pass through at least two singularities. These are necessary filters, not a complete low-genus classification.

### Testa–Stoll 2026 — current Picard/low-degree classification

Damiano Testa and Michael Stoll, *Curves on the surface of cuboids*, Mathematics of Computation, DOI `10.1090/mcom/4238` (2026 publication record; accepted/published version linked by AMS/Warwick).

The current paper explicitly determines the Picard group/Galois module and completely classifies integral curves only through degree 6. It also records the stronger exceptional-divisor incidence constraints used by the frozen Stage29 contract: a rational non-conic has `C.E >= 8`, while a geometric-genus-1 curve has `C.E >= 4`.

The paper itself treats the higher low-genus locus as incomplete; the degree-6 classification does not extend to the full FSM16 `176/192` windows.

## Reconciliation against Stage32 B16

The repaired Stage32-18BG audit proves exactly the bounded `D16/B16` numerical claim and explicitly leaves

- `FULL_D16_G0_ROW_COMPLETE = false`,
- `R29_LG2 = NOT_DISCHARGED`,
- `R29_LG2_EFF = NOT_DISCHARGED`,
- `R29_LG2_MB = NOT_DISCHARGED`.

No literature statement above supplies an adapter from the audited B16 bounded computation to a complete orbit census for all even degrees through 176/192. No source supplies effectivity for all surviving numerical classes, and FSM16 does not cover the multibranch ledger.

Therefore:

`D16_B16_NUMERICAL_CREDIT=true` **does not imply** `R29_LG2=DISCHARGED`.

## What the literature does improve

The current theorem set justifies keeping or strengthening the following production filters in the later residual feasibility analysis:

1. exact FSM16 unibranch degree windows `176/192`;
2. known degree-`<=6` subtraction from Testa–Stoll;
3. exceptional/node incidence constraints (`C.E>=8` for rational non-conics, `C.E>=4` for genus 1);
4. BTVA22 node-count/spanning constraints where their hypotheses match;
5. GFU20 smooth-at-node degree bound only on the explicitly certified smooth-at-singular subpopulation.

None of these filters is receiver discharge by itself.

## MAIN reconciliation verdict

`PASS_LITERATURE_RECONCILIATION_NO_RECEIVER_DISCHARGE_FILTER_STRENGTHENING_ONLY`

Proposed next step **only after fresh hostile audit of this checkpoint**:

`RESIDUAL_FEASIBILITY_GATE`

That gate should measure the remaining full-window production problem under the exact receiver population and the admissible literature filters before any residual production workload is authorized.

## Firewalls

- `D16_B16_NUMERICAL_CREDIT = true`
- `FULL_D16_G0_ROW_COMPLETE = false`
- `R29_LG2 = NOT_DISCHARGED`
- `R29_LG2_EFF = NOT_DISCHARGED`
- `R29_LG2_MB = NOT_DISCHARGED`
- `G10_LOWGENUS_PICARD = AMBER`
- theorem credit = false
- receiver credit = false
- route-color change authorized = false
- endpoint credit = false
- B18 release authorized = false
- perfect-cuboid existence claim = false
- perfect-cuboid nonexistence claim = false

No heavy compute or run-key arming is authorized by this checkpoint.
