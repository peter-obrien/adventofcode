import sys
import time

if __name__ == '__main__':
    filename = './sample.txt' if '-s' in sys.argv else './input.txt'
    start_time = time.time()

    with open(filename) as f:
        lines = f.readlines()
        # If puzzle is a numerical matrix
        matrix = [list(map(int, line.strip())) for line in lines]

    result = None
    print(f"{result} (took {(time.time() - start_time)}s)")