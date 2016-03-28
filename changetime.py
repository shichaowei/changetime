#coding:utf-8
import datetime
import sys
import os
import time

if __name__=="__main__":
    if len(sys.argv)<6:
        print "argv not enough"
    else:
        day=int(sys.argv[1])
        print day
        hour=int(sys.argv[2])
        minite=int(sys.argv[3])
        second=int(sys.argv[4])
        step=int(sys.argv[5])
    	totalsecond=day*24*3600+hour*3600+minite*60+second
    	print totalsecond
    	currentsecond=0
    	while currentsecond<totalsecond:
        	d1 = datetime.datetime.now()
        	d3 = d1 + datetime.timedelta(seconds=step)
        	d4=str(d3)
        	#print d4
		time.sleep(1)
        	currentsecond=currentsecond+step
		print currentsecond
		os.system("date -s '%s'"%d4)
		
