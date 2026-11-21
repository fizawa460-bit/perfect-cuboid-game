#!/bin/bash
# One share of a profile split over K machines (mono_par OWN=r/K).  Restart-safe: rerun the same command after a stop.
# usage: bash split9.sh <workdir> <n> <profile> <r> <K> <shared dir holding base_<tag>.pkl>
# The share tracks only targets whose symmetry orbit hashes to r mod K, so the shares never track the same cover.
# The base is read with bigfile.sh get (base_<tag>.parts/, .nparts, .sha256).  When the share has nothing left to track
# it puts delta_<tag>_<r>of<K> to the shared dir with bigfile.sh (and writes done_<r>of<K>).
# Afterwards one machine fetches base and deltas (bigfile.sh get), runs merge9.py base + all deltas -> ckpt_dir_<tag>.pkl and continues with run9.sh as usual
# (the plain run then tracks whatever the split missed and does the endgame).
# HPENDGAME=1 in the environment: the share also tracks its missing classes at 40 digits first (split phase 2).
set -u
W=$1; n=$2; p=$3; r=$4; K=$5; SH=$6
HERE=$(cd "$(dirname "$0")" && pwd); FM=$HERE/../fastmono-20261119
t=$(echo $p | tr -d ,); tag=${n}_$t
mkdir -p $W/split_${t}_${r}of$K; cd $W/split_${t}_${r}of$K
[ -f $SH/done_${r}of$K ] && { echo "share $r/$K of $p already done"; exit 0; }
if [ ! -f ckpt_dir_$tag.pkl ]; then      # the base comes in parts (bigfile.sh), the shared folder drops big files
  if [ -f $W/base_$tag.pkl ]; then cp $W/base_$tag.pkl ckpt_dir_$tag.pkl
  else bash $HERE/bigfile.sh get $SH base_$tag ckpt_dir_$tag.pkl || { echo "base not (yet) complete in $SH"; exit 1; }; fi
fi
NB=$(cat $SH/nbase_$tag.txt)
echo "$p share $r/$K start $(date +%T)" >> log_split.txt
OWN=$r/$K NBASE=$NB DELTA_OUT=$PWD/delta.pkl PAR=${PAR:-4} NOENDGAME=1 HPENDGAME=${HPENDGAME:-} \
  python3 $HERE/mono_par.py $n $p --rules $FM/aut_rules_7_222222.pkl --loops 0 >> log_split.txt 2>&1
ec=$?
echo "$p share $r/$K exit $ec $(date +%T)" >> log_split.txt
if [ $ec -eq 0 ] && [ -f delta.pkl ]; then
  bash $HERE/bigfile.sh put delta.pkl $SH delta_${tag}_${r}of$K && date +%T > $SH/done_${r}of$K
fi
exit $ec
