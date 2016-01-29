class Node(object):
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = None
    
    def __repr__(self):
        return "%s" % (self.data)
    
    def __str__(self):
        return "%s" % (self.data)

class Stack(object):
    
    def __init__(self, head = None, N = 0):
        self.head = head
        self.N = N
    
    # Same as insert_at_head!
    def push(self, i=None):
        n = Node(data=i,nxt=None)
        n.nxt = self.head
        self.head = n
        self.N += 1
    
    def pop(self):
        # If stack is empty
        if (self.head == None):
            print "Error in pop: Tried to pop empty stack"
            return None
        # Otherwise pop away!
        else:
            # get value of data at head
            i = self.head.data
            # set head to next
            self.head = self.head.nxt
            # decrement N
            self.N -= 1
        return i
    
    def top(self):
        if (self.head == None):
            print "Error in top: No data in top"
            return None
        else:
            i = self.head.data
        return i
    
    def size(self):
        return self.N
    
    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            return False
    
    def __repr__(self):
        return "Stack --> head:%s, size:%s" % (self.head, self.N)
    
    def __str__(self):
        n = self.head
        l = '<'
        while n != None:
            l = l +' '+ str(n.data)
            n = n.nxt
        l = l + ' >'
        return l
        
