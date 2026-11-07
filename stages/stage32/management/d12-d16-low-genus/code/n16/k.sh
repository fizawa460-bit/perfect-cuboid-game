for pid in $(ps -eo pid,args | grep "scx_67987_3_3" | grep -v grep | awk '{print $1}'); do kill $pid; done
sleep 3; ps -eo rss,args --sort=-rss | head -3; free -g | head -2
