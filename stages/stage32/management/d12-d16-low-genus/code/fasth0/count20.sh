cd /root; c=0
for f in s20sym/out_*.txt; do b=$(basename $f .txt); if [ -e j20/$b.h0 ] && [ $(wc -l < $f) = $(wc -l < j20/$b.h0) ]; then c=$((c+1)); fi; done
echo finished_shards $c of $(ls s20sym/out_*.txt | wc -l); cat j20/*.h0 | wc -l
