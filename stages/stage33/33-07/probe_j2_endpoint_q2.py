#!/usr/bin/env python3
import hashlib
import json
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"

# Exact affine ruled-model chart for the audited K_c Euler K3:
#   w^2 = t^2(1-s^2)^2 + s^2(1-t^2)^2.
# The endpoint double cover restores the space diagonal.  With
# e=(1-t^2)(1-s^2), x=2t(1-s^2), y=2s(1-t^2), one has
#   c^2 = e^2+x^2+y^2 = e^2+4w^2.
# We use t=2,s=3.  Then w^2=337 and c^2=1924=4*481, both Q_2-squares
# (337 == 1 mod 8 and 481 == 1 mod 8), so this is a genuine nondegenerate
# Q_2-point of the endpoint dense chart.
t0 = Fraction(2)
s0 = Fraction(3)
F0 = t0*t0*(1-s0*s0)**2 + s0*s0*(1-t0*t0)**2
D0 = (1-t0*t0)**2*(1-s0*s0)**2 + 4*F0
assert F0 == 337
assert D0 == 1924
assert int(F0) % 8 == 1
assert int(D0/4) % 8 == 1

# Specialize the audited Stage33-05 Creutz--Viray J2 representative.
# At t=2 the branch algebra is the quartic number field
#   L = Q(alpha), alpha^4 + alpha^2/4 + 1 = 0,
# and ell_J2 = -(16 alpha^2+8)/3.  Point evaluation is the corestriction
# Cor_{L/Q}((ell_J2, 3-alpha)_2).  At Q_2 the invariant of corestriction is
# the sum of the local invariants over primes of L above 2; for 2-torsion this
# is nonzero iff the product of the local Hilbert symbols is -1.
code = r'''
Q := Rationals();
P<x> := PolynomialRing(Q);
f := x^4 + (1/4)*x^2 + 1;
assert IsIrreducible(f);
L<a> := NumberField(f);
OL := MaximalOrder(L);
ell := L!(-(16*a^2+8)/3);
rhs := L!(3-a);
fac := Factorization(2*OL);
hs := [ HilbertSymbol(ell, rhs, pp[1]) : pp in fac ];
prod := &*hs;
printf "STAGE33_07_J2_Q2_BEGIN\n";
printf "DEGREE=%o\n", Degree(L);
printf "PRIME_COUNT=%o\n", #fac;
printf "RESIDUE_DEGREES=%o\n", [ Degree(pp[1]) : pp in fac ];
printf "RAMIFICATION_INDICES=%o\n", [ pp[2] : pp in fac ];
printf "HILBERT_SYMBOLS=%o\n", hs;
printf "PRODUCT=%o\n", prod;
printf "STAGE33_07_J2_Q2_END\n";
'''
payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": "https://magma.maths.usyd.edu.au/calc/",
        "User-Agent": "perfect-cuboid-stage33/2.0",
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=180) as resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "j2-q2-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_07_J2_Q2_END" not in stdout or any(
    bad in stdout for bad in ("Runtime error", "Internal error", "Assertion failed", "User error")
):
    print(stdout)
    raise SystemExit("Magma Q2 J2 evaluation failed")

m_hs = re.search(r"^HILBERT_SYMBOLS=\[(.*)\]$", stdout, re.M)
m_prod = re.search(r"^PRODUCT=(-?\d+)$", stdout, re.M)
m_pc = re.search(r"^PRIME_COUNT=(\d+)$", stdout, re.M)
if not (m_hs and m_prod and m_pc):
    print(stdout)
    raise SystemExit("missing Magma output fields")
hs = [int(x.strip()) for x in m_hs.group(1).split(",") if x.strip()]
prod = int(m_prod.group(1))
prime_count = int(m_pc.group(1))
if len(hs) != prime_count or any(x not in (-1,1) for x in hs):
    raise SystemExit("invalid Hilbert symbol ledger")

cert = {
    "schema": "STAGE33_07_J2_ENDPOINT_Q2_PULLBACK_PROBE_V1",
    "source_locks": {
        "stage33_05_j2": "stages/stage33/33-05/j2_arithmetic_descent.py",
        "stage29_kc_identification": "stages/stage29/29-02e/global-k3-eigenspace-adapter.md",
        "coordinate_quotient": "stages/stage29/29-02ha/coordinate-k3-subcover-adapter.md",
        "endpoint_equations": "c^2=e^2+x^2+y^2 with e=(1-t^2)(1-s^2), x=2t(1-s^2), y=2s(1-t^2)",
        "local_corestriction_law": "inv_Q2(Cor_{L/Q} A)=sum_{P|2} inv_{L_P}(A)",
    },
    "local_field": "Q_2",
    "test_point": {"t": 2, "s": 3, "w_squared": 337, "space_diagonal_squared": 1924},
    "k3_local_lift_exists": True,
    "endpoint_local_lift_exists": True,
    "branch_number_field_polynomial": "x^4+x^2/4+1",
    "j2_specialized_ell": "-(16*alpha^2+8)/3",
    "j2_specialized_second_slot": "3-alpha",
    "primes_above_2": prime_count,
    "local_hilbert_symbols": hs,
    "hilbert_symbol_product": prod,
    "corestriction_invariant": "1/2" if prod == -1 else "0",
    "j2_endpoint_pullback_nonzero_certified": prod == -1,
    "proof_logic": "a zero Brauer class evaluates trivially at every local point; nonzero Q2 invariant on an endpoint lift certifies nonzero endpoint pullback",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "j2-endpoint-q2-pullback.json").write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n")
print(json.dumps(cert, indent=2, sort_keys=True))
if prod != -1:
    raise SystemExit("this witness does not certify nonzero J2 endpoint pullback")
