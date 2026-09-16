import sys
from vector import Vector
if len(sys.argv) != 2:
    print('USAGE: <program> <commands_file>')
    sys.exit(1)
else:
    command_file = sys.argv[1]
    try:
        open(command_file)
    except FileNotFoundError:
        print('USAGE: <program> <commands_file>')
        sys.exit(1)