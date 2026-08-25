#!/usr/bin/env python3
"""Run the audited q64 coordinate-sign shard against the split endpoint package.

The solver implementation is source-reused verbatim from
certify_elementary_index512_q64_coordinate_sign_shard.py.  Only the endpoint
finite quadratic module/action package is replaced: the split package carries
q, cc, ct and all seven signs in one common locally-computed Smith basis.
"""
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=HERE/'certify_elementary_index512_q64_coordinate_sign_shard.py'
src=p.read_text()
src=src.replace("endpoint-coordinate-sign-discriminant-actions.json","endpoint-coordinate-sign-discriminant-actions-split.json")
src=src.replace("STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_V1","STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_SPLIT_V2")
needle="SIGNt=SIG['sign_actions_mixed_moduli']"
replacement=needle+r'''
if SIG['discriminant_moduli']!=mods:raise SystemExit('split endpoint moduli regression')
# The split package records the Picard discriminant form.  The endpoint
# transcendental form is its negative; action matrices are unchanged under the
# retained Picard/T anti-isometry.
Bt=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(SIG['discriminant_bilinear_numerator_over_8_reduced'])]
CCt=[[int(x)%mods[j] for j,x in enumerate(row)] for row in SIG['cc_action_mixed_moduli']]
CTt=[[int(x)%mods[j] for j,x in enumerate(row)] for row in SIG['ct_action_mixed_moduli']]
'''
if needle not in src:raise SystemExit('audited q64 sign source layout moved')
src=src.replace(needle,replacement,1)
exec(compile(src,str(p),'exec'),{'__file__':str(p),'__name__':'__main__'})
