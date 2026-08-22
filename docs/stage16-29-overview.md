# Stage16-29 research overview — what was done, what closed, what remains

Status: **Stage16-28 closed program + Stage29 current through audited 29-14**.

This is the short-form research-state document for the Stage16-29 perfect-cuboid program. It is intentionally different from the canonical roadmap: the roadmap says **what to do**; this file says **what was actually learned, what is closed at its stated scope, and what is still open**.

For operating details, read this file first, then descend into:

- [Stage16-29 canonical roadmap](stage16-29-population-roadmap.md)
- [Stage29 roadmap](../stages/stage29/roadmap.md)
- [Stage29 route registry](../stages/stage29/29-05/route-registry.json)
- [Stage29 numerical ledger](../stages/stage29/numerical-ledger.md)

## 1. One-screen current state

All numbered populations use the same physical convention unless explicitly stated:

```text
0 < a < b < c
gcd(a,b,c)=1
R=sqrt(a^2+b^2+c^2) <= B
```

Define:

- `M1`: exactly one integral face diagonal, no space requirement;
- `N1`: exactly one integral face diagonal + integral space diagonal;
- `M2`: exactly two integral face diagonals, no space requirement;
- `N2`: exactly two integral face diagonals + integral space diagonal;
- `M3`: all three face diagonals integral = primitive canonical Euler cuboids, no space requirement;
- `P`: all three face diagonals + integral space diagonal = perfect-cuboid endpoint.

The strongest certified population surface entering/inside Stage29 is:

| Population | Strongest certified global result | Current status |
|---|---|---|
| `M1(B)` | `~ 3/(4*pi^2) B^2 log B` | asymptotic scale closed |
| `N1(B)` | `~ kappa/(24*pi) B(log B)^3`, `kappa>0` | asymptotic scale closed |
| `M2(B)` | `~ C_M2 B(log B)^5`, `C_M2>0` | asymptotic scale closed |
| `N2(B)` | `B^(1/4) << N2(B) <<_eps B^(1/2+eps)` | infinite and zero-density; true exponent open |
| `M3(B)` | `liminf M3(B)/B^(1/3) >= 27/(40*pi^2)` and `M3(B) <<_eta B(log B)^(5-eta)` for every fixed `eta<1/46` | infinite; true exponent/asymptotic open |
| `P(B)` | `P(B) <<_eps B^(1/2+eps)`; exact census `P(B)=0` for `B<=10^9` | existence/nonexistence and true scale open |

The main literal-survival ratios are now:

```text
N1/M1 ~ (kappa*pi/18) (log B)^2/B -> 0

B^(-3/4)(log B)^(-5)
  << N2/M2
  <<_eps B^(-1/2+eps)(log B)^(-5)
  -> 0

M3/(M2+M3) -> 0

P/M3 = UNKNOWN
```

The final population frontier is therefore not whether earlier conditions are rare — that is already proved — but:

```text
FINAL_LITERAL_SURVIVAL = P(B)/M3(B)
GLOBAL_SCALE           = UNKNOWN
PERFECT_CUBOID_EMPTY   = NOT PROVED
PERFECT_CUBOID_EXISTS  = NOT PROVED
```

## 2. What each Stage did

