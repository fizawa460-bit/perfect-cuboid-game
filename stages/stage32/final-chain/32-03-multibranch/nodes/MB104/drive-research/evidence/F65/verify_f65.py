#!/usr/bin/env python3
"""Read-only finite evidence for the F65 cohomology/norm-dimension proof."""
import argparse, hashlib, io, json, subprocess, sys, tempfile, zipfile
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
PRIOR_SHA='6f85a0e25e8cc715d40230a1a2683299686e53c457261b292b84ddd34247fe8e'
EXPECTED_FILES={'verify_f65.py','negative_tests.py','MB104-F64-20261029.zip'}
def require(value,message='verification condition failed'):
    if not value:raise ValueError(message)
def dot(x,a,y):return sum(x[i]*a[i][j]*y[j] for i in range(len(x)) for j in range(len(y)))
def plus(*polys):return [sum(p[i] if i<len(p) else 0 for p in polys) for i in range(max(map(len,polys)))]
def scale(p,c):return [x*c for x in p]
def at(p,m):return sum(x*m**j for j,x in enumerate(p))

def prior():
    zpath=ROOT/'MB104-F64-20261029.zip'
    require(hashlib.sha256(zpath.read_bytes()).hexdigest()==PRIOR_SHA,'frozen F64 hash mismatch')
    with zipfile.ZipFile(zpath) as z:
        cert=json.loads(z.read('F64-certificate.json'))
        for name,h in cert['files_sha256'].items():require(hashlib.sha256(z.read(name)).hexdigest()==h,'nested F64 payload mismatch')
        with zipfile.ZipFile(io.BytesIO(z.read('MB104-F63-20261029.zip'))) as zz:
            f63=json.loads(zz.read('F63-certificate.json'))
            witness=json.loads(zz.read('F63-witnesses97.json'))
    require(f63['claims']['half_degree_m1_dimension']==242 and f63['claims']['even_dimension']==124)
    return cert,f63,witness

def unit_values(cert,w):
    rows=[];p=97
    for point in cert['computed']['nodes']['omitted']:
        kind,rz,oz,rw,ow=point['node']
        zp,wp=((rz,oz,0),(rw,ow,0)) if kind=='v' else ((rz,0,oz),(rw,0,ow))
        def mon(leg,q):
            j,a,b=leg;r,u,v=q
            return pow(r,j,p)*pow(u,a,p)*pow(v,b,p)%p
        values=[mon(z,zp)*mon(q,wp)%p for z,q in w['columns']]
        f=sum(x*y for x,y in zip(values,w['witnesses'][0]))%p
        tf=sum(x*y*(-1 if (z[0]+q[0])%2 else 1) for x,y,(z,q) in zip(values,w['witnesses'][0],w['columns']))%p
        even=(f+tf)*pow(2,-1,p)%p
        require(f and tf and even,'missing formal-neighborhood trivializing section')
        rows.append({'node':point['node'],'F':f,'tauF':tf,'even':even})
    require(len(rows)==4)
    return rows

