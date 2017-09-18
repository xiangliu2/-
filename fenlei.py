#coding utf-8
import os
import numpy as np
import cv2
dir = "./"
namelist = os.listdir(dir)

n=0
m=0
for name in namelist:
	if name == "fenlei.py":
		pass
	else:
		#print (name)
		img = cv2.imread(name,cv2.IMREAD_COLOR)
		cv2.imshow('image',img)
		k = cv2.waitKey(10000)
		if k==122:
			#122即字母z的ascii值
			cv2.destroyAllWindows()			
			os.rename(name,"北京"+str(n)+'.jpg')
			n=n+1
			print(n)
		elif k==109:
			#109即m的ascii值
			cv2.destroyAllWindows()
			os.rename(name,"上海"+str(m)+'.jpg')
			m=m+1
		else:
			print ("误操作")