| Stage | Main object / comparison | What it established | What remained |
|---|---|---|---|
| **16** | `M1`: exactly one integral face | one-face population has order `B^2 log B`; common primitive/canonical `R<=B` population contract frozen | no endpoint question |
| **17** | `N1`: one face + space | exact asymptotic `N1 ~ kappa/(24*pi) B(log B)^3`; space condition is zero-density inside `M1` | none at this stratum's scale |
| **18** | `M2`: exactly two faces | exact asymptotic `M2 ~ C_M2 B(log B)^5`; zero density in the ambient 3D primitive population | constant structure can still be refined, but scale is closed |
| **19** | `N2`: two faces + space | half-power upper, exact squareclass/Gaussian-norm formulation, independent local zero-density mechanism | true exponent and lower scale were initially open; later Stages25/27 upgrade lower to `B^(1/4)` |
| **20** | `M3`: Euler cuboids | K3 completion model, local blocker law and global log-saving upper | original lower was weak; Stages26/28 upgrade it to exact one-third-scale liminf; true exponent still open |
| **21** | `16 -> 17` | exact space cost after one face: intrinsic polynomial cost `B^-1` with positive `(log B)^2` interaction enhancement versus ambient space integrality | fine decomposition of the two logarithms not canonical |
| **22** | `16 -> 18` | `M2/M1 ~ const*(log B)^4/B`; isolates second-face polynomial loss and logarithmic compensation | no unique factor-by-factor decomposition of `log^4` |
| **23** | `17 -> 19` | second-face condition remains zero-density when space integrality is already present; no double charging of the space condition | true `N2` exponent remained open |
| **24** | literal `18 -> 19` | proved `N2/M2 ->0` and `N2 -> infinity`; separated thin-cover, local-squareclass and quantitative-upper mechanisms | true exponent, strict sub-sqrt upper, and interaction sign were not yet closed |
| **25** | `16 -> 19` combined thinning | constructed primitive `N2` families of order `B^(1/4)`; proved positive divergent interaction between second-face and space conditions | no lower exponent above `1/4`; no sub-sqrt whole-family upper |
| **26** | `18 -> 20` | proved Euler completion probability tends to zero; restored full two-parameter Saunderson input and raised `M3` lower to `B^(1/3-o(1))` | `M3` true exponent/asymptotic and fixed-power upper remain open |
| **27** | strict `18 -> 19` reattack | aggressively exhausted current repo-native upper/lower routes; retained `1/4 <= exponent <= 1/2`; localized the missing input to same-measure support/correlation/uniformity or a denser construction | true `N2` exponent remains open |
| **28** | matched `19 -> 20` bridge | put the Stage19 space-completion K3 and Stage20 third-face K3 over the same toric base and same physical polarization; identified branch/fixed-curve differences; normalized the interaction threshold | no eventual ordering of `M3` vs `N2`; moving-complement interaction theorem remains open |
| **29** | direct endpoint foundation/route synthesis | global endpoint geometry, sign/Kummer and quotient architecture, exact population adapters, local/parametric/quotient attacks, thin-family closures, natural-slice coverage tests, exact finite endpoint census | 10 endpoint routes remain AMBER; endpoint existence/nonexistence and `P/M3` remain open |

Primary source bundles:

- [Stage16 final](../stages/stage16/final.md)
- [Stage17 final](../stages/stage17/final.md)
- [Stage18 final](../stages/stage18/final.md)
- [Stage19 final](../stages/stage19/final.md)
- [Stage20 final](../stages/stage20/final.md)
- [Stage21 final](../stages/stage21/final.md)
- [Stage22 closeout](../stages/stage22/22-70/result.md)
- [Stage23 closeout](../stages/stage23/23-70/result.md)
- [Stage24 closeout](../stages/stage24/24-70/result.md)
- [Stage25 closeout](../stages/stage25/25-70/result.md)
- [Stage26 closeout](../stages/stage26/26-70/result.md)
- [Stage27 final](../stages/stage27/final.md)
- [Stage28 final](../stages/stage28/final.md)

## 3. The important condition-interaction picture

The program began as a population ladder, but the main mathematical lesson is that the conditions are **not independent filters**.

### One face -> space

```text
N1/M1 ~ (kappa*pi/18)*(log B)^2/B.
```

The underlying space-diagonal polynomial cost is `B^-1`, but one-face conditioning enhances survival by `(log B)^2`.

### One face -> two faces

```text
M2/M1 ~ const*(log B)^4/B.
```

The second Pythagorean face removes one polynomial degree of freedom but brings a large logarithmic compensation from the coupled toric/shared-edge structure.

### Two faces -> space

```text
B^(-3/4)(log B)^(-5)
  << N2/M2
  <<_eps B^(-1/2+eps)(log B)^(-5).
```

This is a literal subset transition. It is zero-density but infinite. Stage25/27 show that two-face conditioning **positively enhances** space survival relative to the ambient and one-face-conditioned baselines.

### Two faces -> three faces

The literal host is `H_ge2=M2 disjoint_union M3`. The Euler share tends to zero:

```text
M3/(M2+M3) -> 0.
```

The true `M3` exponent remains unknown despite the one-third lower construction and log-saving upper.

### Stage19 vs Stage20

Stage28 compares two different completions of the same two-face geometry rather than treating them as nested populations.

Both are degree-two K3 covers of

```text
Y = Bl_4(P1 x P1),  L=-K_Y,
M_sp^2=M_face^2=8.
```

The first certified geometric differential is:

