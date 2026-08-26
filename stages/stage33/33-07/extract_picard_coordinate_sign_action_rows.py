#!/usr/bin/env python3
"""Extract one 64x64 Picard coordinate-sign action matrix at a time.

Usage:
  python extract_picard_coordinate_sign_action_rows.py a1|a2|a3|b1|b2|b3|c

The public Magma calculator has an effective wall around one minute.  Building
the endpoint Picard lattice already costs about 45 seconds, so the seven signs
must not be computed in one request.  This extractor performs exactly one sign
action after the common source-locked Picard construction.
"""
import ast,hashlib,json,pathlib,re,sys
from stoll_cuboid_source import load_pinned_source,run_magma

NAMES=('a1','a2','a3','b1','b2','b3','c')
if len(sys.argv)!=2 or sys.argv[1] not in NAMES:
    raise SystemExit('usage: extract_picard_coordinate_sign_action_rows.py '+'|'.join(NAMES))
mode=sys.argv[1]; idx=NAMES.index(mode)
HERE=pathlib.Path(__file__).resolve().parent
_,core,blob,source_attempt=load_pinned_source()
# Build the literal coordinate substitution in the pinned projective model.
coords=['a1','a2','a3','b1','b2','b3','c']
subs=[('-'+x if j==idx else x) for j,x in enumerate(coords)]
subtxt='['+','.join(subs)+']'
extra=r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
act := func<sch, subs | Curve(Pr6, [Evaluate(e, subs) : e in DefiningEquations(sch)])>;
function actpt2(pt, subs)
  i0 := 1; while pt[i0] eq 0 do i0 +:= 1; end while;
  pteqns := [Pr6.j*pt[i0] - Pr6.i0*pt[j] : j in [1..7] | j ne i0];
  return Rep(Points(Scheme(Pr6, [Evaluate(e, subs) : e in pteqns])));
end function;
su := SUBSTITUTION;
perm := [Position(C1s,act(C,su)):C in C1s]
 cat [#C1s+Position(C2s,act(C,su)):C in C2s]
 cat [#C1s+#C2s+Position(C3s,act(C,su)):C in C3s]
 cat [#Cs+Position(pts,actpt2(pt,su)):pt in pts];
G := Matrix(Integers(),[Eltseq(actperm(Pic.j,perm)):j in [1..64]]);
assert G*pmPic*Transpose(G) eq pmPic;
assert G^2 eq IdentityMatrix(Integers(),64);
printf "STAGE33_07_SIGN_ROW_BEGIN\n";
for r in [1..64] do printf "G_ROW_%o=%o\n",r,[G[r,c]:c in [1..64]]; end for;
printf "STAGE33_07_SIGN_ROW_END\n";
'''.replace('SUBSTITUTION',subtxt)
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
stdout,attempt=run_magma(code,180,f'Stage33-07 Picard coordinate sign {mode} rows Magma')
(HERE/f'picard-action-sign-{mode}-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_SIGN_ROW_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout);raise SystemExit(f'Picard sign {mode} row extraction failed')
rows=[]
for r in range(1,65):
    m=re.search(rf'^G_ROW_{r}=(.+)$',stdout,re.M)
    if not m:raise SystemExit(f'missing {mode} row {r}')
    row=ast.literal_eval(m.group(1))
    if len(row)!=64:raise SystemExit('sign row length regression')
    rows.append([int(x) for x in row])
out={
 'schema':'STAGE33_07_PICARD_COORDINATE_SIGN_ACTION_ROWS_V1',
 'coordinate':mode,
 'coordinate_index_0based':idx,
 'upstream_git_blob_sha1':blob,
 'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),
 'magma_request_attempt':attempt,
 'picard_action_64x64':rows,
}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/f'picard-action-sign-{mode}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate':mode,'rank':64,'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
