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
cwd = os.getcwd()

shutil.move('sample_file20.xml', '/home/descentis/research/working_packages/witpy/grawitas_extension/sample_file20.xml')

os.chdir('/home/descentis/research/working_packages/witpy/grawitas_extension')
subprocess.call(shlex.split('./controller.sh sample_file20.xml sample.json'))
subprocess.call(shlex.split('rm sample_file20.xml'))

start = 0
with open('sample.json','r') as myFile:
    for line in myFile:
        with open('/home/descentis/research/working_datasets/wikipedia_current/talk_pages_json.txt', 'a') as newFile:
            start = newFile.tell()
            newFile.write(line+'\n')
with open('file_id.txt', 'a') as myFile:
    myFile.write(str(start)+'\n')

subprocess.call(shlex.split('rm sample.json'))

os.chdir(cwd)
shutil.move('sample_file88.xml', '/home/descentis/research/working_packages/witpy/grawitas_extension/sample_file88.xml')

os.chdir('/home/descentis/research/working_packages/witpy/grawitas_extension')
subprocess.call(shlex.split('./controller.sh sample_file88.xml sample.json'))
subprocess.call(shlex.split('rm sample_file88.xml'))

start = 0
with open('sample.json','r') as myFile:
    for line in myFile:
        with open('/home/descentis/research/working_datasets/wikipedia_current/talk_pages_json.txt', 'a') as newFile:
            start = newFile.tell()
            newFile.write(line+'\n')
with open('file_id.txt', 'a') as myFile:
    myFile.write(str(start)+'\n')

subprocess.call(shlex.split('rm sample.json'))

'''
file_list = glob.glob('*.xml')

for f in file_list:
    shutil.move(f, '/home/descentis/research/working_packages/witpy/grawitas_extension'+f)
'''    
    
