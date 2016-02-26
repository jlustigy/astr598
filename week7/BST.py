class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data  # Key
        self.left = left
        self.right = right

class BinarySearchTree(object):
    
    def __init__(self,N=0,root=None):
        self.N = N
        self.root = root
        
    def insert(self, i):
        
        # Create new node
        n = Node(data=i, left=None, right=None)
        
        # Increment N
        self.N += 1
        
        # If tree is empty
        if (self.root == None):
            self.root = n
        # Otherwise
        else:
            local_insert(self.root,n)
    
    def find(self, i):
        return local_find(self.root,i)
    
    def traverse_pre_order(self):
        local_traverse_pre_order(self.root)
            
    def traverse_in_order(self):
        local_traverse_in_order(self.root) 
            
    def traverse_post_order(self):
        local_traverse_post_order(self.root)
            
    def size(self):
        return self.N
    
    def minimum(self):
        if (self.root == None):
            print "Error in minimum: root == None"
            return None
        else:
            local_root = self.root
            i = local_root.data
        
        while (local_root != None):
            i = local_root.data
            local_root = local_root.left
        
        return i
    
    def maximum(self):
        if (self.root == None):
            print "Error in minimum: root == None"
            return None
        else:
            local_root = self.root
            i = local_root.data
        
        while (local_root != None):
            i = local_root.data
            local_root = local_root.right
        
        return i
        
    def isEmpty(self):
        if (self.N == 0):
            return True 
        else:
            return False


# Use Binary recursion to insert according to left/right rules
def local_insert(local_root, n):
        
    # If tree is empty throw error
    if (local_root == None):
        print("Error in local_insert(): local_root == None")
        return
        
    # If new node is less than local root, insert at left leaf
    if (n.data < local_root.data):
        
        # If left child is None, then insert new node there. End condition.
        if (local_root.left == None):
            local_root.left = n
        # Otherwise, recursively call local_insert
        else:
            local_insert(local_root.left, n)
        
    # Otherwise, new node is greater than local root, so insert at right leaf
    else:
    
        # If right child is None, then insert new node there. End condition.
        if (local_root.right == None):
            local_root.right = n
        # Otherwise, recursively call local_insert
        else:
            local_insert(local_root.right, n)

def local_find(local_root, i):
    # If local_root is None, then i isn't in tree
    if (local_root == None):
        return False
    # If local_root contains i, then i is in tree
    elif (local_root.data == i):
        return True
    # If i is less than local_root, then recursively enter left leaf
    elif (i < local_root.data):
        return local_find(local_root.left, i)
    # If i is greater than local_root, then recursively enter right leaf
    else:
        return local_find(local_root.right, i)

def local_traverse_pre_order(local_root):
    # First process parent
    if (local_root == None):
        return
    else:
        # Print out local root value
        print local_root.data
        # Process left subtree
        local_traverse_pre_order(local_root.left)
        # Process right subtress
        local_traverse_pre_order(local_root.right)

def local_traverse_in_order(local_root):
    # First process parent
    if (local_root == None):
        return
    else:
        # Process left subtree
        local_traverse_in_order(local_root.left)
        # Print out local root value
        print local_root.data
        # Process right subtress
        local_traverse_in_order(local_root.right)

def local_traverse_post_order(local_root):
    # First process parent
    if (local_root == None):
        return
    else:
        # Process left subtree
        local_traverse_post_order(local_root.left)
        # Process right subtress
        local_traverse_post_order(local_root.right) 
        # Print out local root value
        print local_root.data