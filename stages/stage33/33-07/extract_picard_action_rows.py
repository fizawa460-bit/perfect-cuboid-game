#!/usr/bin/env python3
"""Extract one 64x64 Picard Galois-action matrix at a time.

Usage: python extract_picard_action_rows.py cc|ct
Each Magma request emits only one matrix, row by row, to stay below the public
calculator output cap.  The induced mixed-modulus discriminant action is
computed later in Python together with the separately extracted Gram matrix.
"""
import ast, hashlib, json, pathlib, re, sys
from stoll_cuboid_source import load_pinned_source, run_magma

if len(sys.argv)!=2 or sys.argv[1] not in ('cc','ct'):
    raise SystemExit('usage: extract_picard_action_rows.py cc|ct')
mode=sys.argv[1]
HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()
common=r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
'''
if mode=='cc':
    extra=common+r'''
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
perm := [Position(C1s, actcc(C)) : C in C1s]
 cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
G := Matrix(Integers(), [Eltseq(actperm(Pic.j, perm)) : j in [1..64]]);
printf "STAGE33_07_ACTION_BEGIN\n";
for r in [1..64] do printf "G_ROW_%o=%o\n",r,[G[r,c]:c in [1..64]]; end for;
printf "STAGE33_07_ACTION_END\n";
'''
else:
    extra=common+r'''
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
perm := [Position(C1s, actct(C)) : C in C1s]
 cat [#C1s+Position(C2s, actct(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
G := Matrix(Integers(), [Eltseq(actperm(Pic.j, perm)) : j in [1..64]]);
printf "STAGE33_07_ACTION_BEGIN\n";
for r in [1..64] do printf "G_ROW_%o=%o\n",r,[G[r,c]:c in [1..64]]; end for;
printf "STAGE33_07_ACTION_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
stdout,attempt=run_magma(code,180,f'Stage33-07 Picard {mode} action rows Magma')
(HERE/f'picard-action-{mode}-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_ACTION_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout); raise SystemExit(f'Picard {mode} action row extraction failed')
rows=[]
for r in range(1,65):
    m=re.search(rf'^G_ROW_{r}=(.+)$',stdout,re.M)
    if not m: raise SystemExit(f'missing {mode} row {r}')
    row=ast.literal_eval(m.group(1))
    if len(row)!=64: raise SystemExit('action row length regression')
    rows.append([int(x) for x in row])
out={
 'schema':'STAGE33_07_PICARD_ACTION_ROWS_V1',
 'action':mode,
 'upstream_git_blob_sha1':blob,
 'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),
 'magma_request_attempt':attempt,
 'picard_action_64x64':rows,
}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/f'picard-action-{mode}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'action':mode,'rank':64,'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
