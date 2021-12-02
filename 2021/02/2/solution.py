position = 0
depth = 0
aim = 0
with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.strip().split(' ')
        if tokens[0] == 'forward':
            x = int(tokens[1])
            position += x
            depth += (aim * x)
        elif tokens[0] == 'up':
            aim -= int(tokens[1])
        elif tokens[0] == 'down':
            aim += int(tokens[1])
        else:
            print('Unknown command')

print(f'Horizontal position = {position}')
print(f'Depth = {depth}')
print(f'Solution = {position * depth}')
