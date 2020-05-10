#!/bin/bash

read -p "running mode: train/eval/infer): " mode

# 加入环境变量
CUR_PATH=`pwd`
export PYTHONPATH=$CUR_PATH:$PYTHONPATH

if [ "$mode" == "train" ];then
  python similarity.py --mode=$mode > logs/"similarity_"$mode.log 2>&1 &
  echo "check train log with command: tail -f logs/similarity_$mode.log"
elif [ "$mode" == "eval" ];then
  python similarity.py --mode=$mode > logs/"similarity_"$mode.log 2>&1 &
  echo "check eval log with command: tail -f logs/similarity_$mode.log"
elif [ "$mode" == "infer" ];then
  python similarity.py --mode=$mode
else
  echo "parameter error, choose from train/eval/infer"
  exit 1
fi
