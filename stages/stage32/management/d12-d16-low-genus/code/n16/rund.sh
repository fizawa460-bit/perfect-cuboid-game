cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
for x in $(cat dlist.txt); do [ -s d_$x.out ] && continue; timeout 20000 Singular -q d_$x.sing > d_$x.out 2>&1; echo "done $x"; done
