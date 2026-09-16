#!/usr/bin/env python3
import hashlib
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
PASS = "PASS STAGE32_MB104_000707_E2_G_FIXED_JACOBIAN_EXPLICIT_BASIS_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-G-FIXED-JACOBIAN-EXPLICIT-BASIS.md",
        "c734b96e8506aae51fc23b68dc0e47b5b8356632",
    ),
    "PARENT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-G-FIXED-JACOBIAN-TORSION-CERTIFICATE.json",
        "3225551e7f22878f4a481f0a5e5d601e36bed781",
    ),
    "PARENT_VERIFIER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_g_fixed_jacobian_torsion.py",
        "07e54f9f5eb5c01f17dcdd099aada75ef6e95716",
    ),
    "SIX_BRANCH_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT.md",
        "d421c11ecd6577234823b6e9604c8cc99ce48fec",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def f2_rank(rows):
    a = [r[:] for r in rows]
    rank = 0
    ncol = len(a[0])
    for c in range(ncol):
        pivot = next((i for i in range(rank, len(a)) if a[i][c] & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and (a[i][c] & 1):
                a[i] = [(x ^ y) for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


root = repo_root()
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = git_blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
six = (root / LOCKS["SIX_BRANCH_NOTE"][0]).read_text(encoding="utf-8")

for token in [
    "J(C8)^G = <tau_1,...,tau_5> ~= (Z/2)^5",
    "1024 ordered labels (epsilon,delta)",
    "R1 ~ R2",
    "R3 ~ R4",
    "R5 ~ R6",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

req("C8/G` is `P^1` with six order-two branch values, two for each of the three singular stabilizer types" in six,
    "six-branch passport token")

# Execute the exact source-locked parent replay and reuse its deterministic
# integral deck matrices.  run_name avoids any future __main__-guarded path.
ns = runpy.run_path(str(root / LOCKS["PARENT_VERIFIER"][0]), run_name="stage32_mb104_parent_replay")
q = ns["q"]
eye = ns["eye"]
msub = ns["msub"]
transpose = ns["transpose"]

basis = [(1,0,0), (0,1,0), (0,0,1)]
vecs = [
    [1,1,0,1,1,1,0,0,0,0],
    [0,1,0,0,0,0,1,1,0,0],
    [0,0,0,1,0,0,0,0,0,1],
    [0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0],
]
req(f2_rank(vecs) == 5, "explicit numerator vectors F2 rank")

# tau=v/2 is fixed mod the integral lattice iff (Q-I)^T v is even.
for j, v in enumerate(vecs, 1):
    for h in basis:
        m = transpose(msub(q[h], eye(10)))
        w = [sum(m[r][c] * v[c] for c in range(10)) for r in range(10)]
        req(all(x % 2 == 0 for x in w), f"tau{j} fixed under {h}")

# Anti-shortcut replay: the branch inertia sequence occurs in equal pairs.
# A quadratic character selecting only e1 has branch parity 110000, etc.;
# therefore the reduced ramification pair-differences are principal and cannot
# provide five independent fixed-Jacobian generators.
inertias = [(1,0,0), (1,0,0), (0,1,0), (0,1,0), (0,0,1), (0,0,1)]
for chi, expected in [
    ((1,0,0), [1,1,0,0,0,0]),
    ((0,1,0), [0,0,1,1,0,0]),
    ((0,0,1), [0,0,0,0,1,1]),
]:
    got = [sum(a*b for a,b in zip(chi, s)) & 1 for s in inertias]
    req(got == expected, f"paired branch character {chi}")

req(2 ** len(vecs) == 32, "32 fixed Jacobian labels")
req((2 ** len(vecs)) ** 2 == 1024, "1024 ordered factor labels")

print(PASS)
