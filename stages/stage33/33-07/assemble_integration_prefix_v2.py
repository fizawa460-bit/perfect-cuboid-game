#!/usr/bin/env python3
"""Compatibility adapter for the audited Stage33-06 nested exact-result schema."""
from pathlib import Path
root = Path(__file__).resolve().parent
src = (root / "assemble_integration_prefix.py").read_text(encoding="utf-8")
src = src.replace('line9["exact_zero_survival_certificate"]', 'line9["accepted_exact_result"]["exact_zero_survival_certificate"]')
src = src.replace('line9["endpoint_relevant_surviving_dimension_f2"]', 'line9["accepted_exact_result"]["endpoint_relevant_surviving_dimension_f2"]')
exec(compile(src, str(root / "assemble_integration_prefix.py") + "[stage33-06-schema-v2]", "exec"), {"__name__":"__main__", "__file__":str(root / "assemble_integration_prefix.py")})
