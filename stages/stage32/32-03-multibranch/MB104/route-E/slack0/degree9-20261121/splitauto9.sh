#!/bin/bash
# Work through the shares of a split profile, any number of machines at once.  Restart-safe.
# usage: bash splitauto9.sh <workdir> <n> <profile> <K> <shared dir>
# Each machine first finishes shares it already claimed (local split_<t>_<r>of<K> without done), then claims free
# shares with an atomic mkdir <shared dir>/claim_<r>, until none is left.  Uses split9.sh for each share.
set -u
W=$1; n=$2; p=$3; K=$4; SH=$5
HERE=$(cd "$(dirname "$0")" && pwd); t=$(echo $p | tr -d ,)
mkdir -p $W
for r in $(seq 0 $((K-1))); do
  if [ -d $W/split_${t}_${r}of$K ] && [ ! -f $SH/done_${r}of$K ]; then bash $HERE/split9.sh $W $n $p $r $K $SH || exit $?; fi
done
for r in $(seq 0 $((K-1))); do
  if mkdir $SH/claim_$r 2>/dev/null; then
    echo "$(hostname) $(date +%T)" > $SH/claim_$r/who; bash $HERE/split9.sh $W $n $p $r $K $SH || exit $?
  fi
done
echo "no free share of $p left; done: $(ls $SH | grep -c '^done_')/$K"
