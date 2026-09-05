# Repository agent instructions

Keep this root file small. Stage-specific startup, history, and operating detail belong in the Stage entrypoint/state; reusable research-process detail belongs under `docs/research-os/`.

During ordinary Stage startup, do not preload Research OS. Follow the Stage-local startup contract and open Research OS only on the explicit triggers below.

## Repository traversal discipline

Repository discovery is search-first, not tree-first. **Never acquire a recursive/full repository tree, and never call a recursive tree endpoint (including `recursive=1`) for discovery, exhaustive enumeration, or as a fallback after any search miss. There is no Stage/task exception to this rule.** Fetch known paths directly; use GitHub search for filenames/paths and GitHub code search for terms, symbols, identifiers, or phrases; follow controller, roadmap, source-lock, certificate, index, or other authority references only to the exact targets needed for the active leaf. If exhaustive enumeration is genuinely required, use bounded/paginated targeted search, explicit non-recursive directory traversal, or a task-specific repository index instead; if those mechanisms cannot establish exhaustive coverage, stop and record that limitation rather than requesting a recursive/full tree. A search miss never proves repository-wide absence; broaden only under the active Stage/search policy.

## Large-file / context-safety gate

**Never whole-fetch or whole-open a repository file before checking its byte size from metadata.** This is a hard context-safety rule, not an optimization. Determine size without reading file contents: in a local clone use metadata commands such as `git cat-file -s <ref>:<path>` or `git ls-tree -l`; through GitHub use an immediate-parent directory listing or non-recursive tree metadata and inspect the entry's `size`. Do not fetch the target file itself merely to learn its size.

- If byte size is unknown, treat the file as unsafe and do not whole-fetch it.
- **Files >= 65536 bytes (64 KiB) must not be whole-fetched into assistant/chat context.** Use a repo-side script, import, hash check, exact locator, bounded structured output, or another compact adapter instead.
- Generated, encoded, minified, compressed, vendored, binary-like, or opaque-payload files must not be whole-fetched when a compact adapter can answer the active question, even below the threshold.
- A line-range request is **not** a valid safety preflight for a suspected encoded/minified/single-line payload: one logical line may contain the entire large object. Do not request a line that may contain such a payload.
- When inspection is necessary, make the repository/runner perform the heavy read and emit only small deterministic JSON/text containing the required fields, ranks, hashes, witnesses, locators, or summaries.
- Never expand Base64/Base85/compressed retained payloads into assistant context merely to inspect their contents.

**Permanent whole-fetch denylist:**
- `stages/stage33/33-07/picard_base_rows_retained.py`
- `stages/stage33/33-07/stage32_picard_marking_retained.py`

For these denylisted files, use their existing loaders/adapters, locked hashes/metadata, or a lightweight repo-side verifier. Do not whole-fetch them and do not use line-range fetching as a workaround.

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