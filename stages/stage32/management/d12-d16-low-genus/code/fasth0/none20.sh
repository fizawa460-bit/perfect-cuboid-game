cd /root/s20sym
for f in $(ls out_*.txt); do b=${f%.txt}; [ -s $f ] || continue; paste $f /root/j20/$b.h0 | awk -F'\t' -v s=$b '$2 ~ /^None/ {print s "\t" $0}'; done > /root/x20_none.txt
wc -l < /root/x20_none.txt; ls -la /root/x20_none.txt
