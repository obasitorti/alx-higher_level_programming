#!/usr/bin/python3
"""
    this module defines a node and a linked list
"""

class Node:
    """
        this is the node class
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    @property
    def data(self):
        return self.data
    
    @data.setter
    def data(self, value):
        # self.value = value
        # self.next = None
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.data = value

    @property
    def next_node(self):
        return self.next

    @next_node.setter
    def next_node(self,value):
        if value != None:
            raise TypeError("next_node must be a Node object")
        if type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.next_node = value
    

class SinglyLinkedList:
    def __init__(self):
        self.head=Node(data)
    
    def sorted_insert(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
            cur.next = new_node

    def __str__(self):
        elements = ""
        cur_node = self.head
        while cur_node != None:
            cur_node = cur_node.next
            elements += str(cur_node.data) + "\n"
        return elements


SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
