# Create Node Class
class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None      
        
    def __repr__(self):
        return "%s" % (self.data)
    
    def __str__(self):
        return "%s" % (self.data)

# Create LinkedList Class
class LinkedList(object):
    
    def __init__(self, head=Node(), tail=Node()):
        self.head = None
        self.tail = None
        
    def __repr__(self):
        return "LinkedList --> head:%s, tail:%s" % (self.head, self.tail)
    
    def __str__(self):
        n = self.head
        l = '<'
        while n != None:
            l = l +' '+ str(n.data)
            n = n.next_node
        l = l + ' >'
        return l
    
    def insert_at_head(self, val):
        n = Node(val, None)
        # If No nodes
        if (self.head == None and self.tail == None):
            self.head = n
            self.tail = self.head
        # Else Many nodes
        else:
            n.next_node = self.head
            self.head = n
    
    def delete_at_head(self):
        # If No Nodes
        if (self.head == None):
            return None
        # If Many Nodes
        else:
            val = self.head.data
            self.head = self.head.next_node
            if (self.head == self.tail):
                self.tail = self.head
            return val
    
    def insert_at_tail(self, val):
        # Create new Node
        n = Node(val, None)
        # If No Nodes
        if (self.head == None):
            self.head = n
            self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n
            # If One Node (redundant in python)
            if (self.head == self.tail):
                self.head.next_node = n
