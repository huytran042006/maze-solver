from maze_reader import load_maze, print_maze

result = load_maze('Mazes/maze1.txt')
if result is not None:
    grid, rows, cols = result
    print_maze(grid)
else:
    print('Load failed')