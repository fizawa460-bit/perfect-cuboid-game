# StageA2 closeout — published equation-(6) `-18` family

## Status

StageA2 closes the published Bremner–Elsholtz–Ulas equation-(6) anchor line after A2-5 completed the rational-point closure of the exact two-cover receiver.

The source coefficient remains locked to

```text
c^8 - 18 c^4 d^4 + d^8.
```

StageA1's historical `-8` arithmetic remains quarantined and is not used here.

## Audited chain

A2-3 restarted directly from arXiv:2604.05459v1 equation (6), verified the source coefficient by PDF inspection and by the nondegenerate source parameter point `(c,d,G,H)=(3,1,7,1)`, and derived

```text
4 k(k-1)u^2-(k^4-18k^2+1)u-16k^2(k-1)=0,
```

```text
D18(k)=k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1,
```

and

```text
E18: Y^2=z^4-40z^2+256z-112.
```

A2-4 factored the quotient exactly and reduced every rational point to the two covers

```text
Cplus:  R^2=t^2-5t-5,  S^2=t^2-t-1,
Cminus: R^2=-(t^2-5t-5), S^2=-(t^2-t-1).
```

The independent audit strengthened the squareclass arguments to exact classes `1` and `±1` and repaired the `t=infinity` landmark.

A2-5 birationally converted the two covers to quartics with common Jacobian

```text
E: Y^2=X^3-12987X-263466=(X+102)(X+21)(X-123).
```

The audit supplied the explicit rational isomorphism to LMFDB `15.a5`, independently confirmed rank `0` and torsion `Z/2Z x Z/4Z`, and certified that both cover quartics already display all eight rational points. Every cover point maps either to an `E18` projective infinity or to

```text
z=2 -> k=1 -> c^2=d^2,
```

the excluded source wall.

Therefore

```text
PUBLISHED_EQUATION6_MINUS18_ANCHOR_NONDEGENERATE_RATIONAL_POINTS=0
FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
```

## Scope firewall

This closeout is intentionally narrow.

- Equation (6) is not proved to parametrize every anchored Hilbert cube.
- No reverse map from an arbitrary perfect cuboid into this family is known.
- The family-specific exclusion does not prove nonexistence of arbitrary perfect cuboids.
- No perfect cuboid was constructed.
- Stage27 and StructureRadar receivers are unchanged.
- StageA1 `-8` results remain historical auxiliary-curve computations only.

## Closeout audit

The independent closeout audit found no new mathematical issue. The PR base is the merged A2-5 commit, the complete A2-3/A2-4/A2-5 audit ledger is preserved, and the terminal statement does not exceed the proved family-specific scope.

Audit record: `stages/stageA2/A2-CLOSE/audit.md`.

## Final StageA2 statement

```text
STAGE_A2_STATUS=CLOSED_PUBLISHED_MINUS18_FAMILY_EXCLUSION
SOURCE_COEFFICIENT=-18
A2_3_AUDIT=PASS
A2_4_AUDIT=PASS_WITH_ELEMENTARY_STRENGTHENING_AND_LANDMARK_REPAIR
A2_5_AUDIT=PASS_WITH_CONTROLLER_HISTORY_REPAIR
A2_CLOSE_AUDIT=PASS
PUBLISHED_EQUATION6_ANCHOR_NONDEGENERATE_POINTS=0
FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
GENERAL_COVERAGE_PROVED=false
PERFECT_CUBOID_FOUND=false
ARBITRARY_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
EXACT_HEAD_STAGEA2_CI=NOT_CONFIGURED
AUDIT_REQUIRED=false
MERGE_ALLOWED=true
STOP_AFTER_AUDIT=true
NEXT_EXPECTED_COMMAND=merge_this_PR_to_finalize_StageA2
```
