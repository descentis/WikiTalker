#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:06:00 2020

@author: descentis
"""
count = 0
with open('/media/descentis/0FC10BE60FC10BE6/WikipediaData/CurrentRevision/all_talk_pages/all_talk_pages.txt', 'r') as myFile:
    for line in myFile:
        with open('sample_file'+str(count)+'.xml', 'a') as newFile:
            newFile.write(line)
        
        if '</page>' in line:
            count+=1
        
        if count == 100:
            break