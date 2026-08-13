from pathlib import Path
import cmath

base = Path('stages/stage15')
dm = (base/'15-6dm/result.md').read_text()
dn = (base/'15-6dn/result.md').read_text()
do = (base/'15-6do/result.md').read_text()

# Required route/controller markers.
assert 'CENTERED_OCCUPANCY_SECOND_MOMENT_EXACT=true' in dm
assert 'DECORATED_DE_ASSIGNMENT_PRESERVED=true' in dm
assert 'EXACT_PAIR_CROSS_MAIN_EXPANSION=true' in dm
assert 'OCCUPIED_PAIR_Q2_DIVIDES_ORIENTATION_BLIND_RESULTANT=true' in dm
assert 'CENTERING_REQUIRED_FOR_GAIN=true' in dn
assert 'FIXED_SMALL_MODULUS_OBSTRUCTION=true' in dn
assert 'RESULTANT_SUPPORT_KAPPA=1' in dn
assert 'NEGATIVE_CERTIFICATE=true' in dn
assert 'SELECTED_ROUTE=CHARACTER_RAMANUJAN_OCCUPANCY_DISPERSION' in do
assert 'CENTERED_INDICATOR_NONZERO_FOURIER_EXPANSION_EXACT=true' in do
assert 'ZERO_MODE_EQUALS_LOCAL_MAIN_DENSITY=true' in do
assert 'KAPPA_LT_1_PROVED=false' in do
assert 'DELTA_PROVED=false' in do and 'SIGMA_PROVED=false' in do
assert 'CURRENT_SUBSTAGE=Stage15-6do' in do
assert 'AUDIT_REQUIRED=true' in do and 'MERGE_ALLOWED=false' in do

# Exact centered pair/cross/main expansion.
X = 20
Omega = 3
q = 5
N = 15
alpha = Omega/(q*q)
B = N - alpha*X
expanded = N*N - 2*alpha*X*N + alpha*alpha*X*X
assert abs(B*B-expanded) < 1e-12

# Orientation-blind occupied-pair resultant local check at q=5.
# x has m/n=2, r/s=1; y has m/n=-2=3, r/s=-1=4 modulo 5.
mx,nx,rx,sx = 2,1,1,1
my,ny,ry,sy = 3,1,4,1
Aminus = mx*ny-my*nx
Aplus = mx*ny+my*nx
Bminus = rx*sy-ry*sx
Bplus = rx*sy+ry*sx
R = Aminus*Aplus*Bminus*Bplus
assert R % (q*q) == 0

# Exact nonzero Fourier expansion for one root-line orientation cell.
def cell_centered(m,n,r,s,rho,sigma,q):
    total = 0j
    for u in range(q):
        for v in range(q):
            if u == 0 and v == 0:
                continue
            phase = (u*(m-rho*n) + v*(r-sigma*s)) % q
            total += cmath.exp(2j*cmath.pi*phase/q)
    return total/(q*q)

rho, sigma = 2, 1
occ = cell_centered(2,1,1,1,rho,sigma,q)
unocc = cell_centered(1,1,1,1,rho,sigma,q)
assert abs(occ.real-(1-1/(q*q))) < 1e-10 and abs(occ.imag) < 1e-10
assert abs(unocc.real-(-1/(q*q))) < 1e-10 and abs(unocc.imag) < 1e-10

print('Stage15-6 main-batch dm-do: PASS')