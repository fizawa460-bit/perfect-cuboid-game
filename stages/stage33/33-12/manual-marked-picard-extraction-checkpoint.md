# Stage33-12 manual marked-Picard extraction checkpoint

Status: `READY_FOR_MANUAL_EXACT_EXTRACTION`

The Stage33-12 4/5 mathematical state is unchanged: the named J2 infinity exceptional class is geometrically attached, but its pinned marked-Picard coordinate has not yet been promoted to exact retained evidence.

The manual-only workflow `.github/workflows/stage33-12-j2-kc-exceptional-order.yml` now runs the order-independent source-locked materializer `materialize_j2_stoll_marked_picard_input.py`, then the deterministic checkpoint finalizer. The materializer identifies `P_inf_K=[1:0:0:0:-1:-1]` by its complete `CsK` incidence signature rather than treating Magma's `ptsK` enumeration order as semantic identity.

Persisted Actions evidence is bounded to the compact generated certificate plus the locally finalized result/controller checkpoint, with `retention-days: 1`. No expanded Stoll/Picard evidence is uploaded. This manual diagnostic is not an ordinary PR merge gate.

Firewalls remain unchanged:

- `STAGE33_12_CLOSED_EXACT=false`
- Stage33-13 remains blocked.
- Stage33-07 remains open.
- theorem/receiver/endpoint credit remains false.
- perfect-cuboid existence/nonexistence claims remain false.
