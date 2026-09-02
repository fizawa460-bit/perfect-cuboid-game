# Stage34 MAIN batch handoff

```text
STATUS=MAIN_AWAITING_SEPARATE_CANDIDATE_AUDITS
PR=#1482 OPEN
BRANCH=stage34-02b-genus2-rankle1-rationalpoints
AUTHORITATIVE_REMAINING=22
AUTHORITATIVE_SIGN_ORBITS=11
FIVE_ORBIT_CANDIDATE_BRANCHES_WITH_SIGN_TRANSFER=10
FIVE_ORBIT_CANDIDATE_SIGN_ORBITS=5
HARD_MOD13_CANDIDATE_BRANCHES=4
HARD_MOD13_CANDIDATE_SIGN_ORBITS=2
DO_NOT_MERGE=true
```

Authoritative state is unchanged from the previous hostile-audit promotion: residual `22` d1 branches / `11` audited sign orbits, by-q `{20/99:4,24/7:0,48/55:0,60/11:6,80/39:4,84/13:8}`. Neither candidate family below is authoritative without its own separate hostile audit. Do **not** combine prospective counts as current state.

Ordinary audit review `5085206299` at head `5504e131e798b841423eef5d0cfb187872787d7f` failed only because Candidate A's machine-readable q=20/99 exclusion set contained two mistyped branch IDs. The manifest is now repaired to the authoritative hard representatives `0de8f4d61c834bdf136b` and `6c9e0174b4ec2e232143`; no closure credit or MAIN promotion follows from this repair. A fresh separate audit is still required.

## Candidate A — five exact sign orbits

Read first:

1. `stages/stage34/34-02/d2-stageA2-five-exact-orbit-preaudit-manifest.json` — blob `ed500535ab9258bbf3319ddfe520c29ca96840f1`;
2. `stages/stage34/34-02/d2-stageA2-five-exact-orbit-replay-lock.json` — blob `9a1b13e5bf5be8b0f16a98df238a18e1cbf4a417`;
3. only source evidence named there if deeper replay is required.

Five direct representatives have complete exact quotient point sets plus exact parent pullback with zero nondegenerate full-parent lifts:

- q=`60/11`: `06bcc4e821a7d482a435`, `6c6d7f3a758500d6b585`, `70158c7fb753b71bd2dd`;
- q=`84/13`: `54a9782fc24a5475166c`, `8f9ca1a5b214779b0af7`.

Their five listed sign partners are candidate-only. If and only if a separate hostile audit validates the five direct proofs plus the already-audited sign transfer, this candidate alone would give residual `12` branches / `6` sign orbits, by-q `{20/99:4,24/7:0,48/55:0,60/11:0,80/39:4,84/13:4}`.

The repaired generation-2 source is artifact `9828805411`, digest `sha256:e226ab93347c0ee0bfa3f3390f7c1c916d22df206507106482501edb677effab`; generation-1 six-adapter credit remains explicitly revoked. Four generation-2 compute-incomplete cases remain OPEN and are not mathematical failures: `169f94dd000a9c5c053f`, `40dc8f63e92a8a3a65e8`, `7a7ef1a67e794fe1651f`, `99448685b81e29427c3f`.

The bounded retry run `33582894768` completed operationally green but closed `0/4`; the retained certificate records HTTP 504 or missing `PROOF_REPLAY_COMPLETE`, so all four remain OPEN.

## Candidate B — hard q=20/99 receiver intersection, exact p=13 obstruction

Read first:

1. `stages/stage34/34-02/d2-stageA2-hard-rank02-receiver-intersection-mod13-preaudit.json` — blob `c21a53416a2e0f82d0a7d3d291965641d2f99b0c`;
2. `stages/stage34/34-02/verify_d2_stageA2_hard_rank02_receiver_intersection_mod13.py` — blob `d80d7e959fdd0106ab076c3b71b478fabb79eaa7`;
3. `stages/stage34/34-02/d2-stageA2-hard-rank02-two-orbit-lock.json` — blob `fc8fb6fe8557ab1b626bfb49228733753556bb2b`.

Exact hard orbits:

- `0de8f4d61c834bdf136b` ↔ `1f5f04661b6ace1279b8`, delta `[-6,10,510,-34]` / its global negative;
- `6c9e0174b4ec2e232143` ↔ `81bdbd19aed01cc4a379`, delta `[-5,3,17,-255]` / its global negative.

Important semantic repair: the previously found nondegenerate four-factor points `t=1/5` and `t=2/3` are genuine reconstruction-branch points, but the StageA2 four-factor condition alone is an overapproximation of the receiver fiber product. They map to rational `E_{20/99}` points with receiver x-values `-16/33` and `-25/297`, yet direct exact evaluation gives the same nonsquare `F3=730249/480249`; they are not `K_{20/99,1}` points.

For d=1 write

```text
U=T^2-S^2
V=2TS
A=20U+99V
B=99U+20V
x=(20/99) U/V
```

The required split quartic condition is exactly

```text
A^2+B^2 = 99^2 K_{20/99,1}^{hom}(T,S) = square.
```

At `p=13`, every delta entry is a unit and `13 ∤ 2ab(a^2-b^2)`. Exhaustive `P^1(F_13)` replay for each of the four exact delta tuples leaves only the same two four-square branch residues:

- `[T:S]=[5:1]`: `(U,V,A,B)=(11,10,1,2)`, so `A^2+B^2=5 mod 13`;
- `[T:S]=[8:1]`: `(U,V,A,B)=(11,3,10,5)`, so `A^2+B^2=8 mod 13`.

Both `5` and `8` are nonsquares mod 13. The p-integrality reduction in the preaudit manifest therefore gives empty receiver/K intersection for all four branches. This does **not** claim the factor branches themselves have no Q-points and does not require complete genus-two point enumeration.

If and only if a separate hostile audit validates the K identity, p-integrality argument, all 14 projective residues per branch, and receiver-scope adapter, this candidate alone would close exactly `4` branches / `2` sign orbits for the receiver population, giving prospective residual `18` / `9`, by-q `{20/99:0,24/7:0,48/55:0,60/11:6,80/39:4,84/13:8}`.

Do not arm the cold higher-rank `TwoCoverDescent` diagnostic while this cheaper exact local obstruction is pending audit.

## Next exact obligations

Separate hostile audit is required before either candidate receives promotion. Candidate A and Candidate B are logically independent preaudit bundles. After any audit result, fresh-read PR head / reviews / `MAIN-STATE.json` and promote only the specifically authorized scope.

Keep OPEN: `D2_all_factor_branches_closed`, `direct_cover_rational_points_complete`, `all_multiples_closed`, `R29-EXT-CHANG-C`, and all parent-route / perfect-cuboid claims.
