import binary_tree as bt
import physical as phy

class DBDB(object):
    def __init__(self, f):
        self.storge = phy.Stroge(f)
        self.tree = bt.BinaryTree(self.storge)

    def getitem(self, key):
        self.assert_not_closed()
        return self.tree.get(key)

    def setitem(self, key, value):
        return self.tree.set(key, value)

    def assert_not_closed(self):
        if self.storge.closed:
            raise ValueError('database closed.')