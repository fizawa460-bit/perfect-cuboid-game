#!/usr/bin/env python3
"""TOMBSTONE — superseded R4 attempt2 named-torsor verifier.

Historical executable blob:
  afe04c70fabbc6797ef882e69ff2d7a0aed58d56
Historical certificate:
  j2-r4-bisection-relative-component-incidence.json

The local Tr component-specialization and f2 ramification calculations are
retained only as fixed-Jacobian relative regression data. The historical
attempt2 certificate source-locked the superseded attempt1 quartic as the named
torsor, so this verifier must not regenerate a fresh PASS that can be consumed
as current named-Kc-torsor evidence.

Current semantic authority:
  j2-r4-historical-attempts-semantic-status.json
Current R4 orientation authority:
  j2-r4-2isogeny-orientation-correction.json

Inspect the historical blob through git when the retained local algebra is
needed; do not use it to promote the old torsor interpretation.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "SUPERSEDED_R4_ATTEMPT2: retained local regression only; "
        "NOT_VALID_AS_NAMED_KC_TORSOR_EVIDENCE. No certificate regenerated.\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
