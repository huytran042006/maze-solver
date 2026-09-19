
from maze_reader import load_maze, solve_maze, print_path

result = load_maze('Mazes/maze1.txt')
grid, rows, cols = result

solve_result = solve_maze(grid)
print(solve_result)
length, path = solve_result
print(length)
print(path._data)
print_path(path)