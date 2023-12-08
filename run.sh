#!/bin/bash
now=$(date +'%Y-%m-%d_%T')
#echo "$now"
/usr/local/bin/ipython /home/ec2-user/git/ets/test.py > /home/ec2-user/git/ets/log/out_${now}.log
