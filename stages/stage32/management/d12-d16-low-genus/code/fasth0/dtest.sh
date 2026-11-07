cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
gcc -O2 -march=native -o /root/decomp decomp.c || exit 1
time /root/decomp decomp_tab.txt $2 < $1 > /root/dres.txt
cut -d' ' -f1 /root/dres.txt | sort | uniq -c
paste -d' ' $1.exp <(cut -d' ' -f1,2 /root/dres.txt) | awk '{print $3, $4}' | sort | uniq -c
