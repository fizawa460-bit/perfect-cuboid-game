# MB102 — canonical retained archive (PR #1846)

Status: RETAINED_NO_CREDIT / SOURCE_BLOBS_PRESERVED / EXECUTION_NOT_VALIDATED

Canonical location in this draft branch: `stages/stage32/32-03-multibranch/MB102/`.

The three original files (CERTIFICATE.json, RESULT.md, and the Python verifier) retain the exact Git blob SHA values from main at `b647f33e1c36c6f156d2a81a1e6f146ae2c7b550`. The source bytes were also independently compared with the Google Drive node folder. The old `final-chain` tree and shallow duplicate copies are **not present on this branch**. Historical commits preserve their provenance; they are not live execution paths.

The original Python verifier is deliberately unchanged, including `Path(__file__).resolve().parents[6]` and source-locked paths. Because the directory depth has changed, **do not execute it from this new location until an independently checked relocation has been performed**. There is no new replay or mathematical credit.

The Stage32 control/credit firewalls remain binding. No candidate exclusion, finite-window result, receiver, theorem, endpoint, audit PASS, or merge authorization is granted by this archival relocation.
