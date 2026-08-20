# Stage16-28 repository write reliability policy

This file is a normative addendum to `docs/stage16-28-execution-controller-template.md`.
It applies to repository writes performed by Stage16-28 workflows.

Repository mechanics are operational only. They must not change mathematical
claims, evidence levels, audit semantics, merge gates, or population contracts.

## Required operating rules

- Prefer high-level file operations such as `create_file` and `update_file` when
  they can express the intended change directly.
- Keep commit messages short and descriptive. Large controller or audit payloads
  belong in repository files, not in commit messages.
- Split logically independent file writes when one large mutation is unnecessary.
- Preserve the exact mathematical content and audit state when changing the
  repository operation used to record them.
- After an alternate supported write path is used, fetch the affected file or PR
  again and verify the intended content, branch, and state.
- Do not force-write over unrelated work or change review and merge boundaries as
  a side effect of repository mechanics.

Controllers may record the compact marker

```text
GITHUB_WRITE_POLICY=prefer_high_level_file_mutations_and_verify_after_fallback
```

```text
POLICY_SCOPE=Stage16-28
PREFER_HIGH_LEVEL_FILE_MUTATIONS=true
KEEP_COMMIT_MESSAGES_COMPACT=true
MATHEMATICAL_CONTENT_PRESERVED=true
AUDIT_STATE_PRESERVED=true
VERIFY_AFTER_ALTERNATE_WRITE=true
FORCE_OVERWRITE_UNRELATED_WORK=false
```
