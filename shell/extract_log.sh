#!/bin/bash

cd ../logs
cat train.log | grep "INFO:tensorflow:loss" | awk -F '[=, ]' '{print $4,$9}' > loss.log