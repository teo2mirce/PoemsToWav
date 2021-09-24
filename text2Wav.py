from pathlib import Path
import shutil
import os
import subprocess


from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('FisiereTxt') if isfile(join('FisiereTxt', f))]
for f in onlyfiles:
	strToCal=["balcon\\balcon.exe","--encoding","utf8","-n","Andrei","-f","FisiereTxt/"+f,"-w","Waves/"+f.replace(".txt",".wav")]
	subprocess.call(strToCal)