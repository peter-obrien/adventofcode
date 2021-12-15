from collections import defaultdict, deque
import sys
import time

class MyGraph:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        str_row = []
        for row in self.matrix:
            str_r = ''
            for v in row:
                str_r += str(v)
            str_row.append(str_r)
        return '\n'.join(str_row)

    def get_tuple(self, x, y):
        return (self.matrix[y][x], x, y)

    def get_neighbors(self, x, y):
        if y - 1 >= 0:
            yield self.get_tuple(x, y-1)
        if y + 1 < len(self.matrix):
            yield self.get_tuple(x, y+1)
        if x - 1 >= 0:
            yield self.get_tuple(x-1, y)
        if x + 1 < len(self.matrix[0]):
            yield self.get_tuple(x+1, y)

def reconstruct_path(cameFrom: dict, current: tuple):
    total_path = deque()
    total_path.append(current)
    while current in cameFrom:
        current = cameFrom[current]
        total_path.appendleft(current)
    return total_path

def distance(a:tuple, b:tuple):
    # return abs(a[1] - b[1]) + abs(a[2] - b[2])
    return 1

# https://en.wikipedia.org/wiki/A*_search_algorithm
def astar(G: MyGraph, start: tuple, goal: tuple, h):
    # The set of discovered nodes that may need to be (re-)expanded.
    openSetList = []
    openSetList.append(start)
    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    cameFrom = dict()
    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = defaultdict(lambda: sys.maxsize)
    gScore[start] = 0
    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to how short a path from start to finish can be if it goes through n.
    fScore = defaultdict(lambda: sys.maxsize)
    fScore[start] = h(start, goal)

    while len(openSetList) > 0:
        # current := the node in openSet having the lowest fScore[] value
        current = None
        lowest_fScore = sys.maxsize
        for node in openSetList:
            if fScore[node] < lowest_fScore:
                current = node
                lowest_fScore = fScore[node]
        if current == goal:
            return reconstruct_path(cameFrom, current)
        openSetList.remove(current)
        for neighbor in G.get_neighbors(current[1], current[2]):
            tentative_gScore = gScore[current] + neighbor[0]
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor, goal)
                if neighbor not in openSetList:
                    openSetList.append(neighbor)
    raise Exception('End not reached')

if __name__ == '__main__':
    filename = './sample.txt' if '-s' in sys.argv else './input.txt'
    start_time = time.time()

    grid = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = []
            for n in line.strip():
                row.append(int(n))
            grid.append(row)

    expanded_grid = []
    for row in grid:
        expanded_row = []
        for n in range(5):
            for i in row:
                expanded_row.append((i+n-9) if i + n > 9 else (i+n))
        expanded_grid.append(expanded_row)
    extra_rows = []
    for n in range(1,5):
        for row in expanded_grid:
            additional_row = []
            for i in row:
                additional_row.append((i+n-9) if i + n > 9 else (i+n))
            extra_rows.append(additional_row)
    for row in extra_rows:
        expanded_grid.append(row)

    G = MyGraph(expanded_grid)
    path = astar(G, G.get_tuple(0,0), G.get_tuple(len(G.matrix[0])-1, len(G.matrix)-1), distance)
    total_risk = 0
    path.popleft() # Don't count the starting position
    while len(path) > 0:
        total_risk += path.popleft()[0]

    print(f"{total_risk} (took {(time.time() - start_time)}s)")