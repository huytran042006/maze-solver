from maze_reader import load_maze, get_neighbors, find_start

result = load_maze('Mazes/maze1.txt')
grid, rows, cols = result

print(get_neighbors(grid, 1, 1))
print(get_neighbors(grid, 0, 0))
result1 = get_neighbors(grid, 1, 1)
print(result1._data)

result2 = get_neighbors(grid, 0, 0)
print(result2._data)

print(find_start(grid))
