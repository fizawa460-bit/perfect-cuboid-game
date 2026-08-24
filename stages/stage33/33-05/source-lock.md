# Stage33-05 source lock — Creutz--Viray finite presentation

Primary source:

- Brendan Creutz, Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, arXiv:1306.3251, Math. Ann. 362 (2015), 1169--1200.
- Final-version load-bearing locators: Theorem I; §2.3 (`x-alpha`, `gamma'`); Theorem 5.2; Corollary 5.4; §6 dimension calculation, including the `(4,4)` example.
- Earlier combined-preprint numbering for the same material: Part II §9.1 candidate functions, §9.2 presentation, Theorem 9.3 / Corollary 9.5, and Theorem 10.1 / Corollary 10.2 / Example 10.3.

Stage33 uses the source in the already-audited direction:

```text
reduced flat branch with simple singularities on a ruled surface
  -> finite presentation of geometric Br[2]
     by explicit unramified central-simple-algebra generators
     modulo relations coming from NS(X)
  -> presentation carries Galois action and can support arithmetic descent
```

For the present rational ruled base `W=P1`, the source states `L_{c,E}=L_E`.  Its explicit generator construction uses

```text
ell_1,
ell_c,
ell_C for cycles C in the dual graph Gamma,
ell_D for [D] in Jac(B)[2].
```

The dimension proof quotients by `K*L*2`.  Crucially, at a singular branch point the source defines `e(b/w)` as the **sum** of the ramification indices over the normalization points above `b`; this is load-bearing for the Stage33 correction below.

Applied to the frozen `K_c` branch configuration, the corrected exact Stage33 checker certifies:

```text
B=B+ disjoint_union B-, with genera 1 and 1
h0(B)=2
b1(Gamma)=7
Jac(B)[2] dimension=4
q(t)=t^4-6t^2+1 gives four smooth common ramification fibers
nodal ruling fibers t=0,1,-1,infinity also have even e(b/w)=1+1
special even-e fiber count=8
K*/K*2 -> L*/L*2 kernel dimension=1
c square on the generic fiber
raw generator subspace mod L*2 dimension=12
kernel to K*L*2 dimension=7
L_E dimension=5
L_{c,E}=L_E
x-alpha image dimension=3
Br(K_c_Qbar)[2] dimension=2
```

The earlier Stage33 pilot value `L_{c,E}=9` omitted the four nodal fibers and is superseded.

The source itself emphasizes that group structure alone does not suffice for Brauer--Manin arithmetic; explicit representatives are needed. Accordingly Stage33-05 grants no Q-defined-class credit until the five-dimensional `L_{c,E}` basis, exact rank-3 `x-alpha` relation matrix, quotient symbols and Galois action are actually materialized.

Internal source locks:

- `stages/stage29/29-15/k3-ruled2-audit-execution.md`
- `stages/stage29/29-02e/result.md`
- `stages/stage33/33-00/unit-closure-contract.md`

```text
SOURCE_THEOREM_APPLICABILITY=FROZEN_AUDITED
LCE_DIMENSION_SKELETON_MATERIALIZED=true
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
FINITE_EXPLICIT_PRESENTATION_MATERIALIZED=false
QI_OVER_Q_BRAUER_ACTION_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
```
