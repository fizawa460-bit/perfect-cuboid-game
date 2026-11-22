#!/bin/bash
# (9,8) check on one machine: the degree-9 covers whose L7 files are in <L7 dir> as queries, all of degree 8 (L5) as table.
# usage: bash q98.sh <L7 dir> <work dir> <name>      e.g. bash q98.sh /home/user/deg9/gen /home/user/deg9/q98 part1
# Fetches the degree-8 L5 set from /mnt/project-files/deg8L5 (the 4 big files through bigfile.sh parts, checked by sha256)
# into <work dir>/../deg8L5 once, links the L7 files, runs search6 9 8 with MIXED=1 (resumes from its saved blocks
# after a stop: rerun the same command; start only when every profile of the machine has its L7, since the saved
# blocks are numbered by query and a new profile would shift them), and copies the small result files to /mnt/project-files/deg9gen/q98/<name>/.
set -u
L7=$1; W=$2; NAME=$3
HERE=$(cd "$(dirname "$0")" && pwd); D8=$(dirname "$W")/deg8L5
mkdir -p "$D8" "$W"
if [ ! -f "$D8/ok" ]; then
  for f in /mnt/project-files/deg8L5/L5_8_*.pkl /mnt/project-files/deg8L5/L5hp_8_*.npy; do
    b=$(basename "$f"); case $b in L5_8_222233.pkl|L5_8_222323.pkl|L5hp_8_222233.npy|L5hp_8_222323.npy) continue;; esac
    [ -f "$D8/$b" ] || { cp "$f" "$D8/$b.tmp" && mv "$D8/$b.tmp" "$D8/$b"; }
  done
  for b in L5_8_222233.pkl L5_8_222323.pkl L5hp_8_222233.npy L5hp_8_222323.npy; do
    [ -f "$D8/$b" ] || bash $HERE/bigfile.sh get /mnt/project-files/deg8L5/parts $b "$D8/$b" || { echo "fetch $b failed"; exit 1; }
  done
  [ $(ls $D8/L5_8_*.pkl | wc -l) = 75 ] && [ $(ls $D8/L5hp_8_*.npy | wc -l) = 75 ] || { echo "degree-8 set incomplete"; exit 1; }
  touch "$D8/ok"
fi
cd "$W"; for f in "$L7"/L7_9_*; do ln -sf "$f" .; done
MIXED=1 JOBS=${JOBS:-4} OUT=res_9_8_$NAME python3 $HERE/search6.py 9 8 . "$D8" >> s98.log 2>&1; ec=$?
mkdir -p /mnt/project-files/deg9gen/q98/$NAME; grep -av Warn s98.log > /mnt/project-files/deg9gen/q98/$NAME/s98.log
for f in res_9_8_${NAME}*; do [ -f "$f" ] && [ $(stat -c %s "$f") -lt 50000000 ] && cp "$f" /mnt/project-files/deg9gen/q98/$NAME/; done
echo "q98 $NAME exit $ec"; exit $ec
