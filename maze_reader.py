from vector import Vector
from queue import Queue

def load_maze(path):
    with open(path) as f:
        lines = f.readlines()
    first_line = lines[0].strip()
    parts = first_line.split()
    rows = int(parts[0])
    cols = int(parts[1])

    is_valid = True

    grid = Vector(rows)
    for line in lines[1:]:                 # from index 1 to ...
        clean_line = line.strip()          # no more newline == (#.###.#, #.....#, #######, ...)
        row = Vector(cols)                  # new vector name as row
        for char in clean_line:             # (#.###.#, #.....#, #######, ...)
            row.push(char)                  # push "#.....#" vào vector row
        if row.size() != cols:
            is_valid = False
        grid.push(row)                      #grid.row( #.....#, ...)

    if grid.size() != rows:
        is_valid = False
    else:
        countS= 1
        countG= 1
        for i in range(rows): 
            for j in range (cols): 
                if grid.get(i).get(j)=='S':
                    countS -=1
                elif grid.get(i).get(j)=='G': 
                    countG -= 1
        if countS != 0 or countG !=0:
            is_valid = False
    
    if is_valid:
        return grid, rows, cols
    else:
        return None

def find_start(grid):
    for i in range(grid.size()):           
            row = grid.get(i)                                       
            for j in range(row.size()):      
                if grid.get(i).get(j) == 'S':
                    return i, j
                   

def print_maze(grid):                   
    print('MAZE')                          # print MAZE \n
    for i in range(grid.size()):           #grid.size() return hamany rows
        row = grid.get(i)                  #grid.get(i) is ['#','S','.','.','.','G','#']
        line = ''                          #this is where all elements will be add into 1 string line
        for j in range(row.size()):        #from 0 to number of element in row ( which is 7)
            line += row.get(j)             #add elements into string
        print(line)                        #print line

def print_path(path):
    print('PATH')
    for i in range(path.size()):
        coord = path.get(i)
        r, c = coord
        print('-> (' + str(r) + ',' + str(c) + ')')


def get_neighbors(grid, row, col):
    neighbors = Vector(4)
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]     #up, down, left, right
    for dr, dc in offsets:
        new_row= row + dr
        new_col= col + dc
        if (new_row <0 or new_row>= grid.size()) or (new_col <0 or new_col>= grid.get(0).size()):
            pass
        else:
            test_element = grid.get(new_row).get(new_col)
            if test_element != '#':
                neighbors.push((new_row, new_col))
    return neighbors

def solve_maze(grid):                           
    start = find_start(grid)                        # coord of S ex(1,1)
    queue = Queue(grid.size()*grid.get(0).size())   #[none none none ...]
    queue.enqueue(start)                            #[(1,1), None, None, None]
    visited = {}                                    
    visited[start] = True                           # {(1,1): True}
    parent={}                                       # {}

    found = False
    while not queue.is_empty():                                 #loop if still have elements in queue
        current = queue.dequeue()                               #[none none none ...]
        char = grid.get(current[0]).get(current[1])             #(1,1) give S
        if char == 'G':
            found = True
            break
        neighbors = get_neighbors(grid, current[0], current[1]) #at (1,1) neigbors that are valid are (2,1) and (1,2)
        for i in range(neighbors.size()):                       #range of 2 now
            neighbor = neighbors.get(i)                         #get coord such as (2,1) and (1,2)
            if neighbor not in visited:                         #not in visit yet since now it is only has (1,1)
                visited[neighbor] = True                        #now add to visit and parent dict (2,1):True and (2,1):(1,1) 
                parent[neighbor] = current                          
                queue.enqueue(neighbor)                         #neighboor in queue now

    if found == False:
        return None
    else:
        path_reversed = Vector(grid.size() * grid.get(0).size())        
        
        while current != start:                                 #since path vector still reverse from G to S instead of S to G, loop untill get S
            path_reversed.push(current)
            current = parent[current]   
        path_reversed.push(start)
        path = Vector(path_reversed.size())
        for i in reversed(range(path_reversed.size())):
            path.push(path_reversed.get(i))
        length = path.size() -1 
        return length, path