#!/usr/bin/env python3
"""TOMBSTONE — superseded R4 attempt1 named-torsor verifier.

Historical executable blob:
  d82d556ffc86de7e6fd6d99d52ee96ac7ce311dd
Historical certificate:
  j2-r4-tr-kernel-torsor-reduction.json

Attempt4 proved by binary-quartic invariants that the old ``+a,b/f2`` quartic
has Jacobian ``Eprime_Tr``, not ``E_Kc``. Therefore this historical verifier
must not regenerate a fresh ``PASS_EXACT`` that can be mistaken for current
named-Kc-torsor evidence.

Current semantic authority:
  j2-r4-historical-attempts-semantic-status.json
Current R4 orientation authority:
  j2-r4-2isogeny-orientation-correction.json

Inspect the historical blob through git when algebraic regression is needed.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "SUPERSEDED_R4_ATTEMPT1: historical algebra only; "
        "NOT_VALID_AS_NAMED_KC_TORSOR_EVIDENCE. No certificate regenerated.\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
