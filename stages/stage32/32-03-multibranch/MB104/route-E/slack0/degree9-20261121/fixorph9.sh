#!/bin/bash
# After build7 exits 3 (orphans_<n>_<tag>.txt): rebuild the orphan covers at 80 digits from neighbouring covers
# (mono_par REGEN, merged into regen_<n>_<tag>.pkl), drop the build7 chunks that had orphans, run build7 again.
# usage (in the folder with full_/ckpt_dir_/regen_ files): bash fixorph9.sh <n> <profile e.g. 1,1,3,4,3,4> [procs]
set -u
n=$1; p=$2; NP=${3:-4}; t=$(echo $p | tr -d ,)
HERE=$(cd "$(dirname "$0")" && pwd); FM=$HERE/../fastmono-20261119
[ -f orphans_${n}_$t.txt ] || { echo "no orphans file"; exit 1; }
echo "fixorph $p: orphans $(cat orphans_${n}_$t.txt) $(date +%T)"
REGEN=$(cat orphans_${n}_$t.txt) REGEN_OUT=regen_${n}_$t.pkl PAR=1 python3 $HERE/mono_par.py $n $p --rules $FM/aut_rules_7_222222.pkl --ckpt ckpt_dir_${n}_$t.pkl 2>&1 | grep -a "regen"
python3 - <<PY
import numpy as np, glob, os
for f in glob.glob('b7tmp_${n}_$t/c*.npz'):
    if len(np.load(f)['orphans']): os.remove(f); print('dropped chunk', f)
PY
mv orphans_${n}_$t.txt orphans_${n}_$t.txt.done
python3 $HERE/build7.py $n $t . $NP 2>&1 | grep -av Warn | tail -3; ex=${PIPESTATUS[0]}
echo "fixorph $p: build7 exit $ex $(date +%T)"; exit $ex
