# Research Arsenal × Literature Strengthening Audit — Phase 4 Brauer / Kummer / Torsor / Cohomology

```text
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
STAGE36_EXCLUDED=true
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
LITERATURE_DISCOVERY_ONLY=true
ARSENAL_AUTHORITY_CHANGED=false
STABLE_ID_CREATED=false
```

Phase 4 compares the frozen Phase-1 Arsenal snapshot with original peer-reviewed Brauer–Manin, descent, Kummer-variety and purity literature. It does not promote any theorem or modify the Arsenal. Standard literature theorems and repo-specific source/marking adapters are deliberately kept as different typed layers.

## 1. Reviewed Arsenal surface

The frozen `docs/arsenal/index.json` and exact cards were rechecked. Primary Stage33 targets:

- `S33-PW04 EXACT_MARKED_SOURCE_ADAPTER`
- `S33-PW07 TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER`
- `S33-PW08 GERSTEN_CONNECTING_LOCALIZATION_ADAPTER`
- `S33-PW09 MARKED_KUMMER_LIFT_BINDING_ADAPTER`
- `S33-PW10 RESOLVED_PURITY_CECH_CARTIER_SEED_ASSEMBLER`
- `S33-WF01 FIRST_MISSING_WITNESS_TYPE_PROVENANCE_GATE`
- `S33-WF02 MARKED_QUOTIENT_EVALUATION_OBLIGATION_DECOMPOSITION`

Semantic near-neighbours reviewed because they are required to state the downstream theorem interface exactly:

- `S33-PW01 ARITHMETIC_HS_CLASSIFIER`
- `S33-PW06 ABSOLUTE_COHOMOLOGY_RECEIVER_RECIPE`
- audited provisional `S35-PW03 RATIONAL_SOURCE_LIFT_PRESERVING_KUMMER_NORMAL_FORM`

Current Stage33 strength is unusually strong on **class identity and provenance**: marked Picard/Brauer coordinates, literal full-surface Čech representatives, resolved codimension-one/exceptional residue data, exact localization columns, and source-bound `H^2(mu_2) -> Br[2]` binding. It does **not** yet provide the general downstream object

```text
all required local point sets X(k_v)
+ evaluation ev_{alpha,v}: X(k_v) -> Br(k_v)
+ inv_v
+ exact global invariant-sum compatibility
```

and therefore does not by itself give a Brauer–Manin obstruction.

## 2. Non-negotiable type boundary: S33-PW09 versus S35-PW03

These cards are not duplicates.

```text
S33-PW09:
independently named Br[2] source
+ genuine full-surface Cech H^2(mu_2) lift
+ independent marked Brauer coordinate
-> exact marked equality of the cohomological lift and named Brauer source

S35-PW03:
exact algebraic quotient receiver
+ rational-source lift discriminant
-> iff rational square condition
-> simultaneous Kummer-style square equations
-> forward/converse rational reconstruction
```

`S35-PW03` has no cohomological `H^2(mu_2)` or marked Brauer credit. Conversely, `S33-PW09` does not reconstruct rational source lifts from an algebraic quotient receiver. A Phase-6 bridge between them would require an independently proved **2-covering/torsor identification**; equation shape or the word “Kummer” is not such a bridge.

## 3. Literature theorem audit

### L4-BM01 — Brauer–Manin terminal pairing

For a smooth proper geometrically integral variety `X` over a number field `k`, global reciprocity gives

```text
X(k) subset X(A_k)^Br.
```

Hence `X(A_k)^B = empty` for any subgroup `B <= Br(X)` proves `X(k)=empty`. This is the terminal implication that the current Stage33 class-construction machinery does not yet instantiate.

Classification: **BRAUER_MANIN_TERMINAL**.

Repo input already present: source-bound Brauer classes and literal representatives in selected cases. Missing input: the exact variety/open model used for the terminal, complete local point/evaluation semantics at every relevant place, local invariant maps, and an exact proof that the adelic intersection is empty.

Firewall: `alpha != 0 in Br(X)` is not an obstruction. Even nonconstant local evaluation is not an obstruction unless the global adelic invariant-sum condition is empty.

