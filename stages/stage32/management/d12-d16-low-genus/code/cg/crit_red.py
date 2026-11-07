import glob,re,collections,os
low=collections.defaultdict(list)
for pat in ['cg/cg_*.out','cg/cd_*.out']:
    for f in glob.glob(pat):
        s=open(f,errors='replace').read(); m=re.search(r'GENUS-SUM\s+(-?\d+)',s)
        if not m or int(m.group(1))<2:
            b=os.path.basename(f)[3:-4]; rep,dec=b.split('_')[:2]; low[rep].append(b)
print('low reps',len(low))
bad=[]; stat=collections.Counter()
for rep in sorted(low,key=int):
    for f in sorted(glob.glob(f'p16/c_{rep}_*.out')):
        s=open(f,errors='replace').read()
        a=re.search(r'critical points \(with multiplicity\): (\d+)',s); b=re.search(r'distinct critical points: (\d+)',s)
        cc='critical curve' in s
        key=(bool(a and b and a.group(1)==b.group(1)), cc); stat[key]+=1
        if key!=(True,False): bad.append((f, a and a.group(1), b and b.group(1), cc))
print(stat)
for x in bad[:40]: print(x)
