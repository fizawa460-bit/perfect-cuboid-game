#!/bin/bash
# (9,9) check, distributed by TABLE: each machine is the table for its own profiles (L7 with 60-digit points here) and
# takes every orbit representative of all 50 profiles as a query (search7 query-only side, export_q9.py files).
# usage: bash run99.sh <L7 dir> <work dir> <name> [more L7 dirs...]     e.g. bash run99.sh /home/user/deg9/gen /home/user/deg9/w99 part1
#  1. exports qry_9_<tag>.npz of each local profile and puts it to /mnt/project-files/deg9gen/qry/ (bigfile.sh)
#  2. waits until all 50 profiles of hurwitz9.txt are there, fetches them (sha256-checked) into <work dir>/qall
#  3. SELFONLY run on the local L7 (the 24 U o f of each local query), then the table run (queries qall, table local)
#     (both resume from their saved blocks: rerun the same command after a stop)
#  4. copies logs and the small result files to /mnt/project-files/deg9gen/q99/<name>/
# env: XSPLIT (default: table entries / 5e7, at least 1), JOBS (4).
set -u
L7=$1; W=$2; NAME=$3; shift 3; MORE="$@"
HERE=$(cd "$(dirname "$0")" && pwd); SH=/mnt/project-files/deg9gen/qry
mkdir -p "$W/qall" "$W/loc" "$SH"
for d in $L7 $MORE; do for f in "$d"/L7_9_*[0-9].pkl; do
  t=$(basename $f .pkl); t=${t#L7_9_}
  for x in .pkl _z.npy _inf.npy _pq.npy _crit.npy _hp.npy; do ln -sf "$d/L7_9_$t$x" "$W/loc/"; done
  if [ ! -f "$SH/qry_9_$t.sha256" ]; then
    python3 $HERE/export_q9.py 9 $t "$d" "$W/qry_9_$t.npz" && bash $HERE/bigfile.sh put "$W/qry_9_$t.npz" $SH qry_9_$t && rm -f "$W/qry_9_$t.npz"
  fi
done; done
TAGS=$(sed 's/,//g' $HERE/hurwitz9.txt 2>/dev/null | awk '{print $1}'); [ -n "$TAGS" ] || TAGS=$(sed 's/,//g' /home/user/deg9/hurwitz9.txt | awk '{print $1}')
while true; do
  miss=0; for t in $TAGS; do [ -f "$W/qall/qry_9_$t.npz" ] || bash $HERE/bigfile.sh get $SH qry_9_$t "$W/qall/qry_9_$t.npz" > /dev/null 2>&1 || miss=$((miss+1)); done
  [ $miss = 0 ] && break; echo "waiting for $miss query files"; sleep 300
done
NT=$(python3 -c "
import pickle, glob; print(sum(pickle.load(open(f, 'rb'))['N'] for f in glob.glob('$W/loc/L7_9_*[0-9].pkl')))")
XS=${XSPLIT:-$(( NT * 56 / 50000000 + 1 ))}; echo "table covers $NT, XSPLIT $XS"
cd "$W"
SELFONLY=1 MIXED=1 JOBS=${JOBS:-4} OUT=self99_$NAME python3 $HERE/search7.py 9 9 loc loc >> self99.log 2>&1; e1=$?
MIXED=1 JOBS=${JOBS:-4} XSPLIT=$XS OUT=res99_$NAME python3 $HERE/search7.py 9 9 qall loc >> s99.log 2>&1; e2=$?
mkdir -p /mnt/project-files/deg9gen/q99/$NAME
grep -av Warn self99.log > /mnt/project-files/deg9gen/q99/$NAME/self99.log; grep -av Warn s99.log > /mnt/project-files/deg9gen/q99/$NAME/s99.log
for f in self99_$NAME.pkl res99_$NAME.pkl; do [ -f "$f" ] && [ $(stat -c %s "$f") -lt 50000000 ] && cp "$f" /mnt/project-files/deg9gen/q99/$NAME/; done
echo "q99 $NAME exit self $e1 table $e2"; [ $e1 = 0 ] && [ $e2 = 0 ]
