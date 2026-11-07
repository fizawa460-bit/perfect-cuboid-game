# distribution of (m,h0) over all d20 reps, and extraction of h0>=1 reps (rep line TAB judge line), in s20sym ls order
cd /root/s20sym
: > /root/x20_h1.txt
for f in $(ls out_*.txt); do b=${f%.txt}; [ -s $f ] || continue; paste $f /root/j20/$b.h0 | awk -F'\t' -v s=$b '{split($2,a," "); print a[1], a[2] > "/dev/stderr"; if (a[2] != "None" && a[2] >= 1) print s "\t" $0}' >> /root/x20_h1.txt; done 2> >(sort | uniq -c > /root/dist20.txt)
sleep 2; cat /root/dist20.txt; wc -l < /root/x20_h1.txt
