#!/bin/bash
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/d16all/h1
setsid bash -c "s=\$(date +%s); Singular -q g3_t_21.sing < /dev/null 2>&1 | grep --line-buffered -v redefin > g3_t_21.out; echo \"wall \$(( \$(date +%s) - s ))\" >> g3_t_21.out" > /dev/null 2>&1 &
sleep 2; pgrep -fa g3_t_21 | grep -c Singular
