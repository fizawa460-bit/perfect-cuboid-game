#!/bin/bash
# (8,8) production; resumable (block files r88_*_b*.pkl are kept and reused)
cd /home/user/run88m
TOL=1e-11 TIERS=0,300,1000,3000,10000,30000,100000,1000000,inf CELLW=1.5e-6,4e-6,1e-5,3e-5,1e-4,1e-4,1e-4,1e-4 XSPLIT=4 JOBS=4 BLK=2000 OUT=r88m python3 /home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/degree8-20261120/search5.py 8 8 /home/user/deg8/gen >> run.log 2>&1
echo EXIT $? >> run.log
