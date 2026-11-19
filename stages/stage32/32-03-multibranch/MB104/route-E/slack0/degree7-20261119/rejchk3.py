import sys,pickle,numpy as np,time
sys.path.insert(0,'/home/user/work7')
import md_hp, monodromy as md
profs=sys.argv[1]; prof=tuple(int(c) for c in profs); n=7
R=pickle.load(open('rej_7_'+profs+'.pkl','rb')); U=np.array(R['REJ'])
TUP=set(pickle.load(open(''+sys.argv[2]+'','rb'))['TUP'])
import os
HA=f'hardall_{profs}.pkl'
if os.path.exists(HA): TUP|=set(pickle.load(open(HA,'rb')))
fail=[]
for u in U:
    try: md.tuples(u[None,:n+1],u[None,n+1:2*n+2])
    except Exception: fail.append(u)
print('double-failed',len(fail),flush=True)
new={}; t0=time.time(); hpf=0; inval=0; dup=0
for k,u in enumerate(fail):
    try: t=md_hp.tuple1(u[:n+1],u[n+1:2*n+2])
    except Exception as e: hpf+=1; continue
    if not md.check(t,prof): inval+=1; continue
    cf,au=md.canon(t)
    if cf in TUP: dup+=1
    else: new.setdefault(cf,(k,au))
    if k%10==0: print(k,time.time()-t0,'new',len(new),flush=True)
print('hp failed',hpf,'invalid',inval,'dup',dup,'new',len(new),'weighted',sum(1/a for _,a in new.values()))
pickle.dump({'new':new,'fail':fail},open('rejhp_'+profs+'.pkl','wb'))
