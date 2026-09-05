#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09E/character-elliptic-quotient-arithmetic-preflight.json'
INV=ROOT/'stages/stage36/36-02/representative-inventory.json'
PHYS=ROOT/'stages/stage36/36-03/physical-open-boundary.json'
SIGN=ROOT/'stages/stage29/29-02ha/exact-sign-cover-model.md'
PREV=ROOT/'stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
W01=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'

CERT_BLOB='081b704fecaa3bd39e6a523ee7beaefe706683f4'
EXPECTED_BASE='bd402241fa69ea00d00b48695c883d1cbdbc2dbb'
LOCKS={
 INV:'88130b9380a677a191f91c24df87618e65be0a2f',
 PHYS:'fc1947b2de08f7d8a104bdc91902b20e88635349',
 SIGN:'fc2d5284a259750f45d2d756a952002671e3bccc',
 PREV:'7fb67b8bf5a37d16ef527aea6109eb0782d61201',
 W03:'1d5275321f42768a6414d4610ac912c63be43f96',
 W01:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b',
}
MOVING={'A3','B2','B1','C'}
CONST={'A1':'t','A2':'1','B3':'t+1'}
TYPE={
 frozenset(['B2','B1','C']):('M1','t',+1,'X_plus=s+t+1'),
 frozenset(['A3','B2','B1']):('M2','t',-1,'X_minus=-s'),
 frozenset(['A3','B2','C']):('P1','t+1',+1,'X_plus=s+t+1'),
 frozenset(['A3','B1','C']):('P2','t+1',-1,'X_minus=-s'),
}
EXPECTED=[
 ('Q6_GEOM8','010','M1','1','t','1','E_t_PLUS','X_plus=s+t+1'),
 ('Q6_GEOM8','100','M2','t+1','t','-(t+1)','E_t_MINUS','X_minus=-s'),
 ('Q6_GEOM8','101','P1','t','t+1','t','E_t1_PLUS','X_plus=s+t+1'),
 ('Q2_GEOM8','001','P2','t','t+1','-t','E_t1_MINUS','X_minus=-s'),
 ('Q2_GEOM8','010','M2','1','t','-1','E_t_MINUS','X_minus=-s'),
 ('Q2_GEOM8','100','M1','t+1','t','t+1','E_t_PLUS','X_plus=s+t+1'),
 ('Q2_GEOM2','001','M1','t','t','t','E_t_PLUS','X_plus=s+t+1'),
 ('Q2_GEOM2','100','P2','t+1','t+1','-(t+1)','E_t1_MINUS','X_minus=-s'),
 ('Q2_GEOM2','110','M2','1','t','-1','E_t_MINUS','X_minus=-s'),
]

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def xor_support(supports,bits):
    out=set()
    for bit,sup in zip(bits,supports):
        if bit:
            out.symmetric_difference_update(sup)
    return out
def dot(a,b): return sum(int(x)*int(y) for x,y in zip(a,b))%2
def twist_string(const_lines,sign):
    factors=[]
    if 'A1' in const_lines: factors.append('t')
    if 'B3' in const_lines: factors.append('t+1')
    # A2 contributes 1
    d='*'.join(factors) if factors else '1'
    if sign<0:
        if d=='1': return '-1'
        if d=='t': return '-t'
        return f'-({d})'
    return d
def physical_class(param,sign):
    if param=='t': return 'E_t_PLUS' if sign>0 else 'E_t_MINUS'
    return 'E_t1_PLUS' if sign>0 else 'E_t1_MINUS'

