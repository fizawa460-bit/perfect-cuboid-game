# Stage32-18H — rescue-aware exact global b12 aggregation

This stage is a lightweight aggregation/audit adapter for the Stage32-18E/18F/18G exact production chain. It performs no new lattice enumeration.

Inputs are recovered from prior immutable GitHub Actions artifacts with ZIP SHA-256 verification:

- Stage32-18E run `32877018247`: prepared input plus all 63 completed ordinary 64-way shards other than shard 26;
- Stage32-18F run `32896909852`: completed 256-way rescue residues 90, 154, 218, and residue 26 if it happened to complete;
- Stage32-18G run `32901761192`: exact 1024-way deep-rescue residues 26, 282, 538, 794.

The exact nested residue identities are checked independently:

- `h % 64 == 26` iff `h % 256 in {26,90,154,218}`;
- `h % 256 == 26` iff `h % 1024 in {26,282,538,794}`.

Canonical dumps are unioned with duplicate rejection. If the direct 26-of256 result exists, it must be byte/set-identical to the 1024-way union. The global aggregate then checks the hostile-audited b10 predecessor dump byte/set-exactly and runs the independent full Aut-order-1536 canonical verifier.

Traversal work counters are deliberately not reported as a hypothetical single-run global node/trial total. Rescue jobs repeat all work above split coordinate 54; those values are retained only as real execution-work telemetry grouped by run family.

The final production artifact inherits the repository retention policy (currently 14 days) rather than forcing the old five-day intermediate retention.

No numerical credit is granted here. A successful run stops at `PENDING_HOSTILE_AUDIT`; full-row, theorem and receiver firewalls remain false.
