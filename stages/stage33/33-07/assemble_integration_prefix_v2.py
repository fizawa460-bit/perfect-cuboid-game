#!/usr/bin/env python3
"""Compatibility adapter for audited Stage33-06 schema and Stage33-07 audit promotion."""
from pathlib import Path
root = Path(__file__).resolve().parent
src = (root / "assemble_integration_prefix.py").read_text(encoding="utf-8")
src = src.replace('line9["exact_zero_survival_certificate"]', 'line9["accepted_exact_result"]["exact_zero_survival_certificate"]')
src = src.replace('line9["endpoint_relevant_surviving_dimension_f2"]', 'line9["accepted_exact_result"]["endpoint_relevant_surviving_dimension_f2"]')
old='assert controller["stage33_progress"] == "6/11"'
new='assert controller["stage33_progress"] in ("6/11", "7/11")'
if src.count(old)!=1:
    raise SystemExit('expected Stage33 progress assertion not found exactly once')
src=src.replace(old,new)
exec(compile(src, str(root / "assemble_integration_prefix.py") + "[stage33-06-schema-audit-v3]", "exec"), {"__name__":"__main__", "__file__":str(root / "assemble_integration_prefix.py")})
