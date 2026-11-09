#!/usr/bin/env python3
"""Finite-degree de la Maza bound with rational parameters and Arb enclosures.
See PROOF.md for the analytic lemma; no GRH/asymptotic estimate is used.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib
if not __debug__: raise RuntimeError('Certification requires Python without -O')
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
ctx.prec=256
read=lambda n:json.loads((HERE/n).read_text())
p=read('finite_bound_parameters393.json')
assert (p['r1'],p['r2'],p['n'])==(7,49,105)
A=lambda s:arb(Fraction(s).numerator)/Fraction(s).denominator
g,a,b,delta,c,d=[A(p[k]) for k in ['gamma','alpha','beta','delta2','alpha1','alpha2']]
qg,qa,qb,qd,qc,qe=[Fraction(p[k]) for k in ['gamma','alpha','beta','delta2','alpha1','alpha2']]
assert 0<qa<qb<qd<=qg<qc<=qe
# T(s) = Gamma_profile(1-s)/Gamma_profile(s+2gamma+1)
def logT(s):
    return 56*(((1-s)/2).lgamma()-((s+1)/2+g).lgamma())+49*((1-s/2).lgamma()-(1+s/2+g).lgamma())
R=lambda s:(s+a)/((s+b)*(s+c)*(s+d))
logrho=((b-a)/((c-b)*(d-b))).log()+logT(-b)
# Here delta=gamma, hence T(-delta)=1 exactly by complex conjugation.
assert logT(-delta).contains(0)
logM=((delta-a)/(2*(delta-b)*(c-delta))).log()
y0=(logrho-logM)/(delta-b)
# Two independent algebraic forms of T(0)/P(1), enclosed separately.
logratio=logT(arb(0))-(56*((arb(1)/2).lgamma()-(1+g).lgamma())+49*(arb(1).lgamma()-(arb(3)/2+g).lgamma()))
logratio_simple=7*((1+g).lgamma()-(arb(1)/2+g).lgamma())+49*(arb(1)/2+g).log()
assert (logratio-logratio_simple).contains(0)
logt0=(R(0)/R(1)).log()+logratio_simple+arb(105)/2*arb.pi().log()
logZ=logt0+y0
D=read('parent392/different392.json')['absolute_discriminant']
B=arb(D).sqrt()*(-logZ).exp()
assert 2**93<B<2**94
assert B<14*10**27
# A rational, audit-friendly outward enclosure (not a midpoint rounding).
lo=Fraction(133050646407933378580664821548066,10000)
hi=Fraction(133050646407933378580664821548067,10000)
assert arb(lo.numerator)/lo.denominator<B<arb(hi.numerator)/hi.denominator
M=arb(1)
for k in range(1,106):M*=k
M=M/arb(105)**105*(4/arb.pi())**49*arb(D).sqrt()
assert 2**157<M<2**158
# Extend the parent full-strip finite-corpus barrier by overcounting every
# newly decomposed factor. It concerns a distinct analytic method.
old={int(p):v for p,v in read('parent392/factorizations392.json').items()}
new={int(p):v for p,v in read('factorizations393.json').items()}
assert all(new[q]==v for q,v in old.items())
added=sum(len(new[q][0]) for q in new.keys()-old.keys())
base=Fraction(read('parent392/generation_result392.json')['current_corpus_score_safe_upper'])
cap=Fraction(279,10**9)
upper=base+added*cap
extra=upper+800000*cap
assert upper<0 and extra<0
out={'parameter_source':'finite_bound_parameters393.json','uses_GRH':False,'uses_asymptotic_degree_approximation':False,
     'log_negative_residue_interval':str(logrho),'log_remainder_majorant_interval':str(logM),
     'y0_interval':str(y0),'t0_interval':str(logt0.exp()),'logZ_interval':str(logZ),
     'class_representative_bound_interval':str(B),'rational_lower_bound':str(lo),'rational_upper_bound':str(hi),
     'safe_unconditional_generation_bound_integer':2**94,'all_ideal_classes_have_integral_representative_below_safe_bound':True,
     'previous_safe_bound_integer':2**158,'reduction_in_safe_bound_bits':64,'minkowski_bound_interval':str(M),
     'different_principality_used':False,'additional_prime_ideal_count_upper':added,
     'current_corpus_score_safe_upper':str(upper),'current_score_plus_800000_missing_ideals_safe_upper':str(extra),
     'small_factorbase_all_classgroup_mod2_generation':'NOT_CERTIFIED','all_prime_ideals_to_new_bound_enumerated':False,
     'c_Cl':'UNDETERMINED','new_unconditional_signed_exclusion':0}
print(json.dumps(out,indent=2))
