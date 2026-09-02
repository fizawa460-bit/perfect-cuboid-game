# Arsenal cards

These are generated, single-ID views for targeted AI reads. Start from [`../index.json`](../index.json) or [`../catalog.md`](../catalog.md), then open only the selected card.

```text
formal/       audited weapons and selectors
workflows/    reusable proof/audit procedures
provisional/  frozen discovery snapshots; live Stage authority wins
retired/      old IDs routing to their successors
```

Every card has the same metadata header and links its authoritative source document. When the source has an exact matching ID heading, the card contains that section as a generated snapshot. Edit the registry or source, then run `python3 docs/arsenal/sync_arsenal_catalog.py`; never edit generated cards directly.