```text
Stage19 space cover      : 4 genus-0 branch components
Stage20 third-face cover : 2 genus-1 branch components
```

and the low-degree physical spectrum contains:

```text
Stage19 physical M-degree 4 rational curves : absent
Stage20 Saunderson physical M-degree         : 6
Stage19 physical M-degree 6 absence          : not proved
```

This is structural separation, not a theorem ordering the whole populations.

## 4. What Stage29 added beyond population counting

Stage29 changed the project from a sequential population study into a direct endpoint research map.

### Global endpoint architecture

The endpoint is organized simultaneously through:

- the full four-quadric cuboid surface;
- the joint residual `V4` completion over the two-face base;
- the degree-64 seven-line sign/Kummer cover of `P2` with deck group `(Z/2)^6`;
- seven coordinate-sign K3 quotient directions;
- Campedelli quotient compression;
- the Beauville irregular double cover;
- modular / `M(4,8)` / `X(8)` descriptions with field-of-definition firewalls;
- endpoint L-function / K3-character decomposition;
- non-Fano/Hirzebruch recognition over `Q(i)` with an explicit `Q` twist.

The broad 29-02 screen did **not** certify a ninth independent foundation; this is not a literature-exhaustiveness theorem.

### Exact adapters that are now closed

Stage29 proved or audited, among other things:

- exact crosswalk between the full sign cover and the Stage19/20 residual completions;
- exact physical population-mask / selected-subcover incidence dictionary;
- exact Stage20/Testa-Stoll Euler K3 identification with physical polarization match;
- exact Master-Hit global coverage of every primitive Euler brick / endpoint candidate;
- global coordinate-K3 transcendental character decomposition;
- global endpoint pushforward to the smooth loci and minimal resolutions of the Q-defined sign-K3 quotients;
- physical endpoint avoidance of all F7 branch lines;
- no physical endpoint point on the Q-liftable coordinate-permutation fixed loci;
- complete degree-`<=6` endpoint curve-carrier classification with no positive nondegenerate physical family;
- exact one-face and selected-two-face space-survival theorems on legal nested hosts.

### Thin families now closed

Stage29-13 independently closed:

- the full nondegenerate Saunderson Euler-brick family against perfect completion;
- the explicit `B(q)=(4q,q^2-4,2(q^2-1))` family by Pell/Lucas arithmetic.

Together with the audited Saunderson lower construction this gives an explicit positive lower theorem for non-endpoint Euler cuboids:

```text
liminf (M3(B)-P(B))/B^(1/3) >= 27/(40*pi^2) > 0.
```

This still does **not** imply `P/M3 -> 0`.

## 5. Current Stage29 route portfolio

The current authoritative attack portfolio contains 11 primary routes.

```text
G10-FULL-ENDPOINT       = AMBER
G10-LOWGENUS-PICARD     = AMBER
G10-K3-SIGN             = AMBER
Q11-CAMPEDELLI          = AMBER
Q11-BEAUVILLE           = AMBER
Q11-MODULAR             = AMBER
Q11-BRAUER              = AMBER
J12-JOINT-V4            = AMBER
J12-LOCAL-SQUARECLASS   = AMBER
J12-PARAMETRIC          = AMBER
J12-POP-INTERACTION     = GREEN
```

`GREEN` here means a route produced new certified theorem-level progress. It does **not** mean the perfect-cuboid endpoint is solved. `J12-POP-INTERACTION` is GREEN because exact incidence/nested-host survival theorems were proved; its final `P/M3` step is still open.

The main unresolved endpoint-decisive gaps are:

- full endpoint: no effective theorem making the physical endpoint open empty;
- low-genus/Picard: `R29-LG2`, `R29-LG2-EFF`, `R29-LG2-MB` remain open, and curve-carrier closure still lacks a point-coverage theorem;
- K3: exact quotients exist, but no standalone rational-point obstruction closes the endpoint;
- Campedelli: no audited quotient with `C_H(Q)=empty`;
- Beauville: no finite physical twist set / uniform Selmer closure;
- modular: twisted arithmetic defect/action and cusp adapters remain open;
- Brauer: proper algebraic and odd-primary pieces are largely closed negatively, but the physical-open boundary/two-primary problem remains;
- joint V4: the final joint ratios including `P/M3` remain unknown;
- local squareclass: exact local data exist, but the physical-height global transfer is missing;
- parametric: Master-Hit has global candidate coverage, but the universal exponent-one blocker remains conjectural.

