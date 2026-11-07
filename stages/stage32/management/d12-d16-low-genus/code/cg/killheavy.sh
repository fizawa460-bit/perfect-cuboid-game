#!/bin/bash
for p in $(pgrep -x Singular); do
  a=$(tr '\0' ' ' < /proc/$p/cmdline)
  case "$a" in *cg_28761_*|*cd_28169_*|*cd_38725_3_0*) kill $p; echo killed $a;; esac
done
