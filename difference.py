#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:17:30 2018

@author: tommystarlit
"""
import re
from datetime import datetime
with open('/home/tommystarlit/Downloads/BIAF.prj', 'r') as file1:
    names = re.findall('(?<=L_DESC=)".*?"', file1.read())
       
with open('/home/tommystarlit/Downloads/diff2.txt', 'w') as df:
    for name in names:
        df.write(name+'\n')

with open('/home/tommystarlit/Downloads/diff1.txt', 'r') as file1:
    with open('/home/tommystarlit/Downloads/diff2.txt', 'r') as file2:
        diff = set(file2).difference(file1)

with open('/home/tommystarlit/Downloads/diff.txt', 'a') as df:
    df.write('\n')
    df.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')
    df.write('\n')
    for line in diff:
        df.write(line)
        
"""
[x]Regex positive lookbehind L_DESC
[x]dodaj date w logu
[]dodaj klase w logu,
[x]append day by day
"""