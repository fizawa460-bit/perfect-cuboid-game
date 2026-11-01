#!/usr/bin/env python3
"""Check both witness values at all 34 excluded A1 nodes of the fixed model.
Values at infinity use the leading weighted-degree coefficient; its frame
differs by a nonzero canonical-bundle unit, immaterial for zero testing.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
P=97;b=14;ii=22;e=ii*b%P;c=(1+ii)%P

def main():
    data=json.loads((ROOT/'matrix97.json').read_text());cols=data['columns']
    witnesses=json.loads((ROOT/'witness97.json').read_text())['witnesses']
    points=[]
    # The 8 hv nodes on sigma_w=-2, outside the selected half-fiber.
    for rz in (b,-b%P,e,-e%P):
        for uz in (b,-b%P):points.append(('hv_other',('finite',rz,uz,0),('finite',e,b,0)))
    # The 8 hu nodes on sigma_z=-2i, outside the selected half-fiber.
    for rw in (c,-c%P,ii*c%P,-ii*c%P):
        for vw in (e,-e%P):points.append(('hu_other',('finite',ii*c%P,0,e),('finite',rw,0,vw)))
    half=pow(2,-1,P)
    for ztype,zpoint in [('finite',('finite',0,1,ii)),('infinity',('infinity',0,half,half))]:
        for wtype in ('finite','infinity'):
            for su in (1,-1):
                for sv in (1,-1):
                    wpoint=('finite',0,su%P,sv*ii%P) if wtype=='finite' else ('infinity',0,su*half%P,sv*half%P)
                    points.append(('T_'+ztype+'_'+wtype,zpoint,wpoint))
    points.extend([('P27',('finite',e,b,0),('finite',b,b,0)),('P35',('finite',c,0,e),('finite',c,0,-e%P))])
    def mon(leg,point):
        j,a,bb=leg;kind,r,u,v=point
        if kind=='infinity':return 0 if j+2*a+2*bb!=28 else pow(u,a,P)*pow(v,bb,P)%P
        return pow(r,j,P)*pow(u,a,P)*pow(v,bb,P)%P
    rows=[]
    for label,zpoint,wpoint in points:
        row=[mon(z,zpoint)*mon(w,wpoint)%P for z,w in cols]
        values=[sum(a*b for a,b in zip(row,x))%P for x in witnesses]
        assert any(values)
        rows.append({'type':label,'z':zpoint,'w':wpoint,'values':values})
    assert len(rows)==34
    good=json.loads((ROOT/'witness97.json').read_text())
    print(json.dumps({'excluded_nodes':len(rows),'no_common_excluded_zero':True,
                      'each_witness_excluded_zeros':[sum(not r['values'][k] for r in rows) for k in range(2)],
                      'all_tangent_axis_coefficients_nonzero':all(f[0] and f[-1] for forms in good['leading_forms'] for f in forms)}))
    (ROOT/'F61-excluded-nodes97.json').write_text(json.dumps({'prime':P,'nodes':rows,'all_34_have_no_common_zero':True},indent=2)+'\n')
if __name__=='__main__':main()
