#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:49:29 2017

@author: arunnekkalapudi
"""

# 1.5 Priority Queue

import heapq

class PriroityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        if isinstance(item,Item):
            heapq.heappush(self._queue,(-priority,self._index, item))
            self._index += 1
            return self._queue 
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    def __string__(self):
        return self._queue
    
class Item:
    def __init__(self,name):
        self.name = name 
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriroityQueue()
q.push(Item('foo'),1)
print(q.push(Item('foo'),1))
q.push(Item('poo'),3)
q.push(Item('qoo'),2)
q.push(Item('roo'),6)
q.pop()
q.pop()
