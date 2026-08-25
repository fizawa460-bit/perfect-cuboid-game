#!/usr/bin/env python3
"""Derive exact K_a/K_b/K_c Picard-discriminant V4 actions from pullbacks.

The 20x64 Picard pullback for each coordinate K3 is injective.  Therefore the
integral action G_K is recovered uniquely from

    G_K * pullback = pullback * G_S.

This keeps the calculation integral and avoids importing the semisimple modular
twist labels into the two-adic lattice.  The resulting Picard discriminant
actions are the finite-form inputs for reconstructing the scaled coordinate-K3
transcendental pullback lattice L0.
"""
import hashlib,json,math
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent

ccs=json.loads((HERE/'picard-action-cc.json').read_text())
cts=json.loads((HERE/'picard-action-ct.json').read_text())
GScc=sp.Matrix(ccs['picard_action_64x64']); GSct=sp.Matrix(cts['picard_action_64x64'])
if GScc.shape!=(64,64) or GSct.shape!=(64,64): raise SystemExit('endpoint action shape regression')

def derive(mode):
    x=json.loads((HERE/f'{mode}-picard-maps.json').read_text())
    P=sp.Matrix(x['picard_gram_20x20']); KS=sp.Matrix(x['MatKtoS_20x64']); V=sp.Matrix(x['smith_right_transform_V_20x20'])
    diag=[abs(int(d)) for d in x['picard_smith_diagonal']]
    pos=[i for i,d in enumerate(diag) if d>1]; mods=[diag[i] for i in pos]
    expected={'kb':[4,4],'kc':[4,8],'ka':[4,8]}[mode]
    if mods!=expected: raise SystemExit(f'{mode} discriminant moduli regression {mods}')
    piv=list(KS.rref()[1])
    if len(piv)!=20: raise SystemExit(f'{mode} pullback rank regression')
    B=KS[:,piv]
    if B.det()==0: raise SystemExit(f'{mode} pivot minor singular')
    Binv=B.inv()
    def induced(GS):
        G=(KS*GS)[:,piv]*Binv
        if any(sp.denom(v)!=1 for v in G): raise SystemExit(f'{mode} induced action nonintegral')
        G=sp.Matrix([[int(v) for v in row] for row in G.tolist()])
        if G*KS!=KS*GS: raise SystemExit(f'{mode} pullback equivariance regression')
        if G*P*G.T!=P or G*G!=sp.eye(20): raise SystemExit(f'{mode} integral isometry regression')
        return G
    Gcc=induced(GScc); Gct=induced(GSct)
    if Gcc*Gct!=Gct*Gcc: raise SystemExit(f'{mode} V4 commuting regression')
    Vin=V.inv()
    if any(sp.denom(v)!=1 for v in Vin): raise SystemExit(f'{mode} Smith V not unimodular')
    def disc_action(G):
        A=Vin*G.T*V
        if any(sp.denom(v)!=1 for v in A): raise SystemExit(f'{mode} discriminant action nonintegral')
        return [[int(A[pos[i],pos[j]])%mods[j] for j in range(len(pos))] for i in range(len(pos))]
    Mcc=disc_action(Gcc); Mct=disc_action(Gct)
    den=math.lcm(*mods)
    Bd=Vin*P.inv()*Vin.T; N=den*Bd
    if any(sp.denom(N[i,j])!=1 for i in pos for j in pos): raise SystemExit(f'{mode} discriminant pairing denominator regression')
    qnum=[]
    for ai,i in enumerate(pos):
        row=[]
        for aj,j in enumerate(pos):
            mod=(2*den if ai==aj else den)
            row.append(int(N[i,j])%mod)
        qnum.append(row)
    return {
      'source_sha256':x['canonical_sha256'],'picard_determinant':int(P.det()),
      'picard_discriminant_moduli':mods,'cc_action_mixed_moduli':Mcc,'ct_action_mixed_moduli':Mct,
      'discriminant_bilinear_numerator_denominator':den,
      'discriminant_bilinear_numerator_reduced':qnum,
      'integral_picard_action_recovered_from_endpoint_pullback':True,
      'semisimple_twist_used_for_integral_action':False,
    }

pieces={m:derive(m) for m in ('kb','kc','ka')}
# K_a and K_c are geometrically isomorphic, so their discriminant-form groups
# must have the same invariant factors; this is only a regression, not a Galois
# identification.
if pieces['ka']['picard_discriminant_moduli']!=pieces['kc']['picard_discriminant_moduli']:
    raise SystemExit('Ka/Kc geometric discriminant type regression')
cert={
 'schema':'STAGE33_07_COORDINATE_K3_DISCRIMINANT_V4_ACTIONS_V1',
 'source_locks':{'endpoint_cc_action_sha256':ccs['canonical_sha256'],'endpoint_ct_action_sha256':cts['canonical_sha256']},
 'pieces':pieces,
 'coordinate_piece_multiplicities':{'kb':3,'kc':1,'ka':3},
 'scaled_pullback_lattice':'<8>^10 direct_sum <16>^4',
 'scaled_discriminant_action_not_yet_constructed':True,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-LIFT-EACH-RANK2-DISCRIMINANT-ACTION-TO-INTEGRAL-T-ISOMETRY-THEN-CLASSIFY-V4-STABLE-INDEX512-GLUE',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'coordinate-k3-discriminant-v4-actions.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,
 'kb_cc':pieces['kb']['cc_action_mixed_moduli'],'kb_ct':pieces['kb']['ct_action_mixed_moduli'],
 'kc_cc':pieces['kc']['cc_action_mixed_moduli'],'kc_ct':pieces['kc']['ct_action_mixed_moduli'],
 'ka_cc':pieces['ka']['cc_action_mixed_moduli'],'ka_ct':pieces['ka']['ct_action_mixed_moduli'],
 'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
