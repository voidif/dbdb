import interface

def connect(dbname):
    f = open(dbname, 'r+b')
    return interface.DBDB(f)