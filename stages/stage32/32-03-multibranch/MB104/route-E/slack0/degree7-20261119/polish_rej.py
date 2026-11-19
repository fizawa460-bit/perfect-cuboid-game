import sys,glob,pickle,numpy as np, mpmath as mp
S='/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/'
sys.path.insert(0,S+'numeric-upto5-20261118'); sys.argv=['x','0','0','1']
from covers import BP
mp.mp.dps=40; n=6; worst=0
for fn in sorted(glob.glob('rej_6_*.pkl')):
    R=pickle.load(open(fn,'rb')); ys=list(R['ys'])
    for k,u in enumerate(R['sols']):
        p=[mp.mpc(complex(v)) for v in u[:n+1]]; q=[mp.mpc(complex(v)) for v in u[n+1:2*n+2]]
        for j in range(len(ys)):
            y=ys[j]; f=[mp.mpc(BP[y][1])*a-mp.mpc(BP[y][0])*b for a,b in zip(p,q)]
            d1=[m*f[m] for m in range(1,n+1)]; d2=[m*d1[m] for m in range(1,n)]
            z=mp.mpc(complex(u[2*n+2+j])); z0=z
            for _ in range(30):
                a=sum(c*z**m for m,c in enumerate(d1)); b=sum(c*z**m for m,c in enumerate(d2))
                z=z-a/b
            worst=max(worst,float(abs(z-z0))); u[2*n+2+j]=complex(z)
    pickle.dump(R,open(fn,'wb'))
print('max move',worst)
