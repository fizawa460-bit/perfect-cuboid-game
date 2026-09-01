# Stage33 MAIN transient handoff

status: STOPPED_BY_USER_AFTER_EXTERNAL_QPIC_PRODUCER_SUCCESS
base_main_state_canonical_sha256: a864da1b51732a0ddf9874e8215efd7c42cdd2383935874f37bd56d091ab9c66

stop_boundary:
- User explicitly authorized the existing external/public Magma marked-Picard-bridge producer in this batch.
- User then explicitly requested STOP. Do not continue mathematical descent, Kummer/order-4 testing, state promotion, merge, or any further external producer dispatch until a later command resumes MAIN.

completed_external_step:
- Existing Stage33-07 marked Picard basis bridge producer path was armed with a one-shot bounded runkey and executed through GitHub Actions.
- Successful producer run: `33559031775`.
- The external Magma producer reached SUCCESS against the pinned Stoll source and emitted the literal 64x64 INDLIST-to-Magma Picard bridge.
- Emitted bridge canonical SHA-256 reported by the producer/artifact: `0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f`.
- The run's certifier also reached SUCCESS and checked the source-locked marked bridge plus actual swap/S3/V4/intertwining conditions. No theorem/receiver/endpoint/perfect-cuboid credit was promoted from this.

important_artifact_retention_state:
- During manual retention, an initial write of `stages/stage33/33-07/indlist-to-magma-picard-basis.json` was accidentally truncated to only two matrix rows. That truncated blob must never be treated as authority.
- Current branch was re-read after that incident at head `46dea6099ae2dc3d60ada66988fd190510a58b05`; the artifact path now has blob SHA `c9eb0e195e95263f6753fb29099ffa6d5d74dc13`, contains the nontrivial emitted matrix beginning with full 64-entry rows, and carries canonical SHA `0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f`.
- Because the user stopped immediately afterward, MAIN has NOT yet independently re-run the branch-local certifier against this retained blob and has NOT promoted the bridge into `MAIN-STATE.json` / controller authority. Treat the retained file as `PRESENT_BUT_PENDING_BRANCH_LOCAL_RECERTIFICATION_AND_STATE_SYNC`.

current_authority_firewall:
- Compact V9 / hostile-audit PASS authority remains the governing promoted state until branch-local recertification + explicit state sync are completed.
- progress remains `6/11` for authority purposes.
- `merge_allowed=false`.
- named J2 orientation remains `u1=[1,0]`.
- historical Picard-adjoint mask 6 is not authoritative named J2; `C2+C3=h_J2` remains revoked; masks 742/736 remain diagnostics only.
- Do not fall back to retained Smith/symmetry/nonunique bridge witnesses now that a source-authorized literal bridge has been produced.

resume_exactly_here:
1. Fresh-check PR #1476 / branch head first because parallel Stage33 chats may have moved it.
2. Read compact startup authority + this handoff only.
3. Verify `indlist-to-magma-picard-basis.json` is the complete retained artifact from run `33559031775`, shape exactly 64x64, canonical SHA exactly `0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f`.
4. Run the existing branch-local `certify_marked_picard_basis_bridge.py` against that retained artifact. Do NOT dispatch Magma again unless genuinely necessary and explicitly authorized again.
5. Only if recertification passes: descend the now-authoritative actual swaps into the pending order-4 affine-slice/Kummer leaf, write exact evidence, sync controller/MAIN-STATE, reset handoff when no delta remains, and run exact replay CI.
6. No merge and no theorem/receiver/endpoint/perfect-cuboid conclusion unless separately justified by later authority.
