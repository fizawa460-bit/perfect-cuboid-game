cd /mnt/c/Users/fizaw/claudework/stage32_research/split
gcc -O2 -o /root/canon canon.c || exit 1
/root/canon canon_tab.txt < $1 | sort -u > /root/ca_new.txt
/root/canon canon_tab.txt < $2 | sort -u > /root/ca_old.txt
wc -l < $1; wc -l < /root/ca_new.txt; wc -l < $2; wc -l < /root/ca_old.txt
cmp /root/ca_new.txt /root/ca_old.txt && echo SAME_SETS
