cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
cat dlist2.txt | xargs -P 5 -I{} bash one_d.sh {}
