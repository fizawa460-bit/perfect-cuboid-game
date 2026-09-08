# EX1-05G — h=4 common-cover correspondence coupling

Status: **candidate, unaudited**. Audited predecessor is #1688 at exact head `93c455e1e69ed65fbfb553462fdcfbc8e2becbae`, hostile re-audit PASS review `5135375926`, merged as `6431ec2a90ed9260d4362d7146a9788cbc21c8d1`.

## 1. Exact notation adapter

For the h=4 branch already forced by EX1-05C/05D, let

- `Z=X(8)`;
- `H=G0plus ~= (Z/2)^2`;
- `C2=Z/H`;
- `Y=(Z x Z)/H_diag -> C2 x C2`;
- `D` be the normalization of the pullback of the hypothetical V6 genus-1 carrier `N` to `Y`;
- `f1,f2:D->C2` be the two projections.

EX1-05E gives `deg(f1),deg(f2)=(105,81)` for every residual h=4 state. EX1 `Q` means `deg Ram(D->N)` and must not be confused with the Stage32 Rosati norm `Q(T)`.

## 2. Relative-V4 common-cover consequence

The audited Stage32 relative-V4 source identifies `Y` as the relative `H`-isomorphism torsor between the two pullbacks of `Z->C2`. Since `D` maps to `Y`,

`f1^*Z ~= f2^*Z`.

For the two-dimensional character plane

`W=image(H^* -> H^1(C2,F2))`,

odd projection degrees 105 and 81 imply, by push-pull,

- `T|W=id mod 2`;
- `T^dagger|W=id mod 2`.

Thus every residual EX1 h=4 carrier has the same common fixed-plane necessary condition

`dim_F2(Fix(T) intersect Fix(T^dagger)) >= 2`.

This use is independent of the label `O=210` in the historical Stage32 source because EX1 separately re-establishes the relative torsor, h=4, and the two odd projection degrees.

## 3. Fixed correspondence arithmetic versus moving EX1 Q

The Stage32 Rosati repair explicitly separates its retained fixed-class/deck arithmetic from its later `O=210` normalization calculation. Reusing only the former for the same fixed V6 class and h=q'=4 gives

- pair map birational;
- bidegree `(105,81)`;
- `Gamma^2=15806`;
- `sigma(Gamma)=1204`;
- Rosati norm `Q_Rosati=Q(T)=602`;
- `p_a(Gamma)=8090`.

These are numerical correspondence-class invariants at the fixed V6 h=4 layer; they do not depend on which EX1 ramification state `Q=210+2r` occurs.

On the other hand Riemann–Hurwitz for the degree-two map `D->N`, with `g(N)=1`, gives

`g(D)=1+Q/2=106+r`.

Because the pair map is birational, `D` is the normalization of `Gamma`, hence

`delta_Gamma = p_a(Gamma)-g(D) = 8090-(106+r) = 7984-r`.

Together with EX1-05E,

- `R105=2r`;
- `R81=48+2r`;
- `2 delta_Gamma + R105 = 15968`;
- `2 delta_Gamma + R81 = 16016`.

So 05G produces an exact defect/ramification ladder, but not yet a local distribution theorem.

## 4. Mod-2 shell replay and nonpruning boundary

The audited Stage32 finite shell calculation at `Q(T)=602` finds 96 realized mod-2 residue classes. The common fixed-plane condition leaves exactly 28:

`[20,60,65,67,69,73,75,77,81,97,99,105,107,113,150,190,193,195,199,201,203,207,211,225,227,233,235,243]`.

Since every one of the 29 EX1 states has the same `Q_Rosati=602` and the same fixed-plane predicate, while no retained source couples a particular residue to `r`, the present resolution gives a coarse product ledger

`29 x 28 = 812`

arithmetically compatible cells.

This removes **0/29** EX1 Q states.

The 812 cells are not geometric curves, maps, or correspondences. They only demonstrate that the retained numerical/cohomological predicates do not yet contradict any Q state.

## 5. Deliberate non-import

The later Stage32 `16 -> 3` transvection refinement and final residues `[73,97,235]` are **not** imported here. That refinement was established inside the historical O210 route using additional marked/Weierstrass information. EX1-05G has not source-locked an adapter proving that extra transvection predicate uniformly for all `Q=210..266`.

## 6. Exact blocker and next route

The common-cover cohomology sees a two-plane fixed by `T,T^dagger`, and the fixed V6 class determines the Rosati norm and arithmetic genus. What remains absent is a theorem or member-level identity that connects those correspondence invariants to the **actual off-cusp ramification divisors** of `f1` and `f2` for the same `D`.

Next route:

`EX1-05H_CORRESPONDENCE_DEFECT_TO_OFF_CUSP_RAMIFICATION_COUPLING`.

05H should look for an exact relation between `delta_Gamma`, local singularity branches of the correspondence, and the two projection ramification divisors. A pure fixed-plane or Rosati-shell replay is already exhausted at the current invariant resolution.

## Credit firewall

No full V6 genus-1 exclusion, no genuine V6 carrier, no `FULL_TARGET_CLOSURE`, no Stage32 MAIN/Q602/O210 exclusion, and no theorem/receiver/endpoint/perfect-cuboid credit is claimed.