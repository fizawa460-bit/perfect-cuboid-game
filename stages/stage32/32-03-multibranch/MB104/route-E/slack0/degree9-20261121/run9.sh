#!/bin/bash
# Degree-n covers for a list of profiles, one profile after another, each on PAR cores (mono_par.py).
# usage: bash run9.sh <workdir> <n> <profile> [<profile> ...]      e.g. bash run9.sh /home/user/deg9/gen 9 2,2,3,3,3,3
# Phase 1 (NOENDGAME=1): the bulk.  Phase 2: the same command resumes from the checkpoint and runs the endgame.
# After each phase the log and the regen file are copied to $COPYTO
# (default /mnt/project-files/deg9gen/) when that folder exists.
set -u
HERE=$(cd "$(dirname "$0")" && pwd); FM=$HERE/../fastmono-20261119
W=$1; n=$2; shift 2; mkdir -p "$W"; cd "$W"
COPYTO=${COPYTO:-/mnt/project-files/deg9gen/}
for p in "$@"; do
  t=$(echo $p | tr -d ,)
  for phase in 1 2; do
    if [ $phase = 1 ]; then NE=1; HPE=; else NE=; HPE=1; fi      # phase 2: missing classes at 40 digits on all cores
    grep -q "^$p phase $phase exit 0 " done.txt 2>/dev/null && { ec=0; continue; }     # finished before a restart
    SEEDARG=; [ -f seeds_${n}_$t.pkl ] && SEEDARG="--seedfile seeds_${n}_$t.pkl"
    echo "$p phase $phase start $(date +%T)" >> done.txt
    PAR=${PAR:-4} NOENDGAME=$NE HPENDGAME=$HPE python3 $HERE/mono_par.py $n $p --rules $FM/aut_rules_7_222222.pkl --loops ${LOOPS:-0} --seedtries ${SEEDTRIES:-40} $SEEDARG >> log_$t.txt 2>&1
    ec=$?; echo "$p phase $phase exit $ec $(date +%T)" >> done.txt
    if [ -d "$COPYTO" ]; then
      cp -f log_$t.txt "$COPYTO" 2>/dev/null      # big files no longer (the shared folder holds 10 GB): pack9.py after build7
      [ -f regen_${n}_$t.pkl ] && cp -f regen_${n}_$t.pkl "$COPYTO"
    fi
    [ $ec -ne 0 ] && { echo "$p phase $phase failed (exit $ec); queue stopped, rerun the same command to resume" >> done.txt; exit $ec; }
  done
  grep -q "^$p final " done.txt 2>/dev/null || echo "$p final $(grep "^done:" log_$t.txt | tail -1)" >> done.txt
done