### L4-BM02 — effective algebraic Brauer computation on surfaces

Martin Bright and Peter Swinnerton-Dyer, *Computing the Brauer–Manin obstructions*, Math. Proc. Cambridge Philos. Soc. **137** (2004), 1–16. DOI `10.1017/S0305004104007571`.

Exact variety class in the paper: complete nonsingular projective surface `V/k` over a number field, trivial Picard variety, torsion-free `Pic(Vbar)`, and local solubility at all completions for the obstruction computation. It uses

```text
Br^0(V) = Br_1(V)/Br_0(V) ~= H^1(k,Pic(Vbar))
```

and gives effective procedures for computing the algebraic Brauer contribution and its Brauer–Manin obstruction.

Classification: **BRAUER_EVALUATION_EXTENSION** for `S33-PW01`, `S33-PW04`, `S33-WF02`.

Current repo fit: Stage33 already has exact marked Picard/Galois/cohomological infrastructure much closer to the source side of this theorem than a generic CAS input. Missing adapter: `MARKED_BRAUER_CLASS_TO_LOCAL_AZUMAYA_OR_SYMBOL_EVALUATION` plus exact surface hypotheses and local-point models.

Important mismatch: this is primarily an **algebraic Brauer** (`Br_1/Br_0`) computation. A Stage33 class shown to be transcendental cannot be moved into this interface by analogy.

### L4-BM03 — efficient local evaluation

Martin Bright, *Efficient evaluation of the Brauer–Manin obstruction*, Math. Proc. Cambridge Philos. Soc. **142** (2007), 13–23. DOI `10.1017/S0305004106009844`.

Main paper result: at suitable primes the local evaluation problem can be reduced from enumerating p-adic points to points over a closed subset, and at other primes to reduction modulo `p`. This is an efficiency theorem **after** a valid Brauer class/evaluation and suitable model/reduction hypotheses are present.

Classification: **BRAUER_EVALUATION_EXTENSION**.

Theorem-number source lock was not recovered from the accessible journal metadata in this Phase-4 search; exact proposition/theorem numbering is therefore a Phase-6 promotion gate rather than guessed here.

### L4-BM04 — finite relevant-place reduction

Jean-Louis Colliot-Thélène and Alexei N. Skorobogatov, *Good reduction of the Brauer–Manin obstruction*, Trans. Amer. Math. Soc. **365** (2013), 579–590. DOI `10.1090/S0002-9947-2012-05556-5`.

Exact hypothesis package: smooth projective variety over a number field, torsion-free geometric Picard group, finite transcendental Brauer group. Conclusion: only archimedean places, primes of bad reduction, and primes dividing the order of the transcendental Brauer group can matter in the description of the Brauer–Manin set.

Classification: **BRAUER_EVALUATION_EXTENSION** / finite-place reducer.

Potential gain: convert an all-place Stage33 evaluation obligation into a certified finite place set. Missing inputs: proper smooth terminal model, exact good-reduction set/model, proof that `Pic(Xbar)` is torsion-free, and a certified finite transcendental Brauer group/order bound. It is not applicable to an open receiver without another theorem/adapter.

### L4-DESC01 — descent equals étale Brauer–Manin for proper varieties

Alexei Skorobogatov, *Descent obstruction is equivalent to étale Brauer–Manin obstruction*, Math. Ann. **344** (2009), 501–510. DOI `10.1007/s00208-008-0314-4`.

Theorem 1.1: for a smooth projective geometrically integral variety `X/k` over a number field and a torsor `f:Y->X` under a finite `k`-group scheme `F`, the descent set is reconstructed from twists and their descent sets. Corollary 1.2, together with the cited descent/Brauer comparison, yields

```text
X(A_k)^desc = X(A_k)^{et,Br}.
```

Classification: **DESCENT_TERMINAL** as an obstruction-set identity, not as an algorithm that automatically produces emptiness.

Current repo fit: `S33-PW07` supplies exact torsor/cocycle semantics in a source-bound instance; `PW06/PW08` supply arithmetic cohomology/localization infrastructure. Missing adapter: exact `Y->X` finite torsor/twist family and local adelic twist computation for the actual terminal variety.

