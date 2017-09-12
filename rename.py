#coding utf-8
import os
dir = "./"
namelist = os.listdir(dir)
i=0
for name in namelist:
	if name == "rename.py":
		pass
	else:
		os.rename(name,str(i))
		i+=1