cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/n16
for f in m_*.out; do [ -s "$f" ] && grep -q "^time" "$f" || rm -f "$f"; done
cat ${1:-mjobs.txt} | xargs -P ${2:-12} -I{} bash one.sh {}
