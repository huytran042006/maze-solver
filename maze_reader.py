from vector import Vector

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
        
def print_maze(grid):                   
    print('MAZE')                          # print MAZE \n
    for i in range(grid.size()):           #grid.size() return hamany rows
        row = grid.get(i)                  #grid.get(i) is ['#','S','.','.','.','G','#']
        line = ''                          #this is where all elements will be add into 1 string line
        for j in range(row.size()):        #from 0 to number of element in row ( which is 7)
            line += row.get(j)             #add elements into string
        print(line)                        #print line