from os import walk
from CaptchaParser import CaptchaParser
import timeit
from PIL import Image
f = []
for (dirpath, dirnames, filenames) in walk('samples\\'):
    f.extend(filenames)
    break
timesum=0
size=len(f)
count=1
maxtime=0
mintime=100
currtime=0
for im in f:
	img=Image.open("samples\\"+str(im))
	c=CaptchaParser()
	starttime = timeit.default_timer()
	print "CAPTCHA:"+c.getCaptcha(img)
	endtime = timeit.default_timer()
	currtime=endtime-starttime
	if(currtime>maxtime):
		maxtime=currtime
		maximg=img.copy()
		print "new max:"+str(maxtime)
	if(currtime<mintime):
		mintime=currtime
		minimg=img.copy()
		print "new min:"+str(mintime)

	timesum+=currtime
	print "Comparing image "+str(count)+"/"+str(size)
	count+=1
avg=timesum/size

print "========================================"
print "Maximum Time:"+str(maxtime)
print "Minimum Time:"+str(mintime)
print "Total Time:"+str(timesum)
print "Average Time:"+str(avg)
print "========================================"