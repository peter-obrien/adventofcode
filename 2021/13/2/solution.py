grid = []

max_x = 0
max_y = 0

dots = []
folds = []

reading_folds = False

def print_grid():
    print()
    for row in grid:
        for x in row:
            print(x, end='')
        print()

def fold(axis: str, val: int):
    global grid
    new_grid = []
    if axis == 'y':
        for r in range(0, val):
            new_grid.append(grid[r])
        for y in range(val+1, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == '#':
                    new_grid[val - (y - val)][x] = '#'
    else:
        values_in_fold = []
        for row in grid:
            values_in_fold.append(row[val])
            new_row = []
            for x in range(0, val):
                new_row.append(row[x])
            for x in range(val+1, len(row)):
                if row[x] == '#':
                    new_row[val - (x - val)] = '#'
            new_grid.append(new_row)
    grid = new_grid

with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            reading_folds = True
            continue
        if reading_folds:
            tokens = line.strip()[11:len(line.strip())].split('=')
            folds.append((tokens[0], int(tokens[1])))
        else:
            dots.append(list(map(int, line.strip().split(','))))

for dot in dots:
    max_x = max(max_x, dot[0])
    max_y = max(max_y, dot[1])

for y in range(0, max_y+1):
    row = []
    for x in range(0, max_x+1):
        row.append('.')
    grid.append(row)

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

for f in folds:
    fold(f[0], f[1])
print_grid()