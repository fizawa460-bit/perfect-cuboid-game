#!/usr/bin/env python3
"""Materialize the exact failed linear-factor pullback data for diagnosis.

The first two pilot valuation conventions did not make the 18 hyperplane
sections linearly equivalent on the resolved Picard lattice.  Instead of
continuing to guess exceptional orders, record the complete 72-divisor and
64-Picard vectors so the exceptional valuations can be solved as an exact
integer lifting problem.
"""
from pathlib import Path

root=Path(__file__).resolve().parent
src=(root/"materialize_q_units.py").read_text(encoding="utf-8")
# Use the ordinary-double-point order-one pilot for the diagnostic input.
src=src.replace(
    'pm := [pt in C select Multiplicity(C, pt) else 0 : pt in pts];',
    'pm := [pt in C select 1 else 0 : pt in pts];'
)
old='''classes = [sp.Matrix(1, 72, v) * Bpic for v in divisors]\nif any(c != classes[0] for c in classes[1:]):\n    raise SystemExit("linear-factor divisors do not have a common Picard class")\n'''
new='''classes = [sp.Matrix(1, 72, v) * Bpic for v in divisors]\nif any(c != classes[0] for c in classes[1:]):\n    diagnostic = {\n        "schema": "STAGE33_04_QUNIT_PULLBACK_DIAGNOSTIC_V1",\n        "factor_names": FACTOR_NAMES,\n        "pilot_exceptional_rule": "coefficient 1 at every singular point lying on the linear section",\n        "factor_divisor_vectors_72": divisors,\n        "factor_picard_class_vectors_64": [[int(x) for x in list(c)] for c in classes],\n        "class_difference_vectors_vs_factor1_64": [[int(x) for x in list(c-classes[0])] for c in classes],\n        "common_picard_class_under_pilot": False,\n        "next_exact_leaf": "L33-04-SOLVE-EXCEPTIONAL-VALUATIONS-FROM-PICARD-EQUIVALENCE",\n        "theorem_credit": False,\n        "endpoint_credit": False,\n    }\n    canonical = json.dumps(diagnostic, sort_keys=True, separators=(",", ":")).encode()\n    diagnostic["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()\n    (ROOT / "q-unit-pullback-diagnostic.json").write_text(json.dumps(diagnostic, indent=2, sort_keys=True)+"\\n", encoding="utf-8")\n    print(json.dumps({\n        "success": True,\n        "diagnostic_only": True,\n        "common_picard_class_under_pilot": False,\n        "nonzero_class_difference_count": sum(int(c != classes[0]) for c in classes[1:]),\n        "next_exact_leaf": diagnostic["next_exact_leaf"],\n        "certificate_sha256": diagnostic["canonical_sha256"],\n    }, indent=2, sort_keys=True))\n    raise SystemExit(0)\n'''
if src.count(old)!=1:
    raise SystemExit("could not locate common-Picard pilot gate")
src=src.replace(old,new)
exec(compile(src,str(root/"materialize_q_units.py")+"[diagnostic]","exec"),{"__name__":"__main__","__file__":str(root/"materialize_q_units.py")})
