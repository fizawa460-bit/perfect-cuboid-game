from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(p): return (ROOT / p).read_text(encoding='utf-8')

s126=text('stages/stage14/14-s7-126/result.md')
s127=text('stages/stage14/14-s7-127/result.md')
s128=text('stages/stage14/14-s7-128/result.md')
q18=text('stages/stage14/archive/docs/q-research/stage14-q18-summary.md')

assert 'Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST=PASS_EXACT_RESTRICTED_WEIGHT' in s126
assert 'N_mult(z)' in s126 and 'd_3(c_C*z) <= B^o(1)' in s126
assert 'Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST=PASS_EXACT_PAIR_INDEXED_WEIGHT' in s127
assert 'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false' in s127
assert '#Supp(N) <= M1(N) <= B^o(1)*#Supp(N)' in s128
assert 'Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=true' in s128
assert 'Q18_NEXT_SEARCH_TRIGGER_REACHED=true' in s128
assert 'FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=false' in q18
assert 'Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST' in q18
assert 'Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST' in q18

# Finite sanity: bounded nonnegative multiplicity gives support/first-moment sandwich.
weights=[0,1,3,0,2,1]
supp=sum(w>0 for w in weights)
m1=sum(weights)
M=max(weights)
assert supp <= m1 <= M*supp

print('STAGE14_S_BATCH_S7_126_128_AUDIT=PASS')
