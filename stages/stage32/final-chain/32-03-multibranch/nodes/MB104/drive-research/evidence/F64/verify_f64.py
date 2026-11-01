#!/usr/bin/env python3
"""Read-only F64 finite checks; the geometric proof is in the research note."""
import argparse, hashlib, json, math, subprocess, sys, tempfile, zipfile
from fractions import Fraction as Q
from pathlib import Path
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
P, II, SQRT2 = 97, 22, 14
PRIOR_SHA = 'c84db83eced17f31fa8467c7c0f9a6bbab652ea569e5e94f0ea2bff7b899cd7c'
EXPECTED_FILES = {'verify_f64.py', 'negative_tests.py', 'MB104-F63-20261029.zip'}

def require(value, message='verification condition failed'):
    if not value:
        raise ValueError(message)

def prior():
    path = ROOT/'MB104-F63-20261029.zip'
    require(hashlib.sha256(path.read_bytes()).hexdigest() == PRIOR_SHA, 'frozen F63 hash mismatch')
    with zipfile.ZipFile(path) as z:
        c = json.loads(z.read('F63-certificate.json'))
        for name, h in c['files_sha256'].items():
            require(hashlib.sha256(z.read(name)).hexdigest() == h, 'nested F63 payload hash mismatch')
        names = ['F63-witnesses97.json', 'even/matrix97.json', 'odd/matrix97.json', 'even/A97.bin', 'odd/A97.bin']
        out = {name: z.read(name) for name in names}
    return out

def node_checks(data):
    b, e, c = SQRT2, II*SQRT2 % P, (1+II) % P
    allnodes = [('v', rz, uz, rw, b) for rz in (b, -b%P, e, -e%P)
                for uz in (b, -b%P) for rw in (b, -b%P, e, -e%P)]
    allnodes += [('u', rz, e, rw, vw) for rz in (c, -c%P, II*c%P, -II*c%P)
                 for rw in (c, -c%P, II*c%P, -II*c%P) for vw in (e, -e%P)]
    require(len(allnodes) == len(set(allnodes)) == 64)
    ev = json.loads(data['even/matrix97.json'])
    selected = {tuple(x) for x in ev['nodes']}
    selected |= {(kind, -rz%P, oz, -rw%P, ow) for kind, rz, oz, rw, ow in selected.copy()}
    require(len(selected) == 28)
    def kappa(n):
        _, rz, _, rw, _ = n
        return (rz*rz-2*II)*(rw*rw-2) % P
    zero = {x for x in allnodes if kappa(x) == 0}
    require(len(zero) == 32 and selected <= zero)
    omitted = sorted(zero-selected)
    require(len(omitted) == 4)
    w = json.loads(data['F63-witnesses97.json'])
    def mon(leg, point):
        j,a,bb = leg; r,u,v = point
        return pow(r,j,P)*pow(u,a,P)*pow(v,bb,P)%P
    values = []
    for n in omitted:
        kind, rz, oz, rw, ow = n
        zp,wp = ((rz,oz,0),(rw,ow,0)) if kind=='v' else ((rz,0,oz),(rw,0,ow))
        row = [mon(z,zp)*mon(q,wp)%P for z,q in w['columns']]
        val = sum(x*y for x,y in zip(row,w['witnesses'][0]))%P
        require(val != 0, 'F63 section vanishes at omitted node')
        values.append({'node':list(n), 'F_value':val})
    return {'Y_H_nodes':64, 'kappa_zero_nodes':32, 'selected':28, 'omitted':values}

def subsystem_checks(data):
    w = json.loads(data['F63-witnesses97.json'])
    cols = [tuple(z)+tuple(q) for z,q in w['columns']]
    index = {x:j for j,x in enumerate(cols)}
    require(len(index) == 684)
    # kappa^4 = (r^2-2i)^4 (R^2-2)^4. Its 25 monomials preserve tau parity.
    polynomial = [(2*k,2*l,math.comb(4,k)*pow(-2*II,4-k,P)*math.comb(4,l)*pow(-2,4-l,P)%P)
                  for k in range(5) for l in range(5)]
    basis = [(j,a,b,k,a,b) for a in (0,1) for b in (0,1)
             for j in range(7-2*a-2*b) for k in range(7-2*a-2*b)]
    require(len(basis) == 108)
    leading = set(); checked=0
    for j,a,b,k,_,_ in basis:
        sparse = [(index[(j+x,a,b,k+y,a,b)],coef) for x,y,coef in polynomial]
        parity=(j+k)%2; offset=0 if parity==0 else 344; c=344 if parity==0 else 340
        raw=data[('odd' if parity else 'even')+'/A97.bin']
        for row in range(224):
            require(sum(raw[row*c+col-offset]*v for col,v in sparse)%P==0, 'canonical subsystem violates F63 jet row')
            checked+=1
        leading.add((j+8,a,b,k+8,a,b))
    require(len(leading) == 108 and polynomial[-1][2] == 1)
    return {'canonical_cubed_dimension':108, 'kappa_fourth_terms':25,
            'jet_identities_checked':checked, 'distinct_leading_monomials':108}

