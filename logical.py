class ValueRef(object):
    def __init__(self):
        return


class LogicalBase(object):
    node_ref_class = None


    def __init__(self, storge):
        self.storge = storge
        self.refresh_tree_ref()

    def refresh_tree(self):
        self.tree_ref = self.node_ref_class()
    
    def get(self, key):
        return

    def set(self, key, value):
        self.insert(key, value)

    def insert(self, key, value):
        return None