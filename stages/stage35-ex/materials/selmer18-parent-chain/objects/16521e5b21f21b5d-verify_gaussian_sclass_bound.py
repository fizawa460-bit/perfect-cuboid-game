"""Unconditional Hilbert S-class field bound, exact rational arithmetic only.
Weil explicit formula + Gaussian positivity are mathematical dependencies,
not proved by this numerical verifier. No GRH/table approximation/class-group CAS.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys,time
P=Path(__file__).resolve().parent
checks=0;negatives=0;start=time.time()
def check(ok,label):
 global checks
 if not ok:raise RuntimeError(label)
 checks+=1
def negative(ok,label):
 global negatives
 if ok:raise RuntimeError('unrejected negative control: '+label)
 negatives+=1

def log_interval(x,terms=48):
 x=Q(x);check(x>0,'positive logarithm argument')
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(y):
  z=(y-1)/(y+1);power=z;s=Q(0)
  for j in range(terms):s+=2*power/(2*j+1);power*=z*z
  tail=2*power/((2*terms+1)*(1-z*z))
  return s,s+tail
 lo,hi=series(x);l2,h2=series(Q(2))
 if k>=0:return lo+k*l2,hi+k*h2
 return lo+k*h2,hi+k*l2

def atan_interval(x,terms=36):
 x=Q(x);s=Q(0)
 for j in range(terms):s+=(-1)**j*x**(2*j+1)/(2*j+1)
 nxt=(-1)**terms*x**(2*terms+1)/(2*terms+1)
 return min(s,s+nxt),max(s,s+nxt)

def coarse(q,side,digits=12):
 scale=10**digits;n=q.numerator*scale//q.denominator
 if side=='upper'and Q(n,scale)!=q:n+=1
 return Q(n,scale)
def pair(q):return [q.numerator,q.denominator]
def coarse_interval(lo,hi):return [pair(coarse(lo,'lower')),pair(coarse(hi,'upper'))]

O=json.loads((P/'parents/signed18_c2_full_maximal_order_certificate.json').read_text())
S=json.loads((P/'parents/signed18_c2_global_sunits_preflight_certificate.json').read_text())
L=json.loads((P/'parents/signed18_c2_true_local_kummer_dimensions_certificate.json').read_text())
U=json.loads((P/'parents/unit12_certificate.json').read_text())
R=json.loads((P/'parents/row356_global_local_restriction_certificate.json').read_text())
I=json.loads((P/'parents/sunit_ideal_relations_certificate.json').read_text())
check(O['global_maximal_order_established']is True,'certified maximal order inherited')
check(O['number_field_signature']==[4,16]==S['signature'],'fixed signature4,16')
check(len(O['h2_coefficients_ascending'])==37 and O['h2_coefficients_ascending']==U['h2_coefficients_ascending'],'same degree36 polynomial')
check(L['dyadic_residual_orbit_lengths']==[4,8] and L['dyadic_tame_inertia_orbit_size']==3,'norm16 prime inherited from dyadic e3 f4')
check(S['finite_S_prime_ideals_counts']['2']==2 and S['finite_S_total']==21,'all dyadic primes belong to S')
check(2 in S['bad_rational_primes_finite'],'S contains prime of norm16')
check(R['new_true_Selmer_upper']=='28+c_S' and R['additional_independent_global_restrictions']==4,'audited row356 symbolic bound inherited')
D=(2**24)*2843*13963*329475607*1034386920659*23910039195629
check(O['odd_discriminant_factor']==D//2**24,'old exact discriminant factors')
check(O['basis_discriminant_two_valuation']==24,'maximal-basis discriminant v2=24')

# Machin's formula and alternating atan tails produce rigorous pi enclosure.
a,b=atan_interval(Q(1,5));c,d=atan_interval(Q(1,239))
pi_lo=coarse(16*a-4*d,'lower');pi_hi=coarse(16*b-4*c,'upper')
check(Q(314159,100000)<pi_lo<pi_hi<Q(314160,100000),'Machin pi range')
log4pi_lo=coarse(log_interval(4*pi_lo)[0],'lower')
log4pi_hi=coarse(log_interval(4*pi_hi)[1],'upper')
logD_lo,logD_hi=log_interval(D);logD_lo=coarse(logD_lo,'lower');logD_hi=coarse(logD_hi,'upper')
log16_lo,log16_hi=log_interval(16);log16_lo=coarse(log16_lo,'lower');log16_hi=coarse(log16_hi,'upper')

# Elementary monotone harmonic bounds on Euler gamma, no assumed decimal constants.
N=8192;HN=sum((Q(1,j)for j in range(1,N+1)),Q(0))
gamma_lo=coarse(HN-log_interval(N+1)[1],'lower')
gamma_hi=coarse(HN-log_interval(N)[0],'upper')
check(Q(5771,10000)<gamma_lo<gamma_hi<Q(5773,10000),'Euler gamma harmonic enclosure')
# Decreasing sum / integral bound for zeta(3).
M=100;Z=sum((Q(1,j**3)for j in range(1,M+1)),Q(0))
zeta_lo=coarse(Z+Q(1,2*(M+1)**2),'lower');zeta_hi=coarse(Z+Q(1,2*M**2),'upper')
check(Q(1202,1000)<zeta_lo<zeta_hi<Q(12021,10000),'zeta3 integral-tail enclosure')

alpha=Q(1,128)
# 1-exp(-a*x^2)<=a*x^2; exact archimedean moment evaluations.
sinh_moment_upper=Q(7,2)*zeta_hi
cosh_moment_upper=pi_hi*pi_hi/3
penalty_upper=alpha*(36*sinh_moment_upper+4*cosh_moment_upper)
# One prime of norm16 in K splits into h primes in the S-Hilbert class field.
# Drop all positive prime powers except m=1; exp(-t)>=1-t.
unit_prime_weight_lower=1-alpha*log16_hi**2
check(0<unit_prime_weight_lower<1,'positive Gaussian lower bound at log16')
prime_lower=4*log16_lo*unit_prime_weight_lower/17
constant_lower=36*(gamma_lo+log4pi_lo)+4-logD_hi
Delta_lower=constant_lower-penalty_upper+prime_lower
check(Delta_lower>3,'Gaussian class-field gap greater than3')
# Pole correction E=2 sqrt(pi/alpha). No numerical square root is needed.
check(4*pi_hi/alpha<41**2,'Gaussian pole correction less than41')
check(14*Delta_lower>41,'all degrees h>=14 excluded')
# Useful independent route using only Odlyzko's downward/upward-rounded Table4 row.
table_A=Q(57510,1000);table_B=Q(21682,1000);table_E=Q(38667,1000)
table_gap_lo=4*log_interval(table_A)[0]+32*log_interval(table_B)[0]-logD_hi
check(16*table_gap_lo>table_E,'table4 b14.5 independently forbids h>=16 even without S-prime term')
# Table comparison is a cross-check only; main proof does not depend on OCR tables.
negative(constant_lower-penalty_upper>3,'missing S-splitting prime must not certify gap>3')
negative(4*pi_hi/alpha<40**2,'pole term must not be rounded down to40')
negative(12*Delta_lower>41,'h<=11 is not justified by this coarse certificate')
negative(13<8,'order bound13 must not be misread as c_S<=2')
check(2**3<=13<2**4,'S class 2-torsion rank at most3')
check(28+3==31 and 27+3==30,'numeric true and fake upper bounds')
# Ordinary abelian 2-parts of order <=13 are exactly the 7 partitions below.
types=[[],[2],[4],[2,2],[8],[4,2],[2,2,2]]
for t in types:
 product=1
 for x in t:product*=x
 check(product<=13 and product&(product-1)==0,'finite list2-primary order bound')

files=sorted(f for f in(P/'parents').glob('*.json'))
out={'run_id':'R3-20261104-SIGNED18-C2-UNCONDITIONAL-GAUSSIAN-SCLASS-ORDER13-CS3','scope':'fixed degree36 field of signed18 C2 only; ordinary S ideal class group','degree':36,'signature':[4,16],'field_discriminant':D,'test_function_f':'exp(-x^2/128)','test_function_F':'exp(-x^2/128)/cosh(x/2)','GRH_assumed':False,'unconditional_positivity':'Gaussian Fourier >=0 on Re(s)=0,1 and bounded-strip harmonic minimum principle','class_field':'ordinary Hilbert S-class field, unramified at finite and infinite places, all primes S split completely','relative_degree':'h_S=order Cl(O_K,S)','class_field_signature':['4*h_S','16*h_S'],'class_field_discriminant':'D_K^h_S','used_split_prime_norm':16,'used_prime_powers':[1],'gamma_harmonic_N':N,'zeta3_sum_N':M,'logarithm_series_terms':48,'arctangent_series_terms':36,'constant_intervals':{'pi':[pair(pi_lo),pair(pi_hi)],'gamma':[pair(gamma_lo),pair(gamma_hi)],'zeta3':[pair(zeta_lo),pair(zeta_hi)],'logD':[pair(logD_lo),pair(logD_hi)],'log4pi':[pair(log4pi_lo),pair(log4pi_hi)],'log16':[pair(log16_lo),pair(log16_hi)]},'archimedean_penalty_upper':pair(coarse(penalty_upper,'upper')),'prime_term_lower':pair(coarse(prime_lower,'lower')),'gap_Delta_lower':pair(coarse(Delta_lower,'lower')),'coarse_gap_lower':3,'pole_E_strict_upper':41,'integer_consequence':'h_S*Delta <= E <41 and Delta>3 => h_S<=13','S_class_group_order_upper':13,'S_class_2_torsion_rank_upper':3,'S_class_group_exact_order':'UNKNOWN','S_class_group_exact_2_rank':'UNKNOWN','possible_2_primary_invariant_types':types,'old_true_Selmer_upper_retained':'28+c_S','true_Selmer_dimension_numeric_upper':31,'fake_Selmer_image_numeric_upper':30,'MW_rank_lower_retained':7,'MW_rank_numeric_upper':31,'rank_upper16_proved':False,'full_global_squareclass_basis_constructed':False,'new_global_MW_points':0,'new_source_exclusions':0,'P23_LOW':'OPEN','Branch_B':'OPEN','formal_R0':'C35-200_UNCHANGED','row356_independent_audit_adopted':'PASS_SCOPED global4-cut symbolic28+c_S only','new_result_independent_audit':'PENDING_NOT_RUN','Odlyzko_table4_b14_5_crosscheck_excludes_degree16':True,'table_rounding_crosscheck_is_not_primary_proof':True,'parent_SHA256':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()for f in files},'mathematical_dependencies':['ordinary global class field correspondence and S-class quotient, Milne CFT V.3 Example3.9/Exercise3.15','unconditional Weil explicit formula, Odlyzko1990 Eq2.3 and Belabas-DiazYDiaz-Friedman Eq20/21','Gaussian integral/Fourier positivity; elementary archimedean integrals 7*zeta3/2, pi^2/3']}
cert=P/'gaussian_sclass_bound_certificate.json'
if '--write'in sys.argv:cert.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
else:check(json.loads(cert.read_text())==out,'frozen class bound certificate equals exact recomputation')
log={'status':'PASS_INTERNAL_EXACT_NOT_INDEPENDENT_MATH_AUDIT','checks':checks,'negative_controls':negatives,'h_S_upper':13,'c_S_upper':3,'true_Selmer_numeric_upper':31,'Delta_lower_decimal_display':float(Delta_lower),'proof_uses_display_float':False,'pole_E_strict_upper':41,'GRH':False,'exact_S_class_group_computed':False,'source_exclusions':0,'elapsed_seconds':round(time.time()-start,3)}
(P/('GAUSSIAN_CLASS_BOUND_OPTIMIZED_REPLAY.json'if not __debug__ else'GAUSSIAN_CLASS_BOUND_NORMAL_REPLAY.json')).write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
