"""E02 arithmetic: uniform class D_l = 7l H - 4l sum_{14 nodes} E_p on the resolved box surface (K=H, H^2=16,
E_p^2=-2, H.E_p=0).  Exact rational arithmetic; fail-closed (no assert)."""
from fractions import Fraction as F
ok = True
for l in range(1, 1001):
    d = 7*l*16                      # K.D_l
    ce = -4*l*(-2)                  # C~.E_p
    M_max = 14*ce                   # bound on node branches
    if d != 112*l or ce != 8*l or M_max != d: ok = False
    # genus 0: r_odd >= d + 4 > M_max  -> impossible
    if not (d + 4 > M_max): ok = False
    for e in (1, 2, 4):
        n = F(e*d, 8)               # leg degree on the equality face
        stab = 2*e
        if n != 14*e*l or n/stab != 7*l: ok = False
        area_over_pi = F(e*d*2, stab)          # Area(E)/pi = 2*e*d/(2e) = d
        if area_over_pi != d: ok = False
        if not (area_over_pi >= 64 and area_over_pi > F(256, 3)): ok = False   # Zograf applies; exceeds 256pi/3
        if not (F(16, 1)/area_over_pi < F(3, 16)): ok = False               # lambda1 < 16pi/A < 3/16
print("checked l=1..1000, e in {1,2,4}:", "PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