See [Stage29-10](../stages/stage29/29-10/result.md), [29-11](../stages/stage29/29-11/result.md), [29-12](../stages/stage29/29-12/result.md), [29-13 audit](../stages/stage29/29-13/audit.md), and [29-14 audit](../stages/stage29/29-14/audit.md).

## 6. Exact finite evidence — useful but not a theorem of nonexistence

The matched Stage29 exact census reaches `B=10^9`:

```text
M2(10^9) = 51,379,127,865
N2(10^9) = 4,566
M3(10^9) = 4,362
P(10^9)  = 0
```

Thus no primitive canonical perfect cuboid occurs under the physical cutoff `R<=10^9` in the audited exact census.

Firewall:

```text
P(B)=0 for B<=10^9  !=  P(B)=0 for all B.
```

No finite trend is used to identify a true exponent, eventual ordering, or global endpoint theorem.

## 7. What is genuinely closed now

At the level stated in the corresponding theorem contracts, the following can be treated as stable inputs rather than repeatedly reopened:

1. the common primitive/canonical physical cutoff and multiplicity conventions;
2. the `M1`, `N1`, and `M2` asymptotic scales;
3. `N2` is infinite and zero-density inside `M2`, with certified exponent corridor `[1/4,1/2]` in the power sense;
4. `M3` is infinite and zero-density inside the legal at-least-two-face host, with an explicit one-third lower construction and log-saving upper;
5. the major Stage16-28 condition-interaction identities and no-double-charge firewalls;
6. the Stage19/Stage20 common-base K3 bridge and physical polarization comparison;
7. Stage29 endpoint/sign/K3/Campedelli/Beauville/modular structural maps already explicitly audited;
8. Master-Hit global Euler/endpoint-candidate coverage;
9. Saunderson and explicit `B(q)` endpoint exclusions;
10. degree-`<=6` endpoint carrier classification and the natural branch/permutation-fixed slice exclusions;
11. exact finite census through `R<=10^9`.

“Closed” above means **closed at that scope**. None of these items is a proof of global perfect-cuboid nonexistence.

## 8. What remains before Stage29 closeout

The planned remaining Stage29 sequence is:

```text
29-15  ENDPOINT_ARSENAL_REMATCH
29-16  RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
GAP_SCAN_FINAL / ROADMAP_REVIEW_FINAL
29-17  PERFECT_CUBOID_ATTACK_HANDOFF
29-close
```

Before final closeout, every surviving OPEN receiver should be classified into one of four dispositions:

```text
1. EXECUTE_NOW
   finite/bounded work that can still be completed with current tools;

2. CURRENT_METHOD_EXHAUSTED
   materially distinct repo-native attacks were already carried out and the exact missing theorem is known;

3. NEW_THEOREM_REQUIRED
   a genuinely stronger external mathematical input is needed;

4. DORMANT_NONDECISIVE
   technically open, but closing it would not materially move the endpoint attack at present.
```

Particular still-executable/bounded candidates that must not be silently hidden under `AMBER` include the residual low-genus Picard/effectivity/multibranch work and other explicitly `OPEN_BOUNDED` ledgers recorded in the Stage29 registry.

## 9. Final research interpretation

Stage16-29 has **not solved the perfect-cuboid problem**. What it has done is much more precise than “searched and found nothing”:

```text
1. fixed one physical population language;
2. measured the major lower strata and their interactions;
3. proved strong rarity/zero-density statements without confusing them with emptiness;
4. constructed explicit infinite survivor families and sharp lower corridors where possible;
5. identified the common K3/cover geometry behind competing completion conditions;
6. built a global endpoint map with exact quotient/field/coverage firewalls;
7. eliminated several thin families and low-degree carriers;
8. reduced the remaining endpoint problem to a finite portfolio of explicit theorem/adapter receivers.
```

The clean final frontier is:

```text
Perfect cuboid existence/nonexistence : OPEN
P(B)/M3(B)                            : OPEN
true N2 exponent                      : OPEN
true M3 exponent/asymptotic           : OPEN
11-route endpoint portfolio           : 1 GREEN / 10 AMBER
finite exact endpoint search          : zero hits through R<=10^9
```

That is the state Stage29-15/16 should compress and hand off, rather than reopening the already-audited Stage16-28 program.
