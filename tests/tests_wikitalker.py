#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:06:00 2020

@author: descentis
"""
import glob
import shutil
import subprocess
import shlex
import os

'''
with open('/media/descentis/0FC10BE60FC10BE6/WikipediaData/CurrentRevision/all_talk_pages/file_id.txt','r') as myFile:
    for line in myFile:
        

count = 0
with open('/media/descentis/0FC10BE60FC10BE6/WikipediaData/CurrentRevision/all_talk_pages/all_talk_pages.txt', 'r') as myFile:
    for line in myFile:
        with open('sample_file'+str(count)+'.xml', 'a') as newFile:
            newFile.write(line)
        
        if '</page>' in line:
            count+=1
        
        if count == 100:
            break
'''


shutil.move('sample_file50.xml', '/home/descentis/research/working_packages/witpy/grawitas_extension/sample_file50.xml')

os.chdir('/home/descentis/research/working_packages/witpy/grawitas_extension')
subprocess.call(shlex.split('./controller.sh sample_file50.xml sample.json'))

'''
file_list = glob.glob('*.xml')

for f in file_list:
    shutil.move(f, '/home/descentis/research/working_packages/witpy/grawitas_extension'+f)
'''    
    