Blocker: projective/smooth/geometrically integral hypotheses. Do not apply this proper theorem to an open Stage33 receiver.

### L4-DESC02 — open-variety extension

Yang Cao, Cyril Demarche and Fei Xu, *Comparing descent obstruction and Brauer-Manin obstruction for open varieties*, Trans. Amer. Math. Soc. **371** (2019), 8625–8650. DOI `10.1090/tran/7567`.

Theorem 1.5 (= Theorem 7.5 in the paper): if `X` is smooth quasi-projective and geometrically integral over a number field `k`, then

```text
X(A_k)^desc = X(A_k)^{et,Br}.
```

The paper also treats torsors under connected linear algebraic groups and groups of multiplicative type.

Classification: **DESCENT_TERMINAL** / **LOCALIZATION_EXTENSION** for a genuinely open receiver.

This is the correct literature family to inspect before compactifying an open Stage33 receiver merely to invoke Skorobogatov 2009. Missing repo inputs remain exact smooth quasi-projective structure, geometric integrality, the actual torsor species, and local adelic/twist data.

### L4-DESC03 — curves: finite abelian descent and Brauer set

Michael Stoll, *Finite descent obstructions and rational points on curves*, Algebra & Number Theory **1** (2007), 349–391. DOI `10.2140/ant.2007.1.349`.

Theorem 7.1 gives the general containment for smooth projective geometrically connected varieties. The curve specialization identifies the Brauer set with the finite-abelian-descent set; Theorem 7.5 identifies `n`-abelian descent with the corresponding algebraic Brauer layer. The paper further proves strong rational-point cutout results for curves mapping nontrivially to an abelian variety `A` with `A(k)` finite and `Sha(k,A)` having no nontrivial divisible elements.

Classification: **DESCENT_TERMINAL** for exact curve receivers; **NOT_APPLICABLE** to a Stage33 surface without a source-locked curve reduction.

Firewall: the strong “descent cuts out precisely rational points” conclusion is not a theorem for arbitrary surfaces and is not unconditional for arbitrary genus >=2 curves.

### L4-KUM01 — Brauer groups of an abelian surface and its Kummer surface

Alexei Skorobogatov and Yuri Zarhin, *The Brauer group of Kummer surfaces and torsion of elliptic curves*, J. reine angew. Math. **666** (2012), 115–140. DOI `10.1515/CRELLE.2011.121`.

Theorem 2.4: if `A` is an abelian surface and `X=Kum(A)`, then pullback gives an embedding

```text
Br(X)[n]/Br_1(X)[n] -> Br(A)[n]/Br_1(A)[n],
```

which is an isomorphism for odd `n`; in particular the odd-order transcendental Brauer subgroups are naturally isomorphic. Section 3 supplies stronger formulas for products of elliptic curves, including a separate `n=2` analysis.

Classification: **KUMMER_VARIETY_EXTENSION** / **SOURCE_ANCHOR_ONLY**.

Important hostile boundary: Theorem 2.4 is **not** a general 2-primary isomorphism. `S33-PW09` is an order-two marked lift binding, so the odd-order theorem cannot be used to infer its coordinates. Conversely the theorem becomes useful only after an exact adapter proves that the repo surface is the stated `Kum(A)` and binds the pullback to the repo marking.

### L4-KUM02 — higher-dimensional Kummer Brauer behavior

Alexei Skorobogatov and Yuri Zarhin, *Kummer varieties and their Brauer groups*, Pure Appl. Math. Q. **13** (2017), 337–368. DOI `10.4310/PAMQ.2017.v13.n2.a5`.

Variety class: Kummer varieties attached to 2-coverings of abelian varieties of arbitrary dimension `>=2` over characteristic not 2. Over number fields the paper proves, among other results, that odd-order Brauer elements do not obstruct the Hasse principle and gives sufficient conditions for triviality/non-emptiness results in large-Galois-image families.

Classification: **KUMMER_VARIETY_EXTENSION**.

This is a genuine higher-dimensional extension, but not a license to call an arbitrary simultaneous-square receiver a Kummer variety. A `2-covering of A -> Kummer quotient/desingularization` source adapter is mandatory.

