cd /root
for f in s20sym/out_*.txt; do b=$(basename $f .txt); n=$(wc -l < $f); if [ -e j20/$b.h0 ]; then m=$(wc -l < j20/$b.h0); else m=NA; fi; [ "$n" = "$m" ] || echo $b $n $m; done
