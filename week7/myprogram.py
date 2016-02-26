# Import BinarySearchTree
from BST import BinarySearchTree
import numpy as np

# Initialize BST
B = BinarySearchTree()

# Insert 100 random integers into the BST
for i in range(100):
    B.insert(np.random.randint(100))
    
# Call traverse
B.traverse_in_order()