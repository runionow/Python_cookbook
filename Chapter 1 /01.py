#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:10:57 2017

@author: arunnekkalapudi
"""

# Pyhton CookBook 

# 1.2 Unpacking Elements from Iterables of arbitary length.
import statistics as st

def drop_first_last(grades):
    first,middle,*grade = grades
    return st.mean(grade),grade

grades = ('Arun','Nekkalapudi',98,97,96,95,94,93,92)    
print(drop_first_last(grades))

# 1.3 Want to keep a limited a limited history of last few 'N' items in History.

from collections import deque 

q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
