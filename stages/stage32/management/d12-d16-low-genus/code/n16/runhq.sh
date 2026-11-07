cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
cat hqjobs.txt | xargs -P 2 -I{} bash one.sh {}
