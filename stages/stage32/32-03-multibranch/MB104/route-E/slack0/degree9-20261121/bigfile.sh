#!/bin/bash
# Large files through the shared project folder, which drops single files of a few hundred MB.
#   put: bash bigfile.sh put <local file> <shared dir> <name>   -> <shared dir>/<name>.parts/part_NN (150 MB) + <name>.sha256
#   get: bash bigfile.sh get <shared dir> <name> <local file>   -> reassembles and checks sha256 (exit 1 if parts missing)
set -u
case $1 in
put) f=$2; d=$3; nm=$4; mkdir -p $d/$nm.parts; tmp=$(mktemp -d)
     split -b 150M -d -a 2 $f $tmp/part_
     for p in $tmp/part_*; do cp $p $d/$nm.parts/$(basename $p); done
     ls $tmp | wc -l > $d/$nm.nparts; sha256sum < $f | cut -d' ' -f1 > $d/$nm.sha256; rm -rf $tmp ;;
get) d=$2; nm=$3; out=$4
     [ -f $d/$nm.sha256 ] && [ -f $d/$nm.nparts ] || exit 1
     np=$(cat $d/$nm.nparts); have=$(ls $d/$nm.parts 2>/dev/null | grep -c '^part_')
     [ "$have" -eq "$np" ] || { echo "$nm: $have of $np parts visible"; exit 1; }
     cat $d/$nm.parts/part_* > $out.part
     [ "$(sha256sum < $out.part | cut -d' ' -f1)" = "$(cat $d/$nm.sha256)" ] || { echo "$nm: sha256 mismatch"; rm -f $out.part; exit 1; }
     mv $out.part $out ;;
esac
