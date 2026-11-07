import glob,re,collections,sys
for pat in sys.argv[1:]:
    C=collections.Counter(); low=[]; none=[]
    for f in sorted(glob.glob(pat)):
        s=open(f,errors='replace').read()
        m=re.search(r'GENUS-SUM\s+(-?\d+)',s)
        comps=tuple(sorted((int(a),int(b),int(c)) for a,b,c in re.findall(r'COMP degree (\d+)\s+pa (-?\d+)\s+genus (-?\d+)',s)))
        if not m:
            none.append(f); C['none']+=1; continue
        ok=int(m.group(1))>=2; C['ok' if ok else 'low']+=1
        if not ok: low.append((f,comps))
    print(pat, dict(C))
    for f,c in low: print('  LOW',f,c)
    for f in none: print('  NONE',f, open(f,errors='replace').read()[-150:].replace('\n',' | '))
