#!/usr/bin/python

# Import PriorityQueue class and numpy
from priority_queue import PriorityQueue
import numpy as np

# Initialize empty Priority Queue
PQ = PriorityQueue()

# Insert 20 random integers into the Priority Queue
for i in range(20):
    PQ.insert(np.random.randint(100))

# Delete min from queue 20 times
for i in range(20):
    print PQ.delMin()