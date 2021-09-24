from pathlib import Path
import shutil
import os
import subprocess

file1 = open('links.txt', 'r')
Lines = file1.read().splitlines()
for line in Lines:
	print(line)
	strToCal=["phantomjs.exe","js.js",line]
	
	file_name=(line.split("adrian-paunescu-",1)[1])[:-1]
	with open('FisiereTxt/'+file_name+".txt", "w") as outfile:
		subprocess.call(strToCal,stdout=outfile)