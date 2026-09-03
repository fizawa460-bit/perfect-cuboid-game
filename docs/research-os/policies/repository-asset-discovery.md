# Repository asset discovery

Use this policy when an active research leaf needs an already-existing mathematical weapon, certificate, basis, matrix, label map, adapter, producer, or artifact lock. Discovery routes are routing aids, not proof authority; the live Stage controller and current source locks remain authoritative.

## Stage-local retained evidence

For an already-computed Stage-local fact, start from that Stage's canonical final handoff. Do not maintain a second Stage-local discovery registry.

1. For **Stage16 and later**, the first discovery surface is that Stage's canonical `FINAL.md` handoff. If a historical Stage retained the same filename with a case-only spelling variant, use that retained path; the semantic rule is still “final Markdown handoff first.”
2. For **Stages12–15**, the first discovery surface is the canonical self-contained final HTML because those Stages predate the `FINAL.md` convention:
   - Stage12: `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html`
   - Stage13: `review/STAGE13-FINAL-SELF-CONTAINED-20260810-R07.html`
   - Stage14: `review/STAGE14-FINAL-SELF-CONTAINED-20260813-R06.html`
   - Stage15: `stages/stage15/stage15-final-self-contained.html`
3. Follow exact source, certificate, or provenance paths cited by that final handoff when the active leaf actually needs them.
4. If the requested Stage-local item is absent from the canonical final handoff, treat it as **not retained for ordinary downstream reuse**. This is an operational discovery boundary, not a mathematical claim that the repository lacks the object.
5. Do not automatically broaden a miss into repeated repository-wide, branch-history, or keyword-expanded archaeology. A bounded repository search remains available when the active Stage has a concrete load-bearing reason to suspect an omitted asset; keep that search narrow and stop when that bounded question is answered.
6. If such an exceptional search recovers a reusable Stage-local positive asset, fold it into that Stage's canonical final handoff at closeout rather than creating another discovery registry.

## Arsenal

Arsenal remains the independent mechanism for genuinely cross-Stage reusable weapons. Do not load the full Arsenal during ordinary Stage startup. First identify the active leaf's exact missing object or workflow type, then:

1. Read `docs/arsenal/index.json` as the machine-readable registry.
2. Select one matching ID and open only its generated file under `docs/arsenal/cards/`.
3. Open the linked source document or proof certificate only when the card's exact contract requires it.
4. Treat every `PROVISIONAL` card as discovery routing only; live Stage authority overrides its snapshot.

To add or change an Arsenal weapon, edit its authoritative source section and registry entry, then run `python3 -B docs/arsenal/sync_arsenal_catalog.py`. Never hand-edit `docs/arsenal/catalog.md` or generated ID cards. Before commit, `python3 -B docs/arsenal/sync_arsenal_catalog.py --check` must pass.

If an exceptional bounded search discovers a genuinely cross-Stage reusable weapon, promote it through the normal Arsenal source/registry/sync workflow. Otherwise keep Stage-local evidence in the canonical final handoff.
