#!/bin/bash
# One share of a profile split over K machines (mono_par OWN=r/K).  Restart-safe: rerun the same command after a stop.
# usage: bash split9.sh <workdir> <n> <profile> <r> <K> <shared dir holding base_<tag>.pkl>
# The share tracks only targets whose symmetry orbit hashes to r mod K, so the shares never track the same cover.
# When the share has nothing left to track it writes delta_<tag>_<r>of<K>.pkl to the shared dir (and done_<r>of<K>).
# Afterwards one machine runs merge9.py base + all deltas -> ckpt_dir_<tag>.pkl and continues with run9.sh as usual
# (the plain run then tracks whatever the split missed and does the endgame).
set -u
W=$1; n=$2; p=$3; r=$4; K=$5; SH=$6
HERE=$(cd "$(dirname "$0")" && pwd); FM=$HERE/../fastmono-20261119
t=$(echo $p | tr -d ,); tag=${n}_$t
mkdir -p $W/split_${t}_${r}of$K; cd $W/split_${t}_${r}of$K
[ -f $SH/done_${r}of$K ] && { echo "share $r/$K of $p already done"; exit 0; }
if [ ! -f ckpt_dir_$tag.pkl ]; then
  cp $SH/base_$tag.pkl ckpt_dir_$tag.pkl.part && mv ckpt_dir_$tag.pkl.part ckpt_dir_$tag.pkl
  cmp -s $SH/base_$tag.pkl ckpt_dir_$tag.pkl || { echo "copy of base failed"; rm -f ckpt_dir_$tag.pkl; exit 1; }
fi
NB=$(cat $SH/nbase_$tag.txt)
echo "$p share $r/$K start $(date +%T)" >> log_split.txt
OWN=$r/$K NBASE=$NB DELTA_OUT=$PWD/delta.pkl PAR=${PAR:-4} NOENDGAME=1 \
  python3 $HERE/mono_par.py $n $p --rules $FM/aut_rules_7_222222.pkl --loops 0 >> log_split.txt 2>&1
ec=$?
echo "$p share $r/$K exit $ec $(date +%T)" >> log_split.txt
if [ $ec -eq 0 ] && [ -f delta.pkl ]; then
  cp delta.pkl $SH/delta_${tag}_${r}of$K.pkl.part && mv $SH/delta_${tag}_${r}of$K.pkl.part $SH/delta_${tag}_${r}of$K.pkl
  cmp -s delta.pkl $SH/delta_${tag}_${r}of$K.pkl && date +%T > $SH/done_${r}of$K
fi
exit $ec
