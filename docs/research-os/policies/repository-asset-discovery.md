# Repository asset discovery

Use this policy when an active research leaf needs an already-existing mathematical weapon, certificate, basis, matrix, label map, adapter, producer, or artifact lock. These lookup systems are routing aids, not proof authority; the live Stage controller and current source locks remain authoritative.

## Arsenal

Do not load the full Arsenal during ordinary Stage startup. First identify the active leaf's exact missing object or workflow type, then:

1. Read `docs/arsenal/index.json` as the machine-readable registry.
2. Select one matching ID and open only its generated file under `docs/arsenal/cards/`.
3. Open the linked source document or proof certificate only when the card's exact contract requires it.
4. Treat every `PROVISIONAL` card as discovery routing only; live Stage authority overrides its snapshot.

To add or change an Arsenal weapon, edit its authoritative source section and registry entry, then run `python3 -B docs/arsenal/sync_arsenal_catalog.py`. Never hand-edit `docs/arsenal/catalog.md` or generated ID cards. Before commit, `python3 -B docs/arsenal/sync_arsenal_catalog.py --check` must pass.

## Existing-evidence locator

Before a broad search across Stage history or branches for an already-computed asset, query `docs/evidence-locator/index.json` with:

`python3 -B docs/evidence-locator/query_evidence.py <terms>`

Treat matches only as candidate locations and recheck live Stage authority before use. A query miss never proves that the repository lacks the asset.

If a necessary bounded search discovers a reusable positive asset that was not registered, add its exact path, Git blob SHA, authority/status, object aliases, relations, outputs, limitations, and source ref to the locator, then run `python3 -B docs/evidence-locator/verify_evidence_locator.py`.

Do not centralize negative search conclusions. Keep them in the relevant Stage's head-scoped `resolved_investigations` with explicit reopening conditions.
