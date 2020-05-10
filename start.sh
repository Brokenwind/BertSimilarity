#!/bin/bash

read -p "running mode: train/eval/predict): " mode

# 加入环境变量
CUR_PATH=`pwd`
export PYTHONPATH=$CUR_PATH:$PYTHONPATH
echo "starting "$mode" process"

python similarity.py --mode=$mode > "similarity_"$mode.log 2>&1 &