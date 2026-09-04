# Repository agent instructions

Keep this root file small. Stage-specific startup, history, and operating detail belong in the Stage entrypoint/state; reusable research-process detail belongs under `docs/research-os/`.

During ordinary Stage startup, do not preload Research OS. Follow the Stage-local startup contract and open Research OS only on the explicit triggers below.

## Repository traversal discipline

Repository discovery is search-first, not tree-first. Do not acquire a recursive repository tree by default. Fetch known paths directly; use GitHub search for filenames/paths and GitHub code search for terms, symbols, identifiers, or phrases; follow controller, roadmap, source-lock, certificate, or other authority references only to the exact targets needed for the active leaf. Use a recursive tree only when exhaustive file enumeration is itself an explicit research requirement. A search miss never proves repository-wide absence; broaden only under the active Stage/search policy.

## Repo-wide Actions safety

- Treat GitHub Actions artifact/storage capacity as a hard execution constraint. The repository operating budget is **500 MB** unless explicitly revised.
- Before artifact-producing compute, conservatively preflight peak stored footprint. For a new high-mass workflow, measure a representative shard before scaling.
- Keep raw exhaustive evidence runner-local when possible; persist compact deterministic certificates only after verification. Use bounded waves and short retention for necessary intermediates.
- Storage risk, upload failure, or materially larger-than-estimated artifacts are stop/cancel conditions. Do not trade mathematical exactness for storage.
- **On-demand trigger:** open `docs/research-os/policies/actions-storage-and-evidence-safety.md` only when designing, materially revising, authorizing, rerunning, or diagnosing an artifact-producing/heavy workflow.

## Heavy workflow rerun authorization

Heavy PR workflows must not rerun merely because a PR was synchronized, reopened, or docs/controller/status/source files changed. Every heavy job must remain behind a cheap authorization gate and run only when its dedicated run key is explicitly and semantically advanced/armed in the triggering commit range. If authorization cannot be verified, fail closed and skip heavy compute.

## Research credit and claim promotion

- finite/bounded/sample evidence is not a global theorem;
- computational, numerical, receiver, theorem, effectivity/existence, and endpoint credit stay distinct;
- changes of population, measure, field, quotient, model, mask, height, multiplicity, or other semantics require an exact adapter;
- do not double-charge a restriction/saving or assume independence without proof;
- formal classes/orbits/cohomology do not by themselves prove existence of the required geometric object;
- only the active controller's required audited closure releases downstream credit, and hostile audit may revoke it;
- a blocked route or finite zero hit is not impossibility;
- never claim perfect-cuboid existence/nonexistence without an explicit audited full-endpoint certificate.

Stage-local controllers may strengthen these firewalls but must not weaken them.

- **On-demand trigger:** open `docs/research-os/policies/research-credit-and-promotion-firewalls.md` only when promoting, revoking, or auditing research credit or when an adapter/semantic-scope question is load-bearing.

## Repository-wide research routing

- **Existing weapon/evidence lookup:** open `docs/research-os/policies/repository-asset-discovery.md` only when the active leaf needs an already-existing weapon or evidence asset.
- **Route broadening/parking:** open `docs/research-os/policies/cycle-exploration-safety-protocol.md` only when deciding whether to broaden, park, dominate, reopen, or declare a route exhausted.