### L4-KUM03 — 2-primary suffices for a Brauer–Manin obstruction on a Kummer variety

Brendan Creutz and Bianca Viray, *Degree and the Brauer–Manin obstruction*, Algebra & Number Theory **12** (2018), 2445–2480. DOI `10.2140/ant.2018.12.2445`.

Theorem 1.7: Kummer varieties satisfy `BM_2`. Theorem 1.8 / Appendix Theorem A.1 gives the more useful subgroup statement: for a Kummer variety `X/k` and `B <= Br(X)`, if

```text
X(A_k)^B = empty,
```

then the 2-primary part already obstructs:

```text
X(A_k)^{B[2^infinity]} = empty.
```

Classification: **BRAUER_MANIN_TERMINAL** + **KUMMER_VARIETY_EXTENSION**.

Potential gain for Stage33: if the actual terminal object is proved to be a Kummer variety, a full Brauer–Manin Hasse obstruction can be reduced to 2-primary Brauer information. Crucial blocker: `S33-PW09` currently binds `Br[2]`, not the entire `Br[2^infinity]`. The theorem does **not** imply that order-two classes alone always suffice.

### L4-KUM04 — first/second descent on explicit Kummer surfaces with rational 2-torsion

Alexei Skorobogatov and Peter Swinnerton-Dyer, *2-Descent on elliptic curves and rational points on certain Kummer surfaces*, Adv. Math. **198** (2005), 448–483. DOI `10.1016/j.aim.2005.06.005`.

The paper refines 2-descent on elliptic curves with rational 2-division and studies a Kummer surface attached to the product of two 2-coverings. In the rational-2-torsion setting it gives sufficient conditions for rational points; this part is conditional on finiteness of the relevant Tate–Shafarevich group.

Classification: **SECOND_DESCENT_ADAPTER** / **RESEARCH_GAP** for Stage33.

Required adapter is far stronger than `PW09`: exact elliptic curves/abelian variety, exact 2-coverings and their classes in `H^1(k,A[2])`, rational 2-torsion where used, local solubility/Selmer data, and the relevant `Sha` condition.

### L4-KUM05 — explicit second descent in families

Yonatan Harpaz, *Second descent and rational points on Kummer varieties*, Proc. London Math. Soc. **118** (2019), 606–648. DOI `10.1112/plms.12191`.

Theorem 1.3 is highly specific and therefore especially useful as a hostile comparator. Let

```text
f(x)=product_{i=0}^5 (x-a_i)
```

split completely over the number field `k`, let `C:y^2=f(x)`, `A=Jac(C)`, and let the Kummer surface be the specified smooth complete intersection of three diagonal quadrics defined by coefficients `b_i`. The theorem assumes:

- `[b_1/b_0],...,[b_4/b_0]` linearly independent in `k*/k*^2`;
- finite odd places `w_1,...,w_5`;
- all branch points `a_i` are `w_i`-integral and `val_{w_i}(a_i-a_0)=val_{w_i}(sqrt(disc f))=1`;
- the relevant `b_j/b_0` are units at `w_i` but not all local squares.

Conclusion: the paper's Conjecture 1.1 holds for this Kummer surface; in particular, assuming the 2-primary Tate–Shafarevich conjecture for every quadratic twist of `A`, the 2-primary Brauer–Manin obstruction is the only obstruction to the Hasse principle on `X`.

Classification: **SECOND_DESCENT_ADAPTER** / **BRAUER_MANIN_TERMINAL** / **RESEARCH_GAP**.

Current Stage33 does not establish this split-six-branch model, these local places, this Jacobian/PPAV identification, twist-family Selmer data, or the conditional `Sha` hypothesis. Therefore this theorem is **not directly applicable**.

### L4-KUM06 — large-Galois-image Kummer Hasse principle

Yonatan Harpaz and Alexei Skorobogatov, *Hasse principle for Kummer varieties*, Algebra & Number Theory **10** (2016), 813–841. DOI `10.2140/ant.2016.10.813`.

