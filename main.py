import sys
from vector import Vector
from maze_reader import load_maze
if len(sys.argv) != 2:
    print('USAGE: <program> <commands_file>')
    sys.exit(1)
else:
    command_file = sys.argv[1]
    try:
        with open(command_file) as f:
            pass
    except FileNotFoundError:
        print('USAGE: <program> <commands_file>')
        sys.exit(1)

