# Stage29-02 Work import — primary-source candidate lock

```text
ROLE=PRIMARY_SOURCE_CANDIDATE_LEDGER
STATUS=PENDING_FRESH_STAGE29_AUDIT
```

These source/theorem locators are imported from the independent Work report. They are precise enough for fresh audit but are not yet promoted as repo-certified theorem interfaces.

## Low-genus finite bound

- Eberhard Freitag; Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675--691, DOI `10.1307/mmj/1480734014`, arXiv `1303.6495`.
- Candidate load-bearing locator: **Theorem 3.1**.
- Work-extracted statement: for a curve on the box variety whose normalization map is bijective, with genus `g` and canonical/projective degree `d`,

```text
d <= 176 + 16g.
```

- Audit focus: exact ambient surface/model match, exact meaning of degree, exact normalization hypothesis, and whether singular curves at the 48 nodes fall outside the theorem.

Supporting inputs:

- Testa--Stoll: rank-64 Picard lattice and low-degree finite-enumeration machinery.
- Bruin--Thomas--Varilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasihyperbolicity*, Algebra & Number Theory 16 (2022), Theorem 1.2: node-incidence/span restrictions for genus-0 and genus-1 curves.

## Beauville irregular cover

- Arnaud Beauville, *A tale of two surfaces*, arXiv `1303.1910`.
- Candidate load-bearing locators: **Proposition 1**, **Remark 1**, pp. 2--3 in the cited preprint version.
- Work-extracted package:

```text
X_Beau=(C x C')/Gamma
q=4
pg=7
K^2=32
canonical quotient = complete intersection of four quadrics in P6 with 48 nodes
```

and an etale V4 tower / Albanese map to an abelian fourfold.

Audit focus: exact specialization to the cuboid surface, Q versus Q(i) field of definition, branch/etale locus, and the twist required for lifting a rational endpoint point.

## Algebraic Brauer closure

- Testa--Stoll, *Curves on the surface of cuboids*, Theorem 10, Section 3.
- Work-extracted statement:

```text
Br_1(S)/im Br(Q)=0.
```

Audit focus: whether `S` is exactly the smooth minimal resolution used in Stage29 and the precise consequence for algebraic Brauer--Manin obstructions on the physical open.

## Modular M(4,8) interpretation

- Freitag--Salvati Manni: Theorems 2.4, 6.1, 6.2, 6.3.
- Testa--Stoll: Section 4 Q-form / Weil-restriction description.
- Tom Fisher, *Explicit moduli spaces for congruences of elliptic curves*, Math. Z. 295 (2020), Theorems 1.1--1.2 and Corollary 1.3.

Audit focus: exact fine/coarse moduli conditions, descent from `Q(i)` to `Q`, cusp/stabilizer exceptions, and Fisher's abundance result as a firewall against naive ordinary-8-congruence obstruction claims.

## Cohomology input for transcendental Brauer work

- Horie--Yamauchi, *The L-function of the surface parametrizing cuboids*, arXiv `2512.22520v3`, Theorem 1.1 / Corollaries 4.5--4.6 according to the Work report.

Audit focus: distinguish rational semisimplified l-adic decomposition from the integral lattice/torsion/evaluation information required for the transcendental Brauer group.

## Certification rule

```text
WORK_REPORT_SOURCE_MATCH!=REPO_THEOREM_CERTIFICATION
FRESH_PRIMARY_SOURCE_AUDIT_REQUIRED=true
NO_ENDPOINT_CLAIM_BEFORE_AUDIT=true
```
