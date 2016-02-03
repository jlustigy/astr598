#!/usr/bin/python

# Import Queue and numpy
from queue import Queue
import numpy as np

# Initialize empty Queue
Q = Queue()

# Check to see if Queue is empty
print "Is empty? ",Q.isEmpty()

# Put ten random integers into Queue
for i in range(10):
    Q.put(np.random.randint(100))

# Check Queue
print Q
print "Is empty? ", Q.isEmpty() 
print "Size: ", Q.N

# Get an integer from the queue and print it, 10 times
for i in range(10):
    a = Q.get()
    print a

# Check Queue
print "Is empty? ", Q.isEmpty() 
print "Size: ", Q.N