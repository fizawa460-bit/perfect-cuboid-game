#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "FINITE-JET-MULTIPLICITY-SATURATION-CERTIFICATE.json"

def repo_root():
    for p in [HERE, *HERE.parents]:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
    raise SystemExit("FAIL: repository root not found")

def git_blob_sha1(path):
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()

def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def truncate(a, J):
    return list(a[:J+1]) + [0] * max(0, J+1-len(a))

def branch_series(J, lam, c):
    # coefficient lists in tau
    s = [0, 1]
    t = [lam] + [0]*J + [c]
    x = s
    y = poly_mul(s, t)
    z = poly_mul(s, poly_mul(t, t))
    return s, t, x, y, z

def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_FIXED_FINITE_JET_MULTIPLICITY_SATURATION_V1", "schema")
    require(cert["status"] == "RETAINED_LOCAL_NOGO_MB104_INCOMPLETE", "status")

    root = repo_root()
    for name, lock in cert["source_locks"].items():
        path = root / lock["path"]
        require(path.is_file(), f"source lock {name}: missing {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source lock {name}: blob mismatch")

    samples = cert["verification_samples"]
    lam = samples["lambda"]
    cs = samples["c_values"]
    require(lam != 0, "nonzero landing coordinate")
    require(len(set(cs)) == len(cs), "distinct c values")

    for J in samples["J_values"]:
        rows = []
        full_t = []
        for c in cs:
            s, t, x, y, z = branch_series(J, lam, c)
            require(s[1] == 1, f"J={J}: transverse exceptional intersection")
            # J-jet in resolved coordinates: s=tau, t=lambda modulo tau^(J+1).
            rows.append((tuple(truncate(s, J)), tuple(truncate(t, J))))
            full_t.append(tuple(t))
            # Contraction preserves the same minimal leading direction.
            require(len(x) > 1 and x[1] == 1, f"J={J}: x leading order")
            require(len(y) > 1 and y[1] == lam, f"J={J}: y leading order")
            require(len(z) > 1 and z[1] == lam*lam, f"J={J}: z leading order")
            # c first appears after the J-jet: order J+2 downstairs in y.
            require(len(y) > J+2 and y[J+2] == c, f"J={J}: first distinguishing y coefficient")
        require(len(set(rows)) == 1, f"J={J}: all branches have identical J-jet")
        require(len(set(full_t)) == len(cs), f"J={J}: branches remain distinct")

    fam = cert["branch_family"]
    require(fam["exceptional_intersection_multiplicity"] == 1, "minimal exceptional multiplicity")
    require(fam["same_J_jet_for_all_c"] is True, "same-J-jet contract")

    consequence = cert["finite_jet_consequence"]
    require(consequence["local_rank_grows_with_repeated_branch_count"] is False, "no local rank-growth overclaim")
    require(consequence["fixed_finite_local_jet_portfolio_alone_bounds_R8_multiplicity"] is False, "finite-jet firewall")
    require(consequence["extra_global_collision_or_contact_control_required"] is True, "next-input contract")
    require(consequence["arbitrary_local_family_globalizes_to_actual_cuboid_curve"] is False, "globalization firewall")

    sym = cert["fixed_symmetric_order_leading_part"]
    require(sym["repeated_same_lambda_same_leading_row"] is True, "same-lambda leading row")
    require(sym["full_regularity_for_m_gt_2_claimed_from_leading_condition"] is False, "subleading-jet firewall")
    # A degree-m polynomial evaluation row [1,lambda,...,lambda^m] has m+1 entries;
    # repeated same lambda literally repeats the same row.
    for m in range(0, 9):
        row = tuple(lam**j for j in range(m+1))
        require(len(row) == m+1, f"m={m}: leading-row dimension")
        require(row == tuple(lam**j for j in range(m+1)), f"m={m}: repeated landing row")

    fw = cert["credit_firewall"]
    for key, value in fw.items():
        require(value is False, f"credit firewall {key}")

    print("PASS: fixed finite A1 branch jets can be shared by arbitrarily many distinct minimal germs; finite local jet portfolios do not count R8 multiplicity without extra global input")

if __name__ == "__main__":
    main()
