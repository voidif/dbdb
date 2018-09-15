import logical

class BinaryTree(logical.LogicalBase):
    

    def __init__(self, storge):
        self.rootnode = None

    def get(self, key):
        if self.rootnode == None:
            raise KeyError
        curnode = self.rootnode
        while curnode != None:
            if curnode.key > key:
                curnode = curnode.left
            elif curnode.key < key:
                curnode = curnode.right
            else: 
                return curnode.value
        raise KeyError
        

    def insert(self, node, key, value):
        if self.rootnode == None:
            rootnode = BinaryNode(None, None, key, value)
        curnode = rootnode
        while curnode != None:
            if curnode.key > key:
                if curnode.left == None:
                    curnode.left = BinaryNode(None, None, key, value)
                    return rootnode
                else:
                    curnode = curnode.left
            elif curnode.key < key:
                if curnode.right == None:
                    curnode.right = BinaryNode(None, None, key, value)
                    return rootnode
                else: 
                    curnode = curnode.right
            else: 
                curnode.value = value
                return rootnode
        return rootnode 


class BinaryNode(object):
    def __init__(self, left, right, key, value):
        self.left = left
        self.right = right
        self.key = key
        self.value = value