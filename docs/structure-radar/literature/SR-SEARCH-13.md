# StructureRadar literature ledger — search batch 13

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-13-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-104,SR-STR-105,SR-STR-106,SR-STR-107,SR-STR-108,SR-STR-109,SR-STR-110,SR-STR-111,SR-STR-112,SR-STR-113
SEARCH_BATCH_SIZE=10
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-104 — Integral squareclass gcd kernel and cross-gcd localization
After clearing denominators, the common squareclass is sf(gcd(F,G)); odd common primes are 1 mod 4 and localize to cross-gcd channels.
Potential weapon types: NORMAL_FORM, LOCAL_OBSTRUCTION.
Applicability gaps: No global fixed-power squareclass-support bound is proved.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-105 — Fixed-coordinate squareclass support collapse
For fixed q1, every odd squareclass prime divides rad(a^4-b^4), H(q1)<=2B, and the number of squareclasses is subpolynomial.
Potential weapon types: SUPPORT_RESTRICTION.
Applicability gaps: No global q1 support deficit or uniform fiber bound is proved.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-106 — Fixed q1-delta nonisotrivial genus-one fiber geometry
Fixing q1 and delta gives a smooth complete intersection of two quadrics with an explicit quartic genus-one model; the moving q1 family is nonisotrivial.
Potential weapon types: FIBRATION, NORMAL_FORM.
Applicability gaps: The geometric model alone gives no pointwise or uniform arithmetic count.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-107 — Squareclass support-fiber half-wall gate
After q1 is fixed the squareclass index costs subpower; strict subhalf still requires an independent q1-support plus uniform max-fiber or second-moment theorem.
Potential weapon types: UPPER_BOUND_GATE, NO_DOUBLE_CHARGE_FIREWALL.
Applicability gaps: Tautological support and the energy diagonal cannot be reused as savings.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-108 — Explicit moduli map and geometric twist split
The fixed-fiber quartic has j-invariant depending only on x=q1, delta is purely a geometric twist, and physical q1-to-j multiplicity is at most two.
Potential weapon types: MODULI_ADAPTER.
Applicability gaps: No moduli-support saving or uniform fiber bound is proved.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-109 — Twist-prime support inside the moduli degeneration divisor
Odd twist primes are Gaussian-split and lie in the support of x^4-1, the geometric degeneration divisor.
Potential weapon types: SUPPORT_RESTRICTION, NO_INDEPENDENCE_FIREWALL.
Applicability gaps: No minimal conductor equality or two-adic classification is proved.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-110 — Moduli support exponent-equivalence barrier
Bounded q1-to-j multiplicity makes occupied j-support exponent-equivalent to q1-support; squareclass multiplicity per j is subpower but height-only moduli reparametrization yields no saving.
Potential weapon types: NEGATIVE_CERTIFICATE, UPPER_BOUND_GATE.
Applicability gaps: Requires an arithmetic twist-family theorem, not merely a height change of variables.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED`; Arsenal decision: `ACTIVE`.

## SR-STR-111 — Pointwise fixed q1-delta subpower count and uniformity firewall
For each fixed (q1,delta), bounded-height rational points on the genus-one fiber contribute only a subpower count, but the constants and Mordell-Weil rank are not uniform in moving q1.
Potential weapon types: COUNTING_LEMMA, NO_DOUBLE_CHARGE_FIREWALL, EXTERNAL_GATE.
Applicability gaps: A pointwise fixed-fiber estimate cannot be maximized or averaged over moving q1 without a uniform rank/height theorem.
Primary literature checked:
- Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves*, arXiv:2312.03655. The theorem is uniform for elliptic curves over a fixed number field when there is a rational point of exact prime order ell, with a subpower height bound. The Stage19 moving-q1 Jacobians are not known to satisfy that torsion hypothesis uniformly, so this does not discharge the moving family receiver.
- Tom Fisher and Graham Sills, *Local solubility and height bounds for coverings of elliptic curves*, arXiv:1103.4944. Their explicit height comparison for 2-, 3- and 4-coverings supports fixed-cover height transfer, but it does not supply a uniform Mordell-Weil rank or uniform point-count theorem over the moving q1 family.
Transfer verdict: `PRIMARY_LITERATURE_ADJACENT_FIXED_FIBRE_ONLY`; Arsenal decision: `ACTIVE`.

## SR-STR-112 — Common Jacobian of the fixed-q1 delta covering family
All fixed-(q1,delta) intersections of quadrics are genus-one coverings of one q1-dependent Jacobian, with delta changing the covering class rather than the Jacobian.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: The exact identification is repo-normalized; external covering theory does not itself prove the same-Jacobian statement for this specific coefficient model without the repo algebra.
Primary literature checked:
- Fisher--Sills, arXiv:1103.4944, treats genus-one curves as explicit 2-, 3- and 4-coverings of elliptic curves and gives covering maps and height relations. This is directly adjacent to the covering architecture, but the Stage19 claim that all delta fibres for fixed q1 share one specific q1-dependent Jacobian remains the repo-exact algebraic normalization.
Transfer verdict: `PRIMARY_LITERATURE_SUPPORTS_COVERING_ARCHITECTURE_NOT_SPECIFIC_JACOBIAN_IDENTITY`; Arsenal decision: `ACTIVE`.

## SR-STR-113 — Delta fibers as descent coverings of one Mordell-Weil group
For fixed q1, every soluble delta fiber maps to the same elliptic curve; delta indexes descent data and cannot be charged as independent rank entropy.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Descent-family literature concerns covering/Selmer classes for a fixed elliptic curve or controlled twist family; it does not imply a uniform moving-q1 Stage19 count.
Primary literature checked:
- Fisher--Sills, arXiv:1103.4944, supplies explicit covering maps and height relations for descent coverings; this supports the principle that soluble covering curves map to an elliptic curve rather than carrying independent Mordell-Weil rank.
- Zev Klagsbrun, Barry Mazur and Karl Rubin, *Disparity in Selmer ranks of quadratic twists of elliptic curves*, arXiv:1111.2321, studies parity distributions of 2-Selmer ranks in quadratic-twist families of a fixed elliptic curve over a fixed number field. It is adjacent to the delta-as-descent-data viewpoint but is not a uniform point-count theorem for the moving q1 Jacobian family.
- Zev Klagsbrun, *On the Distribution of 2-Selmer Ranks within Quadratic Twist Families of Elliptic Curves with Partial Rational Two-Torsion*, arXiv:1203.1030, shows that twist-family Selmer behavior can be large and hypothesis-sensitive. This reinforces the firewall against treating delta as a harmless uniformly bounded independent rank parameter.
Transfer verdict: `PRIMARY_LITERATURE_SUPPORTS_DESCENT_INTERPRETATION_NO_MOVING_FAMILY_COUNT`; Arsenal decision: `ACTIVE`.

## Literature-transfer firewall
Repo-exact population, height, multiplicity, modulus-growth, coefficient-uniformity and quantifier contracts are preserved. No external theorem is promoted without exact receiver matching.
Fisher--Sills supplies explicit covering and height machinery, Dujella supplies a uniform bounded-height theorem under rational prime-torsion hypotheses, and quadratic-twist Selmer literature describes fixed-curve twist families; none gives the missing uniform moving-q1 Stage19 counting theorem.
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT remains 1/2; no strict sub-square-root theorem or perfect-cuboid existence/nonexistence claim is made.

## Repair validation
The independent audit's source-coverage defect is repaired by the primary-source checks above. Exact-head StructureRadar controller validation is required on the final repaired head before re-audit.
