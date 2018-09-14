#argv number must between 4 and 5, inclusive
import sys
import init

BAD_ARGS = -1
BAD_KEY = -2
OK = 1

def main(argv):
    if not (4 <= len(argv) <= 5):
        return BAD_ARGS
    argv.append(None)
    dbname = argv[1]
    verb = argv[2]
    key = argv[3]
    value = argv[4]
    if verb not in ['get', 'set', 'delete']:
        return BAD_ARGS
    db = init.connect(dbname)
    try:
        if verb == 'get':
            sys.stdout.write(db.get(key))
        elif verb == 'set':
            return
        else:
            return
    except KeyError:
        print('Key not found', file = sys.stderr)
        return BAD_KEY
    return OK

main(sys.argv)