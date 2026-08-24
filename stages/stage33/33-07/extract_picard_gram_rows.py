#!/usr/bin/env python3
"""Extract only the 64x64 endpoint Picard Gram matrix, one row per output line.

This is intentionally split from the Galois-action extraction so the public
Magma calculator never has to emit three 64x64 matrices in one response.
"""
import ast, hashlib, json, pathlib, re
from stoll_cuboid_source import load_pinned_source, run_magma

HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()
extra=r'''
printf "STAGE33_07_PGRAM_BEGIN\n";
for r in [1..64] do
  printf "P_ROW_%o=%o\n", r, [pmPic[r,c] : c in [1..64]];
end for;
printf "STAGE33_07_PGRAM_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
stdout,attempt=run_magma(code,180,'Stage33-07 Picard Gram rows Magma')
(HERE/'picard-gram-rows-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_PGRAM_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout); raise SystemExit('Picard Gram row extraction failed')
rows=[]
for r in range(1,65):
    m=re.search(rf'^P_ROW_{r}=(.+)$',stdout,re.M)
    if not m: raise SystemExit(f'missing P row {r}')
    row=ast.literal_eval(m.group(1))
    if len(row)!=64: raise SystemExit('P row length regression')
    rows.append([int(x) for x in row])
out={
 'schema':'STAGE33_07_PICARD_GRAM_ROWS_V1',
 'upstream_git_blob_sha1':blob,
 'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),
 'magma_request_attempt':attempt,
 'picard_rank':64,
 'picard_gram_64x64':rows,
}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'picard-gram-rows.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'rank':64,'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
