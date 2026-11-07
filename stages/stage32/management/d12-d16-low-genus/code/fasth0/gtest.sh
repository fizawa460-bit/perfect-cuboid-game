cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
gcc -O2 -o /root/decglpk decglpk.c /usr/lib/x86_64-linux-gnu/libglpk.so.40 -lm || exit 1
head -$1 x16.txt > /root/gx.txt; head -$1 x16.exp > /root/gexp.txt
time /root/decglpk decomp_cm.txt 20000 $2 < /root/gx.txt > /root/gres.txt
paste -d' ' <(cut -d' ' -f2 /root/gexp.txt) <(cut -d' ' -f1,2 /root/gres.txt) | awk '{if($2=="UNK")print "UNK";else if($2=="NONE")print ($1=="None"?"same":"DIFF"); else print ($1==$2?"same":"DIFF")}' | sort | uniq -c