Theorem 2.3: over a number field, for `A=prod A_i` with each `A_i` principally polarized and satisfying explicit conditions on the `G_i`-module `A_i[2]` — simplicity, endomorphism ring `F_2`, `H^1(G_i,A_i[2])=0`, named fixed-quotient elements — plus linear disjointness, named reduction/ramification places, and finiteness of specified 2-primary Tate–Shafarevich groups of quadratic twists, an everywhere locally soluble Kummer variety defined by a suitable unramified/nonzero `H^1(k,A[2])` class has a Zariski-dense set of `k`-points.

Classification: **KUMMER_VARIETY_EXTENSION** / **RESEARCH_GAP**, not an obstruction weapon.

The theorem proves rational-point existence under strong conditions. It cannot be inverted to claim nonexistence when one hypothesis fails.

### L4-KUM07 — generic 2-torsion extension

Adam Morgan, *Hasse principle for Kummer varieties in the case of generic 2-torsion*, Proc. London Math. Soc. **131** (2025), e70066. DOI `10.1112/plms.70066`.

Theorem 1.9: under the paper's Assumptions 1.3 and 1.8 and finiteness of the 2-primary `Sha` of every quadratic twist with `2^infinity`-Selmer rank 1, everywhere local solubility implies a Zariski-dense set of rational points.

Classification: **KUMMER_VARIETY_EXTENSION** / **SECOND_DESCENT_ADAPTER** / **RESEARCH_GAP**.

This broadens the rational-2-torsion regime, but the Galois module and twist/Selmer hypotheses are still concrete load-bearing inputs. No Stage33 adapter currently discharges them.

### L4-PUR01 — Gersten/purity source anchor

Spencer Bloch and Arthur Ogus, *Gersten's conjecture and the homology of schemes*, Ann. Sci. ÉNS **7** (1974), 181–201. DOI `10.24033/asens.1266`.

Jean-Louis Colliot-Thélène, Raymond Hoobler and Bruno Kahn, *The Bloch–Ogus–Gabber theorem*, in *Algebraic K-Theory*, Fields Institute Communications **16** (1997), 31–94.

These supply canonical purity/Gersten exactness machinery in the appropriate smooth/regular/coefficient settings.

Classification for `S33-PW08`/`S33-PW10`: **LOCALIZATION_EXTENSION** + **SOURCE_ANCHOR_ONLY**.

They do not replace the repo-specific work attaching the literal factors to the actual resolved height-one valuations, computing exceptional-divisor residues, or deriving the concrete purity correction. Standard exactness theorem + wrong prime attachment is still wrong.

## 4. Stage33 card → literature connection map

| Arsenal card | Phase-4 verdict | Safe literature connection | Missing typed edge |
|---|---|---|---|
| `S33-PW01` | `BRAUER_EVALUATION_EXTENSION` | algebraic `H^1(k,Pic)` → Brauer representatives/evaluation | complete correct Brauer subgroup, class evaluation, adelic invariant sum |
| `S33-PW04` | `BRAUER_EVALUATION_EXTENSION` | marked coordinates can source-bind literature Brauer classes | marked coordinate → actual local symbol/Azumaya evaluation |
| `S33-PW06` | `DESCENT_TERMINAL` support | absolute `H^1` receiver can host torsor/descent data | exact torsor species/twist family and adelic descent-set computation |
| `S33-PW07` | `DESCENT_TERMINAL` / `SECOND_DESCENT_ADAPTER` | common cocycle/torsor semantics are the correct precondition | prove the specific finite/abelian 2-covering hypotheses used by chosen theorem |
| `S33-PW08` | `LOCALIZATION_EXTENSION` / `BRAUER_EVALUATION_EXTENSION` | Gersten columns are a strong source for local ramification control | localization class → evaluation on every relevant local point stratum |
| `S33-PW09` | `KUMMER_VARIETY_EXTENSION` | exact `Br[2]` lift binding can feed 2-primary Brauer work | actual Kummer-variety/2-covering adapter; higher 2-power control when required |
| `S33-PW10` | `LOCALIZATION_EXTENSION` | literal Čech-Cartier seed is suitable for explicit class materialization | seed → marked Brauer image → local evaluation; these remain separate edges |
| `S33-WF01` | `DUPLICATE` as workflow discipline | literature does not replace first-missing-edge provenance gate | none; keep as repo proof-engineering workflow |
| `S33-WF02` | `BRAUER_EVALUATION_EXTENSION` | finite marked evaluations resemble the source side of explicit Brauer computation | source quotient evaluations are not yet local-point evaluations `X(k_v)->Br(k_v)` |
| `S35-PW03` | `SECOND_DESCENT_ADAPTER` only after another bridge | its square system may become a 2-cover model if proved | exact cohomological 2-cover/torsor/Selmer identification; no Kummer-by-name inference |

