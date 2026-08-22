# Stage29-11 adversarial audit contract

Audit this submission independently. Prior `AUDITED` labels are inputs, not proof of the new 29-11 route classifications.

## Required checks

1. **Campedelli map direction and endpoint implication**
   - Reverify that every admissible kernel is Q-defined and `S -> C_H` is Q-defined degree-8 etale after resolution.
   - Verify the one-way statement `endpoint Q-point -> C_H(Q)` for every audited H.
   - Do not demand torsor lifting for this pushforward implication; torsor descent is needed only for converse/lift classification.
   - Confirm the `8+2` geometric/Q(i) versus `6+2+2` certified Q-symmetry distinction and do not invent an exact Q-isomorphism-class count.

2. **Campedelli involution partial discharge — hostile source check**
   - Re-read Calabri--Mendes Lopes--Pardini, especially the classical `(Z/2)^3` Campedelli case.
   - Determine exactly whether all seven relevant nontrivial involution quotients are geometrically birational to rational or Enriques surfaces.
   - If yes, accept a child `R29-CAMP3-GEOM` discharge only at geometric/birational level.
   - Check whether the source or repo determines the exact rational-versus-Enriques assignment for the three certified Q-symmetry quotient representatives, and whether those birational models descend over Q. If not, keep parent `R29-CAMP3` partial/open.
   - Geometrically rational must never be rewritten as Q-rational.

3. **Campedelli arithmetic ceiling**
   - Search existing repo/source locks for an actual theorem making any audited `C_H(Q)` empty or forcing its physical image empty.
   - If found, the submitted AMBER status is materially wrong and must be repaired.
   - Keep `R29-CAMP4` Brauer computations from double-counting Q11-BRAUER.

4. **Beauville twist family**
   - Reverify the constant-Z/2 Q-cover and exact pointwise twist decomposition.
   - Attack the claim that infinitely many squareclasses can occur: find any theorem forcing finite ramification support or finitely many physical lift classes. If one exists, repair the route materially.
   - Recheck `R29-BEAU2A` swap-equivariance rather than assuming it from factor-swap symmetry.
   - Reconcile the Beauville source locator discrepancy (`Remark 1` versus `Remark 2`) without changing the already-audited mathematical content unless the source truly contradicts it.
   - Do not promote individual genus-two Selmer algorithms to uniform infinite-family closure.

5. **Modular arithmetic defect**
   - Independently verify `kappa in K8`, `|K8|=8`, and ordinary orbit sizes `1,3,3,1` from the audited checker/source.
   - Determine whether the sigma-twisted retained level-4 sign action has already been computed somewhere in the repo. If yes, close/repair `R29-MOD1C`; otherwise leave it open.
   - Recheck cusp/extra-stabilizer scope for `R29-MOD1D` and `R29-MOD2B`.

6. **R29-KUM5**
   - Do not identify arrangement `S4` with modular residual `S4` merely because both abstract groups are `S4`.
   - Attempt to find an explicit action-level correspondence on the seven branch labels / level structures and the associated Q-descent cocycle.
   - Close KUM5 only if the action and field-of-definition data are actually proved.

7. **Brauer open/proper firewall**
   - Reverify proper `Br_1(S)/Br(Q)=0` and proper odd-primary transcendental absence.
   - Verify that these do not kill `H^2(Q,UPic(Ubar))`, boundary Gersten residues, or two-primary evaluations on the physical open.
   - Check whether any current source computes the open Brauer group or its local evaluation sufficiently to give a Brauer--Manin obstruction. If so, the parent route may become GREEN.
   - Treat `NF-PHYS2`, `QWEB-CLIFFORD`, and `NF7` as tools/adapters unless an actual obstruction theorem is proved.

8. **Ownership and colors**
   - Reclassify `Q11-CAMPEDELLI`, `Q11-BEAUVILLE`, `Q11-MODULAR`, `Q11-BRAUER` as GREEN/AMBER/RED/MERGED from executable theorem strength.
   - Preserve 29-12 ownership of joint-V4/local/parametric/population interaction work.
   - Route count remains 11 unless a genuinely new primary mechanism is found.

## Required output

Create `stages/stage29/29-11/audit.md` and repair this same PR branch if needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
Q11_CAMPEDELLI=GREEN|AMBER|RED|MERGED
Q11_BEAUVILLE=GREEN|AMBER|RED|MERGED
Q11_MODULAR=GREEN|AMBER|RED|MERGED
Q11_BRAUER=GREEN|AMBER|RED|MERGED
R29_CAMP3_GEOM=<audited disposition>
R29_CAMP3=<audited disposition>
R29_KUM5=<audited disposition>
ATTACK_ROUTE_COUNT=<integer>
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the audit passes, expected next item is `29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO`.
