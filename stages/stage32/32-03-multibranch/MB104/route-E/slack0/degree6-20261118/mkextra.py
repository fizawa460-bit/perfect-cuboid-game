import pickle,numpy as np
def key(c): return np.round(np.concatenate([c[0],c[1]]),9).tobytes()
O=pickle.load(open('all2_6_old.pkl','rb')); N=pickle.load(open('all2_6.pkl','rb'))
ok=set(key(c) for c in O['reps']); oa=set(key(c) for c in O['all'])
newr=[i for i,c in enumerate(N['reps']) if key(c) not in ok]
print('new reps',len(newr),'weighted',sum(1/N['reps'][i][3] for i in newr))
gone=[c for c in O['reps'] if key(c) not in set(key(d) for d in N['reps'])]; print('old reps missing in new',len(gone))
newa=[c for c in N['all'] if key(c) not in oa]; print('new all',len(newa),'weighted',sum(1/c[3] for c in newa))
print('new all whose rep is old', sum(1 for c in newa if c[4] not in set(newr)))
idx={r:j for j,r in enumerate(newr)}
reps=[N['reps'][i] for i in newr]
allc=[c[:4]+(idx[c[4]],c[5]) for c in N['all'] if c[4] in idx]
print('extra table',len(allc))
pickle.dump({'reps':reps,'all':allc},open('all2_6x.pkl','wb'))
# table covers new w.r.t. old (regardless of rep), reindexed to N reps -> keep N reps list
pickle.dump({'reps':N['reps'],'all':newa},open('all2_6xt.pkl','wb'))
