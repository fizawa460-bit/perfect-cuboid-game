# Repository agent instructions

Keep this root file small. Stage-specific startup, history, and operating detail belong in the Stage entrypoint/state; reusable research-process detail belongs under `docs/research-os/`.

During ordinary Stage startup, do not preload Research OS. Follow the Stage-local startup contract and open Research OS only on the explicit triggers below.

## Repository traversal discipline

- **Recursive repository-tree acquisition is forbidden by default.** Do not enumerate the full repository merely to discover paths or content.
- If an exact path is already known, fetch that path directly.
- If a filename or path must be located, use GitHub search rather than recursive tree enumeration.
- If a term, symbol, identifier, or phrase must be located, use GitHub code search.
- If a controller, roadmap, source-lock, certificate, or other authority cites a path, read only the exact referenced target needed for the active leaf.
- A recursive tree may be acquired only when **enumerating the full file set is itself an explicit research requirement**. Repository size or convenience is not sufficient justification.
- A search miss never proves global repository absence. Broaden only under the active Stage/search policy.
- **Stage33 is stricter:** ordinary exploration follows `controller -> active roadmap -> Arsenal index/card -> exact referenced files`. Use search functions for discovery; do not use a recursive repository tree as a substitute for search.

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
