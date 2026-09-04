# Stage32 post-1504 anti-loop removal policy

Status: active Stage32-main execution-policy change.

The Stage32 anti-loop mechanism is removed as an execution or validation gate. Previously audited negative lanes, closed computations, and earlier asset searches remain retained provenance, but they no longer prohibit reopening a route, repeating an exact calculation, re-querying retained assets, or trying a different source-locked adapter when that work is useful to the active leaf.

This change does **not** weaken research-credit or provenance rules. A revisited route receives no mathematical credit merely because it was reopened. Any promoted claim must still use the active exact source locks, preserve population/model/field/quotient semantics, supply required adapters, and survive the ordinary verifier and hostile-audit process. Historical failures and superseded certificates remain historical evidence and must not be silently promoted.

Repository storage/heavy-compute safety is unchanged. Heavy workflows still require their normal explicit authorization and run-key gates.

For the current post-#1504 Stage32 leaf, retained-asset lookup and bounded source-lock work are authorized. The immediate target remains identification of the concrete `X(8) -> C0` `V4` torsor plane `W` in the retained Bolza `J(C0)[2]` basis, followed by pointwise testing of the 28 certified `Q=602` residue survivors. Reopening an older route is permitted if it contributes exact evidence to that target.
