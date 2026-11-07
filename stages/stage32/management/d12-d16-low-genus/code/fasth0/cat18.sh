cd /root/s18sym
for f in $(ls out_*.txt); do cat /root/j18/${f%.txt}.h0; done > /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0/j18_glpk.txt
wc -l < /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0/j18_glpk.txt
