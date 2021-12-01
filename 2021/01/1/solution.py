priorDepth = None
increases = 0
decreases = 0
with open('./input') as f:
    lines = f.readlines()
    for line in lines:
        text = line.strip()
        currentDepth = int(text)
        if priorDepth is None:
            print('First depth reading')
        elif priorDepth < currentDepth:
            increases += 1
        elif currentDepth < priorDepth:
            decreases += 1
        else:
            # same depth
            print('Same depth reading encountered')
        priorDepth = currentDepth
print(f'{increases} increases were encountered')
print(f'{decreases} decreases were encountered')
