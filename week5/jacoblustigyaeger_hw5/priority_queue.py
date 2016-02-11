import numpy as np

class PriorityQueue(object):
    
    def __init__(self,N=0,MAX=100):
        self.a=[0] * (MAX+1)
        self.N=N
        self.MAX=MAX
        self.a[0] = None
        
    def minimum(self):
        if self.N > 0:
            return self.a[1] # Zero is always None
        else:
            print "Error in Min"
            return None
    
    def size(self):
        return self.N
    
    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.size() == self.MAX:
            return True
        else:
            return False
    
    def insert(self, i):
        
        # Check if queue is full
        if self.isFull():
            print 'Error in insert'
            return None
        
        # Increase N
        self.N += 1
        
        # insert at empty space 1 beyond old N
        self.a[self.N] = i
        
        # Loop while (parent > child) and (not at root) 
        k = self.N
        while (k > 1) & (self.a[int(np.floor(k/2))] > self.a[k]):
            # Exchange using temporary variable
            tmp = self.a[int(np.floor(k/2))]
            self.a[int(np.floor(k/2))] = self.a[k]
            self.a[k] = tmp
            
            # Divide k by 2 to move up one level 
            k = int(np.floor(k/2))
    
    def delMin(self):
        
        # Error condition
        if self.isEmpty():
            print "Error in delMin()"
            return
        
        # Save minimum
        tmin = self.a[1]
        
        # Set smallest child to top 
        self.a[1] = self.a[self.N]
        
        # Set child to zero
        self.a[self.N] = 0
        
        # Decrement N
        self.N -= 1 #self.N
        
        # Loop
        k = 1
        while (2*k <= self.N):
            
            if ((2*k == self.N) or (self.a[2*k] < self.a[2*k+1])):
                j = 2*k     # If the left child is the samllest child
            else:
                j = 2*k+1   # If the right child is the smallest child
            
            # If parent is less than (only child or lesser child)
            if (self.a[k] > self.a[j]):
                temp = self.a[k]
                self.a[k] = self.a[j]
                self.a[j] = temp
                k = j
            else:
                break
        
        return tmin