## 5. Strongest safe strengthening chain

A literature-backed Stage33 downstream chain can be typed as follows:

```text
LITERAL_SOURCE_CLASS
  -- PW10/PW04/PW09 --> SOURCE_BOUND_BRAUER_CLASS
  -- new adapter --> EXPLICIT_LOCAL_EVALUATION_FUNCTIONS
  -- PW08 + new finite-place/model adapter --> COMPLETE_RELEVANT_LOCAL_EVALUATION_TABLE
  -- new terminal --> ADELIC_INVARIANT_SUM_INTERSECTION
  -- if empty --> BRAUER_MANIN_NONEXISTENCE
```

For descent/second descent the chain is different:

```text
SOURCE_BOUND_TORSOR_OR_SQUARE_RECEIVER
  -- PW07 or new S35-PW03 bridge --> EXACT_2_COVERING_CLASS alpha in H^1(k,A[2])
  -- literature theorem + repo local adapter --> Sel_2 / twist / Cassels-Tate data
  -- optional second descent --> smaller admissible descent set
  -- if exact descent/etale-Brauer set empty --> rational-point obstruction
```

These chains must not be conflated. A Kummer `H^2(mu_2)` lift of a Brauer class is not the same datum as a 2-covering class in `H^1(k,A[2])`.

## 6. Exact hypothesis blockers found

1. **Proper versus open.** Skorobogatov 2009 is proper; Cao–Demarche–Xu 2019 is the relevant smooth quasi-projective extension. The terminal object's actual category must be locked first.
2. **Algebraic versus transcendental Brauer.** `H^1(k,Pic)` controls the algebraic layer. Transcendental Stage33 classes require separate theorems/representatives.
3. **Order 2 versus 2-primary.** Creutz–Viray reduces Kummer BM obstruction to `2^infinity`-primary classes, not automatically `Br[2]` alone.
4. **Kummer surface/variety identity.** A simultaneous square system or a K3 label is not an associated Kummer variety. Need exact `Y` 2-covering of `A`, involution quotient and smooth/desingularized model.
5. **Abelian variety structure.** Second descent requires exact `A`, its `A[2]` Galois module, polarization conditions where used, Selmer/Kummer maps and Cassels–Tate pairing.
6. **Rational 2-torsion versus generic action.** SSD 2005/Harpaz 2019 and Harpaz–Skorobogatov/Morgan occupy different Galois-action regimes. They cannot be mixed ad hoc.
7. **Sha hypotheses.** Harpaz/HS/Morgan conclusions are conditional on explicit finiteness hypotheses. Such results cannot become unconditional Arsenal weapons.
8. **Local solubility.** Existence theorems generally start with everywhere local solubility. Failure to verify it is not an obstruction theorem.
9. **Markedness.** Literature may identify an abstract Brauer/Selmer group; Stage33 still needs a source-locked adapter to its exact marked class. Dimension/rank coincidences are insufficient.
10. **Purity regularity.** Standard Gersten/purity exactness does not authorize ignoring exceptional divisors or using an unresolved/incorrect codimension-one attachment.

## 7. Credit firewalls

```text
nonzero Brauer class != Brauer-Manin obstruction
explicit local evaluation != global obstruction
zero localization != Q-defined class
Kummer H2(mu2) lift != rational-point nonexistence
Kummer-style square equations != Kummer variety / 2-covering
Selmer membership/restriction != rational point
empty selected local residue cell != empty adelic Brauer set unless coverage is exact
second descent theorem != applicable without exact torsor/abelian/2-torsion hypotheses
Sha-conditional theorem != unconditional Arsenal weapon
literature theorem != repo source adapter
```

