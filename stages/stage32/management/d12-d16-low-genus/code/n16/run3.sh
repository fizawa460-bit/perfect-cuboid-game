cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
cat jobs3.txt | xargs -P 1 -I{} bash one.sh {}
