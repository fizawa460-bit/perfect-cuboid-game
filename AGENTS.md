# Repository agent instructions

Keep this root file small. Stage-specific startup, history, and operating detail belong in the Stage entrypoint/state. Reusable research-process detail belongs under `docs/research-os/`.

## Repo-wide Actions safety

- Treat GitHub Actions artifact/storage capacity as a hard execution constraint. The repository operating budget is **500 MB** unless explicitly revised.
- Before artifact-producing compute, conservatively preflight peak stored footprint. For a new high-mass workflow, measure a representative shard before scaling.
- Keep raw exhaustive evidence runner-local when possible; persist compact deterministic certificates only after verification. Use bounded waves and short retention for necessary intermediates.
- Storage risk, upload failure, or materially larger-than-estimated artifacts are stop/cancel conditions. Do not trade mathematical exactness for storage.
- Detailed policy: `docs/research-os/policies/actions-storage-and-evidence-safety.md`.

## Heavy workflow rerun authorization

Heavy PR workflows must not rerun merely because a PR was synchronized, reopened, or docs/controller/status/source files changed. Every heavy job must remain behind a cheap authorization gate and run only when its dedicated run key is explicitly and semantically advanced/armed in the triggering commit range. If authorization cannot be verified, fail closed and skip heavy compute.

Detailed policy: `docs/research-os/policies/actions-storage-and-evidence-safety.md`.

## Research credit and claim promotion

Apply `docs/research-os/policies/research-credit-and-promotion-firewalls.md` before promoting any computation, bounded result, receiver, quotient/field/model result, or audited subclaim.

At minimum:

- finite/bounded/sample evidence is not a global theorem;
- computational, numerical, receiver, theorem, effectivity/existence, and endpoint credit stay distinct;
- changes of population, measure, field, quotient, model, mask, height, multiplicity, or other semantics require an exact adapter;
- do not double-charge a restriction/saving or assume independence without proof;
- formal classes/orbits/cohomology do not by themselves prove existence of the required geometric object;
- only the active controller's required audited closure releases downstream credit, and hostile audit may revoke it;
- a blocked route or finite zero hit is not impossibility;
- never claim perfect-cuboid existence/nonexistence without an explicit audited full-endpoint certificate.

Stage-local controllers may strengthen these firewalls but must not weaken them.

## Repository-wide research routing

Do not preload repository-wide catalogs during ordinary Stage startup. When the active leaf needs an existing weapon or evidence asset, use `docs/research-os/policies/repository-asset-discovery.md` for bounded Arsenal/evidence-locator lookup. For route broadening or parking decisions, use `docs/research-os/policies/cycle-exploration-safety-protocol.md`.
