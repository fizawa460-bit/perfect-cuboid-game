#!/usr/bin/env python3
"""Goal4AJ diagnostic: Q-defined orbit packet for all extension-valued denominator strict curves.

The retained denominator residual has 22 strict components.  Seven conjugate pairs are
written over Q(i) or Q(sqrt(2)); this leaf computes each pair union exactly, requires
its reduced Groebner basis to descend to Q, and emits the compact rational basis packet.
Diagnostic only: no literal denominator/F_B/E1 credit.
"""
from __future__ import annotations
import hashlib,json,subprocess,tempfile
from pathlib import Path

ORBIT_PREFLIGHT_SHA='4ae1a39e7c3b800e972f01202ec87a463dc5c3cdc6a7a6b2f71f05488edcc1e5'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
PAIRS=[(37,39),(26,31),(58,60),(25,32),(33,35),(28,29),(65,67)]
IDEALS={
37:'b2,ii*a3+a1,a2+c',39:'b2,ii*a3-a1,a2+c',
26:'c,ii*a1-b1,ii*a2+b2,ii*a3+b3',31:'c,ii*a1+b1,ii*a2-b2,ii*a3-b3',
58:'a2-a3,ss*a2+b1,b2-b3',60:'a2-a3,ss*a2-b1,b2-b3',
25:'c,ii*a1+b1,ii*a2+b2,ii*a3+b3',32:'c,ii*a1-b1,ii*a2-b2,ii*a3-b3',
33:'b1,ii*a2+a3,a1+c',35:'b1,ii*a2-a3,a1+c',
28:'c,ii*a1-b1,ii*a2-b2,ii*a3+b3',29:'c,ii*a1+b1,ii*a2+b2,ii*a3-b3',
65:'a3-a1,ss*a3+b2,b3+b1',67:'a3-a1,ss*a3-b2,b3+b1',
}
parts=[r'''
option(redSB);
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
''']
for i,j in PAIRS:
    parts.append(f'ideal P{i}={IDEALS[i]}; ideal P{j}={IDEALS[j]};\n')
    parts.append(f'ideal I{i}=std(surf+P{i}); ideal I{j}=std(surf+P{j});\n')
    parts.append(f'ideal J{i}_{j}=std(intersect(I{i},I{j}));\n')
    parts.append(f'print("PAIR_{i}_{j}_GENS="+string(size(J{i}_{j})));\n')
    parts.append(f'print("PAIR_{i}_{j}_BEGIN"); print(string(J{i}_{j})); print("PAIR_{i}_{j}_END");\n')
parts.append('print("GOAL4AJ_DEN_Q_ORBIT_PACKET_SINGULAR=PASS"); quit;\n')
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'q-orbits.sing'; p.write_text(''.join(parts),encoding='utf-8')
    cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=300)
if cp.returncode!=0 or 'GOAL4AJ_DEN_Q_ORBIT_PACKET_SINGULAR=PASS' not in cp.stdout:
    print(cp.stdout[-12000:]); print(cp.stderr[-4000:]); raise SystemExit('Q-orbit packet computation failed; no mathematical obstruction credit')
lines=cp.stdout.splitlines(); packet={}
for i,j in PAIRS:
    a=lines.index(f'PAIR_{i}_{j}_BEGIN'); b=lines.index(f'PAIR_{i}_{j}_END')
    text='\n'.join(lines[a+1:b]).strip(); gens=int(next(x for x in lines if x.startswith(f'PAIR_{i}_{j}_GENS=')).split('=',1)[1])
    if 'u' in text: raise SystemExit(f'pair {i},{j} reduced basis did not descend to Q')
    packet[f'{i}_{j}']={'indices':[i,j],'standard_basis_generator_count':gens,'basis_text':text,'basis_text_sha256':hashlib.sha256(text.encode()).hexdigest(),'basis_contains_extension_symbol_u':False,'descends_to_Q':True}
# exact previously proved compact formulas remain visible in the packet
assert packet['37_39']['basis_text_sha256']=='4505c270b54c43158488c8aa1ca772458f19204ad85daaf10ced00563333660a'
assert packet['26_31']['basis_text_sha256']=='3a67cfb347e3ca9b8e72b84c5d84dfbc5c77588e4930adfaf1efe9b3f5ac62f2'
assert packet['58_60']['basis_text_sha256']=='6262a9a4b6e7cb5f06381c60364c28f03f204b6fb9c1d4e9df6eed9edb75b392'
out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_Q_ORBIT_PACKET_DIAGNOSTIC_V1',
 'source_locks':{'orbit_pair_compactification_canonical_sha256':ORBIT_PREFLIGHT_SHA,'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA},
 'extension_pair_count':len(PAIRS),'extension_component_count':2*len(PAIRS),'all_pair_reduced_bases_descend_to_Q':True,
 'pair_packet':packet,
 'rational_singleton_indices':[1,8,9,17,11,21,16,24],
 'all_22_denominator_strict_components_representable_over_Q':True,
 'rational_field_constructor_enabled':True,
 'literal_denominator_coefficients_materialized':False,'literal_numerator_coefficients_materialized':False,'literal_F_B_materialized':False,'E1_proved':False,'theorem_credit':False,'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_DEN_Q_ORBIT_PACKET_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_DEN_Q_ORBIT_PACKET=PASS')
