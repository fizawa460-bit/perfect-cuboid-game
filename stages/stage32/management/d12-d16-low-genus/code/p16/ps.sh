ps -eo etimes,rss,args | grep "[S]ingular -q c_" | awk '{print $1, int($2/1024)"MB", $NF}'
