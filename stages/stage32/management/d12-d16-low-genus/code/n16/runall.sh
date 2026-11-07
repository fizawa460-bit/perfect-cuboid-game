cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
cat jobs.txt | xargs -P 11 -I{} bash one.sh {}
