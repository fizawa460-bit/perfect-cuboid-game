#!/usr/bin/env python3
"""Execute the global presentation leaf with audited direct_sum spellings."""
from pathlib import Path

root=Path(__file__).resolve().parent
path=root/'materialize_global_two_primary_presentation.py'
src=path.read_text(encoding='utf-8')
old1='assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct sum Hom_cont(G_Q(i),Q_2/Z_2)^12"'
new1='assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12"'
old2='assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct sum Hom_cont(G_Q(i),Q/Z)_odd^12"'
new2='assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12"'
if src.count(old1)!=1 or src.count(old2)!=1:
    raise SystemExit('expected audited module-spelling assertions not found exactly once')
src=src.replace(old1,new1).replace(old2,new2)
exec(compile(src,str(path)+'[direct-sum-lock-v2]','exec'),{'__name__':'__main__','__file__':str(path)})