## 8. Phase-6 freeze manifest

| Candidate | Targets | Classification | Promotion gate |
|---|---|---|---|
| `STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER` | `PW04,PW08,PW09,PW10,WF02` | `BRAUER_EVALUATION_EXTENSION` | exact terminal variety, source-bound Brauer representative, local evaluation maps and invariant normalization, all boundary strata |
| `BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL` | `PW01,PW04,PW08,PW09` | `BRAUER_MANIN_TERMINAL` | exact local point populations/evaluation images at every required place and certified empty invariant-sum intersection |
| `BRAUER_GOOD_REDUCTION_FINITE_PLACE_REDUCER` | `PW08,PW10` | `BRAUER_EVALUATION_EXTENSION` | smooth proper model, torsion-free geometric Picard, finite transcendental Brauer/order, exact bad-reduction set |
| `OPEN_DESCENT_ETALE_BRAUER_TERMINAL` | `PW06,PW07,PW08` | `DESCENT_TERMINAL` | smooth quasi-projective geometrically integral receiver, exact finite/group torsors and twists, adelic descent computation |
| `KUMMER_2PRIMARY_BM_REDUCTION_GATE` | `PW09,PW07` | `KUMMER_VARIETY_EXTENSION` + `BRAUER_MANIN_TERMINAL` | prove actual Kummer variety from a 2-covering; distinguish `Br[2]` from `Br[2^infinity]` |
| `KUMMER_SECOND_DESCENT_ADAPTER` | `PW07,PW09,S35-PW03` | `SECOND_DESCENT_ADAPTER` | exact `A`, 2-covering class in `H^1(k,A[2])`, Galois/polarization hypotheses, local Selmer and Cassels–Tate data, conditional Sha flags |
| `KUMMER_TRANSCENDENTAL_BRAUER_COMPARISON_ADAPTER` | `PW04,PW09` | `KUMMER_VARIETY_EXTENSION` | exact abelian surface/Kummer pullback and marked coordinate bridge; no odd-to-2 extrapolation |
| `GERSTEN_PURITY_THEOREM_ANCHOR` | `PW08,PW10` | `LOCALIZATION_EXTENSION` + `SOURCE_ANCHOR_ONLY` | exact regular/smooth coefficient setting and continued repo-specific valuation/exceptional-residue replay |
| `CURVE_FINITE_ABELIAN_DESCENT_TERMINAL` | `PW06,PW07` and any future curve receiver | `DESCENT_TERMINAL` / `RESEARCH_GAP` | source-lock a curve receiver and Stoll's exact abelian/Sha hypotheses before rational-point cutout credit |

Priority:

```text
P0 STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER
P0 BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL
P0 KUMMER_2PRIMARY_BM_REDUCTION_GATE
P1 OPEN_DESCENT_ETALE_BRAUER_TERMINAL
P1 KUMMER_SECOND_DESCENT_ADAPTER
P1 BRAUER_GOOD_REDUCTION_FINITE_PLACE_REDUCER
P2 KUMMER_TRANSCENDENTAL_BRAUER_COMPARISON_ADAPTER
P2 GERSTEN_PURITY_THEOREM_ANCHOR
P2 CURVE_FINITE_ABELIAN_DESCENT_TERMINAL
```

## 9. Stop boundary

Phase 4 found a genuine path beyond Stage33 class construction: **explicit source-bound Brauer classes can be promoted to rational-point obstruction only through a new local-evaluation layer and an adelic Brauer–Manin terminal**. The most promising second route is an exact `H^1(k,A[2])` 2-covering adapter followed by Selmer/Cassels–Tate second descent, but existing Kummer theorems have much stronger variety/Galois/local/Sha hypotheses than the current cards record.

No current Stage33 card is weakened or declared duplicate because a standard theorem exists. The preferred architecture is

```text
LITERATURE_THEOREM + REPO_SOURCE_ADAPTER + REPO_EVALUATION/COVERAGE_CERTIFICATE.
```

No novelty conclusion is drawn from any literature-search miss.