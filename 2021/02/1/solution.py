position = 0
depth = 0
with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.strip().split(' ')
        if tokens[0] == 'forward':
            position += int(tokens[1])
        elif tokens[0] == 'up':
            depth -= int(tokens[1])
        elif tokens[0] == 'down':
            depth += int(tokens[1])
        else:
            print('Unknown command')

print(f'Horizontal position = {position}')
print(f'Depth = {depth}')
print(f'Solution = {position * depth}')
