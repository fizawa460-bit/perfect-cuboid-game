#!/usr/bin/env python3
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT = Path(__file__).with_name("HODGE-EXCEPTIONAL-MASS-CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    c = json.loads(CERT.read_text())
    require(c["schema"] == "STAGE32_MB104_HODGE_EXCEPTIONAL_MASS_WALL_V1", "schema")
    require(c["status"] == "RETAINED_NECESSARY_BOUND_INSUFFICIENT", "status")
    require(c["receiver"] == "R29-LG2-MB", "receiver")

    inp = c["intersection_inputs"]
    require(inp["H_squared"] == 16, "H^2")
    require(inp["H_dot_E_i"] == 0, "H.E")
    require(inp["E_i_dot_E_j_for_i_ne_j"] == 0, "E_i.E_j")
    require(inp["E_i_squared"] == -2, "E_i^2")
    require(inp["exceptional_count"] == 48, "48 exceptionals")

    h = c["hodge_contract"]
    require(h["z_orthogonal_to_H_and_E"] is True, "orthogonal residual")
    require(h["z_squared_nonpositive"] is True, "negative complement")
    require(h["upper_D_squared"] == "D^2<=d^2/16-(1/2)sum_i M_i^2", "Hodge bound")

    a = c["adjunction_contract"]
    require(a["MB102_identity"] == "D^2=2g-2+2Delta_total-d", "MB102 identity")
    require(a["Delta_total_nonnegative"] is True, "Delta>=0")
    require(a["lower_D_squared"] == "D^2>=2g-2-d", "adjunction lower bound")

    b = c["derived_bounds"]
    require(b["sum_M_i_squared"] == "sum_i M_i^2<=d^2/8+2d-4g+4", "mass square bound")
    require(b["R8_le_M"] is True, "R8<=M")
    require(b["cauchy"] == "R8^2<=M^2<=48 sum_i M_i^2", "Cauchy")
    require(b["R8_bound"] == "R8<=sqrt(6d^2+96d-192g+192)", "R8 formula")
    require(math.sqrt(6) > b["required_slope_strictly_less_than"], "asymptotic route too weak")
    require(b["closes_MB104"] is False, "no closure")

    # Exact algebraic replay on representative even degrees and g=0,1.
    for g in (0, 1):
        for d in range(2, 1002, 2):
            rhs_mass2_times8 = d*d + 16*d - 32*g + 32
            require(rhs_mass2_times8 >= 0, "nonnegative mass-square envelope")
            r8sq_rhs = 6*d*d + 96*d - 192*g + 192
            require(r8sq_rhs == 48 * rhs_mass2_times8 // 8, "Cauchy scaling identity")

    for lock in c["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    for key, val in c["credit_firewall"].items():
        require(val is False, f"credit firewall {key}")

    print("PASS: MB104 Hodge exceptional-mass bound retained; asymptotic slope sqrt(6) is insufficient")


if __name__ == "__main__":
    main()
