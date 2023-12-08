#!/bin/bash
now=$(date +'%Y-%m-%d_%T')
#echo "$now"
/usr/local/bin/ipython /home/ec2-user/git/ets/DII-Template.py > /home/ec2-user/git/ets/log/dii_${now}.log
