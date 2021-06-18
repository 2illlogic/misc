#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:10:16 2019

@author: bob
"""
def fart():
    print('fart')

class Node(object):
    """
    """
    def __init__(self, val=None, next_val=None):
        self.val = val
        self.next = next_val
        
    def get_val(self):
        return self.val

    def get_next(self):
        return self.next 

    def set_next(self, next_val):
        self.next = next_val
       
class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
    
    def addAtHead(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
    
    def get(self, index):
        node = self.head
        i = 0
        while i < index:
            node = node.get_next()
            i += 1
        return node
    
    def addAtIndex(self, val, index):
        prev_node = self.get(index-1)
        new_node = Node(val)
        new_node.set_next(prev_node.get_next())
        prev_node.set_next(new_node)
        
    def deleteAtIndex(self, index):
        delete = self.get(index)
        prev_node = self.get(index-1)
        prev_node.set_next(delete.get_next())
        
    def print_list(self):
        node = self.head
        while node != None:
            print(node.get_val(), end=" ")
            node = node.get_next()
       
newlist = LinkedList()
for i in range(1,11):
    newlist.addAtHead(i)
#        
#    def addAtIndex(self, index, val):
#        """insert a value at a specified index"""
#        
#    def deleteAtIndex(self, index):
#        """deletes a list item at the specified index"""
#        
