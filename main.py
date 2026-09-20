import sys
from vector import Vector
from maze_reader import load_maze, print_maze, solve_maze, print_path

if len(sys.argv) != 2:
    print('USAGE: <program> <commands_file>')
    sys.exit(1)

command_file = sys.argv[1]
try:
    with open(command_file) as f:
        lines = f.readlines()
except FileNotFoundError:
    print('USAGE: <program> <commands_file>')
    sys.exit(1)

current_grid = None
current_path = None
for line in lines:
    clean = line.strip()
    if clean == '' or clean.startswith('#'):
        continue
    parts = clean.split()
    command = parts[0].upper()
    
    if command == 'LOAD_MAZE':
        maze_path = parts[1]
        result = load_maze(maze_path)
        if result is None:
            print('ERROR: INVALID_MAZE')
            current_grid = None
        else:
            current_grid, rows, cols = result
            print('MAZE_LOADED rows=' + str(rows) + ' cols=' + str(cols))
    
    elif command == 'PRINT_MAZE':
        if current_grid == None:
            print('ERROR: NO_MAZE')
        else:
            print_maze(current_grid)
    
    elif command == 'SOLVE':
        if current_grid == None:
            print('ERROR: NO_MAZE')
        else:
            solve_result = solve_maze(current_grid)
            if solve_result == None:
                print('UNSOLVABLE')
                current_path = None
            else:
                length, current_path = solve_result
                print('SOLVED')
                print('-> length=' + str(length))
    
    elif command == 'PRINT_PATH':
        if current_grid is None:
            print('ERROR: NO_MAZE')
        elif current_path is None:
            print('PATH')
            print('NO_PATH')
        else:
            print_path(current_path)

    elif command == 'CLEAR':
        current_grid = None 
        current_path = None
        print('CLEARED')

    elif command == 'QUIT':
        sys.exit(0)

    else: 
        print('ERROR: UNKNOWN_COMMAND')