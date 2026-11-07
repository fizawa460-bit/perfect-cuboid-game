# 32R-70 type sorting with GLPK:  bash judge_glpk.sh XDIR OUTDIR NPAR   (XDIR/out_*.txt = x lists, one x per line)
cd /mnt/c/Users/fizaw/claudework/stage32_research/stoll/fasth0
gcc -O2 -o /root/decglpk decglpk.c /usr/lib/x86_64-linux-gnu/libglpk.so.40 -lm || exit 1
mkdir -p $2
s=$(date +%s)
ls $1/out_*.txt | xargs -P $3 -I{} bash -c 'b=$(basename {} .txt); /root/decglpk decomp_cm.txt 20000 0 2848 < {} 2> '$2'/${b}.err | python3 h0stream.py > '$2'/${b}.h0'
echo "total $(( $(date +%s) - s )) s"
cat $2/*.h0 | wc -l; grep -h UNK $2/*.h0 | wc -l
