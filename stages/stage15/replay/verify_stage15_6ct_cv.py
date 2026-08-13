from math import gcd
from pathlib import Path

base=Path('stages/stage15')
ct=(base/'15-6ct/result.md').read_text()
cu=(base/'15-6cu/result.md').read_text()
cv=(base/'15-6cv/result.md').read_text()

assert 'CROSS_GCD_CELLS_EXACT=true' in ct
assert 'CHANNEL_GCD_COPRIME_TO_H=true' in ct
assert 'NORMALIZER_ONLY_DELTA=false' in cu
assert 'CONDITIONAL_BETA=-1' in cu
assert 'NORMALIZER_ONLY_SIGMA=false' in cv
assert 'SPLIT_TRIGGER=false' in cv
assert 'AUDIT_REQUIRED=true' in cv and 'MERGE_ALLOWED=false' in cv

# Exact diagnostic example used in 6cv.
m,n,r,s=77,36,71,65
assert gcd(m,n)==gcd(r,s)==1
a,b,c,d=gcd(m,r),gcd(m,s),gcd(n,r),gcd(n,s)
H=a*b*c*d
GS=gcd(m*m+n*n, r*r-s*s)
GO=gcd(m*m-n*n, r*r+s*s)
assert (a,b,c,d)==(1,1,1,1)
assert H==1 and GS==17 and GO==4633 and GS*GO==78761
assert gcd(H,GS*GO)==1

print('Stage15-6 main-batch ct-cv: PASS')
