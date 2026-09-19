#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z41-TRICANONICAL-DESCENT-QGORENSTEIN-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z41_TRICANONICAL_DESCENT_QGORENSTEIN_V1"
s48=d["supports"]["size48"]; s768=d["supports"]["size768"]
assert s48["P_identity"]=="P=3K+4(Q1+Q2+Q3+Q4+Ea+Eb)"
assert s768["P_identity"]=="P=3K+8A+8B+4Ea+4Eb"
assert s48["eY"]==50 and s48["singular_points"]==34 and s48["eYreg"]==16
assert s768["eY"]==49 and s768["singular_points"]==33 and s768["eYreg"]==16
c=d["contraction"]
assert c["P2"]==336
assert c["P_semiample"] is True
assert c["relation"]=="A_Y~_Q3K_Y"
assert c["K_Y_Q_Cartier"] is True and c["K_Y_ample"] is True
assert c["q_gorenstein_index_divides"]==3
assert Fraction(c["K_Y2"])==Fraction(112,3)
assert d["discrepancies"]["size48"]==["-4/3"]*3
assert d["discrepancies"]["size768"]==["-8/3","-8/3","-4/3","-4/3"]
assert d["discrepancies"]["nonrational_points_log_canonical"] is False
r=d["carrier_reformulation"]
assert r["avoids_exceptional_locus"] is True
assert r["lies_in_Y_reg"] is True
assert r["class"]=="3lK_Y" and r["normalization_genus"]==1
assert d["next_leaf"]=="MB104-Z42-QGORENSTEIN-CONTRACTION-LOCAL-SYMMETRIC-EULER-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z41 exact tricanonical descent / Q-Gorenstein contraction")
print("A_Y~_Q3K_Y, K_Y^2=112/3, e(Y_reg)=16")
print("next: Z42 local symmetric-Euler preflight on the actual non-lc graph singularities")
