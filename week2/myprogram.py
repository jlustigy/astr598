#!/usr/bin/python

# Import LinkedList module
from linkedlist import LinkedList

# Create an empty LinkedList
print '1. Create LinkedList: '
L = LinkedList()
print L

# Insert 3 values at head
print '2. Insert 3 values at head: ' 
L.insert_at_head(-1)
L.insert_at_head(-2)
L.insert_at_head(-3)
print L

# Delete one value at the head
print '3. Delete one value at the head: '
L.delete_at_head()
print L

# Insert 3 values at the tail
print '4. Insert 3 values at the tail: '
L.insert_at_tail(0)
L.insert_at_tail(1)
L.insert_at_tail(2)
print L
print 'Done.'
