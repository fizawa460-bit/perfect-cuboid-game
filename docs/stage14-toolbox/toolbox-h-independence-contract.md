# Optional Stage14-toolbox-H independence contract

Toolbox-H is useful but not required. Toolbox main continues \`an -> ao -> ap\` without waiting.

- H consumes merged sources only and produces candidate lemmas, derivations, countermodels, diagnostics, or hypothesis maps.
- H is read-only on \`docs/stage14-toolbox/index.json\`, exponent ledgers, canonical cards and toolbox-main result files.
- H writes only under \`stages/stage14/14-toolbox-H*/\` and \`stages/stage14/scripts/14-toolbox-H*/\`.
- A blocked H subproblem is PARKED and never changes main \`NEXT\`.
- H does not own a Stage14 theorem and does not replace tH14.
- Main may import an H output only after merge and canonical-contract recheck.

Recommended first task: \`Stage14-toolbox-H0\` independently audits the interface between centered \((\xi,k)\) collision energy and selector-sensitive off-diagonal two-auxiliary Gaussian residue dispersion. It produces a hypothesis map and counterexample catalogue only.

| state | toolbox main | toolbox-H |
|---|---:|---:|
| canonical index/ledger/cards | write | read-only |
| H workspace | read after merge | write |
| main NEXT | owns | cannot block |
| new theorem claim | no | no |
