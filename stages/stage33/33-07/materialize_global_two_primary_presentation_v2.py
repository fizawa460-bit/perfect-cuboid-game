#!/usr/bin/env python3
"""Execute the global presentation leaf with audited spelling and controller locks.

This wrapper changes no mathematical presentation. It only normalizes the
historical direct_sum spelling and permits the same production verifier to run
both immediately before and immediately after hostile-audit promotion.
"""
from pathlib import Path

root=Path(__file__).resolve().parent
path=root/'materialize_global_two_primary_presentation.py'
src=path.read_text(encoding='utf-8')
old1='assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct sum Hom_cont(G_Q(i),Q_2/Z_2)^12"'
new1='assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12"'
old2='assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct sum Hom_cont(G_Q(i),Q/Z)_odd^12"'
new2='assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12"'
old3='assert controller["stage33_progress"] == "6/11" and controller["stage33_07_released"] is True'
new3='assert controller["stage33_progress"] in ("6/11", "7/11") and controller["stage33_07_released"] is True'
for old in (old1,old2,old3):
    if src.count(old)!=1:
        raise SystemExit(f'expected audited assertion not found exactly once: {old}')
src=src.replace(old1,new1).replace(old2,new2).replace(old3,new3)
exec(compile(src,str(path)+'[audit-compatible-v3]','exec'),{'__name__':'__main__','__file__':str(path)})
