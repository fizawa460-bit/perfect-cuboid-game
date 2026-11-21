#!/bin/bash
# Degree-n covers for a list of profiles, one profile after another, each on PAR cores (mono_par.py).
# usage: bash run9.sh <workdir> <n> <profile> [<profile> ...]      e.g. bash run9.sh /home/user/deg9/gen 9 2,2,3,3,3,3
# Phase 1 (NOENDGAME=1): the bulk.  Phase 2: the same command resumes from the checkpoint and runs the endgame.
# After each phase the outputs (cov_/full_/rej_/extra_/regen_/ckpt_dir_ files and the log) are copied to $COPYTO
# (default /mnt/project-files/deg9gen/) when that folder exists.
set -u
HERE=$(cd "$(dirname "$0")" && pwd); FM=$HERE/../fastmono-20261119
W=$1; n=$2; shift 2; mkdir -p "$W"; cd "$W"
COPYTO=${COPYTO:-/mnt/project-files/deg9gen/}
for p in "$@"; do
  t=$(echo $p | tr -d ,)
  for phase in 1 2; do
    if [ $phase = 1 ]; then NE=1; else NE=; fi
    SEEDARG=; [ -f seeds_${n}_$t.pkl ] && SEEDARG="--seedfile seeds_${n}_$t.pkl"
    echo "$p phase $phase start $(date +%T)" >> done.txt
    PAR=${PAR:-4} NOENDGAME=$NE python3 $HERE/mono_par.py $n $p --rules $FM/aut_rules_7_222222.pkl --loops ${LOOPS:-0} $SEEDARG >> log_$t.txt 2>&1
    echo "$p phase $phase exit $? $(date +%T)" >> done.txt
    if [ -d "$COPYTO" ]; then
      cp -f cov_${n}_$t.pkl full_${n}_$t.pkl rej_${n}_$t.pkl extra_${n}_$t.pkl ckpt_dir_${n}_$t.pkl log_$t.txt "$COPYTO" 2>/dev/null
      [ -f regen_${n}_$t.pkl ] && cp -f regen_${n}_$t.pkl "$COPYTO"
    fi
  done
  grep "^done:" log_$t.txt | tail -1 >> done.txt
done
