# Stage32EX6 scratch — V6 degree-8 genus-3 nef re-entry adapter wall

Status: `SCRATCH_SOURCE_LOCKED_DEGREE8_GENUS3_REENTRY_ADAPTER_REQUIRED_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

- retained EX6 PR inspected in this investigation: #1715, exact head `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`;
- parent scratch head before this write: `26925a4568268acddc56f096d8eb5ff77538def4`;
- preceding exact scratch verifier: `stages/stage32-ex6/scratch_verify_v6_eight_conic_exceptional_order_projection.py`;
- current V6 witness: `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`, canonical SHA256 `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`;
- Michael Stoll / Damiano Testa verification source: repository `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## 1. Input carried from the previous bounded leaf

For the current V6 class `C`, put

`D = C-K`.

The exact scratch chain found eight simultaneous fixed conics

`F = R_17+R_21+R_24+R_25+R_26+R_28+R_30+R_31`

and then

`D1 = C-K-F`.

The latest replay resolves the exceptional-row order and proves, against the source-locked classical 140 curves,

- `D1_negative_classical140_rows = []`;
- `D1_zero_classical140_rows = [11,98,116,128,132,137]`;
- `D1_classical140_all_nonnegative = true`.

This is a bounded nonnegativity statement on the known 140 curves only. It is not global nefness.

## 2. First curve layer not covered by the low-degree classification

The same Stoll--Testa verification source explicitly constructs the next negative-curve layer:

- `C4s`: genus-3 hyperelliptic curves of degree 8. The source has four sign families indexed by `(e1,e2,e3) in {+1,-1}^3`, hence `4*8 = 32` explicit curves;
- `C5s`: genus-3 nonhyperelliptic curves of degree 8 indexed by `(e1,e2,e3,e4) in {+1,-1}^4`, hence `16` explicit curves.

Thus there are `32+16 = 48` explicit degree-8 genus-3 curves immediately beyond the canonical-degree-at-most-six classification used in the previous leaf.

The source also defines an exact strict-transform intersection routine `intersection(C,j)` against the `92 known curves + 48 exceptional divisors` ordering and an `imageinPic(C)` routine that reconstructs a curve's Picard class from intersections with the fixed 64-index primitive basis.

## 3. What is and is not currently source-locked in Stage32

A search of the current `perfect-cuboid-game` default-branch code for the literal source identifiers `C4s` and `C5s` returned no registered adapter/output. This search miss is used only as a discovery result, not as a repository-wide nonexistence theorem.

In particular, the current Stage32 retained/scratch inputs inspected here do not contain a source-locked vector giving, for all 48 degree-8 curves,

- their intersections with the current V6 class `C`, or equivalently their Picard coordinates in the exact Stage32 basis;
- their intersections with the eight-conic fixed sum `F`;
- therefore the values `D1.G = C.G - K.G - F.G` needed for the next nef-obstruction scan.

The external Magma source contains enough algorithms to compute these data, but it does not serialize the required current-V6 48-curve intersection table in the inspected source text. Producing it would be a new algebraic-geometry computation, not a zero-cost reuse of the existing 140-curve replay.

## 4. Exact re-entry unit

The next bounded positivity unit is therefore:

1. source-lock the 48 curves in `C4s cat C5s` at the Stoll--Testa commit above;
2. compute and retain their exact strict-transform intersections with the Stage32 `indlist` basis, or an equivalent exact Picard-coordinate table;
3. bind that table to the current V6 witness canonical SHA256 above;
4. compute all 48 values `D1.G`;
5. if any value is negative, peel the forced component(s) and replay; if all are nonnegative, record only degree-8-layer nonnegativity and do not infer global nefness without a theorem covering higher canonical degree.

A heavyweight Magma/artifact-producing run is not authorized by the ordinary EX6 startup contract and was not started in this batch.

## 5. Decision

Canonical scratch decisions:

- `SIMULTANEOUS_TWO_PROJECTION_COMMON_CRITICAL_SUPPORT_AT_O266_NODES = EMPTY`;
- `SIMULTANEOUS_TWO_PROJECTION_ROUTE_GIVES_INDEPENDENT_ETA_RHO_CAP = false`;
- `D1_CLASSICAL140_ALL_NONNEGATIVE = true`;
- `D1_GLOBAL_NEF = UNPROVEN`;
- `NEXT_UNCHECKED_EXPLICIT_NEGATIVE_CURVE_LAYER = DEGREE8_GENUS3`;
- `DEGREE8_HYPERELLIPTIC_CURVE_COUNT = 32`;
- `DEGREE8_NONHYPERELLIPTIC_CURVE_COUNT = 16`;
- `DEGREE8_TOTAL_EXPLICIT_CURVE_COUNT = 48`;
- `CURRENT_STAGE32_DEGREE8_V6_INTERSECTION_ADAPTER = NOT_REGISTERED_IN_INSPECTED_INPUTS`;
- `NEW_MAGMA_OR_EQUIVALENT_EXACT_PICARD_COMPUTATION_REQUIRED = true`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`;
- `STAGE32_MAIN_ADVANCED = false`.

## Firewalls

- Nonnegativity on the classical 140 curves is not global nefness.
- The 48 degree-8 curves are an explicit next test layer, not a complete Mori-cone classification.
- A code-search miss for `C4s`/`C5s` is not proof that no adapter exists anywhere; exact discovery may be repeated before authorizing new compute.
- No `h1(C)=0`, `h0(C)=294`, O266 exclusion, or lower-O descent follows here.
- No heavy workflow, hostile-audit credit, MAIN promotion, or merge is authorized by this scratch leaf.
