# Stage29-10 — global and K3 attack portfolio

```text
STAGE=Stage29
ITEM=29-10_GLOBAL_AND_K3_ATTACK_PORTFOLIO
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PRIMARY_MECHANISMS=FULL_ENDPOINT_DIRECT|LOWGENUS_PICARD|K3_SIGN_QUOTIENTS
ATTACK_ROUTE_COUNT_RETAINED=11
NEW_ATTACK_ROUTE_CREATED=false
NEW_ENDPOINT_THEOREM_PROVED_IN_29_10=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Scope and inputs

This stage consumes the audited pre-attack stack rather than replaying it:

- Gap Scan B targeted Stage14 backflow, including the certified endpoint upper theorem;
- 29-02c-LG2 finite Picard reduction and the Testa--Stoll low-degree curve package;
- 29-02e global coordinate-K3 eigenspace/modular identification;
- 29-06 exact endpoint-hub canonical/resolution distinction;
- 29-07 exact sign-tower and physical-population adapters;
- 29-08 exact Stage20/Testa--Stoll `K_c` adapter and physical polarization;
- 29-09 local arithmetic only as background, without re-crediting it here.

The three 29-10 route owners are

```text
G10-FULL-ENDPOINT
G10-LOWGENUS-PICARD
G10-K3-SIGN
```

No 29-11/12 receiver is executed here.

## 2. G10-FULL-ENDPOINT — strongest direct theorem is quantitative, not decisive

Gap Scan B certified the previously missed Stage14 corollary. Under the exact primitive/canonical endpoint convention,

```text
P(B)=T(B)
R=d on endpoint
```

and for every `epsilon>0`,

\[
\boxed{P(B)=T(B)\ll_\epsilon B^{1/2+\epsilon}.}
\]

This is now the strongest certified whole-endpoint counting input in the route. It is genuinely about perfect cuboids, not about an auxiliary exact-two stratum.

The bound has a hard logical ceiling:

- it does not imply `P(B)=0`;
- it does not imply `P(Q)` is finite;
- it is compatible with one, finitely many, or infinitely many sufficiently sparse endpoint points;
- the exact finite census `P(B)=0` through `10^9` cannot be concatenated with this asymptotic upper bound to obtain a global height cutoff.

Therefore rediscovering the same Stage14 bound earns no 29-10 attack credit.

### Fundamental-group / Chabauty--Kim rematch

The refreshed cuboid fundamental-group source (`arXiv:2310.12710v3`, 2026-07-06) proves simple connectedness of the projective cuboid surface and its resolution, and computes nontrivial fundamental groups/Malcev completions for selected smooth opens on the **face-cuboid** surface. It does not compute the unipotent fundamental group of the Stage29 physical endpoint open

```text
U = Sbar intersect D_+(a1*a2*a3),
```

nor does it construct a Kim function on that endpoint open.

Dan-Cohen--Jarossay's higher-dimensional Chabauty--Kim work on `M_{0,5}` supplies a genuine surface example, but not a general theorem that can be applied to the cuboid endpoint after a formal change of variables. The missing geometric and arithmetic adapters remain substantial.

```text
R29-PI1-OPEN=AMBER_NO_EFFECTIVE_CUBOID_ENDPOINT_KIM_ADAPTER
G10-FULL-ENDPOINT=AMBER_STRONG_GLOBAL_UPPER_NO_DECISIVE_FINISH
```

The exact next theorem species for this route is not another density estimate. A decisive continuation needs a **cuboid-specific effective rational-point theorem**: for example an effective finite-height classification, a local/global obstruction, or another theorem that actually makes `U(Q)` empty. A non-effective sparsity or density-zero statement is insufficient.

## 3. G10-LOWGENUS-PICARD — exact finite search, but no point-coverage theorem

The current Testa--Stoll paper, electronically published by *Mathematics of Computation* on 2026-08-10 (DOI `10.1090/mcom/4238`), states the complete classification of integral curves of degree at most six on the cuboid surface. This current publication does not invalidate the already-audited 29-02c-LG2 source lock; the repo had already consumed the degree-`<=6` computation and its K3-assisted degree-six step.

Together with the audited Freitag--Salvati Manni bound and the even-degree constraint, the residual unibranch finite search remains

```text
g=0: even d <= 176
g=1: even d <= 192
```

with degree `<=6` already classified. The Picard reduction to a finite negative-definite lattice ball is exact, but the repo correctly did **not** certify naive enumeration to these bounds as tractable.

The unresolved components remain

```text
R29-LG2     = symmetry-reduced complete numerical Picard-class enumeration
R29-LG2-EFF = effective-curve certification of surviving numerical classes
R29-LG2-MB  = multibranch/node carrier ledger outside the unibranch theorem
```

Even a complete discharge of all three would only exclude the corresponding rational/elliptic **curve carriers**. There is currently no theorem that every physical endpoint rational point must lie on one of those low-genus curves. A rational point on a surface is not automatically contained in a rational or elliptic curve.

Thus the finite Picard computation is useful supporting geometry, but it is not by itself an endpoint-emptiness algorithm.

```text
G10-LOWGENUS-PICARD=AMBER_FINITE_ENUMERATION_SUPPORT_NO_POINT_COVERAGE
LOWGENUS_ENUMERATION_ENDPOINT_DECISIVE_BY_ITSELF=false
R29-LG2=OPEN_EXACT_FINITE_SEARCH_RUNTIME_UNCLOSED
R29-LG2-EFF=OPEN
R29-LG2-MB=OPEN
```

Systematic slice/curve coverage is not silently imported here; the roadmap assigns that question to 29-14.

## 4. G10-K3-SIGN — exact quotient structure, no standalone rational-point obstruction

The endpoint has seven exact coordinate-sign quotient directions. At the normal-model level these are finite degree-two quotients of `Sbar`; their minimal resolutions are K3 surfaces. The audited Q-orbit pattern is

```text
3*K_a + 3*K_b + 1*K_c
```

and 29-02e globally identifies their transcendental pieces as

```text
K_a -> h8
K_b -> h16
K_c -> h32.
```

These are exact endpoint-specific quotient/cohomology statements. They do not say that a rational point on a K3 quotient lifts to the endpoint, and cohomological decomposition is not a rational-point obstruction.

29-08 additionally identifies `K_c` exactly with the Stage20/Testa--Stoll Euler K3 at normal/resolution/polarization level. That K3 has known rational families/curves, so a naive strategy of proving the relevant K3 surface has no rational points is already unavailable for this orbit.

### Terasoma receiver

Terasoma's 1988 four-quadric correspondence is valuable for smooth/normal-crossing complete intersections. Its quoted isomorphism/correspondence statements require the smooth/normal-crossing hypotheses in the relevant form, whereas the cuboid canonical model has 48 `A1` nodes. The singular-specialization/resolution adapter therefore remains unproved.

More importantly for the current endpoint attack, the cohomological output that motivated `R29-TERA1` is already supplied more directly by the exact cuboid-specific coordinate-K3 quotient and eigenspace argument of 29-02e. Proving the missing Terasoma specialization merely to reproduce that decomposition would not produce a new rational-point implication.

Accordingly this stage does **not** falsely mark the specialization theorem discharged. It demotes its execution priority:

```text
R29-TERA1=DORMANT_DOMINATED_FOR_CURRENT_RATIONAL_POINT_ATTACK
TERASOMA_SINGULAR_SPECIALIZATION_PROVED=false
TERASOMA_REPLAY_EARNS_ATTACK_CREDIT=false
```

A future theorem with genuinely stronger Chow/rational-point consequences may reactivate it.

The K3 route itself remains live as a supporting route because K3-specific curve, fibration, and arithmetic information can be pulled back along an exact Q-defined quotient. But simultaneous compatibility among several quotient conditions is joint/cross information and belongs to 29-12, not to this route.

```text
G10-K3-SIGN=AMBER_STRUCTURAL_SUPPORT_NO_STANDALONE_OBSTRUCTION
K3_CROSS_COMPATIBILITY_PRIMARY_OWNER=J12-JOINT-V4
```

## 5. Attack classification

No 29-10 route is promoted to GREEN on the present theorem surface.

```text
G10-FULL-ENDPOINT      = AMBER
G10-LOWGENUS-PICARD    = AMBER
G10-K3-SIGN            = AMBER
GREEN_ROUTE_COUNT_29_10=0
RED_ROUTE_COUNT_29_10=0
```

This is not a negative result about the perfect-cuboid problem. It means each direct/global route still lacks one endpoint-decisive theorem or coverage adapter.

The most important positive input is the certified global endpoint upper bound imported from Stage14. The most important compression is that neither a full low-genus Picard enumeration nor a replay of Terasoma's smooth correspondence should be mistaken for a standalone endpoint solution.

## 6. Downstream handoff

29-10 does not alter the 11-route count and does not reorder 29-11/12.

```text
ATTACK_ROUTE_COUNT_RETAINED=11
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-11_QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
