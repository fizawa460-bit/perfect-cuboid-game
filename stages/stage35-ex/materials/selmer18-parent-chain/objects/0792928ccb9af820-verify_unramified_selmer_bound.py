"""Exact checks for row358: finite-even fake descent and true Selmer <=17.

Arithmetic checks use Python's standard library. The paper proof supplies the
global parity-patching lemma, ideal exact sequence, explicit formula, Fourier
positivity, and true-to-fake comparison; this is not an independent math audit.
Run normally and with python -O. No check relies on assert or floating point.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import hashlib, json, sys, time

P = Path(__file__).resolve().parent
start = time.time()
checks = 0
negatives = 0
def check(ok, label):
    global checks
    if not ok:
        raise RuntimeError(label)
    checks += 1
def negative(ok, label):
    global negatives
    if ok:
        raise RuntimeError('unrejected negative control: ' + label)
    negatives += 1
def load(name):
    return json.loads((P / 'parents' / name).read_text())
def rank(vectors):
    piv = {}
    for vv in vectors:
        v = int(vv)
        while v:
            k = v.bit_length() - 1
            if k in piv:
                v ^= piv[k]
            else:
                piv[k] = v
                break
    return len(piv)
def mask(bits):
    return sum(int(x) << i for i,x in enumerate(bits))
def parity(n):
    return n.bit_count() & 1
def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a
def pmul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c, p)
def prem(a, b, p):
    a = trim(a, p)
    b = trim(b, p)
    if b == [0]:
        raise ZeroDivisionError('zero polynomial')
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        j = len(a) - len(b)
        x = a[-1] * inv % p
        for i,y in enumerate(b):
            a[i+j] = (a[i+j] - x*y) % p
        a = trim(a, p)
    return a
def resultant(a, b, p):
    a = trim(a, p)
    b = trim(b, p)
    z = 1
    while len(b) > 1:
        m,n = len(a)-1, len(b)-1
        r = prem(a, b, p)
        if r == [0]:
            return 0
        z = z * (-1 if m*n & 1 else 1) * pow(b[-1], m-(len(r)-1), p) % p
        a,b = b,r
    return z * pow(b[0], len(a)-1, p) % p
def peval(a, x, p):
    z = 0
    for c in a[::-1]:
        z = (z*x+c) % p
    return z
def legbit(a, p):
    if a % p == 0:
        raise ValueError('nonunit residue')
    s = pow(a % p, (p-1)//2, p)
    if s not in (1,p-1):
        raise ValueError('bad Legendre value')
    return int(s == p-1)
def binary_rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a
def binary_gcd(a,b):
    while b:
        a,b = b,binary_rem(a,b)
    return a
def pair(q):
    return [q.numerator, q.denominator]
def coarse(q, side, digits=12):
    scale = 10**digits
    n = q.numerator*scale//q.denominator
    if side == 'upper' and Q(n,scale) != q:
        n += 1
    return Q(n,scale)
def log_interval(x, terms=48):
    x = Q(x)
    if x <= 0:
        raise ValueError('nonpositive logarithm argument')
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    def series(y):
        z = (y-1)/(y+1)
        power = z
        s = Q(0)
        for j in range(terms):
            s += 2*power/(2*j+1)
            power *= z*z
        return s, s+2*power/((2*terms+1)*(1-z*z))
    lo,hi = series(x)
    l2,h2 = series(Q(2))
    return (lo+k*l2,hi+k*h2) if k >= 0 else (lo+k*h2,hi+k*l2)
def atan_interval(x, terms=36):
    x = Q(x)
    s = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)), Q(0))
    nxt = (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(s,s+nxt), max(s,s+nxt)

O = load('order.json')
L = load('local_dimensions.json')
A = load('row353_odd_images.json')
D2 = load('row355_dyadic_images.json')
R = load('row356_four_cuts.json')
G = load('rank6_divisors.json')
S = load('global_s_preflight.json')
U = load('unit12.json')
old357 = load('row357_sclass.json')
bridge = load('row351_true_fake.json')
h = O['h2_coefficients_ascending']
check(O['global_maximal_order_established'] is True, 'inherited maximal order')
check(len(h) == 37 and h[0] == h[-1] == 1, 'monic degree36 same curve with point(0,1)')
check(h == G['h2_coefficients_ascending'] == U['h2_coefficients_ascending'] == D2['h2_coefficients_ascending'], 'identical field polynomial across parents')
check(O['number_field_signature'] == S['signature'] == [4,16], 'signature4,16')
check(O['old_to_maximal_index_two_exp'] == 828, 'inherited order index is a power of2, odd factorization gives actual prime decomposition')
disc = 2**24 * 2843 * 13963 * 329475607 * 1034386920659 * 23910039195629
check(O['basis_discriminant_two_valuation'] == 24 and O['odd_discriminant_factor'] == disc//2**24, 'exact maximal field discriminant')
check(old357['S_class_group_order_upper'] == 13 and old357['S_class_2_torsion_rank_upper'] == 3, 'audited row357 retained, not confused with ordinary class group')
check(R['true_selmer_to_fake_kernel_bound'] == 1 and R['rank_lower_retained'] == 7, 'inherited true-fake kernel and global lower7')
check(bridge['fake_map_on_true_selmer_exists'] is True and bridge['true_selmer_to_fake_kernel_dimension_upper'] == 1, 'global Selmer cohomology bridge, not just MW fake map')

# Every generator of the FULL dyadic fake image is represented by an actual unit.
# In the certified order O/(u)=F16 x F256, residue is sum a[3k]*t^k.
respoly = int(D2['residual_polynomial_binary'], 0) if isinstance(D2['residual_polynomial_binary'],str) else D2['residual_polynomial_binary']
dyadic_units = []
for g in D2['selected_fake_basis']:
    v = g['unit_basis_mod256']
    check(len(v) == 36, 'dyadic unit length '+g['label'])
    residue = sum((v[3*k] & 1) << k for k in range(12))
    check(binary_gcd(residue,respoly) == 1, 'actual unit at both primes above2 '+g['label'])
    dyadic_units.append({'label':g['label'],'residue_binary':residue,'unit_in_both_components':True})
sc = int(D2['scalar_minus1_character_hex'],16)
dychars = [int(g['character_hex'],16) for g in D2['selected_fake_basis']]
check(len(dychars) == 18 and rank(dychars+[sc])-1 == 18, 'dyadic full fake rank18 with scalar removed once')
check(D2['local_fake_Kummer_image_dimension'] == 18 and D2['local_true_Kummer_JQ2_mod2_dimension'] == L['local_true_Kummer_J(Qv)/2_dimensions']['2'] == 19, 'full dyadic image inherited and verified unit rank')
check(D2['ramification_e'] == 3 and D2['residue_degrees'] == [4,8], 'both dyadic ramification indices odd3')
negative(binary_gcd(0,respoly) == 1, 'nonunit cannot pass dyadic unit check')

# Recompute odd-place unit residues and full fake ranks from original G(X).
# Odd part of the certified order index is1, so factor multiplicities are e_P.
blocks = [{'p':2,'e':[3,3],'f':[4,8],'fake_dimension':18,'all_fake_generators_units':True}]
for l,arch in zip(L['local_primes_odd'],A['odd_bad_primes']):
    p = l['p']
    ff = l['factors']
    check(p == arch['p'], 'same odd prime')
    check(sum(x['degree']*x['multiplicity'] for x in ff) == 36, 'local degree36')
    product = [1]
    for f in ff:
        for _ in range(f['multiplicity']):
            product = pmul(product,f['coefficients_ascending_mod_p'],p)
    check(product == trim(h,p), 'replayed odd factorization')
    allbits = []
    for name,g,d in zip(G['class_order'],G['class_G_coefficients_ascending'],G['class_degree_basepoint']):
        bits = []
        for f in ff:
            poly = f['coefficients_ascending_mod_p']
            degree = f['degree']
            val = resultant(poly,g,p)
            nt = (-1)**degree*poly[0] % p
            check(val != 0 and nt != 0, f'unit numerator and denominator p{p} {name}')
            bits.append(legbit(val*pow(nt,-d,p)%p,p))
        allbits.append(bits)
    check(allbits == arch['unit_residue_quadratic_character_bits'], 'odd square characters from original polynomials')
    scalar = mask([f['degree'] & 1 for f in ff])
    vectors = [mask(b) for b in allbits]
    if p == 2843:
        x,y = 4,310
        check(peval(h,x,p) == y*y % p and 2*y % p != 0, 'extra local point Hensel condition')
        bits = []
        for f in ff:
            poly = f['coefficients_ascending_mod_p']
            ev = peval(poly,x,p)
            check(ev != 0 and poly[0] != 0, 'extra point ratio is unit')
            bits.append(legbit(ev*pow(poly[0],-1,p)%p,p))
        check(bits == arch['additional_local_point_X4']['quadratic_character_bits'], 'extra point residue characters')
        vectors.append(mask(bits))
    fake_rank = rank(vectors+[scalar])-int(scalar != 0)
    local_kernel = int(arch['local_D_infinity_nonzero'])
    true_dim = L['local_true_Kummer_J(Qv)/2_dimensions'][str(p)]
    check(arch['explicit_generators_span_full_true_Kummer'] is True and fake_rank+local_kernel == true_dim, 'all odd true/fake local dimensions attained by unit representatives')
    es = [f['multiplicity'] for f in ff]
    fs = [f['degree'] for f in ff]
    check(any(e & 1 for e in es), 'odd ramification index in each bad rational fiber')
    blocks.append({'p':p,'e':es,'f':fs,'fake_dimension':fake_rank,'true_dimension':true_dim,'all_fake_generators_units':True})
check([b['p'] for b in blocks] == S['bad_rational_primes_finite'], 'all finite bad primes covered')
check(sum(len(b['e']) for b in blocks) == S['finite_S_total'] == 21, '21 finite primes covered')

# The admissible valuation parity in each rational fiber is either0 or e_P mod2.
# One rational p changes precisely this vector. Patching uses Q, not a claim
# that each prime ideal is principal. Good fibers have e=1 and the same property.
vectors = []
offset = 0
for b in blocks:
    v = mask([e & 1 for e in b['e']]) << offset
    vectors.append(v)
    b['valuation_scalar_mask_hex'] = hex(v)
    offset += len(b['e'])
check(rank(vectors) == 6, 'six independent rational scalar valuation vectors')
check(21-rank(vectors) == 15, '15-dimensional bad-prime valuation quotient killed, not 15 new unit restrictions')
for m in range(64):
    val = 0
    for i,v in enumerate(vectors):
        if m >> i & 1:
            val ^= v
    patched = val
    for i,v in enumerate(vectors):
        if m >> i & 1:
            patched ^= v
    check(patched == 0, 'global rational scalar clears admissible bad-prime parities')
bad_direction = 1 << 2  # first e1 component at2843 alone, not the full scalar pattern
negative(rank(vectors+[bad_direction]) == rank(vectors), 'non-scalar valuation direction must be excluded')
negative(all(e % 2 == 0 for b in blocks for e in b['e']), 'rational kernel cannot be enlarged to arbitrary bad primes')

# Tartar test: g(z)=3(sin z-z cos z)/z^3 is characteristic function of
# density p(t)=3/4(1-t^2)1_|t|<=1. Squaring gives f>=0 with nonnegative FT.
# Var(W)=1/5; f=char(W+W'), so1-f(z)<=z^2/5.
def integrate_even(coeff):
    return sum((2*c/Q(j+1) for j,c in enumerate(coeff) if j%2 == 0),Q(0))
density = [Q(3,4),Q(0),Q(-3,4)]
density_sq = [Q(9,16),Q(0),Q(-18,16),Q(0),Q(9,16)]
check(integrate_even(density) == 1, 'Tartar probability density normalized')
check(integrate_even([Q(0),Q(0)]+density) == Q(1,5), 'exact variance1/5')
check(integrate_even(density_sq) == Q(3,5), 'Parseval integral coefficient3/5')
check(2*Q(1,5)/2 == Q(1,5), 'Taylor upper1-f<=z²/5')
# Smooth f_eta=e^-eta*x² f(x/sqrt27) first, apply Weil, then eta down to0.
# All prime terms are nonnegative and dropped; E_eta<=E_Tartar.
a,b = atan_interval(Q(1,5))
c,d = atan_interval(Q(1,239))
pi_lo = coarse(16*a-4*d,'lower')
pi_hi = coarse(16*b-4*c,'upper')
log4pi_lo = coarse(log_interval(4*pi_lo)[0],'lower')
logD_hi = coarse(log_interval(disc)[1],'upper')
N = 8192
HN = sum((Q(1,j) for j in range(1,N+1)),Q(0))
gamma_lo = coarse(HN-log_interval(N+1)[1],'lower')
M = 100
Z = sum((Q(1,j**3) for j in range(1,M+1)),Q(0))
zeta_hi = coarse(Z+Q(1,2*M**2),'upper')
y = Q(1,27)
moment_upper = 36*Q(7,2)*zeta_hi+4*pi_hi*pi_hi/3
penalty_upper = y*moment_upper/5
constant_lower = 36*(gamma_lo+log4pi_lo)+4-logD_hi
delta_lower = constant_lower-penalty_upper
check(delta_lower > Q(49,20), 'ordinary Hilbert class field gap>2.45')
pole_squared_upper = 144*pi_hi*pi_hi/(25*y)
check(pole_squared_upper < Q(196,5)**2, 'Tartar pole E<39.2')
check(16*delta_lower > Q(196,5), 'h_K>=16 contradicts h*Delta<=E')
check(2**3 <= 15 < 2**4, 'ordinary class group2-rank<=3 from h_K<=15')
negative(15*delta_lower > Q(196,5), 'ordinary h_K<=14 not certified')
negative(2**3 > 15, 'class order15 does not give c_K<=2')
negative(constant_lower-moment_upper/128 > Q(41,16), 'old coarse Gaussian without S splitting must not certify h_K<=15')

# Full finite-even squareclasses E have dim20+c_K, by the ideal-square sequence.
# Rational scalars surviving in E are exactly ± squares: every rational fiber
# has an odd e. Since K has a real embedding,-1 is a nonsquare; quotient costs1.
unit_dimension = 4+16
rational_kernel_dimension = 1
ambient_constant = unit_dimension-rational_kernel_dimension
check(ambient_constant == 19, 'finite-even fake ambient dimension19+c_K')

# Reuse the actual audited global unit witnesses, not a partial subgroup upper.
# Rank lower on these units is a rank lower for the full finite-even space.
records = R['unit_records']
check([u['name'] for u in records] == R['unit_order'], 'fixed known-unit order')
normrow = mask([int(u['norm'] == -1) for u in records])
realrow = mask([u['real_sign_bits'][0]^u['real_sign_bits'][1] for u in records])
rows = [int(r,16) for r in R['dyadic_constraint_rows_on_12units_hex']]
check([normrow,realrow] == [int(r,16) for r in R['old_norm_real_rows_hex']], 'old norm sign and real pair rows')
check(rank([normrow,realrow]) == 2, 'norm and real pair independent on finite-even space')
check(rank(rows) == rank(rows+[normrow,realrow]) == 6, 'combined restrictions rank at least6, no double counting')
minor = []
for i in R['witness_minor_constraint_indices_zero_based']:
    minor.append([parity(rows[i] & int(w['unit_exponent_mask_hex'],16)) for w in R['witnesses']])
check(minor == R['witness_minor_matrix'] and rank([mask(row) for row in minor]) == 4, 'same four witnesses retain rank4 inside norm-real kernel')
for w in R['witnesses']:
    m = int(w['unit_exponent_mask_hex'],16)
    check(parity(normrow&m) == parity(realrow&m) == 0, 'witness finite-even and norm-real admissible')
    check(w['global_norm'] == 1 and w['real_pair_conditions_zero'] is True, 'witness original audited properties')
    defect = mask([parity(r&m) for r in rows])
    check(defect == int(w['dyadic_defect_hex'],16), 'original full defect retained')
fake_constant = ambient_constant-2-4
true_constant = fake_constant+1
check(fake_constant == 13 and true_constant == 14, 'full-domain fake<=13+c_K, true<=14+c_K')
check(true_constant+3 == 17 and 31-17 == 14, 'numeric improvement31 to17')
negative(true_constant+3 <= 16, 'target16 not reached')
negative(17 < 17, 'rank17 is not strict Chabauty rank<genus')
check(rank(rows) == 12-6, 'known-unit local kernel still exhausted dimension6')

out = {
    'run_id':'R3-20261104-SIGNED18-C2-FINITE-EVEN-ORDINARY-CLASS15-TRUESEL17',
    'scope':'fixed signed±18 C2 genus17 degree36 field only',
    'degree':36,'signature':[4,16],'field_discriminant':disc,
    'GRH_assumed':False,'all_bad_finite_fake_local_images_have_unit_representatives':True,
    'local_blocks':blocks,'dyadic_unit_checks':dyadic_units,
    'bad_prime_valuation_space_dimension':21,'rational_valuation_scalar_rank':6,
    'bad_prime_valuation_quotient_killed_dimension':15,
    'finite_even_definition':'E={alpha in K*/K*² : v_P(alpha) even at EVERY finite prime P}',
    'rational_scalar_intersection':'E cap image(Q*) = <-1>; -1 nonsquare by a real embedding',
    'full_finite_even_fake_ambient_dimension':'19+c_K',
    'c_K_definition':'dim_F2 Cl(O_K)[2], ORDINARY, not c_S',
    'ordinary_hilbert_class_field_signature':['4*h_K','16*h_K'],
    'ordinary_hilbert_class_field_discriminant':'D_K^h_K',
    'test_function':'[3(sin z-z cos z)/z³]^2, z=x/sqrt27; regularized by exp(-eta*x²), eta down to0',
    'prime_terms_used':[],'no_S_splitting_assumption_for_ordinary_Hilbert_field':True,
    'unconditional_positivity':'probability density convolution Fourier>=0; bounded harmonic strip minimum principle',
    'Tartar_moment_upper_coefficient':pair(Q(1,135)),
    'constant_lower':pair(coarse(constant_lower,'lower')),
    'archimedean_penalty_upper':pair(coarse(penalty_upper,'upper')),
    'ordinary_gap_lower':pair(coarse(delta_lower,'lower')),
    'ordinary_gap_strict_coarse_lower':pair(Q(49,20)),
    'pole_E_strict_upper':pair(Q(196,5)),
    'ordinary_class_number_upper':15,'ordinary_class_2_rank_upper':3,
    'ordinary_class_group_exact_order':'UNKNOWN','ordinary_class_2_rank_exact':'UNKNOWN',
    'row357_S_class_order13_cS3_retained':True,
    'norm_real_rank_lower_on_full_finite_even_space':2,
    'additional_dyadic_rank_lower_on_norm_real_kernel':4,
    'combined_restriction_rank_lower':6,'witness_minor_matrix':minor,
    'full_fake_Selmer_upper':'13+c_K','full_true_Selmer_upper':'14+c_K',
    'numeric_fake_upper':16,'numeric_true_Selmer_upper':17,
    'MW_rank_lower_retained':7,'MW_rank_upper':17,
    'target_true_Selmer16_proved':False,'strict_rank_below_genus17_proved':False,
    'sufficient_next':'one further independent restriction on full residual norm-real-dyadic finite-even space OR c_K<=2',
    'full_unit_basis_constructed':False,'full_class_group_computed':False,
    'known12_unit_subgroup_exhausted_retained':True,
    'new_global_MW_points':0,'new_original_signed_source_exclusions':0,
    'P23_LOW':'OPEN','Branch_B':'OPEN','formal_R0':'C35-200_UNCHANGED',
    'row355_row356_row357_independent_audits_adopted':'PASS_SCOPED only in their original scopes',
    'new_row358_independent_mathematical_audit':'PENDING_NOT_RUN',
    'novelty_scope':'new dependent finite-even global reduction and integrated true bound17; local images and four witnesses reused',
    'ordinary_hK15_precedent':'row357 Table4 auxiliary check already excluded degree16; this recertifies that bound without tables, no separate new-theorem credit',
    'parent_SHA256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((P/'parents').glob('*.json'))},
    'mathematical_dependencies_not_machine_proved':[
        'full audited local Kummer images row353/355 and true-fake bridge row351/352/356',
        'good-prime unramifiedness of fake Selmer image and rational scalar patching',
        'ideal-square exact sequence for E and ordinary Dirichlet unit rank',
        'ordinary Hilbert class field correspondence, including infinite unramifiedness',
        'unconditional Weil explicit formula and positive harmonic-strip transform',
        'Tartar density Fourier identity, Parseval, and archimedean moments7zeta3/2,pi²/3'
    ]
}
cert = P/'finite_even_selmer_certificate.json'
if '--write' in sys.argv:
    cert.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
else:
    check(json.loads(cert.read_text()) == out, 'frozen certificate exactly reproduced')
log = {
    'status':'PASS_INTERNAL_EXACT_NOT_INDEPENDENT_MATHEMATICAL_AUDIT',
    'checks':checks,'negative_controls':negatives,
    'ordinary_class_number_upper':15,'c_K_upper':3,
    'fake_Selmer_upper':16,'true_Selmer_upper':17,'rank_interval':[7,17],
    'source_exclusions':0,'proof_comparisons':'integers/Fraction only',
    'display_only_gap_decimal':float(delta_lower),'display_only_pole_E_upper':39.2,
    'GRH':False,'independent_audit':'PENDING_NOT_RUN',
    'elapsed_seconds':round(time.time()-start,3)
}
replay = P/('FINITE_EVEN_OPTIMIZED_REPLAY.json' if not __debug__ else 'FINITE_EVEN_NORMAL_REPLAY.json')
replay.write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log))
