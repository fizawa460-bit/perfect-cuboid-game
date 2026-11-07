cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
for f in e_*.out; do [ -s "$f" ] && grep -q "^time" "$f" || rm -f "$f"; done
cat jobs_v2b.txt | xargs -P 12 -I{} bash one.sh {}
