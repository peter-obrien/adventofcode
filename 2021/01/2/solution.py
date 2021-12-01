priorDepth = None
increases = 0
decreases = 0
measure1 = [None, None]
measure2 = [None]
measure3 = []
with open('./input') as f:
    lines = f.readlines()
    for line in lines:
        val = int(line.strip())
        measure1.append(val)
        measure2.append(val)
        measure3.append(val)

# range(inclusive, exclusive)
for n in range(2, len(measure1)-3+1):
    currentDepth = measure1[n] + measure2[n] + measure3[n]
    # print(f'{priorDepth} v {currentDepth} = {measure1[n]} + {measure2[n]} + {measure3[n]}')
    if priorDepth is None:
        print('First depth reading')
    elif priorDepth < currentDepth:
        increases += 1
    elif currentDepth < priorDepth:
        decreases += 1
    else:
        # print('Same depth reading encountered')
        continue
    priorDepth = currentDepth
print(f'{increases} increases were encountered')
print(f'{decreases} decreases were encountered')
