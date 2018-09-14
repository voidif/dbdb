#argv number must between 4 and 5, inclusive
import sys

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
    try:
        if verb == 'get':
            return
        elif verb == 'set':
            return
        else:
            return
    except KeyError:
        print('Key not found', file = sys.stderr)
        return BAD_KEY
    return OK

main(sys.argv)