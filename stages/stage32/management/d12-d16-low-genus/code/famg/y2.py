import sys, json, glob, numpy as np
ARGS = sys.argv[1:]
sys.argv=['x']; g={}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
Cm, K, Gq = g['Cm'], g['K'], g['Gq']
Gn = np.array([[int(Gq[i,j].p) for j in range(64)] for i in range(64)], dtype=np.int64)
ip = lambda a,b: int(a @ Gn @ b)
print('checks: conic^2', ip(Cm[0],Cm[0]), 'G40^2', ip(Cm[39],Cm[39]), 'E^2', ip(Cm[92],Cm[92]), 'K.conic', ip(K,Cm[0]), 'K.G40', ip(K,Cm[39]))
nmap = {int(a): int(b) for a, b in (x.split(':') for x in open('famd/nodemap.txt').read().split())}
for fn in ARGS or ['famg/milp2.json']:
  R = json.load(open(fn))
  for tag, v in R.items():
    D = {int(k): c for k, c in v['D'].items()} if 'D' in v else None
    fix = {int(k): c for k, c in v['fix'].items()}; m = v['alt']['m']; D2 = {int(k): c for k, c in v['alt']['D2'].items()}
    y = m*K - sum(c*Cm[k-1] for k, c in D2.items())
    pa = (ip(y,y) - ip(y, -K) ) // 2 + 1   # K_S~ = -K? (hyperplane H = K here); p_a via adjunction with K_S~ = 0 (K3-type)? printed for info
    print(tag, 'y^2', ip(y,y), 'deg y', ip(y,K), 'y.Fix', ip(y, sum(c*Cm[k-1] for k,c in fix.items())))
