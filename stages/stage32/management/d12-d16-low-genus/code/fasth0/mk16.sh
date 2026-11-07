mkdir -p /root/x16; rm -f /root/x16/*
split -d -a 3 -n l/40 /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0/x16.txt /root/x16/out_
for f in /root/x16/out_*; do mv $f $f.txt; done
ls /root/x16 | wc -l
