#!/bin/bash
# Resolve the distributed (9,9) run after run99.sh: hits and deferred candidates of a table machine X need the
# 60-digit points (and p, q) of their query covers, which live on the query's owner machine.
# usage: bash resolve99.sh <work dir of run99> <name>        (same work dir and name as run99.sh; loc/ is reused)
#  1. for every finished table machine X (/mnt/project-files/deg9gen/q99/X/res99_X.pkl), cut the needed query covers
#     of the local profiles into mini L7 files (mkmini9.py) and put them to /mnt/project-files/deg9gen/mini/X/
#  2. once this machine's own res99_<name>.pkl is done and all its needed tags are in mini/<name>/: rerun just those
#     queries in full mode against the local table (search7, both sides with 60-digit points, birationality);
#     result res99r_<name>.pkl and log r99.log to /mnt/project-files/deg9gen/q99/<name>/
#  Loops (every 5 minutes) until all five machines' res99 files were exported and step 2 is done.  Safe to rerun.
set -u
W=$1; NAME=$2; HERE=$(cd "$(dirname "$0")" && pwd); Q=/mnt/project-files/deg9gen/q99; MI=/mnt/project-files/deg9gen/mini
ALL="me part1 part2 part3 part4"; cd "$W"; mkdir -p exported
while true; do
  left=0
  for X in $ALL; do
    if [ -f exported/$X ]; then continue; fi
    if [ ! -f $Q/$X/res99_$X.pkl ]; then left=$((left+1)); continue; fi
    rm -rf mini_$X; python3 $HERE/mkmini9.py $Q/$X/res99_$X.pkl loc mini_$X > mini_$X.log 2>&1 || { echo "mkmini $X failed"; exit 1; }
    mkdir -p $MI/$X; for f in mini_$X/*; do [ -e "$f" ] && cp "$f" $MI/$X/; done
    for f in mini_$X/*.done; do [ -e "$f" ] && cp "$f" $MI/$X/; done      # markers last
    head -1 mini_$X.log; touch exported/$X; echo "exported for $X: $(ls mini_$X | grep -c done) tags"
  done
  if [ ! -f $Q/$NAME/res99r_$NAME.pkl ] && [ -f res99_$NAME.pkl ]; then
    TAGS=$(python3 -c "import sys; sys.path.insert(0, '$HERE'); import mkmini9; print(' '.join(sorted(mkmini9.needed('res99_$NAME.pkl'))))")
    miss=0; for t in $TAGS; do [ -f $MI/$NAME/L7_9_$t.done ] || miss=$((miss+1)); done
    if [ -z "$TAGS" ]; then
      mkdir -p $Q/$NAME; echo "nothing to resolve" > $Q/$NAME/r99.log; python3 -c "import pickle; pickle.dump({'hits': [], 'bir': [], 'note': 'nothing to resolve'}, open('$Q/$NAME/res99r_$NAME.pkl', 'wb'))"
    elif [ $miss = 0 ]; then
      rm -rf rmini; mkdir rmini; for t in $TAGS; do for s in .pkl _z.npy _inf.npy _pq.npy _crit.npy _hp.npy; do cp $MI/$NAME/L7_9_$t$s rmini/; done; done
      NT=$(python3 -c "
import pickle, glob; print(sum(pickle.load(open(f, 'rb'))['N'] for f in glob.glob('loc/L7_9_*[0-9].pkl')))")
      XS=${XSPLIT:-$(( NT * 56 / 50000000 + 1 ))}
      ALLQ=1 MIXED=1 JOBS=${JOBS:-4} XSPLIT=$XS OUT=res99r_$NAME python3 $HERE/search7.py 9 9 rmini loc >> r99.log 2>&1; e=$?
      mkdir -p $Q/$NAME; grep -av Warn r99.log > $Q/$NAME/r99.log
      [ $e = 0 ] && cp res99r_$NAME.pkl $Q/$NAME/ && echo "resolve $NAME: $(grep -a 'BIRATIONAL or unclear' r99.log | tail -1)"
      [ $e = 0 ] || { echo "resolve run failed ($e)"; exit 1; }
    else echo "waiting for $miss mini tags of $NAME"; fi
  fi
  [ $left = 0 ] && [ -f $Q/$NAME/res99r_$NAME.pkl ] && break
  sleep 300
done
echo "resolve99 $NAME done"
