import portalocker
import os

class Stroge(object):
    SUPERBLOCK_SIZE = 4096

    def __init__(self, f):
        self.locked = False
        self.f = f
        self.ensure_superblock()

    def ensure_superblock(self):
        self.lock()
        self.seek_end()
        end_address = self.f.tell()
        if end_address < self.SUPERBLOCK_SIZE:
            self.f.write(b'\x00' * (self.SUPERBLOCK_SIZE - end_address))
        self.unlock()

    def lock(self):
        if not self.locked:
            portalocker.lock(self.f, portalocker.LOCK_EX)
            self.locked = True
            return True
        else:
            return False

    def unlock(self):
        if self.locked:
            portalocker.unlock(self.f)
            self.locked = False
            return True
        else:
            return False

    def seek_end(self):
        self.f.seek(0, os.SEEK_END)
