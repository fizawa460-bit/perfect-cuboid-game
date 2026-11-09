# split the d16 all-rep judge (s16allmu + j16all) into classes already in the unibranch-compatible reps (s16sym, closed by R2) and new classes; writes /root/j16all_new_h0pos.txt (run in WSL: python3 d16all/split_new.py)
import glob, os, collections
uni = set()
for l in open('/root/s16sym/all.txt'):
    uni.add(l.strip())
print('unibranch reps', len(uni))
cnt = collections.Counter(); new = collections.Counter(); out = open('/root/j16all_new_h0pos.txt', 'w')
for f in sorted(glob.glob('/root/s16allmu/out_*.txt')):
    b = os.path.basename(f)[:-4]
    X = open(f).read().split('\n')[:-1]; H = open('/root/j16all/%s.h0' % b).read().split('\n')[:-1]
    assert len(X) == len(H), b
    for x, h in zip(X, H):
        hv = h.split()[1]
        isnew = x.strip() not in uni
        cnt[(hv, isnew)] += 1
        if isnew and hv not in ('0',): out.write(b + '\t' + x.strip() + '\t' + h + '\n')
for k in sorted(cnt): print(k, cnt[k])
