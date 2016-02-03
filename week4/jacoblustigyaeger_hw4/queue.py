class Node(object):
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = None
    
    def __repr__(self):
        return "%s" % (self.data)
    
    def __str__(self):
        return "%s" % (self.data)

class Queue(object):
    def __init__(self, head = None, tail = None, N = 0):
        self.head = None
        self.tail = None
        self.N = 0
    
    def put(self, i):
        # Create new Node
        n = Node()
        # Set n's data and next
        n.data = i
        n.nxt = None
        # Empty Queue
        if (self.head == None):
            self.head = n
            self.tail = n
        # One element in Queue
        elif (self.head == self.tail):
            self.head.nxt = n
            self.tail = n
        # Many elements in Queue
        else:
            self.tail.nxt = n
            self.tail = n
        # Increment size, N
        self.N += 1
    
    def get(self):
        # Empty Queue 
        if (self.head == None):
            print "Error in get: Empty Queue"
            return None
        # Get data at head
        i = self.head.data
        # Set head to next
        self.head = self.head.nxt
        # Decrement size
        self.N -= 1
        # Return i
        return i
    
    def front(self):
        if (self.head == None):
            print "Error in front: No data in Queue"
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
        return "Stack --> front:%s, size:%s" % (self.head, self.N)
    
    def __str__(self):
        n = self.head
        l = '|'
        while n != None:
            l = l +' '+ str(n.data)
            n = n.nxt
        l = l + ' |'
        return l