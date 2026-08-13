from math import gcd, isqrt
from pathlib import Path

base = Path('stages/stage15')
cz = (base/'15-6cz/result.md').read_text()
da = (base/'15-6da/result.md').read_text()
db = (base/'15-6db/result.md').read_text()

assert 'ODD_CORE_DIVIDES_FIXED_X4_MINUS_Y4=true' in cz
assert 'FIXED_MN_CORE_CANDIDATES=B^o(1)' in cz
assert 'FIXED_THREE_RESIDUALS_COMPLETION=B^o(1)' in da
assert 'PELL_COMPLETION_MULTIPLICITY=B^o(1)' in da
assert 'RECONSTRUCTION_BOUND_CERTIFIED=true' in db
assert 'CONDITIONAL_BETA=-1' in db
assert 'DELTA_PROVED=false' in db and 'SIGMA_PROVED=false' in db
assert 'NEXT_LIVE_ROUTE=ROOT_RATIO_DISCREPANCY_DISPERSION_ON_RECONSTRUCTED_GRAPH' in db
assert 'AUDIT_REQUIRED=true' in db and 'MERGE_ALLOWED=false' in db

# Exact S-channel witness from Stage15-6aa.
m,n,r,s = 13,1,9,1
a,b,c,d = gcd(m,r), gcd(m,s), gcd(n,r), gcd(n,s)
assert (a,b,c,d) == (1,1,1,1)
M,N,U,V = 13,1,9,1
A0 = a**4*M*M*U*U + d**4*N*N*V*V
B0 = b**4*M*M*V*V + c**4*N*N*U*U
assert A0 == 13690 and B0 == 250
k = 10
P,Q = 37,5
assert A0 == k*P*P and B0 == k*Q*Q
assert ((m**4-n**4) % 5) == 0
C = a*a*M*U
L = d*d*N*V
assert L*L - k*P*P == -C*C

print('Stage15-6 main-batch cz-db: PASS')