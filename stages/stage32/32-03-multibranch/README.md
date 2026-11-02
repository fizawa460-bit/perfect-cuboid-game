# Stage32 32-03 multibranch — canonical directory (DRAFT MIGRATION)

**Canonical path proposed in draft PR #1846:** `stages/stage32/32-03-multibranch/`.

- `STATE.json`, `MISSION.json`, `PREFLIGHT.json`, `LIVE.json`, and `fib/`: original 32-03 routing and frozen audit state.
- `MB101/`: retained multibranch normalization profile.
- `MB102/`: retained local delta / genus ledger.
- `MB103/`: retained `Aut(S)` semantic orbit quotient (not a production orbit table).
- `MB104/`: existing numerical / frozen-audit verifier, source data, and `runkeys/`.
- `MB104/drive-research/`: 170 Google Drive research, audit and evidence artifacts, with internal SHA256SUMS.

The former `stages/stage32/final-chain/32-03-multibranch` is retained **only as a symlink alias** pointing here. This is for compatibility with previously source-locked Stage32 entrypoints and historical proof records; it is not a second copy of the research corpus. The three former shallow folders `stages/stage32/mb101/`, `mb102/` and `mb103/` are removed in this draft migration in favour of the single canonical node folders above.

**Audit HOLD / NO CREDIT.** Some Python entrypoints were adjusted to resolve the repository root at the new path. This changes their Git blob identities; existing pinned hashes, frozen `STATE.json` records, legacy Git path lookups, and CI/independent replay are **not yet re-audited**. The legacy source-locked status remains preserved exactly as historical evidence. Do not infer that symlink compatibility proves that every Git path lookup, frozen verification or workflow will pass. Do not merge or promote any mathematics, exclusions or receiver/endpoint credit without a clean exact-head audit and source-lock reconciliation.

PR #1846 is a **draft, unmerged** archive-and-structure migration; `main` is unchanged.
