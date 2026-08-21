# Stage29-08 — source refresh and coverage-scope audit target

## Peschmann source sequence

The Stage29-02hd screen used `arXiv:2604.09328` and `arXiv:2604.28072`. Stage29-08 additionally refreshes against the later Peschmann source `arXiv:2605.00573` (May 2026), because it materially affects coverage wording and adds an elliptic-fibration construction.

### arXiv:2604.09328

Audited-use facts:

- two Euclid pairs give two automatic face diagonals;
- Master and H-total are the remaining third-face and space square conditions;
- after a conic reduction the problem is encoded by a genus-3 family `C_A` with three elliptic quotients;
- perfect cuboid implies a nondegenerate rational point on the genus-3 curve;
- the specialized converse is not used without extra verification.

### arXiv:2604.28072

The abstract states a structural classification claiming every primitive Euler brick arises from the standard `(a,b,m,n)` parametrization up to scaling, and proves nonexistence on 1,072 explicit master-tuple fibers.

The 1,072 result is a finite fiber theorem, not global perfect-cuboid nonexistence.

### arXiv:2605.00573

The later source gives:

- the same Master-Hit edge formulas;
- an elliptic fibration over `(m,n)`, with genus-one quartic `H_mn` and Weierstrass model `E_mn`;
- a rational square-value lift test `tau(P)=t^2`;
- rigorous construction of a large finite collection of Euler bricks;
- an exponent-one blocker conjecture verified only on a finite fully-factorized database;
- an explicit scope statement that the paper does **not** claim every primitive body cuboid arises from a Master-Hit.

## Coverage conflict firewall

The global coverage language of `2604.28072` and the explicit non-converse language of `2605.00573` cannot both be silently promoted into one certified Stage29 theorem without an exact reconciliation of hypotheses/definitions/versions.

Therefore Stage29-08 uses the conservative audited target:

```text
PESCHMANN_EXACT_JOINT_V4_CROSSWALK=true_PENDING_AUDIT
PESCHMANN_GLOBAL_EULER_BRICK_COVERAGE_CERTIFIED=false
PESCHMANN_COVERAGE_SOURCE_SCOPE_CONFLICT=true
R29-PESCH-COV=OPEN_SOURCE_RECONCILIATION_AND_GLOBAL_COVERAGE_ADAPTER
```

This does not reopen `29-02h*`: exact crosswalk already shows Peschmann is not a ninth endpoint foundation. The open issue is coverage of the parametrization, not independence of the endpoint geometry.

## New May-source attack candidate

The universal exponent-one blocker is explicitly conjectural in the May source. It is potentially strong only after both a proof and sufficient coverage are established.

```text
R29-PESCH-E1=UniversalExponentOneBlockerProofOrCertifiedTheoremAdapter
OWNER=J12-PARAMETRIC
DEPENDENCY=[R29-PESCH-COV]
CURRENT_STATUS=AMBER_CONJECTURAL_FINITE_VERIFICATION_ONLY
```

No finite database is promoted to a theorem or population density statement.
