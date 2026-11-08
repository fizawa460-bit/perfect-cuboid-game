#!/usr/bin/env python3
"""Unique norm-one unit correction of a local code in loc_2(V).

Global preconditions are necessary: an ideal A with A^2=(alpha), and
N(alpha) a positive rational square. Local membership alone does not certify
that arbitrary user-supplied data define a global unramified Kummer class.
"""
from pathlib import Path
import json


class UnitCorrection:
    def __init__(self,images):
        self.images=list(images);self.echelon={}
        assert len(self.images)==55
        for i,row in enumerate(self.images):
            value=row;expression=1<<i
            for p,(r,e) in sorted(self.echelon.items(),reverse=True):
                if value>>p&1:value^=r;expression^=e
            assert value
            self.echelon[value.bit_length()-1]=(value,expression)

    def solve(self,code):
        assert code>=0 and code.bit_length()<=107
        value=code;expression=0
        for p,(r,e) in sorted(self.echelon.items(),reverse=True):
            if value>>p&1:value^=r;expression^=e
        return value,expression

    def code_of_unit(self,mask):
        assert mask>=0 and mask.bit_length()<=55
        value=0
        for i,c in enumerate(self.images):
            if mask>>i&1:value^=c
        return value

    def left_inverse_rows(self):
        columns=[self.solve(1<<j)[1] for j in range(107)]
        return [sum(1<<j for j,c in enumerate(columns) if c>>i&1) for i in range(55)]


def main():
    here=Path(__file__).resolve().parent
    data=json.loads((here/'units381_exact.json').read_text())
    images=[int(x['unit_local_code'],16) for x in data['basis_images']]
    correct=UnitCorrection(images);rows=correct.left_inverse_rows()
    for i,c in enumerate(images):assert correct.solve(c)==(0,1<<i)
    for c,m in zip(data['kernel_basis_local_codes'],data['kernel_basis_as_unit_bitmasks']):
        assert correct.solve(int(c,16))==(0,int(m,16))
    projector=[]
    for j in range(107):
        _,e=correct.solve(1<<j);p=correct.code_of_unit(e)
        assert correct.code_of_unit(correct.solve(p)[1])==p
        projector.append(p)
    print(json.dumps({'local_code_dimension':107,'norm_one_unit_dimension':55,
        'unit_images':list(map(hex,images)),
        'left_inverse_55_rows':list(map(hex,rows)),
        'projector_107_columns':list(map(hex,projector)),
        'global_domain':'V: all finite valuations even, norm a positive rational square',
        'global_formula':'eta = alpha * product(u_i^e_i), where e = left_inverse(loc2(alpha))',
        'global_kernel_of_loc2':'H_nr (parent theorem)',
        'map_Hnr_to_Cl_2torsion':'isomorphism (parent V decomposition)',
        'actual_2torsion_ideal_basis':'NOT_CONSTRUCTED',
        'actual_nontrivial_unramified_classes':'NOT_CONSTRUCTED'},indent=2))


if __name__=='__main__':main()
