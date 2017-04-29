#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:04:11 2017

@author: arunnekkalapudi
"""

# 1.6 Make a dictionary that maps ey to more than one value \

# Example: List 
d = {
     'a' : [1,2,3],
     'b' : [4,5]
     }

# Example: Set 
e = {
     'a' : {1,2,3},
     'b' : {4,5}
     }

# Lets Create a the above using default Dict

from collections import defaultdict

# List 

dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['a'].append(2)
dl['b'].append(3)
dl['c'].append(4)

print(dl)

# Set 
# One Intresting point to be noted in here If you try to add same element to set it 
# wont accept it because set only push the element if it is unique.
# where as the list accepts any element to be appended.

ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['a'].add(2)
ds['b'].add(1)
ds['b'].add(2)
ds['c'].add(1)

print(ds)

# 1.7 To control the order of items to be placed in the dictionary.
# Wikia : In the normal dictionaries order of the data inserted in the dictionary is not preserved.
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1 
d['bar'] = 2 
d['spam'] = 3 
d['grok'] = 4 

print(d)

# Wikia : If you want the data to be precisely oredered in json.It is very good idea to OrderedDict() and then dumping it to JSON
import json
j = json.dumps(d) # TO STRING
print(j)
print(type(d))
print(type(j))

# 1.8 Performing various calculations on a dictionary.

# Example

prices = {
        'ACME' : 45.23,
        'AAPL' : 612.78,
        'IBM' : 205.55,
        'HPQ' : 37.20
        }    






