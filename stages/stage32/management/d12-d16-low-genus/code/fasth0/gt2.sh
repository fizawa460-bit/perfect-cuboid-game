cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
gcc -O2 -o /root/decglpk decglpk.c /usr/lib/x86_64-linux-gnu/libglpk.so.40 -lm || exit 1
head -300 x16.txt > /root/gx.txt; head -300 x16.exp > /root/gexp.txt
for cfg in "0 2592" "0 2593" "0 2596" "0 2600" "0 2848" "0 608"; do
  s=$(date +%s.%N); /root/decglpk decomp_cm.txt 20000 $cfg < /root/gx.txt > /root/gres.txt; e=$(date +%s.%N)
  r=$(paste -d' ' <(cut -d' ' -f2 /root/gexp.txt) <(cut -d' ' -f1 /root/gres.txt) | awk '{if($2=="UNK")u++;else if(($2=="NONE"&&$1=="None")||$1==$2)s++;else d++} END{print s+0, d+0, u+0}')
  echo "cfg $cfg time $(echo "$e - $s" | bc) same/diff/unk $r"
done
