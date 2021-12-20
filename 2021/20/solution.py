from __future__ import annotations
import sys
import time

infinite_pixel = '.'

def get_pixel(grid: list[list[str]], x:int, y: int):
    if y < 0 or y >= len(grid):
        return infinite_pixel
    elif x < 0 or x >= len(grid[y]):
        return infinite_pixel
    else:
        return grid[y][x]

def get_neighbors_as_binary(grid: list[list[str]], x: int, y: int):
    neighbors = [get_pixel(grid, x-1, y-1), get_pixel(grid, x, y-1), get_pixel(grid, x+1, y-1),
            get_pixel(grid, x-1, y), get_pixel(grid, x, y), get_pixel(grid, x+1, y),
            get_pixel(grid, x-1, y+1), get_pixel(grid, x, y+1), get_pixel(grid, x+1, y+1)]
    return ''.join(['0' if pixel == '.' else '1' for pixel in neighbors])

def pad_grid(grid: list[list[str]]):
    result = []
    for _ in range(3):
        result.append(['.' for _ in range(len(grid[0]) + 6)])
    for row in grid:
        new_row = ['.', '.', '.']
        new_row.extend(row)
        new_row.extend(['.', '.', '.'])
        result.append(new_row)
    for _ in range(3):
        result.append(['.' for _ in range(len(grid[0]) + 6)])
    return result

def enhance_grid(grid: list[list[str]], enhancement_algo):
    result = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[y])):
            row.append(enhancement_algo[int(get_neighbors_as_binary(grid, x, y),2)])
        result.append(row)
    return result  


if __name__ == '__main__':
    filename = './sample.txt' if '-s' in sys.argv else './input.txt'
    start_time = time.time()

    enhancement_algo = None

    with open(filename) as f:
        lines = f.read().splitlines()
        enhancement_algo = lines[0]
        # If puzzle is a numerical matrix
        matrix = [list(map(str, line)) for line in lines[2:]]

    matrix = pad_grid(matrix)

    for i in range(2):
        infinite_pixel = enhancement_algo[0] if i % 2 == 1 else '.'
        matrix = enhance_grid(matrix, enhancement_algo)
        if i % 2 == 1:
            matrix = pad_grid(matrix)

    result = sum([sum([1 if pixel == '#' else 0 for pixel in row]) for row in matrix])
    print(f"Part 1: {result} (took {(time.time() - start_time)}s)")
    start_time = time.time()

    for i in range(48):
        infinite_pixel = enhancement_algo[0] if i % 2 == 1 else '.'
        matrix = enhance_grid(matrix, enhancement_algo)
        if i % 2 == 1:
            matrix = pad_grid(matrix)

    result = sum([sum([1 if pixel == '#' else 0 for pixel in row]) for row in matrix])
    print(f"Part 2: {result} (took {(time.time() - start_time)}s)")