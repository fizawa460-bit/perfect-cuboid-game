#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z34-Z12-BTVA-GENERAL-M-SUPPORT-HILBERT-PREFLIGHT-CERTIFICATE.json").read_text())
p=d["publication"]; c=d["cubic"]; i=d["interface"]

assert p["arxiv"]=="1912.08908v3"
assert p["perfect_cuboid_explicit_order"]==2
assert p["perfect_cuboid_h0_order2"]==13
assert p["paper_explicitly_limits_execution_to_small_m"] is True

global_lead=Fraction(-32,3)
chi1=Fraction(4,27)
chi0=Fraction(11,108)
def coeff(N):
    return global_lead+48*chi1+(48-N)*chi0

assert coeff(13)==Fraction(1,108)
assert coeff(14)==Fraction(-5,54)
assert c["coefficient_formula"]=="(144-11*N)/108"
assert c["N13"]=="1/108"
assert c["N14"]=="-5/54"

assert i["executable_variable_m_perfect_cuboid_generator_source_locked"] is False
assert i["primitive_support_hilbert_series_source_locked"] is False
assert i["Z32R_reopen_trigger_satisfied"] is False
assert d["disposition"]=="RESTORE_Z32R_MISSING_GRADED_GENERATOR_INTERFACE"
assert d["next_leaf"]=="MB104-Z35-Z2-ORBIFOLD-CANONICAL-DEGREE-THEOREM-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())

print("PASS: Z34/Z12 BTVA general-m preflight")
print("c_N=(144-11N)/108; N=13 => 1/108, N=14 => -5/54")
print("published perfect-cuboid explicit computation is m=2; no source-locked graded general-m interface")
print("Z32R reopen trigger not satisfied")
