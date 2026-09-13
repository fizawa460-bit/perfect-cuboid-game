#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
INTERFACE=HERE/'INTERFACE.json'
PRODUCER=HERE/'hpadj_full178_terminal_picard64_adapter.py'
HPADJ=ROOT/'stages/stage32/management/hpadj-01/RESULT.json'
MANIFEST=ROOT/'stages/stage32/residual-32-01-production/full178-manifest.json'
FAMILY=ROOT/'stages/stage32/residual-32-01-production/compressed_terminal_family.py'
INDEXER=ROOT/'stages/stage32/residual-32-01-production/compressed_terminal_indexer.py'
PREFIX=ROOT/'stages/stage32/residual-32-01-production/pairing_prefix_engine.py'
HPERP=ROOT/'stages/stage32/residual-32-01-production/hperp_integral_adapter.py'
BUNDLE=ROOT/'stages/stage33/33-07/picard_base_rows_retained.py'

INTERFACE_BLOB='8a30e3aa30777460f344eb19836dc725dd442329'
INTERFACE_CANON='cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6'
PRODUCER_BLOB='756a859a5949b5054202228d9df005b6c55a20fc'
LOCKS={
 HPADJ:'520b6b0f230e23fb5ea34b80fef591cfa5f9be4b',
 MANIFEST:'0a46b34e278688240656b4977e9cb7f589e90e06',
 FAMILY:'90ff82ed312dcc0cb32cf207935945f550e29170',
 INDEXER:'4fb0a8dd34909494bd62646373e42877ed7a3c9e',
 PREFIX:'c8e87c6598fa1cd7ba1675fc35fa83bea983c94b',
 HPERP:'fb1eb380ca786e42a6b00c5ef454b0e79fdba771',
 BUNDLE:'82e4d450a1d852e34f6615440fb88a029c6e54eb',
}

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p):
    raw=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def canon(o):
    c=dict(o); c.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def main():
    req(blob(INTERFACE)==INTERFACE_BLOB,'interface blob drift')
    req(blob(PRODUCER)==PRODUCER_BLOB,'producer blob drift')
    for p,b in LOCKS.items(): req(p.is_file() and blob(p)==b,'source-lock drift '+str(p.relative_to(ROOT)))
    x=json.loads(INTERFACE.read_text())
    req(x.get('canonical_sha256_without_this_field')==INTERFACE_CANON and canon(x)==INTERFACE_CANON,'interface canonical drift')
    req(x.get('schema')=='STAGE32EX5_HPADJ_FULL178_TERMINAL_TO_PICARD64_INTERFACE_V1','schema')
    req(x.get('demand_id')=='S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1','demand id')
    req(x.get('status')=='PRODUCED_SOURCE_LOCKED_EXACT_INTERFACE_NO_MATH_CREDIT','status')
    p=x['population_cardinality_replay']
    req(p['affected_rows']==178 and p['charged_terminal_lower_bound']==27104321327305699275487,'population count')
    req(p['exceptional_prefix_stratum_instances']==19700993066083231249,'prefix count')
    req(p['genus0_terminal_lower_bound']==6263333577918328238904 and p['genus1_terminal_lower_bound']==20840987749387371036583,'genus totals')
    req(p['per_row_stream_sha256']=='5852e58fdd570e05c057d5fcaf426f6b25fefb1eaf83ae1329657b42289775ae' and p['matches_hpadj01_source_lock'] is True,'population identity')
    rows=x['all_178_rows_partition']; req(rows['row_count']==178 and rows['manifest_blob_sha1']==LOCKS[MANIFEST],'row partition')
    t=x['terminal_identity_or_exact_rank_unrank_contract']; req(t['rank_unrank_roundtrip_exact'] is True and t['indexer_blob_sha1']==LOCKS[INDEXER] and t['full_population_materialization_required'] is False,'terminal identity')
    m=x['terminal_to_picard64_map']
    req(m['inverse_denominator']==8 and m['terminal_pairing_count']==11 and m['free_pairing_parameter_count']==53 and m['full_picard64_coordinate_count']==64,'map dimensions')
    fixed=[int(v) for v in m['terminal_fixed_selected_positions_0based']]; free=[int(v) for v in m['free_selected_positions_0based']]
    req(len(fixed)==11 and len(free)==53 and sorted(fixed+free)==list(range(64)),'selected64 partition')
    req(m['inverse_integer_matrix_sha256']=='7b4d0601585f011e168bf5c4b15086950b0e3e3e16c90826b7413cdbe183c233','inverse map')
    req(m['terminal_fixed_coefficient_matrix_sha256']=='e8f4a9004177fc2a2023775431505d4ef39b7b808bd41cb517787c235ab170fe','fixed matrix')
    req(m['free_completion_coefficient_matrix_sha256']=='ad27fa86fbc98d55a97af5fd9d247fb880af9dac58d6429ca029d6b8ca4c288b','free matrix')
    r=x['reconstructed_picard64_coordinate_identity']; req(r['fixed_plus_free_affine_fiber_exact'] is True and r['unique_coordinate_vector_for_each_integral_selected64_completion'] is True and r['terminal_alone_asserts_completion_exists'] is False,'fiber semantics')
    req(all(v is False for v in x['credit_firewall'].values()),'credit firewall')
    print('PASS_STAGE32EX5_HPADJ_FULL178_TERMINAL_PICARD64_INTERFACE',INTERFACE_CANON)
    print('rows=178 charged_terminals=27104321327305699275487 denominator=8 fixed=11 free=53 math_credit=NO merge=NO')
if __name__=='__main__': main()
