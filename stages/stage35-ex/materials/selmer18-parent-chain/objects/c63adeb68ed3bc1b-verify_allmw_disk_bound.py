"""Exact finite checks for the DEPENDENT row360 Chabauty disk bound.

No unknown Mordell-Weil logarithm or annihilating differential is invented.
The infinite tail, saturated-lattice and global annihilation arguments are in
the proof Markdown. Finite truncation alone does not prove these statements.
Python standard library only; assertions are deliberately not used.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, isqrt
import argparse, copy, hashlib, json, time

ROOT = Path(__file__).resolve().parent
P, G, R, TERMS, PRECISION = 163, 17, 14, 180, 4
checks = 0
def require(ok, label):
    global checks
    checks += 1
    if not ok:
        raise ValueError(label)

def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]: a.pop()
    return a

def add(a, b, p=P):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return trim([x % p for x in c])

def mul(a, b, p=P, size=None):
    n = len(a) + len(b) - 1
    if size is not None: n = min(n, size)
    c = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j < n: c[i+j] = (c[i+j] + x*y) % p
    return trim(c)

def divrem(a, b, p=P):
    a, b = trim(a), trim(b)
    if b == [0]: raise ZeroDivisionError()
    q = [0] * max(1, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        d = len(a)-len(b); t = a[-1]*inv % p; q[d] = t
        for i, x in enumerate(b): a[d+i] = (a[d+i]-t*x) % p
        a = trim(a)
    return trim(q), a

def xgcd(a, b, p=P):
    oldr, r = trim(a), trim(b)
    olds, s, oldt, t = [1], [0], [0], [1]
    while r != [0]:
        q, newr = divrem(oldr, r, p)
        oldr, r = r, newr
        olds, s = s, add(olds, [-x for x in mul(q, s, p)], p)
        oldt, t = t, add(oldt, [-x for x in mul(q, t, p)], p)
    inv = pow(oldr[-1], -1, p)
    return [[x*inv % p for x in z] for z in [oldr, olds, oldt]]

def rank(a, p=P):
    a = [row[:] for row in a]
    rows, cols, k = len(a), len(a[0]) if a else 0, 0
    for j in range(cols):
        i = next((i for i in range(k, rows) if a[i][j] % p), None)
        if i is None: continue
        a[k], a[i] = a[i], a[k]
        a[k] = [x*pow(a[k][j] % p, -1, p) % p for x in a[k]]
        for i in range(rows):
            if i != k:
                z = a[i][j] % p
                a[i] = [(x-z*y) % p for x, y in zip(a[i], a[k])]
        k += 1
        if k == rows: break
    return k

def vp(n, p=P):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

def sqrt_and_inverse(h, n=TERMS, precision=PRECISION):
    mod = P ** precision; half = pow(2, -1, mod)
    y = [1]
    for k in range(1, n):
        hn = h[k] if k < len(h) else 0
        y.append((hn-sum(y[i]*y[k-i] for i in range(1, k))) * half % mod)
    inverse = [1]
    for k in range(1, n):
        inverse.append(-sum(y[i]*inverse[k-i] for i in range(1,k+1)) % mod)
    b = [x*half % mod for x in inverse]
    return y, inverse, b

def binomial_inverse_half(h, n=17):
    # An independent characteristic-zero calculation of (1+(h-1))^(-1/2)/2.
    v = [Fraction(x) for x in h[:n]]; v[0] -= 1
    out = [Fraction(0) for _ in range(n)]
    power = [Fraction(1)] + [Fraction(0)] * (n-1)
    coefficient = Fraction(1)
    for k in range(n):
        for i in range(n): out[i] += coefficient * power[i] / 2
        power = [sum(power[j]*v[i-j] for j in range(i+1)) for i in range(n)]
        coefficient *= Fraction(-(2*k+1), 2*(k+1))
    return out

def guard(d):
    require(d['prime'] == P and d['genus'] == G, 'fixed curve and prime scope')
    require(d['inherited_MW_rank_upper'] == R < G, 'audited strict rank gate')
    require(d['all_MW_annihilator_dimension_lower'] == G-R == 3, 'whole-MW annihilator dimension')
    require(d['saturated_integral_lattice_required'] is True, 'reduction requires saturation')
    require(d['max_first_unit_index'] == R and G-(R+1) < G-R, 'projection kernel too small')
    require(d['nonzero_source_points_upper'] == R and d['whole_P0_disk_points_upper'] == R+1, 'separate P0 from nonzero points')
    require(d['source_base_injection_requires_positive_primitive_labelled'] is True, 'positive primitive labelled base required')
    require(d['specific_all_MW_differential_constructed'] is False and d['a0_unit_proved'] is False, 'existence is not an explicit a0-unit certificate')
    require(d['source_exclusions_new'] == 0 and d['new_independent_mathematical_audit'] == 'PENDING_NOT_RUN', 'scoped research, not independent audit or exclusion')

def build_certificate():
    hdoc = json.loads((ROOT/'parents/rank6_divisors.json').read_text())
    parent = json.loads((ROOT/'parents/row359_three_new_units.json').read_text())
    h = hdoc['h2_coefficients_ascending']
    require(len(h) == 37 and h[0] == h[-1] == 1, 'same monic h2 degree36 with h2(0)=1')
    require(parent['MW_rank_interval'] == [7,14] and parent['numeric_true_Selmer_upper'] == 14, 'inherited audited row359 bound')
    dh = [i*h[i] % P for i in range(1, len(h))]
    dd, s, t = xgcd([x % P for x in h], dh)
    require(dd == [1], 'good reduction: gcd(h2,h2prime)=1 mod163')
    require(add(mul(s,h), mul(t,dh)) == [1], 'explicit Bezout identity')
    y, inv, b = sqrt_and_inverse(h)
    mod = P ** PRECISION
    hh = [(h[i] if i<len(h) else 0) % mod for i in range(TERMS)]
    for n in range(TERMS):
        require(sum(y[i]*y[n-i] for i in range(n+1)) % mod == hh[n], 'sqrt coefficient '+str(n))
        require(sum(y[i]*inv[n-i] for i in range(n+1)) % mod == (n==0), 'inverse coefficient '+str(n))
    rational_b = binomial_inverse_half(h)
    for i, q in enumerate(rational_b):
        require(q.denominator & (q.denominator-1) == 0, 'dyadic rational denominator')
        require(q.numerator*pow(q.denominator,-1,mod) % mod == b[i], 'independent binomial coefficient '+str(i))
    jet = [[b[i-j] % P if i>=j else 0 for j in range(G)] for i in range(G)]
    require(rank(jet) == G and rank(jet[:R+1]) == R+1, 'unit-triangular jet map')
    # Boundary checks supplement the infinite valuation proof; they do not replace it.
    for e in [1,2]:
        for n in range(R+1):
            require(vp(n+1) == 0, 'unit denominator at first unit index')
            for m in range(n+1, TERMS):
                require(e*m-vp(m+1) > e*n, 'strict tail valuation boundary')
    require(P-2 == 161 > R, 'infinite tail: k=1 lower bound')
    require((P-1)*P-1 > 0, 'infinite tail induction increment positive for all k>=1')
    # Countermodel for the erroneous implication dimension>=3 => a0 unit.
    counter = [[int(j==i) for j in range(G)] for i in [14,15,16]]
    require(rank(counter) == 3 and all(z[0] == 0 for z in counter), 'rank alone does not certify a0')
    require(rank([[P*x % P for x in row] for row in counter]) == 0, 'unsaturated basis can lose reduction rank')
    # Algebraic source-map checks on independent primitive examples, not a candidate search.
    examples = [(3,4,5),(4,3,5),(20,21,29),(21,20,29),(119,120,169),(120,119,169)]
    xs = []
    for a,bb,c in examples:
        require(a*a+bb*bb==c*c and gcd(a,bb)==1, 'primitive positive Pythagorean regression')
        x = Fraction((a*c)**2, bb**4); rad = 1+4*x
        root = Fraction(isqrt(rad.numerator),isqrt(rad.denominator))
        require(root*root == rad and (root-1)/2 == Fraction(a*a,bb*bb), 'exact positive inverse for A/B')
        require((root+1)/2 == Fraction(c*c,bb*bb), 'exact positive inverse for C/B')
        xs.append(str(x))
    require(len(set(xs))==len(xs), 'label-swapped positive primitive examples stay distinct')
    d = {
        'run_id':'R3-20261105-SIGNED18-C2-ALLMW-P163-DISK-BASECOUNT14',
        'scope':'Fixed signed±18 C2 only, P23-LOW; dependent numerical corollary of audited row359 and old row339 source map.',
        'prime':P,'genus':G,'inherited_MW_rank_upper':R,
        'all_MW_annihilator_dimension_lower':G-R,
        'saturated_integral_lattice_required':True,
        'max_first_unit_index':R,
        'whole_P0_disk_points_upper':R+1,
        'nonzero_source_points_upper':R,
        'source_positive_primitive_labelled_bases_upper':R,
        'source_base_injection_requires_positive_primitive_labelled':True,
        'source_disk_X_valuation_at_least':2,
        'larger_disk_proved_X_valuation_at_least':1,
        'h2_coefficients_ascending':h,
        'good_reduction_Bezout':{'s':s,'t':t,'identity':'s*h2+t*h2prime=1 mod163'},
        'local_series':{'precision_p_power':PRECISION,'terms':TERMS,'sqrt_h':y,'inverse_sqrt_h':inv,'one_over_2sqrt_h':b,'independent_exact_first17':[str(q) for q in rational_b]},
        'jet_rank':G,'first15_jet_rank':R+1,'first15_jet_kernel_dimension':2,
        'infinite_tail_proof':{'for_k0':'m>=15 implies m-vp(m+1)>=15','for_k_ge1':'m>=163^k-1 implies m-k>=163^k-1-k>=161','base_k1':161,'successive_lower_bound_increment':'162*163^k-1>0 for k>=1','strassmann_last_maximum_index_upper':14,'finite_checks_are_not_an_infinite_tail_proof':True},
        'abstract_a0_countermodel':counter,
        'specific_all_MW_differential_constructed':False,'a0_unit_proved':False,
        'actual_first_unit_index':'UNKNOWN_LE14','known7_MW_finite_index_proved':False,
        'source_points_or_bases_enumerated':False,'height_bound_proved':False,
        'new_independent_mathematical_audit':'PENDING_NOT_RUN','inherited_row359_audit':'PASS_SCOPED_20261105',
        'source_exclusions_new':0,'P23_LOW':'OPEN','Branch_B':'OPEN','formal_R0':'C35-200_UNCHANGED',
        'novelty':'New project-level dependent fixed-C2 numerical bound; no credit for the standard Chabauty/Strassmann method, old local series lemma, old source quotient, or old rank<=14.',
        'parent_SHA256':{str(q.relative_to(ROOT)):hashlib.sha256(q.read_bytes()).hexdigest() for q in sorted((ROOT/'parents').glob('*.json'))}
    }
    guard(d)
    return d

def negative_controls(d):
    edits = [
        ('prime',13),('inherited_MW_rank_upper',17),
        ('saturated_integral_lattice_required',False),('max_first_unit_index',15),
        ('nonzero_source_points_upper',15),
        ('source_base_injection_requires_positive_primitive_labelled',False),
        ('specific_all_MW_differential_constructed',True),('source_exclusions_new',1)
    ]
    for key,value in edits:
        q=copy.deepcopy(d);q[key]=value
        try: guard(q)
        except ValueError: continue
        raise RuntimeError('negative control accepted: '+key)
    return len(edits)

def main():
    global checks
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--log');args=parser.parse_args()
    started=time.monotonic();d=build_certificate();positive_checks=checks
    negative=negative_controls(d);checks=positive_checks
    path=ROOT/'allmw_disk_bound_certificate.json'
    if args.write:path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    else:require(d==json.loads(path.read_text()),'frozen certificate matches exact recomputation')
    out={'status':'INTERNAL_EXACT_PASS','positive_checks':checks,'negative_controls':negative,'prime':P,'whole_P0_disk_points_upper':15,'nonzero_source_points_and_positive_primitive_labelled_bases_upper':14,'specific_all_MW_form_constructed':False,'source_exclusions_new':0,'new_independent_mathematical_audit':'PENDING_NOT_RUN','elapsed_seconds':round(time.monotonic()-started,4)}
    if args.log:(ROOT/args.log).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
