cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
gcc -O2 -o /root/decglpk decglpk.c /usr/lib/x86_64-linux-gnu/libglpk.so.40 -lm || exit 1
head -300 x16.txt > /root/gx.txt
DEC_TRACE=1 /root/decglpk decomp_cm.txt 20000 0 2592 < /root/gx.txt 2> /root/trace.txt > /dev/null
grep "^T 2" /root/trace.txt | awk '{print $3}' | sort -g | awk '{a[NR]=$1; s+=$1} END{print "n",NR,"sum",s,"p50",a[int(NR*.5)],"p90",a[int(NR*.9)],"p99",a[int(NR*.99)],"max",a[NR]; c=0; for(i=NR;i>0;i--){c+=a[i]; if(c>s/2){print "top",NR-i+1,"calls take half the time"; break}}}'
