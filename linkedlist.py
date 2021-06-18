#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:30:05 2019

@author: bob
"""
def make_linked_list(l):
    """Input list object l, return dict object ll that is a linked list"""
    n = len(l)
    ll = {}
    ll[l[0]] = (l[0], l[1])
    ll[l[n-1]] = (l[n-2],l[n-1])
    for i in range(1, n-1):
        ll[l[i]] = (l[i-1], l[i+1])
    return ll
        
class LinkedList():
    """
    
    """
    def __init__(self, l):
        self.ll = make_linked_list(l)
        
    def get_first_node(self):
        for node in self.ll:
            if self.ll[node][0] == node:
                return node
    
    def next_val(self, node):
        return self.ll[self.ll[node][1]]
    
    def index(self, index):
        first = self.get_first_node()
        
        
test = [1,2,3,4,5]
d = LinkedList(test)

