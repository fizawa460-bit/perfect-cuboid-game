cd /mnt/c/Users/fizaw/claudework/stage32_research/split
gcc -O2 -pg -fno-inline -o /root/se_prof splitenum3.c -lm
cd /root && SPLIT_UB=1 ./se_prof < /mnt/c/Users/fizaw/claudework/stage32_research/split/r16_in_401.txt > /dev/null 2>/dev/null
gprof -b -p ./se_prof gmon.out | head -15
