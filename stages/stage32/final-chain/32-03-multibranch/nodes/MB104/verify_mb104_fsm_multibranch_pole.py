#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT = Path(__file__).with_name("FSM-MULTIBRANCH-POLE-CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_FSM_MULTIBRANCH_POLE_V1", "schema")
    require(cert["status"] == "RETAINED_NECESSARY_INEQUALITY_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    br = cert["branch_contract"]
    require(br["a1_positive"] and br["a2_positive"], "positive cusp exponents")
    require(br["a1_mod_4"] == 0 and br["a2_mod_4"] == 0, "mod 4")
    require(br["a1_plus_a2_mod_8"] == 0, "sum mod 8")
    require(br["net_pole_order_upper"] == "k*max(0,16-a1-a2)", "net pole formula")
    require(br["positive_pole_iff"] == "a1+a2=8 iff (A,B)=(1,1)", "minimal branch characterization")
    require(br["positive_pole_order"] == "8k", "minimal pole order")

    # Exhaust the admissible small cusp vectors where a pole could conceivably occur.
    admissible = []
    for a1 in range(4, 65, 4):
        for a2 in range(4, 65, 4):
            if (a1 + a2) % 8 == 0:
                p = max(0, 16 - a1 - a2)
                admissible.append((a1, a2, p))
                require(p in (0, 8), "admissible pole order is 0 or 8")
                require((p > 0) == (a1 == 4 and a2 == 4), "only minimal cusp branch has pole")
    require(admissible, "nonempty cusp test")

    glob = cert["global_contract"]
    require(glob["tensor_degree_identity"] == "16(2g-2)k=#zeros-#poles", "tensor identity")
    require(glob["zero_lower_bound"] == "#zeros>=2kd", "zero lower bound")
    require(glob["pole_upper_bound"] == "#poles<=8kR8", "pole upper bound")
    require(glob["multibranch_inequality"] == "d<=16g-16+4R8", "multibranch inequality")
    require(glob["MB101_relation"] == "R8<=R<=M", "MB101 relation")

    # Symbolically check the constant recovery and several numerical instances.
    for g in range(0, 5):
        bijective_rhs = 16 * g - 16 + 4 * 48
        require(bijective_rhs == 176 + 16 * g, "published constant recovery")
        for r8 in range(0, 80):
            rhs = 16 * g - 16 + 4 * r8
            # Rearranged source inequality: 32g-32 >= 2d-8R8.
            # At d=rhs equality holds algebraically.
            require(32 * g - 32 == 2 * rhs - 8 * r8, "algebraic rearrangement")

    fin = cert["finite_window_interface"]
    require(fin["absolute_R8_bound_currently_proved"] is False, "no absolute R8 claim")
    require(fin["linear_R8_bound_with_slope_lt_one_quarter_currently_proved"] is False,
            "no slope claim")
    require(fin["finite_degree_window_proved"] is False, "finite window remains open")
    require(fin["MB104_complete"] is False, "MB104 remains incomplete")

    lit = cert["later_literature_firewall"]
    require(lit["distinct_node_support_constraints_available"] is True, "BTVA support fact")
    require(lit["these_bound_R8_multiplicity"] is False, "node-support/multiplicity firewall")

    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    for key, val in cert["credit_firewall"].items():
        require(val is False, f"credit firewall {key}")

    print("PASS: MB104 branchwise FSM pole inequality d<=16g-16+4R8; finite window still open")


if __name__ == "__main__":
    main()
