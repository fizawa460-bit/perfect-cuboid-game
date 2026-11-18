import pickle,sys,numpy as np,hp
from multiprocessing import Pool
n=int(sys.argv[1]); D=pickle.load(open(f'all2_{n}.pkl','rb'))
def key(c): return np.round(np.concatenate([c[0],c[1]]),9).tobytes()
done=set()
try:
    _o=pickle.load(open(f'hp_{n}.pkl','rb'))
    if isinstance(_o,dict): done=set(_o)
except Exception: pass
def work(i):
    p,q,an,aut=D['reps'][i][:4]
    an2,res,co,hpo=hp.refine(p,q,an,n,iters=10)
    return i,res,{y:[None if z is None else (str(z.real),str(z.imag)) for z in v] for y,v in hpo.items()}
if __name__=='__main__':
    todo=[i for i in range(len(D['reps'])) if key(D['reps'][i]) not in done]
    with Pool(int(sys.argv[2])) as P: out=P.map(work,todo,chunksize=20)
    out.sort(); print('computed',len(out),'max res',max([r for _,r,_ in out]+[0]))
    old={}
    try: old=pickle.load(open(f'hp_{n}.pkl','rb'))
    except Exception: pass
    if isinstance(old,list): old={}
    for i,r,h in out: old[key(D['reps'][i])]=h
    pickle.dump(old,open(f'hp_{n}.pkl','wb'))
