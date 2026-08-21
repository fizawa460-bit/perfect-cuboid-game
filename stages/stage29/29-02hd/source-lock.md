# Stage29-02hd — source lock for broad independent-foundation screen

STATUS=SUBMISSION_CANDIDATE_REQUIRES_FRESH_AUDIT
PURPOSE=broad screen only; do not promote internal continuations of F1–F8 to a new foundation

## Primary / scholarly sources checked

### Peschmann 2026 — quartic / genus-3 reduction

René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328 (2026).

Primary source: https://arxiv.org/abs/2604.09328

Load-bearing source claims used here:
- an exact Euclid-pair formulation of the perfect-cuboid problem;
- two face-diagonal conditions are built into the parametrization;
- the remaining third-face and space-diagonal conditions become a pair of quartic square conditions;
- the pair is reorganized through genus-3 curves with elliptic quotients;
- no unconditional global solution/nonexistence theorem is claimed.

Freshness / status firewall: this is a 2026 arXiv preprint. It is treated as research input, not as a certified repo theorem until a separate exact adapter and fresh audit are completed.

### Terasoma 1988 — complete intersections of quadrics

Tomohide Terasoma, *Complete intersections of hypersurfaces — the Fermat case and the quadric case*, Japan. J. Math. 14 (1988), 309–384. DOI: 10.4099/math1924.14.309.

Primary journal record: https://www.jstage.jst.go.jp/article/math1924/14/2/14_2_309/

Load-bearing source claims used here:
- a general theory of special diagonal complete intersections of quadrics;
- in the four-quadric P6 case, algebraic correspondences to K3 surfaces arising from associated hyperplane data;
- the result belongs to the complete-intersection/K3 correspondence ecosystem.

Firewall: applying the smooth/general statements verbatim to the 48-node cuboid specialization requires a specialization/resolution adapter. Stage29-02hd does not self-certify such an adapter.

### Jarossay–Saettone–Svoray 2023 — fundamental groups

David Jarossay, Francesco Maria Saettone, Yotam Svoray, *On the fundamental groups of surfaces parametrizing cuboids*, arXiv:2310.12710 (2023).

Primary source: https://arxiv.org/abs/2310.12710

Load-bearing source claims used here:
- the complex cuboid surface and its minimal resolution are simply connected;
- the face-cuboid surface and its resolution are simply connected;
- selected open subsets of the face-cuboid surface have explicit nontrivial fundamental groups;
- the authors explicitly motivate future arithmetic use through Chabauty–Kim / unipotent fundamental-group ideas, while noting that a fully developed surface analogue is not available.

Firewall: this gives a theorem ecosystem and future route, not a present endpoint rational-point obstruction.

### Adler–van Moerbeke 1987/88 — four quadrics / Abelian surfaces

Mark Adler, Pierre van Moerbeke, *The Intersection of Four Quadrics in P6, Abelian Surfaces and their Moduli*, Math. Ann. 279 (1987/88), 25–86.

Record: https://eudml.org/doc/164307

Use here: a screen against the possibility that the cuboid's four-quadric web falls into the special rank-4-curve configurations that compactify to Abelian surfaces.

Firewall: the exact cuboid diagonal web has no positive-dimensional rank-<=4 locus (see committed exact checker), so this Abelian-surface route is not promoted.

### Auel–Bernardara–Bolognesi 2014 — Clifford / quadric-fibration technology

Asher Auel, Marcello Bernardara, Michele Bolognesi, *Fibrations in complete intersections of quadrics, Clifford algebras, derived categories, and rationality problems*, J. Math. Pures Appl. 102 (2014), 249–291. DOI: 10.1016/j.matpur.2013.11.009. arXiv:1109.6938.

Use here: screen the dual web of cuboid quadrics for a direct section/Brauer obstruction.

Firewall: the cuboid web consists of rank-7 quadratic forms generically. The standard quadric-surface rank-4 equivalence 'Brauer class trivial iff rational section' is not transferable to this rank-7 family without a separate reduction theorem. No such endpoint adapter is claimed here.

### Super-4 / square-difference route

R. van Luijk, *On Perfect Cuboids* (Utrecht thesis, 2000), and the later MathOverflow discussion *Sequences of Squares with all square differences* (2011; accepted answer by Noam Elkies).

Use here:
- a perfect cuboid gives a four-square / pairwise-square-difference configuration;
- the Super-4 variety is itself a difficult general-type rational-point problem.

Firewall: this is a necessary projection to another open problem, not a presently stronger endpoint foundation.

## Already-covered ecosystems excluded from earning 29-02hd

The screen also rechecked current/recent cuboid literature and explicitly excludes as already represented:
- Testa–Stoll full surface / curves -> F1 / 29-02a;
- Beauville/Schoen irregular cover -> 29-02d;
- Freitag–Salvati Manni / X(8) modular model -> F5 / 29-02g;
- Horie–Yamauchi L-function -> F6 / 29-02e;
- non-Fano/Hirzebruch recognition -> F7 adapter / 29-02hc;
- Campedelli quotient layer -> F8 / 29-02hb.

LITERATURE_EXHAUSTIVENESS_CLAIM=false
NO_MORE_FOUNDATIONS_EXIST_CLAIM=false
