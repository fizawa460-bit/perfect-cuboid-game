import pickle,collections,sys
sys.argv_=sys.argv
exec(open('code/count.py').read().split('c=collections')[0])
import itertools
# Aut(B) perms
S='/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/numeric-upto5-20261118'
sys.path.insert(0,S); sys.argv=['x','0','0','1']
from covers import AUT
import functools
@functools.lru_cache(None)
def rep(t):
    for k in H:
        for M,perm in AUT:
            if tuple(k[[y for y in range(6) if perm[y]==z][0]] for z in range(6))==t: return k
c=collections.Counter(); orb=collections.defaultdict(set)
for fn in sys.argv_[1:]:
    for r in pickle.load(open(fn,'rb'))['all']:
        an=r[2]; t=tuple(len(an[y][1]) for y in range(6)); k=rep(t); c[k]+=1/r[3]; orb[k].add(t)
tot=0
for k in sorted(H):
    e=H[k]*len({tuple(k[[y for y in range(6) if perm[y]==z][0]] for z in range(6)) for M,perm in AUT}); tot+=e
    print(k,e,round(c[k],3),len(orb[k]),'' if abs(c[k]-e)<1e-6 else 'DIFF %+.3f'%(c[k]-e))
print(tot,sum(c.values()))
