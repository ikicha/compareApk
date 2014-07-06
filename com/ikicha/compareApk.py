'''
Created on 2014. 7. 5.

@author: jeongik.cha
'''

import zipfile
import os
import sys

num_argv = len(sys.argv)
argv = sys.argv

if num_argv<3:
    print "ERROR : Wrong Arguments Type"
    print "compareApk.pyc [APK FILE NAME] [RES FOLDER IN PROJECT] ... ( RES FOLDER CAN BE ONE OR MORE )"
    exit()

with zipfile.ZipFile(argv[1]) as myZip: 
    apkFileNames = myZip.namelist()

resFileFromApk = []
for name in filter(lambda s:'res/' in s and 'drawable' in s, apkFileNames):
    resFileFromApk.append(str(name.split("res/")[1]))

resFileFromProject = []

roots = argv[2:]
    
for root in roots:
    for base, dirs, names in os.walk(root):
        if("res"+os.path.sep in base and "drawable" in base):
            for name in names:
                if name != "Thumbs.db":
                    resFileFromProject.append(str(os.path.join(base.split("res"+os.path.sep)[1], name)).replace('\\', '/'))
            
resFileFromApk.sort()            
resFileFromProject.sort()

sizeApk = len(resFileFromApk)
sizeProject = len(resFileFromProject)

print str(sizeApk) +" res files in Apk"
print str(sizeProject) + " res files in Project"
'''print resFileFromApk
print resFileFromProject'''
ever_miss = 0
for fileInProject in resFileFromProject:
    hit = False
    for fileInApk in resFileFromApk:
        if(fileInApk == fileInProject):
            hit = True
    if not hit:
        print fileInProject + " is not in Apk"
        ever_miss = ever_miss + 1
if ever_miss == 0:
    print "PASS"
else:  
    print "FAIL"
    print str(ever_miss) + " files is missing in Apk."
