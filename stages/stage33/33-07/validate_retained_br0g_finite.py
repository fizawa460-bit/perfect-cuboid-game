#!/usr/bin/env python3
"""Validate the retention-safe exact BR0G finite residue certificate.

The large historical Stage33-04 artifacts are rebuild provenance only.  The
compact certificate retained in git contains every datum consumed by the
33-07 arithmetic-HS repair, including the exact 29x29 quotient presentation.
"""
import hashlib, json
from collections import Counter
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent
p=HERE/'br0g-finite-ramified-residue-presentation.json'
x=json.loads(p.read_text(encoding='utf-8'))
claimed=x['canonical_sha256']
y=dict(x); y.pop('canonical_sha256')
actual=hashlib.sha256(json.dumps(y,sort_keys=True,separators=(',',':')).encode()).hexdigest()
EXPECTED='4ff7731ec06df0fbd676c7c310e29c50ef1898690530d7f7497ce832a1e0d71d'
FULL='5725302099557d0770d032e901a3cb6429107f108afc673ba61ea0e555d836cf'
if claimed!=EXPECTED or actual!=EXPECTED:
    raise SystemExit(f'BR0G retained certificate hash regression claimed={claimed} actual={actual}')
if x['schema']!='STAGE33_07_BR0G_FINITE_RAMIFIED_RESIDUE_PRESENTATION_RETAINED_V2':
    raise SystemExit('BR0G retained schema regression')
if x['full_certificate_original_canonical_sha256']!=FULL:
    raise SystemExit('BR0G full-certificate source lock moved')
assert x['retention_safe_compact_certificate']
assert x['finite_ramified_boundary_residue_module_exact']
assert x['finite_ramified_boundary_residue_module']=='(Z/2)^49 direct_sum (Z/4)^12'
assert x['unit_symbol_rank_f2']==44
assert x['graph_residual_rank_f2']==17
assert x['combined_exponent_two_rank_f2']==61
assert x['order4_generator_count']==12
assert x['order4_double_rank_f2']==12
assert x['order4_double_projection_to_R17_rank_f2']==3
assert x['order4_double_intersection_U44_rank_f2']==9
assert x['relation_matrix_exact_for_boundary_finite_ramified_residue_branch']
assert not x['relation_matrix_exact_for_full_two_primary_BrU_branch']
R=sp.Matrix([[int(v) for v in row] for row in x['diagnostic_quotient_by_U44_relation_matrix_29x29']])
if R.shape!=(29,29): raise SystemExit('BR0G retained quotient matrix shape regression')
D=smith_normal_form(R,domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(29) if D[i,i]!=0]
if Counter(diag)!=Counter({1:3,2:23,4:3}):
    raise SystemExit(f'BR0G retained quotient Smith regression {Counter(diag)}')
if diag!=x['diagnostic_quotient_smith_nonzero_diagonal']:
    raise SystemExit('BR0G retained stored Smith diagonal regression')
assert x['diagnostic_quotient_by_U44']=='(Z/2)^23 direct_sum (Z/4)^3'
assert x['diagnostic_quotient_not_promoted_to_final_class_group']
print(json.dumps({
 'success':True,
 'source':'RETAINED_EXACT_COMPACT_CERTIFICATE',
 'canonical_sha256':actual,
 'full_certificate_original_canonical_sha256':FULL,
 'finite_ramified_module':x['finite_ramified_boundary_residue_module'],
 'diagnostic_quotient':x['diagnostic_quotient_by_U44'],
 'smith_counts':{'1':3,'2':23,'4':3},
 'artifact_rebuild_required':False,
 'stage33_progress':'6/11'
},indent=2,sort_keys=True))
