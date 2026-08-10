#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4]
GOT=ROOT/'stages/stage14/data/14-t63/transverse_vertical_defect.json'
FROZEN=ROOT/'stages/stage14/data/14-t63/transverse_vertical_defect_frozen.json'

def main():
    got=json.loads(GOT.read_text()); frozen=json.loads(FROZEN.read_text())
    assert got['stage']==frozen['stage']
    for k,v in frozen['totals'].items(): assert got['totals'][k]==v,(k,got['totals'][k],v)
    for k,v in frozen['decision'].items(): assert got['decision'][k]==v,(k,got['decision'][k],v)
    P=got['totals']['auxiliary_prime_count']; assert P==8
    for r in got['packets']:
        assert r['transverse_defect'] >= P*P*r['transverse_principal']
        assert r['full_s4'] >= P*P*r['squareclass_energy']
        assert r['squareclass_energy']==r['states']+r['same_row_principal']+r['same_col_principal']+r['transverse_principal']
    print('Stage14-t63 frozen boundary verified')

if __name__=='__main__': main()
