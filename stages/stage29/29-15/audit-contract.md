# Stage29-15 — adversarial audit contract

Audit the endpoint Arsenal rematch independently. Do not accept a theorem classification merely because it appeared in Stage14, StructureRadar, or the submission. The point of 29-15 is to catch both false promotions and missed existing weapons.

## 1. Reconstruct the surviving receiver surface

Re-read the audited final states of 29-10, 29-11, 29-12, 29-13 and 29-14. Reconstruct the eleven primary attack routes and confirm their current colors before examining theorem matches.

Required baseline unless evidence changes it:

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

No theorem/tool species may be counted as a new primary route merely because it is useful on more than one receiver.

## 2. Full endpoint surface Chabauty — highest-priority hostile check

The submission claims a structural nonapplicability certificate.

Verify from the audited endpoint geometry that the smooth minimal resolution `S` satisfies

```text
q(S)=h^1(S,O_S)=0.
```

Then verify the universal property of the Albanese: every morphism from the smooth projective `S` to an abelian variety factors through `Alb(S)`. Conclude carefully whether `Alb(S)=0` indeed prevents a positive-dimensional embedding of `S` into any abelian variety.

Read the exact hypotheses of Caro–Pasten's surface Chabauty-Coleman theorem and the Balakrishnan–Caro refinement. If the theorem does not require an abelian embedding in the form stated by the submission, repair the classification.

Only if the full chain survives accept

```text
R29_ARS_SURFACE_CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

Do not extend this nonapplicability to auxiliary covers, curves, or irregular quotient/cover constructions without checking their own Albanese data.

## 3. Curve arithmetic toolkit

Check the fresh rank-zero elliptic-quotient source and the standard Chabauty/MW-sieve/quadratic-Chabauty theorem species.

For each proposed use against `R29-LG2`, `R29-LG2-EFF`, `R29-FIB1`, `R29-FIB2`, `R29-PESCH2` verify that the required data are genuinely available:

```text
Q-defined curve/fiber,
exact quotient or Jacobian,
Mordell-Weil rank/Selmer information,
map/reconstruction to the physical endpoint,
field of definition,
uniformity if the base parameter moves.
```

Do not convert a successful individual-fiber algorithm into a uniform infinite-family theorem.

Search the current literature for a theorem that actually supplies the missing uniformity for the specific genus-5 / Master-Hit family. If one exists, repair positively rather than deferring it.

## 4. K3 / Brauer rematch

Check Tawfik–Newton and any stronger current K3 Brauer theorem against the exact coordinate-sign K3 quotients.

Verify whether any cuboid K3 is already proved in the repo to be a Kummer surface `Kum(E x E')` satisfying a source theorem's CM and field hypotheses. Cohomological newform matching alone is not a Kummer-model isomorphism.

If an exact model exists, compute whether the theorem provides a nonconstant Brauer class and whether its evaluation obstructs the **physical endpoint image locus**, not merely weak approximation on the whole K3.

If not, retain `APPLICABLE_AFTER_EXACT_ADAPTER`.

## 5. Campedelli / Beauville / modular

### Campedelli
Verify that the geometric involution/rational-or-Enriques classification is already consumed and that no current arithmetic theorem turns the exact Q-defined quotient into endpoint Q-point emptiness.

### Beauville
Attack the claim that current twist statistics are insufficient. Search for a theorem controlling **every** quadratic twist in the exact family, or proving that physical endpoint points use only finitely many twist classes. An almost-all theorem is not enough unless the exceptional twist set is explicitly and exhaustively controlled.

### Modular
Search current 8-congruence/X(8) literature for an exact theorem eliminating the relevant sigma-twisted classes or solving the action-level S4/cocycle adapter. Do not identify abstract isomorphic S4 groups without an action-level proof.

## 6. Physical-open Brauer

Re-read 29-11. Confirm what is proved for the proper endpoint and what remains for the physical open.

Search for a theorem that makes the two-primary boundary calculation formal from the known 72-component boundary, or otherwise computes the required UPic/Gersten/Brauer group and local evaluations. If exact input data are still missing, keep the theorem species adapter-gated.

Do not treat proper Brauer triviality as open-locus Brauer triviality.

## 7. Local / sieve / StructureRadar rematch

Read at least:

```text
docs/stage14-arsenal.md
docs/structure-radar/arsenal/SR-ARSENAL-24.md
docs/structure-radar/arsenal/SR-ARSENAL-25.md
docs/structure-radar/PAUSE_AND_RETURN_STAGE27_2026-08-20.md
```

Check the submission's treatment of `SR-STR-161,162,163,164,165,166,169,170,171,173,174,223` against their exact receiver/measure contracts.

In particular, determine whether 29-06 through 29-14 has supplied any adapter that was absent when StructureRadar classified a card as `EXTERNAL_GATE`. If yes, reopen that card **only for the exact new endpoint receiver** and test the actual theorem immediately.

This is the most important anti-miss check in 29-15.

## 8. Parametric route

Reconfirm that global Master-Hit coverage is proved and that `R29-PESCH-E1` is still a conjecture rather than a theorem.

Search current source/repository state for a proof or independently certifiable replacement of E1. If found, this is material and may turn `J12-PARAMETRIC` GREEN or stronger.

Do not replay finite 1,072-fiber or bounded Mordell-Weil computations as global coverage.

## 9. Population interaction

Recheck that the population/counting Arsenal has already been consumed in the endpoint upper and 29-12 relative-density theorem.

Search specifically for any existing theorem in Stage14–28 / StructureRadar that, after the new Saunderson nonendpoint lower and current `M3` knowledge, actually controls

```text
P(B)/M3(B).
```

If none does, preserve the firewall. Do not divide upper/lower bounds whose exponents do not justify a ratio limit.

## 10. Fresh literature completeness check

The submission searched these ecosystems:

- surface Chabauty / higher-dimensional Chabauty;
- curve Chabauty and rank-zero quotients;
- K3 Brauer/rational points;
- Campedelli/involutions;
- Beauville/twist descent;
- modular/8-congruence;
- local/sieve/thin-set/counting.

Perform a targeted search for omitted theorem species whose hypotheses now match an exact Stage29 receiver. Search absence is not a novelty claim, but a concrete theorem match must be applied now rather than postponed to 29-16.

## 11. Double-credit and route compression firewall

Imported results do not earn 29-15 attack credit:

```text
Stage14 endpoint upper
29-08 Master-Hit global coverage
29-11 Campedelli/Beauville/modular/Brauer structure
29-12 local data and population GREEN theorem
29-13 Saunderson/B(q) closures and M3-P lower
29-14 slice/quotient coverage semantics
Testa-Stoll degree<=6 classification.
```

29-15 may create theorem-applicability or nonapplicability certificates, but final primary-route compression belongs to 29-16 unless an exact redundancy/death is already proved.

## Required output

Create `stages/stage29/29-15/audit.md` and repair this same branch/PR if needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
ARSENAL_REMATCH_COMPLETE=true|false
R29_ARS_SURFACE_CHABAUTY=<audited disposition>
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=true|false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=<integer>
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=<integer>
ATTACK_ROUTE_COUNT=<integer>
GREEN_ROUTE_COUNT=<integer>
AMBER_ROUTE_COUNT=<integer>
P_OVER_M3_SCALE_KNOWN=true|false
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the submitted routing survives, next item is

```text
29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO.
```
