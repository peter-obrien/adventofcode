import sys

frequencies = dict()
instructions = dict()
iterations = 40
least = sys.maxsize
most = 0

with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            continue
        if '->' in line:
            tokens = line.strip().split(' -> ')
            instructions[tokens[0]] = tokens[1]
        else:
            sequence = line.strip()
            for i in range(len(sequence)):
                pair = sequence[i:i+2]
                # Track the frequency of each individual letter
                frequencies[sequence[i]] = frequencies.get(sequence[i], 0) + 1
                if len(pair) == 2:
                    # Track the frequency of each pair
                    frequencies[pair] = frequencies.get(pair, 0) + 1

for i in range(iterations):
    new_frequencies = dict()
    for k in frequencies:
        if len(k) == 1:
            new_frequencies[k] = new_frequencies.get(k, 0) + frequencies[k]
        else:
            freq = frequencies[k]
            left = k[0] + instructions[k]
            right = instructions[k] + k[1]
            new_frequencies[left] = new_frequencies.get(left, 0) + freq
            new_frequencies[right] = new_frequencies.get(right, 0) + freq
            new_frequencies[instructions[k]] = new_frequencies.get(instructions[k], 0) + freq
    frequencies = new_frequencies

for k in frequencies:
    if len(k) == 1:
        v = frequencies[k]
        most = max(most, v)
        least = min(least, v)

print(most - least)