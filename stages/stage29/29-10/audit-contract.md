# Stage29-10 adversarial audit contract

Audit this submission independently. Do not treat prior `AUDITED` labels as proof of the new route classifications.

## Required checks

1. **Stage14 endpoint theorem inheritance**
   - Verify that Gap Scan B's audited `P(B)=T(B)<<_epsilon B^(1/2+epsilon)` is imported exactly and not re-proved/re-credited.
   - Confirm that 29-10 makes no finiteness or nonexistence inference from it.

2. **Full-endpoint logical ceiling**
   - Check that finite `P(B)=0` data through `10^9` plus the asymptotic upper bound cannot produce a global height cutoff.
   - Check that no density-zero statement is treated as emptiness.

3. **Fundamental-group / Chabauty--Kim source scope**
   - Verify the current `arXiv:2310.12710v3` scope: compact cuboid surface/resolution versus selected open face-cuboid loci.
   - Verify that no computed unipotent fundamental group/Kim function for the Stage29 physical endpoint open has been silently imported.
   - Check that `M_{0,5}` is used only as a method example, not a transfer theorem.

4. **Low-genus/Picard route**
   - Verify the current Testa--Stoll publication state and that degree `<=6` classification was already consumed by 29-02c-LG2.
   - Recheck the `d<=176/192` finite-lattice reduction and its unibranch hypothesis.
   - Confirm that `R29-LG2`, `R29-LG2-EFF`, and `R29-LG2-MB` remain genuinely open.
   - Most importantly, attack the statement that low-genus carrier exclusion lacks point coverage: find any theorem in the repo or cited literature proving every physical endpoint rational point lies on a controlled low-genus curve. If such a theorem exists, the submitted AMBER classification is materially wrong.

5. **K3 quotient route**
   - Verify canonical-model versus resolution distinctions for all coordinate-sign quotients.
   - Verify the global `K_a/K_b/K_c -> h8/h16/h32` package is already supplied by 29-02e.
   - Verify the exact Stage20/Testa--Stoll `K_c` adapter from 29-08.
   - Check whether any individual Q-defined K3 quotient currently carries a theorem that excludes the relevant endpoint image open. Do not confuse target nonemptiness with lift compatibility.

6. **Terasoma demotion**
   - Re-read Terasoma's precise hypotheses and determine whether the 48-node cuboid specialization is covered directly.
   - If not, confirm that the singular-specialization adapter is still open.
   - Independently decide whether Terasoma has any rational-point/Chow consequence not already dominated by the exact cuboid-specific K3/eigenspace package. If yes, do not accept the `DORMANT_DOMINATED` disposition without repair.

7. **Ownership / double charge**
   - Simultaneous K3/V4 compatibility must stay with `J12-JOINT-V4`.
   - Peschmann/fibration coverage must stay with `J12-PARAMETRIC`.
   - 29-09 local arithmetic must not be re-credited.
   - Route count must remain 11 unless the audit finds a genuinely new primary mechanism.

8. **Final route colors**
   - Reclassify each of `G10-FULL-ENDPOINT`, `G10-LOWGENUS-PICARD`, and `G10-K3-SIGN` as GREEN/AMBER/RED/MERGED based on executable theorem strength, not optimism.
   - A GREEN route must name an exact theorem path whose successful discharge has an endpoint consequence.

## Required audit output

Create `stages/stage29/29-10/audit.md` and repair the same PR branch if necessary.

The final audit record must state at least:

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
G10_FULL_ENDPOINT=GREEN|AMBER|RED|MERGED
G10_LOWGENUS_PICARD=GREEN|AMBER|RED|MERGED
G10_K3_SIGN=GREEN|AMBER|RED|MERGED
R29_TERA1=<audited disposition>
ATTACK_ROUTE_COUNT=<integer>
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the audit passes, the expected next item is `29-11_QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO`.
