cd /mnt/c/Users/fizaw/claudework/stage32_research/split
for sh in 401 250 7; do SPLIT_UB=1 /root/se_id < r16_in_$sh.txt 2>&1 >/dev/null | tail -1; echo "exit $?"; done
