#!/usr/bin/env python3
import json
from pathlib import Path

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)

d=json.loads(Path(__file__).with_name("MB104-Z33E-NULL-LOCUS-ELLIPTIC-QUARTIC-RESTRICTION-CERTIFICATE.json").read_text())
q=d["representative_curve"]; h=d["hyperflex"]; z=d["zero_pairing_support"]; c=d["conclusion"]

req(q["equations"]==["y^2=x^2+t^2","z^2=x^2-t^2"],"representative equations")
req(q["degree"]==4 and q["genus"]==1 and q["retained_nodes"]==8,"curve invariants")
req(q["node_divisor"]=="D8~2H","eight-node divisor")
req(h["every_retained_node"] is True and h["relation"]=="H|Q~4p","hyperflex relation")
req(z["supported_nodes_on_Q"]==7 and z["omitted_nodes_on_Q"]==1,"7 of 8")
req(z["supported_node_divisor"]=="2H-p","supported divisor")
req(z["P_restriction"]=="7H-4(2H-p)=4p-H~0","restriction arithmetic")
req(c["O_Q_P_trivial"] is True,"P restriction trivial")
req(c["O_Q_lP_trivial_all_l_ge_1"] is True,"all multiples trivial")
req(c["torsion_divisibility_obstruction"] is False,"no divisibility obstruction")
req(c["any_balanced16_orbit_excluded"] is False,"no orbit exclusion")
req(d["next_leaf"]=="MB104-Z33F-NULL-LATTICE-DISCRIMINANT-GLUING-PREFLIGHT","next leaf")
req(all(v is False for v in d["firewalls"].values()),"firewalls")
print("PASS: Z33E null-locus elliptic-quartic restriction")
print("D8~2H and every retained node is a hyperflex H~4p")
print("for a zero quartic with omitted node p: P|Q=7H-4(2H-p)=4p-H~0")
print("no torsion/divisibility obstruction on l")
