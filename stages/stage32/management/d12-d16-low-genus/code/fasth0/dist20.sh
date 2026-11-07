cat /root/j20/*.h0 | awk '{c[$1" "$2]++} END{for(k in c) print c[k], k}' | sort -k2,3 > /root/dist20.txt
cat /root/dist20.txt; awk '{s+=$1} END{print "total", s}' /root/dist20.txt
