from pathlib import Path

base=Path('stages/stage15')
dc=(base/'15-6dc/result.md').read_text()
dd=(base/'15-6dd/result.md').read_text()
de=(base/'15-6de/result.md').read_text()

assert 'MATERIAL_RECEIVER_CHANGE_ACKNOWLEDGED=true' in dc
assert 'EXHAUSTIVE_VIEW_AUDIT=true' in dc
assert 'DOUBLE_ELIMINANT=true' in dc
assert 'BLIND_REDISCOVERY=true' in dd
assert 'BLIND_TOP_ROUTE=DOUBLE_ELIMINANT_MIXED_FACTOR_INCIDENCE' in dd
assert 'SELECTED_ROUTE=DOUBLE_ELIMINANT_MIXED_FACTOR_INCIDENCE' in de
assert 'DISPERSION_ROUTE=LIVE_BACKUP' in de
assert 'CONDITIONAL_BETA=-1' in de
assert 'DELTA_PROVED=false' in de and 'SIGMA_PROVED=false' in de
assert 'SPLIT_TRIGGER=false' in de
assert 'AUDIT_REQUIRED=true' in de and 'MERGE_ALLOWED=false' in de

# Exact S-channel witness from Stage15-6da.
a=b=c=d=1
M,N,U,V=13,1,9,1
k,P,Q=10,37,5
X=a*b*M
Y=c*d*N
Delta=X**4-Y**4
A0=a**4*M**2*U**2+d**4*N**2*V**2
B0=b**4*M**2*V**2+c**4*N**2*U**2
assert A0==k*P**2
assert B0==k*Q**2
lhs1=Delta*U**2
rhs1=k*((b*b*M*P)**2-(d*d*N*Q)**2)
lhs2=Delta*V**2
rhs2=k*((a*a*M*Q)**2-(c*c*N*P)**2)
assert lhs1==rhs1
assert lhs2==rhs2

print('Stage15-6 reconstructed-graph audit dc-de: PASS')