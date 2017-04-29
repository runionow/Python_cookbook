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
print(prices.values())
print(prices.keys())
print(type(prices.keys()))
print(min(zip(prices.keys(),prices.values())))
print(sorted(zip(prices.keys(),prices.values())))

# 1.9 Find Commonolities in Dictionary

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
    'a' : 4
    }

b = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
    'w' : 4 
    }

# Finding keys in common
print(a.keys() & b.keys())

# Finding keys that are not in b  
print(a.keys() - b.keys())

# Finding Key value pairs in common 
print(a.items() & b.items()) 



# 1.10 Eliminate duplicate values in a Sequence.

a = [1,5,2,1,4,5,7,8,9,0,1]
# The answer in here is very simple.

# Converting a list to set will elimante duplicate values.
b = set(a)
print(b)

# 1.11 Naming a Slice.
record = '29375692374697234906723987923876908237469802347698023746987326'
SHARES = slice(0,10,2)
PRICE = slice(12,20)

print(record[SHARES])
print(record[PRICE])


cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 1.12 Most Frequently occuring Items in a Sequence.
from collections import Counter 

words = ['rambo','eyes','look' ,'into' ,'my' ,'eyes','look' ,'into' ,'my' ,'eyes','look' ,'into' ,'my' ,'eyes']
word_counts = Counter(words)
top_three = word_counts.most_common(3) # Returns Top 3 in the form of a tuple.
top =  word_counts.most_common() # Returns the count of every single word in the form of Tuple
print(top_three)
print(top)

# 1.13 Sorting List of dictionaries based on one or more dictionary values.


