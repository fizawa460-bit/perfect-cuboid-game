# Stage32 RESIDUAL_32_01_PRODUCTION — exact pairing-prefix engine

This checkpoint is the first implementation released by the hostile-audited post-B16 residual-feasibility gate.

It does **not** run B18 and does **not** authorize the full 178-row residual sweep.

## Exact implementation in this checkpoint

The engine reuses the hostile-audited full-rank 64-row selected pairing subsystem from Stage32-05:

- selected rows: all 48 exceptional pairings plus 16 deterministic normal pairings;
- determinant: `274877906944`;
- inverse denominator: `8`;
- Smith invariants: `1^40, 2^14, 4^6, 8^4`.

If `S` is this 64x64 selected-pairing matrix and `B=8*S^{-1}`, then a full selected pairing vector `y` is in the Picard image lattice exactly when

`B*y == 0 (mod 8)`.

For a partial assignment on selected coordinates `A`, with unassigned coordinates `U`, extendability is tested exactly by the column lattice

`< B_U, 8 I_64 >`.

The implementation computes an exact Hermite normal form of this lattice and converts membership into deterministic integral congruence checks. Floating arithmetic is not used for pruning.

The same module also reconstructs full 140 pairing vectors at complete leaves and provides exact full-group leaf canonicalization after closing the source-locked nine geometric generators to `|Aut(S)|=1536`.

`prefix_aut_canonical_augmentation_implemented=false` in this checkpoint. Full-leaf canonicalization is implemented; safe prefix-level Aut pruning remains the next explicit engineering gate rather than being silently assumed.

## Representative calibration only

The initial calibration uses the exact assignment order

`selected exceptional coordinates 0..9, then selected normal coordinate 48`.

It profiles four representative residual rows, one for each `m=16/gcd(d,16)` class:

- `m=1`: `(g,d,e)=(0,16,8)`;
- `m=2`: `(0,8,8)`;
- `m=4`: `(0,12,8)`;
- `m=8`: `(0,10,8)`.

Each probe has a deterministic node budget of 250,000. Node-budget exhaustion is profile telemetry only; it is never converted to UNSAT, row completion, or receiver credit.

This calibration measures the pairing-lattice prefix layer. It does not yet certify full leaf/Hperp cost for any complete residual row.

## Actions/storage preflight

- heavy jobs: 1;
- effective Stage32 heavy concurrency from this workflow: 1 (`<=18`);
- raw Picard core and Aut export remain runner-local;
- persisted output: one compact JSON calibration certificate only;
- projected new artifact peak: `<1 MB`;
- artifact retention: 7 days;
- no full survivor/raw branch dump is persisted;
- workflow is cold on PR open and requires a dedicated run-key generation change in the exact `before..head` commit range before compute.

## Firewalls

```text
B18_RELEASE_AUTHORIZED=false
FULL_178_ROW_SWEEP_AUTHORIZED=false
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ROUTE_COLOR_CHANGE_AUTHORIZED=false
ENDPOINT_CREDIT=false
```

A successful calibration is an implementation/cost checkpoint only and must stop for fresh hostile audit before any broader production release.