def chart_checks():
    basis=[(j,k) for j in range(3) for k in range(3)]
    charts=[]
    for iz in (0,1):
        for iw in (0,1):
            denominator=(2*iz,2*iw)
            nx,nw=(1,2*iw),(2*iz,1)
            require(denominator in basis and nx in basis and nw in basis)
            exponent_x=((nx[0]-denominator[0])*(-1 if iz else 1),nx[1]-denominator[1])
            exponent_w=(nw[0]-denominator[0],(nw[1]-denominator[1])*(-1 if iw else 1))
            require(exponent_x==(1,0) and exponent_w==(0,1))
            # Coefficients of A=u^2, B=v^2 in ascending degree in the local base coordinate.
            az = [Q(1),Q(0),Q(0),Q(0),Q(1,4)] if not iz else [Q(1,4),Q(0),Q(0),Q(0),Q(1)]
            bz = [Q(-1),Q(0),Q(0),Q(0),Q(1,4)] if not iz else [Q(1,4),Q(0),Q(0),Q(0),Q(-1)]
            aw = [Q(1),Q(0),Q(0),Q(0),Q(1,4)] if not iw else [Q(1,4),Q(0),Q(0),Q(0),Q(1)]
            bw = [Q(-1),Q(0),Q(0),Q(0),Q(1,4)] if not iw else [Q(1,4),Q(0),Q(0),Q(0),Q(-1)]
            require(az[0]-bz[0]==(2 if not iz else 0) and az[4]-bz[4]==(0 if not iz else 2))
            charts.append({'infinity_flags':[iz,iw], 'frame_monomial':list(denominator),
                'recovered_base_numerators':[list(nx),list(nw)],
                'radical_ratios':['U/frame','V/frame'],
                'u_square_z':list(map(str,az)), 'v_square_z':list(map(str,bz)),
                'u_square_w':list(map(str,aw)), 'v_square_w':list(map(str,bw))})
    invariants=[(a,b) for a in range(4) for b in range(4) if (a^b)==0]
    require(invariants==[(0,0),(1,1),(2,2),(3,3)])
    return {'canonical_dimension':11,'base_monomials':9,'radical_generators':2,
            'invariant_character_pairs':[list(x) for x in invariants],'charts':charts}

def intersection_checks():
    # Curves: Qw+,Qw-,Qz+,Qz-, then their four omitted-node exceptional curves.
    a=[[0]*8 for _ in range(8)]
    for j in range(8): a[j][j]=-4 if j<4 else -2
    for j in (0,1):
        for k in (2,3):a[j][k]=a[k][j]=1
    for j in range(4):a[j][j+4]=a[j+4][j]=1
    d=[2]*4+[1]*4; h=[4]*4+[0]*4
    dot=lambda x,y:sum(x[i]*a[i][j]*y[j] for i in range(8) for j in range(8))
    dh=sum(x*y for x,y in zip(d,h));d2=dot(d,d)
    require(dh==32 and d2==-24)
    m_on_components=[3*h[j]+4*sum(d[i]*a[i][j] for i in range(8)) for j in range(8)]
    require(m_on_components==[0]*8)
    m2=9*32+24*dh+16*d2;hm=3*32+4*dh
    require(m2==672 and hm==224 and 7**2*32-4**2*28*2==m2)
    return {'component_order':['Qw+','Qw-','Qz+','Qz-','F27+','F27-','F35+','F35-'],
        'intersection_matrix':a,'D_coefficients':d,'H_intersections':h,
        'D_square':d2,'H_D':dh,'M_intersections':m_on_components,'M_square':m2,'K_M':hm}

def determinant(a):
    a=[[Q(v) for v in row] for row in a];v=Q(1)
    for j in range(len(a)):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None:return Q(0)
        if r!=j:a[r],a[j]=a[j],a[r];v=-v
        q=a[j][j];v*=q;a[j]=[x/q for x in a[j]]
        for r in range(j+1,len(a)):
            q=a[r][j]
            if q:a[r]=[x-q*y for x,y in zip(a[r],a[j])]
    return v

