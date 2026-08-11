from pathlib import Path

stage14 = Path(__file__).resolve().parents[1]
files = {
    't106': stage14 / '14-t106/result.md',
    't107': stage14 / '14-t107/result.md',
    't108': stage14 / '14-t108/result.md',
    'th28': stage14 / '14-t108/th28-target.md',
}
for name, path in files.items():
    assert path.exists(), (name, path)

text106 = files['t106'].read_text()
text107 = files['t107'].read_text()
text108 = files['t108'].read_text()
th28 = files['th28'].read_text()

required106 = [
    'BOUNDARY_BEARING_Q_SUPPORT_IS_EXACT_PROJECTION=true',
    'POSITIVE_Q_WEIGHT_REDUCES_TO_SUPPORT_UP_TO_BO1=true',
    'INNER_FIBER_MULTIPLICITY_RECHARGE_FORBIDDEN=true',
    'TH28_NEEDED=false',
    'NEXT=Stage14-t107',
]
required107 = [
    'Q_SUPPORT_EXPANDED_TO_ORIENTATION_WITNESS_EXISTENCE=true',
    'GENERIC_ORIENTATION_CUBE_SIZE=Bo1',
    'Q_DEPENDENT_ARBITRARY_WEIGHT_AS_ANALYTIC_OBJECT_REMOVED=true',
    'TH28_NEEDED=false',
    'NEXT=Stage14-t108',
]
required108 = [
    'ORIENTATION_WITNESS_TO_PRIMITIVE_NORM_FORM_EQUIVALENCE=true',
    'Q_SUPPORT_IS_PROJECTED_PRIMITIVE_SUM_OF_TWO_SQUARES_INCIDENCE=true',
    'ARBITRARY_Q_WEIGHT_RECEIVER_ELIMINATED=true',
    'PROJECTED_NORM_FORM_SUPPORT_POWER_SAVING_PROVED=false',
    'T_ROUTE_H_NEEDED=true',
    'T_ROUTE_H_BLOCKING=true',
    'NEXT=Stage14-tH28',
]
for token in required106:
    assert token in text106, token
for token in required107:
    assert token in text107, token
for token in required108:
    assert token in text108, token

for token in ('Q=ell*(u^2+v^2)', 'gcd(u,v)=1', 'ell=LPF(Q)', 'ell^2>4B', 'ell^2>2*h*k0*Q', 'h*k0*Q<=2B'):
    assert token in text108, token
assert 'CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion' in th28
assert 'DIRECT_THEOREM_APPLICABLE=true|false' in th28
assert 'UNIFORM_FIXED_POWER_SAVING_PROVED=true|false' in th28

for text in (text106, text107, text108):
    assert 'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2' in text
    assert 'STRICT_SUBSQRT_POWER_SAVING_PROVED=false' in text

print('Stage14-t-batch t106-t108 audit: OK')