def main()->None:
    req(blob(CERT)==CERT_BLOB,'36-09E certificate blob drift')
    for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked source drift: {p}')
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE36_36_09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT_V1','36-09E schema moved')
    req(c['base_main_sha']==EXPECTED_BASE,'36-09E base moved')
    req(c['entry_authority']=={
      'stage36_36_09D_promotion_pr':1592,
      'promotion_exact_head':'631d773a0f341954507eacf303f0c5f7cbdc836a',
      'promotion_exact_head_ci_run':33956504502,
      'promotion_exact_head_ci_job':101280695175,
      'promotion_merged_main_sha':EXPECTED_BASE,
      'selected_route':'B6_FIBRATION_TO_CURVE_BASE'
    },'36-09E entry authority moved')

    prev=json.loads(PREV.read_text())
    req(prev['character_quotient_inventory']['j_multiset_each_representative']==['J_MINUS','J_MINUS','J_PLUS'],'36-09D j inventory moved')
    req(prev['q_defined_pencil']['generic_affine_chart']=='y=1, x=t, z=s','36-09D chart moved')

    sign=SIGN.read_text()
    for text in [
      'simultaneous square roots of these seven forms',
      'the seven values `L_i(q)` have a common square class',
      'q\\text{ lifts to }\\bar S(\\mathbf Q)'
    ]:
        req(text in sign,f'exact sign-cover source phrase missing: {text}')
    phys=json.loads(PHYS.read_text())
    req(phys['seven_line_base']['coordinates']=='[x:y:z]=[a1^2:a2^2:a3^2]','physical base coordinates moved')
    req(phys['physical_open']['side_coordinates_nonzero']==['a1','a2','a3'],'physical side-open moved')

    inv=json.loads(INV.read_text())
    rows=[]
    prev_table={rep:{x['character']:x for x in rdata['genus1_characters']}
                for rep,rdata in prev['representative_fibers'].items()}
    for rep in ['Q6_GEOM8','Q2_GEOM8','Q2_GEOM2']:
        data=inv['representatives'][rep]
        basis=[set(x) for x in data['character_supports']]
        labels=data['label_map']
        for ch,old in prev_table[rep].items():
            bits=[int(x) for x in ch]
            sup=xor_support(basis,bits)
            # Independent cross-check against label-map character support.
            dot_sup={L for L,v in labels.items() if dot(ch,v)}
            req(sup==dot_sup,f'{rep} {ch}: Kummer support disagrees with label-map character support')
            moving=frozenset(sup & MOVING)
            req(moving in TYPE,f'{rep} {ch}: unknown genus-1 moving support {sorted(moving)}')
            typ,param,geom_sign,xexpr=TYPE[moving]
            req(set(old['branch_lines'])-{ 'INF' }==set(moving),f'{rep} {ch}: 36-09D branch support moved')
            const=sup-set(moving)
            req(const <= set(CONST),f'{rep} {ch}: unexpected constant line')
            d_parts=[]
            if 'A1' in const: d_parts.append('t')
            if 'B3' in const: d_parts.append('t+1')
            d='*'.join(d_parts) if d_parts else '1'
            generic=twist_string(const,geom_sign)
            cls=physical_class(param,geom_sign)  # t and t+1 are squares on physical base.
            rows.append((rep,ch,typ,d,param,generic,cls,xexpr))
    req(rows==EXPECTED,f'exact nine-row Legendre/twist table moved: {rows}')
    declared=[(r['representative'],r['character'],r['branch_type'],r['constant_twist'],r['legendre_parameter'],r['generic_twist'],r['physical_class'],r['physical_X'])
              for r in c['nine_genus1_occurrences']]
    req(declared==EXPECTED,'certificate nine-row table differs from reconstruction')

    gd=c['generic_legendre_dictionary']
    req(gd['M1']['change']=='X=s+t+1' and gd['M1']['legendre_twist']=='d' and gd['M1']['legendre_parameter']=='t','M1 transform moved')
    req(gd['M2']['change']=='X=-s' and gd['M2']['legendre_twist']=='-d' and gd['M2']['legendre_parameter']=='t','M2 transform moved')
    req(gd['P1']['change']=='X=s+t+1' and gd['P1']['legendre_twist']=='d' and gd['P1']['legendre_parameter']=='t+1','P1 transform moved')
    req(gd['P2']['change']=='X=-s' and gd['P2']['legendre_twist']=='-d' and gd['P2']['legendre_parameter']=='t+1','P2 transform moved')

    ps=c['physical_squareclass_restriction']
    req(ps['chart_ratio_consequences']=={'t=x/y':'square','s=z/y':'square','t+1=(x+y)/y':'square'},'physical square ratios moved')
    req(ps['therefore_twist_factors_t_and_t_plus_1_are_rational_squares'] is True,'physical twist collapse moved')
    # Exact t=1 exclusion: a rational square has even 2-adic valuation; v2(2)=1.
    n=2; v2=0
    while n%2==0:
        v2+=1; n//=2
    req(v2==1 and v2%2==1,'2-adic nonsquare check failed')
    req(ps['special_t1_status']=='ELIMINATED_FOR_ENDPOINT_IMAGE','t=1 endpoint status moved')

    # Verify the genus-0 parameterization identities:
    # u=(r^2-1)/(2r), v=(r^2+1)/(2r), so v^2-u^2=1.
    # Numerator identity: (r^2+1)^2-(r^2-1)^2 = 4r^2.
    # coefficients low-to-high
    def mul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]+=x*y
        return out
    def sub(a,b):
        n=max(len(a),len(b)); return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)]
    rp=[1,0,1]   # r^2+1
    rm=[-1,0,1]  # r^2-1
    req(sub(mul(rp,rp),mul(rm,rm))==[0,0,4,0,0],'physical base hyperbola parameterization identity failed')
    par=c['physical_base_parameterization']
    req(par['t']=='(r^2-1)^2/(4*r^2)' and par['t_plus_1']=='(r^2+1)^2/(4*r^2)','physical t parameterization moved')
    req(par['physical_exclusions']==['r=0','r=1','r=-1'],'physical r exclusions moved')

    collapse=c['four_family_collapse']
    req(collapse['occurrence_collapse_count']=={'genus1_occurrences':9,'physical_curve_point_types':4},'nine-to-four count moved')
    req(collapse['common_J_MINUS_pair_each_representative']==['E_t_PLUS','E_t_MINUS'],'common J-minus pair moved')
    req(collapse['J_PLUS_across_all_representatives_requires']==['E_t1_PLUS','E_t1_MINUS'],'J-plus +/- pair moved')
    classes={r[-2] for r in rows}
    req(classes=={'E_t_PLUS','E_t_MINUS','E_t1_PLUS','E_t1_MINUS'},'physical classes do not collapse to four')

    pair=c['paired_receiver']
    req(pair['X_plus']=='s+t+1' and pair['X_minus']=='-s','paired X definitions moved')
    req(pair['linear_compatibility']=='X_plus+X_minus=t+1','paired X compatibility moved')
    req(pair['S34_W03_applicability_matched'] is True and pair['S34_W03_intersection_exclusion_executed'] is False,'S34-W03 boundary moved')
    w03=W03.read_text()
    for text in ['RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION','B(Q) intersect K(Q) = empty','factor cover Q-pointset complete = not implied']:
        req(text in w03,f'S34-W03 contract phrase missing: {text}')
    req('SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT' in W01.read_text(),'S34-W01 identity moved')
    req('GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION' in W02.read_text(),'S34-W02 identity moved')

    route=c['route_decision']
    req(route['B6_FIBRATION_TO_CURVE_BASE']=='LIVE_PAIRED_LEGENDRE_PLUS_MINUS_RECEIVER_OVER_GENUS0_PHYSICAL_BASE','B6 36-09E status moved')
    req(route['S34_W03']=='APPLICABILITY_MATCHED_NOT_EXECUTED','S34-W03 route status moved')
    req(route['S34_W02_TRIGGERED'] is False and route['S34_W01_TRIGGERED'] is False,'premature Arsenal trigger')
    req(route['next_route_after_hostile_audit']=='36-09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT','36-09F routing moved')
    req(c['cycle_update']['new_material_block'] is False and c['cycle_update']['B6_remains_sole_live'] is True,'cycle continuation moved')
    req(all(v is False for v in c['claims'].values()),'36-09E higher credit leaked')

    print('PASS STAGE36_36_09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT')
    print('physical base: t=u^2, t+1=v^2 => genus0 r-parameter; special t=1 eliminated')
    print('9 genus1 occurrences => 4 paired Legendre/-1-twist point types with X_plus+X_minus=t+1')
    print('B6=LIVE; S34-W03 applicability matched but intersection exclusion not executed; next=36-09F after hostile audit')

if __name__=='__main__': main()