def jet_checks():
    # In P^10, normalize the two distinct points to e_0,e_1.
    monomials=[]
    for pivot in (0,1):
        others=[j for j in range(11) if j!=pivot]
        e=[0]*11;e[pivot]=3;monomials.append(e)
        for j in others:
            e=[0]*11;e[pivot]=2;e[j]=1;monomials.append(e)
    def jets(e,pivot):
        others=[j for j in range(11) if j!=pivot];degree=sum(e[j] for j in others)
        return [int(degree==0)]+[int(degree==1 and e[j]==1) for j in others]
    columns=[jets(e,0)+jets(e,1) for e in monomials]
    matrix=[list(r) for r in zip(*columns)]
    require(matrix==[[int(i==j) for j in range(22)] for i in range(22)])
    require(determinant(matrix)==1)
    return {'ambient_projective_dimension':10,'degree':3,'two_point_first_jet_length':22,
        'monomials':monomials,'matrix':matrix,'determinant':1,
        'surface_two_point_jet_length':6,'bad_conjugate_tangency_codimension':3}

def claims():
    return {'scope':'SOURCE_CONDITIONAL_COMPLEX_MODEL_RESEARCH_UNAUDITED_ZERO_CREDIT',
        'half_linear_system_base_point_free':True,'canonical_Y_very_ample':True,
        'general_half_strict_curve_smooth_integral':True,
        'all_m_generic_normalization_genus':'336*m^2+112*m+1',
        'all_m_generic_off_support_ordinary_nodes':'336*m^2',
        'all_m_strict_conjugate_intersection':'672*m^2',
        'genus_one_half_strict_required_delta':'336*m^2+112*m',
        'm1_generic_genus':449,'m1_generic_off_support_nodes':336,
        'm1_genus_one_half_strict_delta':448,
        'genus_one_locus_existence_proved':False,'genus_one_locus_empty_proved':False,
        'actual_source_adapter_proved':False,'actual_marked_conductor_evaluated':False,
        'coreless_no_clump_proved':False,'candidate_exclusion':0,'uniform_degree_bound':False,
        'MB104':'OPEN','theorem_credit':0,'receiver_credit':0,'endpoint_credit':0,
        'independently_audited':False}

def compute():
    data=prior()
    table=[]
    for m in (1,2,3,5):
        gd=336*m*m+112*m+1;pc=672*m*m+112*m+1
        require(pc-gd==336*m*m and gd-1==336*m*m+112*m)
        table.append({'m':m,'smooth_half_genus':gd,'norm_off_nodes':pc-gd,'strict_X_pa':pc,
            'genus_one_required_half_delta':gd-1})
    return {'nodes':node_checks(data),'canonical_subsystem':subsystem_checks(data),
        'canonical_charts':chart_checks(),'intersections':intersection_checks(),
        'cubic_jets':jet_checks(),'genus_table':table}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--certificate',type=Path,default=ROOT/'F64-certificate.json')
    p.add_argument('--replay-f63',action='store_true');args=p.parse_args()
    c=json.loads(args.certificate.read_text())
    require(set(c)=={'schema','claims','computed','files_sha256'},'certificate shape mismatch')
    require(c['schema']=='MB104-F64-RESEARCH-CERT-v1' and c['claims']==claims(),'claim scope mismatch')
    require(set(c['files_sha256'])==EXPECTED_FILES,'incomplete dependency hash table')
    for name,h in c['files_sha256'].items():require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'dependency hash mismatch: '+name)
    require(c['computed']==compute(),'computed evidence mismatch')
    if args.replay_f63:
        with tempfile.TemporaryDirectory(prefix='f64-prior-replay-') as tmp:
            with zipfile.ZipFile(ROOT/'MB104-F63-20261029.zip') as z:z.extractall(tmp)
            for flags in ([],['-O']):
                z=subprocess.run([sys.executable]+flags+[str(Path(tmp)/'verify_f63.py')],capture_output=True,text=True)
                require(z.returncode==0,z.stderr or z.stdout)
    print(json.dumps({'status':'PASS','canonical_charts':4,'omitted_nodes_nonzero':4,
        'canonical_subsystem_jet_identities':24192,'two_point_cubic_jet_determinant':1,
        'generic_genus':'336*m^2+112*m+1','generic_off_support_nodes':'336*m^2',
        'geometric_deductions':'conditional; see proof note','candidate_exclusion':0,'MB104':'OPEN'}))

if __name__=='__main__':
    try:main()
    except Exception as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
