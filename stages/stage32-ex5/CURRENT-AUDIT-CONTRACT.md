# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged.

## Direct predecessor authority

BC2-32 hostile audit **PASS** is the direct predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`.

## BC2-33 retained boundary under audit

BC2-33 generation 2 replayed exactly the hostile-audited BC2-32 107-UNKNOWN parent set with `40000 ms` per parent, one heavy runner, no scaleout.

Exact receipts:

- execution head `109aa38ff7e7d18e80697970489976acfd489503`
- workflow `34681698147`
- authorize job `103521379130`
- compute job `103521422359`
- artifact `10294224700`
- artifact ZIP sha256 `2f60580c25eb6564a3daa3cd314cc0b0bf66eccc53f1da9dc32989f43da4052c`
- raw JSON sha256 `924a6b44cdba3152631a2a4ed24c9c37e6a5b23ee160d116903d25f3b7f74346`
- retained result/checkpoint canonical `3310103df67d47d89ac121504a668158e0946070a7b15da07bbb0af7105fa73c`
- checkpoint git blob `465dcb5c535c6cbbedc25ef2afe26915291ce38b`
- status stream sha256 `e921c64caea0da8c75e2e47ade3c4b3d2105fc1583c97548cec7142e931473c5`
- result `26 UNSAT / 81 UNKNOWN / 0 SAT`
- remaining UNKNOWN identity hash `be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071`
- known parent-UNSAT lower bound `7255`

Every remaining UNKNOWN identity is explicitly retained. No timeout UNKNOWN is relabelled UNSAT. There is no SAT witness. Generation 1 is separately retained as `CANCELLED_STALE_HEAD_NO_RESULT_RETAINED` and grants no mathematical credit.

The generation-2 runkey is consumed/disarmed. The BC2-33 authorize/compute heavy jobs have been removed from the active workflow. The live state is frozen with `re_audit_required=true`; BC2-34 is blocked until hostile-audit PASS.

## Hostile-audit obligations

Audit must verify the BC2-32 PASS receipt, BC2-33 source/preflight/checkpoint blob and canonical locks, generation-1 non-credit cancellation receipt, generation-2 exact execution/artifact receipt, exact `26/81/0` partition, retained 81-identity hash, lower bound `7255`, runkey consumption/disarm, heavy-path retirement, and all credit firewalls.

The following remain false: whole-first-block authoritative UNSAT, whole-stratum closure, FULL178 completion, Stage32 MAIN pruning credit, N350 registration, effectivity/actual-curve credit, theorem/endpoint/receiver credit, Perfect Cuboid existence/nonexistence claim, heavy scaleout, and merge authorization.
