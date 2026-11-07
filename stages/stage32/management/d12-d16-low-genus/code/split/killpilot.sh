for pid in $(ps -eo pid,args | grep "/root/splitenum$" | grep -v grep | awk '{print $1}'); do kill $pid; done
sleep 2; ps -eo args | grep -c "/root/splitenum$"
