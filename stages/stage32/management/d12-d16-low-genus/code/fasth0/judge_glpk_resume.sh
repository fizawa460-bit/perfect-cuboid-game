# 32R-71 resumable type sorting: bash judge_glpk_resume.sh XDIR OUTDIR NPAR
# a shard is skipped when OUTDIR/out_k.h0 already has as many lines as XDIR/out_k.txt (finished)
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
[ -x /root/decglpk ] || gcc -O2 -o /root/decglpk decglpk.c /usr/lib/x86_64-linux-gnu/libglpk.so.40 -lm || exit 1
mkdir -p $2
s=$(date +%s)
for f in $1/out_*.txt; do b=$(basename $f .txt); n=$(wc -l < $f); m=$( [ -e $2/$b.h0 ] && wc -l < $2/$b.h0 || echo 0); [ "$n" = "$m" ] || echo $f; done > /root/resume_list.txt
echo "to run: $(wc -l < /root/resume_list.txt)"
cat /root/resume_list.txt | xargs -P $3 -I{} bash -c 'b=$(basename {} .txt); /root/decglpk decomp_cm.txt 20000 0 2848 < {} 2> '$2'/${b}.err | python3 h0stream.py > '$2'/${b}.h0'
echo "total $(( $(date +%s) - s )) s"
cat $2/*.h0 | wc -l; grep -h UNK $2/*.h0 | wc -l
