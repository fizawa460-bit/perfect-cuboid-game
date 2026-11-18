import pickle,numpy as np,subprocess,os
O=pickle.load(open('all2_6_old.pkl','rb'))
import sys
pairs=[tuple(map(int,a.split(':'))) for a in sys.argv[1:]] or [(4391,39982),(1816,42833),(4391,256),(4386,57139),(4386,66137)]
for fi,qi in pairs:
    c=O['all'][qi]
    print(fi,qi,'f aut',O['reps'][fi][3],'q aut',c[3],'q rep',c[4],'U',c[5])
    pickle.dump({'reps':[O['reps'][fi]],'all':[]},open(f'bk_A_{fi}.pkl','wb'))
    pickle.dump({'reps':O['reps'],'all':[c]},open(f'bk_B_{qi}.pkl','wb'))
