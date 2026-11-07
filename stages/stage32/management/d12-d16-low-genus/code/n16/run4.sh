cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
cat j4.txt | xargs -P 4 -I{} bash one_long.sh {}
