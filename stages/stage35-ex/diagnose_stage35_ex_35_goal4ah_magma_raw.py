#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
S33=ROOT/'stages/stage33/33-07'
sys.path.insert(0,str(S33))
import stoll_cuboid_source as scs

AA=json.loads((ROOT/'stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json').read_text())
Z=json.loads((ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json').read_text())
P=json.loads((S33/'galois-known-class-permutations.json').read_text())
assert AA['schema']=='STAGE35_EX_35_GOAL4AA_QI_CYCLIC_LINEAR_HYPERPLANE_BLOCKER_V1'
assert Z['schema']=='STAGE35_EX_35_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_V1'
assert P['canonical_sha256']=='e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30'

formal=[0]*140
cc=[int(x) for x in P['cc_permutation_1based']]
for k,v in Z['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(k); c=int(v); formal[i-1]+=c; formal[cc[i-1]-1]+=c
for k,v in AA['class_B_principalization_target']['simplified_boundary_divisor_E_B'].items():
    formal[int(k)-1]-=int(v)
assert sum(x!=0 for x in formal)==69
strict=formal[:92]
assert sum(x!=0 for x in strict)==33

_,core,blob,source_attempt=scs.load_pinned_source()
assert blob=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
strict_literal='['+','.join(str(int(x)) for x in strict)+']'
code='SetColumns(0);\nquick := true;\n'+core+r'''
targetStrict := __STRICT__;
assert #Cs eq 92;
D := ZeroDivisor(S);
for j in [1..92] do
  if targetStrict[j] ne 0 then
    D +:= targetStrict[j] * Divisor(S, Cs[j] : CheckSaturated := true, CheckDimension := true);
  end if;
end for;
printf "GOAL4AH_RAW_CARTIER=%o\n", IsCartier(D);
printf "GOAL4AH_RAW_DONE\n";
'''.replace('__STRICT__',strict_literal)

payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(scs.MAGMA_URL,data=payload,headers={
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'text/html, application/xml, application/xhtml+xml',
    'Referer':scs.MAGMA_REFERER,
    'User-Agent':'perfect-cuboid-stage35ex/4ah-raw-g1'},method='POST')
resp,attempt=scs.urlopen_retry(req,240,'Stage35-EX Goal4AH raw Magma diagnostic')
with resp:
    raw=resp.read().decode('utf-8',errors='replace')
print('GOAL4AH_RAW_XML_BYTES='+str(len(raw.encode())))
print('GOAL4AH_RAW_XML_PREFIX='+json.dumps(raw[:12000]))
root=ET.fromstring(raw)
results=[]
for result in root.findall('.//results'):
    for line in result.findall('.//line'):
        results.append(''.join(line.itertext()))
stdout='\n'.join(results)+'\n'
print('GOAL4AH_RAW_RESULTS_PREFIX='+json.dumps(stdout[:12000]))
all_nodes=[]
for node in root.iter():
    tag=node.tag.split('}')[-1]
    txt=''.join(node.itertext()).strip()
    if txt and tag.lower() not in {'results'}:
        all_nodes.append([tag,txt[:2000]])
print('GOAL4AH_RAW_NODE_TEXT='+json.dumps(all_nodes[:40],separators=(',',':')))
out={
    'schema':'STAGE35_EX_GOAL4AH_MAGMA_RAW_DIAGNOSTIC_V1',
    'source_blob_sha1':blob,
    'source_fetch_attempt':source_attempt,
    'magma_request_attempt':attempt,
    'raw_xml_bytes':len(raw.encode()),
    'completion_marker_present':'GOAL4AH_RAW_DONE' in stdout,
    'result_line_count':len(results),
    'theorem_credit':False,
    'endpoint_credit':False,
    'explicit_F_B_materialized':False,
    'E1_proved':False,
    'stage35_closed':False,
}
print('GOAL4AH_RAW_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
