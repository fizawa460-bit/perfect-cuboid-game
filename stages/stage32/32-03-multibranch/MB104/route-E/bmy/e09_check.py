"""E09 checks: (1) symbolic collection of terms from Langer's inequality to the stated form; (2) the orbifold numbers;
(3) the E04 equality-face curves satisfy (E09) for all admissible alpha; (4) the thresholds of §2.
usage: python -I -O e09_check.py"""
import sympy as sp
from fractions import Fraction as Fr
ok = True
a, d, g = sp.symbols("alpha d g", positive=True)
mP, rP, dP, dE = sp.symbols("m_P r_P delta_P delta_E")
c1, c2 = sp.symbols("c1 c2")          # one node with two branches (contacts c1, c2)
mp = c1 + c2; rp = 2
# raw: 3*e_orb - (K + aC)^2 with Langer local upper bounds substituted
eP = (1 - a*mP/2)**2; ep = (1 - a*mp/2)**2 / 2
eorb = 8 + a*(2*g - 2) + a*(rP + rp) + (eP - 1) + (ep - sp.Rational(1, 2))
Ctil2 = 2*g - 2 - d + 2*dP + 2*dE
Cbar2 = Ctil2 + mp**2/2
lhs = 16 + 2*a*d + a**2*Cbar2
raw = sp.expand(3*eorb - lhs)
stated = sp.expand(8 + (3*a - a**2)*(2*g - 2) - (2*a - a**2)*d + 3*a*(rP - mP) + a**2*(3*mP**2/4 - 2*dP) - 2*a**2*dE
                   + sp.Rational(3, 2)*a*((2 - c1) + (2 - c2)) - a**2*mp**2/8)
same = sp.simplify(raw - stated) == 0
print("term collection identity:", same); ok &= same
# orbifold numbers
eP_, fix = 64, 3*64
eB = Fr(eP_ + fix, 8); nodes = fix // 4; eorbB = eB - nodes*Fr(1, 2); K2 = Fr(128, 8)
print("e(B) =", eB, " A1 points =", nodes, " e_orb(B) =", eorbB, " K_B^2 =", K2, " c2(S) =", eB + nodes)
ok &= (eB, nodes, eorbB, K2, eB + nodes) == (32, 48, 8, 16, 80)
# E04 equality-face curves (single branch, contact 1 at each node, no interior singularities)
def e09(al, d_, g_, beta, nu, sig):
    return (2*al - al*al)*d_ <= 8 + (3*al - al*al)*(2*g_ - 2) + Fr(3, 2)*al*beta + al*al*(nu - Fr(sig, 8))
bd = all(e09(Fr(k, 100), 2, 0, 6, 0, 6) and e09(Fr(k, 100), 4, 1, 4, 0, 4) for k in range(1, 100))
print("E04 equality-face curves (d=2,g=0,M=6) and (d=4,g=1,M=4) satisfy (E09) for alpha in (0,1):", bd); ok &= bd
# thresholds: beta = d (lambda = 1): need 32*kappa < (2 - 3/2)^2  ->  kappa < 1/128; with sigma >= d^2/48: nu < d^2/96
lam = Fr(1); kap = (2 - Fr(3, 2)*lam)**2 / 32
nu_thr = kap + Fr(1, 48)/8
print("kappa threshold:", kap, " nu threshold (coefficient of d^2):", nu_thr)
ok &= kap == Fr(1, 128) and nu_thr == Fr(1, 96)
# interior local term bound m - m^2/4
loc = [(m, Fr(m) - Fr(m*m, 4)) for m in range(2, 7)]
print("interior cheap weights m - m^2/4:", loc)
ok &= loc[0][1] == 1 and loc[1][1] == Fr(3, 4) and all(w <= 0 for m, w in loc if m >= 4)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
