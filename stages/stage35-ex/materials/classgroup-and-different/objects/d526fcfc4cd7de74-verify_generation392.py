#!/usr/bin/env python3
"""Re-evaluate a general finite bound and inherit the audited finite-corpus barrier."""
from pathlib import Path
from fractions import Fraction
from flint import arb,ctx
import json
HERE=Path(__file__).resolve().parent;ctx.prec=192
old=json.loads((HERE/'parent391'/'strip_barrier391.json').read_text())
base=arb(old['available_score_upper_expression']);cap=arb(old['one_new_atom_weight_cap'])
assert base < -arb(9)/40 and cap < arb(279)/10**9
before={int(p):ds for p,ds in json.loads((HERE/'parent391'/'factorizations391.json').read_text()).items()}
after={int(p):ds for p,ds in json.loads((HERE/'factorizations392.json').read_text()).items()}
assert all(after[p]==ds for p,ds in before.items())
added=sum(len(after[p][0]) for p in after.keys()-before.keys());assert added==3938
# Some newly decomposed degree-one ideals were already in the complete low-norm
# tail. Counting every new factor is deliberately an upper bound.
upper=Fraction(-9,40)+added*Fraction(279,10**9)
upper_extra=upper+800000*Fraction(279,10**9)
assert upper<0 and upper_extra<0
D=json.loads((HERE/'different392.json').read_text())['absolute_discriminant']
B=arb(1)
for n in range(1,106):B*=n
B=B/arb(105)**105*(4/arb.pi())**49*arb(D).sqrt()
assert B>arb(2)**157 and B<arb(2)**158
out={'minkowski_bound_interval':str(B),'safe_unconditional_generation_bound_integer':2**158,
 'parent_corpus_score_safe_upper':'-9/40','one_missing_atom_safe_upper':'279/1000000000',
 'additional_prime_ideal_count_upper':added,'current_corpus_score_safe_upper':str(upper),
 'current_score_plus_800000_missing_ideals_safe_upper':str(upper_extra),
 'numeric_corpus_has_no_positive_full_strip_certificate':True,
 'full_classgroup_mod2_generation':'NOT_CERTIFIED','bnfcertify_executed':False}
print(json.dumps(out,indent=2))