def graph(name,a,hsquare,chi,h0m1):
    size=len(a);n=size//2
    d=[2]*n+[1]*n;r=[1]*size;core=[1]*n+[0]*n;kh=[4]*n+[0]*n
    require(all(a[j][j]==(-4 if j<n else -2) for j in range(size)))
    require(all(sum(a[j][k] for k in range(n) if k!=j)==2 for j in range(n)))
    require(all(a[j][j+n]==1 for j in range(n)))
    dint=[sum(d[i]*a[i][j] for i in range(size)) for j in range(size)]
    rint=[sum(r[i]*a[i][j] for i in range(size)) for j in range(size)]
    require(dint==[-3]*n+[0]*n and rint==[-1]*size)
    dsquare=dot(d,a,d);hd=sum(x*y for x,y in zip(d,kh))
    lsquare=9*hsquare+24*hd+16*dsquare;hl=3*hsquare+4*hd
    require((dsquare,hd,lsquare,hl)==((-24,32,672,224) if name=='Y' else (-12,16,336,112)))
    chi_l=chi+(lsquare-hl)//2;h1=h0m1-chi_l
    require(h1==(6 if name=='Y' else 4))
    # Degrees controlling H1(O_D(-kD)) for every integer k>=1.
    on_core=[0,3];nilpotent_core=[1,3]
    residual=[on_core[0]-2,on_core[1]];nilpotent_residual=[nilpotent_core[0]-2,nilpotent_core[1]]
    require(at(residual,1)>0 and residual[1]>0 and at(nilpotent_residual,1)>0 and nilpotent_residual[1]>0)
    h0_thick=[h1,-hd//2,-dsquare//2]
    require(at(h0_thick,1)==2)
    # RR on L^m and on (3m)K, with h2=0 and the constant h1 derived geometrically.
    chi_poly=[chi,-hl//2,lsquare//2];h0_poly=plus(chi_poly,[h1])
    h0_3k=[chi,-3*hsquare//2,9*hsquare//2]
    h0_4mD=[h1,-2*hd,-8*dsquare]
    require(plus(h0_3k,h0_4mD)==h0_poly)
    return {'name':name,'components':n,'matrix':a,'D_coefficients':d,'R_coefficients':r,
        'core_coefficients':core,'canonical_intersections':kh,'D_intersections':dint,'R_intersections':rint,
        'D_square':dsquare,'K_D':hd,'L_square':lsquare,'K_L':hl,'chi_O':chi,
        'm1_h0_input':h0m1,'m1_chi':chi_l,'all_m_h1':h1,
        'core_degree_k':[0,3],'nilpotent_core_degree_k':[1,3],
        'core_after_two_gluing_points':residual,'nilpotent_after_two_gluing_points':nilpotent_residual,
        'h0_nD_coefficients':h0_thick,'all_m_h0_coefficients':h0_poly,
        'all_m_chi_coefficients':chi_poly,'h0_3mK_coefficients':h0_3k,'h0_4mD_coefficients':h0_4mD}

def computations():
    cert,f63,w=prior()
    y=cert['computed']['intersections']['intersection_matrix']
    require(len(y)==8 and all(len(r)==8 for r in y))
    # Pullbacks of Qa,Qb,F27,F35 on the unramified null configuration.
    pb=[[1,1,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1]]
    x=[]
    for v in pb:
        row=[]
        for u in pb:
            value=dot(v,y,u);require(value%2==0);row.append(value//2)
        x.append(row)
    require(x==[[-4,2,1,0],[2,-4,0,1],[1,0,-2,0],[0,1,0,-2]])
    gy=graph('Y',y,32,12,242);gx=graph('X',x,16,8,124)
    hy=gy['all_m_h0_coefficients'];hx=gx['all_m_h0_coefficients'];target=[hx[0],2*hx[1],4*hx[2]]
    odd=plus(hy,scale(hx,-1));codim=plus(target,scale(hy,-1))
    rank=plus(hy,[-1]);delta=[0,112,336];cokernel=plus(delta,scale(rank,-1))
    gluing_source=[0,0,672];gluing_target=[0,112,672]
    gluing_rank=plus(gluing_source,scale(hx,-1));gluing_cokernel=plus(gluing_target,scale(gluing_rank,-1))
    require(hy==[18,-112,336] and hx==[12,-56,168] and odd==[6,-56,168])
    require(codim==[-6,0,336] and cokernel==[-17,224,0])
    require(plus(rank,cokernel)==delta and plus(cokernel,[17])==[0,224,0])
    require(gluing_rank==[-12,56,504] and gluing_cokernel==[12,56,168])
    table=[]
    for m in (1,2,3,5):
        table.append({'m':m,'h0_Y':at(hy,m),'h0_X_even':at(hx,m),'h0_odd':at(odd,m),
            'target_h0_X_2mP':at(target,m),'norm_image_dimension':at(hy,m)-1,'norm_codimension':at(codim,m),
            'genus_one_delta':at(delta,m),'nodal_map_rank_if_exists':at(rank,m),
            'nodal_map_cokernel_if_exists':at(cokernel,m),'conductor_line_degree':-224*m,
            'F37_gluing_rank_if_inputs_exist':at(gluing_rank,m),
            'F37_gluing_kernel_if_inputs_exist':at(hx,m),'F37_gluing_cokernel_if_inputs_exist':at(gluing_cokernel,m)})
    # Independent recurrence check on thickening Euler characteristics.
    for g in (gx,gy):
        for n in range(2,9):
            h0n=at(g['h0_nD_coefficients'],n);h0prev=at(g['h0_nD_coefficients'],n-1)
            kernel_chi=-(g['D_square']+g['K_D'])//2-(n-1)*g['D_square']
            require(h0n-h0prev==kernel_chi)
    return {'unit_values':unit_values(cert,w),'X':gx,'Y':gy,
        'odd_h0_coefficients':odd,'target_h0_coefficients':target,'norm_codim_coefficients':codim,
        'nodal_smoothing_rank_coefficients':rank,'nodal_smoothing_cokernel_coefficients':cokernel,
        'genus_one_delta_coefficients':delta,'h1_curve_normal_bundle':17,
        'F37_gluing_rank_coefficients':gluing_rank,'F37_gluing_cokernel_coefficients':gluing_cokernel,'table':table}
    

def claims():
    return {'scope':'SOURCE_CONDITIONAL_COMPLEX_MODEL_RESEARCH_UNAUDITED_ZERO_CREDIT',
        'all_m_h1_Y':6,'all_m_h1_X':4,
        'all_m_h0_Y':'336*m^2-112*m+18','all_m_h0_X':'168*m^2-56*m+12',
        'all_m_h0_odd':'168*m^2-56*m+6','all_m_norm_codimension':'336*m^2-6',
        'norm_map_generic_degree':2,'m1_norm_codimension':330,
        'F37_gluing_rank_if_source_complete':'504*m^2+56*m-12','m1_F37_gluing_rank_if_source_complete':548,
        'F37_gluing_actual_test_evaluated':False,
        'genus_one_isolation':'REUSE_EXISTING_ROUTE_C_NOT_NEW_EXCLUSION',
        'nodal_genus_one_tangent_dimension_if_exists':0,
        'nodal_smoothing_cokernel_if_exists':'224*m-17','m1_nodal_smoothing_cokernel_if_exists':207,
        'genus_one_existence_proved':False,'genus_one_nonexistence_proved':False,
        'actual_marked_conductor_evaluated':False,'coreless_no_clump_proved':False,
        'actual_source_adapter_proved':False,'candidate_exclusion':0,'uniform_degree_bound':False,
        'MB104':'OPEN','theorem_credit':0,'receiver_credit':0,'endpoint_credit':0,'independent_audit':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--certificate',type=Path,default=ROOT/'F65-certificate.json')
    ap.add_argument('--replay-f64',action='store_true');a=ap.parse_args()
    c=json.loads(a.certificate.read_text())
    require(set(c)=={'schema','claims','computed','files_sha256'},'certificate shape mismatch')
    require(c['schema']=='MB104-F65-RESEARCH-CERT-v1' and c['claims']==claims(),'claim scope mismatch')
    require(set(c['files_sha256'])==EXPECTED_FILES,'incomplete dependency hash table')
    for name,h in c['files_sha256'].items():require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'dependency hash mismatch: '+name)
    require(c['computed']==computations(),'computed evidence mismatch')
    if a.replay_f64:
        with tempfile.TemporaryDirectory(prefix='f65-prior-replay-') as d:
            with zipfile.ZipFile(ROOT/'MB104-F64-20261029.zip') as z:z.extractall(d)
            for flags in ([],['-O']):
                run=subprocess.run([sys.executable]+flags+[str(Path(d)/'verify_f64.py')],capture_output=True,text=True)
                require(run.returncode==0,run.stderr or run.stdout)
    print(json.dumps({'status':'PASS','all_m_h1_Y':6,'all_m_h1_X':4,
        'norm_codimension':'336*m^2-6','m1_F37_gluing_rank_if_source_complete':548,'m1_nodal_cokernel_if_exists':207,
        'geometric_deductions':'conditional; see proof note','candidate_exclusion':0,'MB104':'OPEN'}))
if __name__=='__main__':
    try:main()
    except Exception as exc:print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
