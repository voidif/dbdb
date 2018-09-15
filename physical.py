class Stroge(object):
    SUPERBLOCK_SIZE = 4096

    def __init__(self, f):
        self.closed = True
