#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-UNION-RESIDUAL-MONODROMY-CERTIFICATE.json"


def req(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gmul(x, y):
    # exact Gaussian integer pair a+b*i
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def connected(vertices, edges):
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    stack = [vertices[0]]
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        stack.extend(adj[v] - seen)
    return seen == set(vertices)


cert = json.loads(CERT.read_text())
req(cert["schema"] == "STAGE32_MB104_000707_E2_ZERO_QUARTIC_UNION_RESIDUAL_MONODROMY_V1", "schema")
rr = root()

# Fail closed on all declared dependencies before any mathematical replay.
for lock in cert["source_locks"]:
    p = rr / lock["path"]
    if not p.is_file():
        raise SystemExit(f"SOURCE_LOCK_FAIL: missing {lock['id']}: {lock['path']}")
    got = blob_sha1(p)
    if got != lock["blob_sha1"]:
        raise SystemExit(f"SOURCE_LOCK_FAIL: {lock['id']}: expected {lock['blob_sha1']}, got {got}")

locks = {x["id"]: x for x in cert["source_locks"]}
two = (rr / locks["TWO_QUARTIC_GLUE"]["path"]).read_text()
node = json.loads((rr / locks["RESIDUAL_NODE_CERT"]["path"]).read_text())
tors = (rr / locks["ZERO_QUARTIC_TORSION"]["path"]).read_text()
h1 = json.loads((rr / locks["AMBIENT_H1_CERT"]["path"]).read_text())
mod = (rr / locks["MODULAR_CHARACTER"]["path"]).read_text()

req("R_+=[1:1:i:0:0:+sqrt(2):1]" in two, "R+ source")
req("R_-=[1:1:i:0:0:-sqrt(2):1]" in two, "R- source")
req("meet transversely" in two, "transverse source")
req(node["inverse_formulas"]["r_z_square"] == "2*(C+W3)/(W1-i*W2)", "rz inverse")
req(node["inverse_formulas"]["r_w_square"] == "2*(C+W3)/(W1+i*W2)", "rw inverse")
req(node["inverse_formulas"]["product"] == "2*Z3/(C-W3)", "product inverse")
req("Q0^+ : fixed second-factor value r_w=+a" in tors, "Q0+ source")
req("Q1^+ : fixed first-factor value  r_z=+u" in tors, "Q1+ source")
req(h1["exact_result"]["complement_h1_integral"] == "Z/2", "integral H1 source")
req(h1["exact_result"]["alpha_abs_unique_nonzero"] is True, "unique alpha source")
req("T : r -> -r" in mod, "residual deck source")

# Exact cross-multiplied evaluation at W1=W2=C=1, W3=i.
# rz^2=2i: (2i)*(1-i)=2*(1+i).
req(gmul((0, 2), (1, -1)) == (2, 2), "rz2 at R+-")
# rw^2=2: 2*(1+i)=2*(1+i).
req(gmul((2, 0), (1, 1)) == (2, 2), "rw2 at R+-")
# For p=sqrt(2)*(1+i), p*(1-i)=2*sqrt(2), matching 2*Z3.
req(gmul((1, 1), (1, -1)) == (2, 0), "product at R+")
# u=1+i has u^2=2i; a^2=2, so (u*a)^2=4i=(2i)*2.
req(gmul((1, 1), (1, 1)) == (0, 2), "u square")
req(gmul((0, 2), (2, 0)) == (0, 4), "product-square compatibility")

res = cert["residual_evaluation"]
req(res["R_plus"]["r_z_square"] == "2i", "cert R+ rz2")
req(res["R_plus"]["r_w_square"] == "2", "cert R+ rw2")
req(res["R_plus"]["r_z_r_w"] == "sqrt(2)*(1+i)", "cert R+ product")
req(res["R_minus"]["r_z_r_w"] == "-sqrt(2)*(1+i)", "cert R- product")
req(res["Q0_plus_definition"] == "r_w=+sqrt(2)", "Q0+ definition")
req(res["Q1_plus_definition"] == "r_z=+(1+i)", "Q1+ definition")

# Lifted dual graph: equal signs over R+, crossed signs over R-.
vertices = ["Q0+", "Q0-", "Q1+", "Q1-"]
edges = [
    ("Q0+", "Q1+"),
    ("Q0-", "Q1-"),
    ("Q0+", "Q1-"),
    ("Q0-", "Q1+"),
]
req(connected(vertices, edges), "lifted graph connected")
req(len(edges) == 4, "four lifted intersection edges")
lg = cert["lifted_graph"]
req(lg["connected"] is True, "cert connected")
req(lg["cycle_monodromy"] == 1, "nontrivial graph monodromy")
req(lg["gamma_Q_alpha_abs"] == 1, "gamma alpha")
req(lg["gamma_Q_link_abs"] == 1, "gamma linking")
req(lg["gamma_Q_h1_class"] == "unique_nonzero_generator_of_H1(U,Z)=Z/2", "gamma generator")

route = cert["routing_consequence"]
req(route["ambient_generator_materialized"] is True, "generator materialized")
req(route["relative_Q0_Q1_plus_orientation_materialized"] is True, "relative plus orientation")
req(route["conductor_edge_class_materialized"] is False, "conductor still open")
req(route["branch_allocation_materialized"] is False, "allocation still open")

for key, value in cert["credit_firewall"].items():
    if key.endswith("_authorized") or key.endswith("_credit") or key.endswith("_closed") or key.endswith("_complete") or key.endswith("_computed") or key.endswith("_proved") or key.endswith("_claim"):
        req(value is False, f"firewall {key}")

print("PASS STAGE32_MB104_000707_E2_ZERO_QUARTIC_UNION_RESIDUAL_MONODROMY_V1")
print("R+=same-sign R-=cross-sign lifted_graph=connected gamma_Q=unique_H1_generator conductor_edges=OPEN")
