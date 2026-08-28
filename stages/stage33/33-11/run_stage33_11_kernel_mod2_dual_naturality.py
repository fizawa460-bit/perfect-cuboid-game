#!/usr/bin/env python3
"""Fail-closed runner correcting the kernel model to the proper Br2 dual.

The base kernel-mod2 scout computes A_T[2] exactly as ker(G mod 2).  Proper
geometric Br[2] is its F2 dual, so every target action must be transposed.
This runner applies that mathematically explicit correction while preserving
all source locks and all downstream regressions in the base scout.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "certify_stage33_11_kernel_mod2_naturality.py"
src = TARGET.read_text(encoding="utf-8")

old_actions = '''B_cc = induce_kernel("cc", A_cc_z)
B_ct = induce_kernel("ct", A_ct_z)
B_signs = [induce_kernel(f"sign_{n}", A) for n, A in zip(order, A_signs_z)]
B_swaps = [induce_kernel("swap12", A_swap12_z), induce_kernel("swap13", A_swap13_z)]
I14 = eye(KDIM)
'''
new_actions = '''AT_cc = induce_kernel("cc", A_cc_z)
AT_ct = induce_kernel("ct", A_ct_z)
AT_signs = [induce_kernel(f"sign_{n}", A) for n, A in zip(order, A_signs_z)]
AT_swaps = [induce_kernel("swap12", A_swap12_z), induce_kernel("swap13", A_swap13_z)]

# A_T[2] is the Gram-kernel module.  Proper Br[2] is Hom(A_T[2],F2), so the
# row-action matrices on the proper receiver are the dual transposes.
def _joint_fixed_dim(A, B):
    I = eye(KDIM)
    NA = sub2(A, I)
    NB = sub2(B, I)
    eqs = []
    for j in range(KDIM):
        eqs.append([NA[i][j] for i in range(KDIM)])
    for j in range(KDIM):
        eqs.append([NB[i][j] for i in range(KDIM)])
    return KDIM - rank2(eqs, KDIM)

at_joint_fixed_dim = _joint_fixed_dim(AT_cc, AT_ct)
if at_joint_fixed_dim != int(br2["A_T_two_torsion_fixed_dimensions"]["joint_v4"]):
    raise SystemExit(f"A_T[2] kernel joint-fixed regression: {at_joint_fixed_dim}")

B_cc = transpose(AT_cc)
B_ct = transpose(AT_ct)
B_signs = [transpose(A) for A in AT_signs]
B_swaps = [transpose(A) for A in AT_swaps]
I14 = eye(KDIM)
'''
if src.count(old_actions) != 1:
    raise SystemExit("Stage33-11 kernel action patch anchor moved")
src = src.replace(old_actions, new_actions)

old_key = 'br2["proper_Br2_joint_V4_fixed_dimension_f2"]'
new_key = 'br2["proper_Br2_joint_v4_fixed_dimension_f2"]'
if src.count(old_key) != 1:
    raise SystemExit("Stage33-11 proper-Br2 joint-fixed key anchor moved")
src = src.replace(old_key, new_key)

old_model = '"model": "A_Pic[2] ~= ker(Picard_Gram mod 2), z mod 2 maps to z/2 mod Pic",'
new_model = '"model": "A_T[2] ~= ker(Picard_Gram mod 2); proper_Br2 ~= Hom(A_T[2],F2), with dual-transpose actions",'
if src.count(old_model) != 1:
    raise SystemExit("Stage33-11 certificate model anchor moved")
src = src.replace(old_model, new_model)

old_conv = '"row_action_convention": "z -> z*A for Picard action matrix A with A*G*A^T=G",'
new_conv = '"row_action_convention": "A_T[2]: z -> z*A; proper_Br2: dual row action transpose(A_T_action)",'
if src.count(old_conv) != 1:
    raise SystemExit("Stage33-11 certificate convention anchor moved")
src = src.replace(old_conv, new_conv)

old_dim = '"kernel_dimension_f2": len(kernel_basis),'
new_dim = '"kernel_dimension_f2": len(kernel_basis),\n        "A_T_joint_V4_fixed_dimension_f2": at_joint_fixed_dim,'
if src.count(old_dim) != 1:
    raise SystemExit("Stage33-11 certificate kernel-dimension anchor moved")
src = src.replace(old_dim, new_dim)

g = {"__name__": "__main__", "__file__": str(TARGET)}
exec(compile(src, str(TARGET), "exec"), g, g)
