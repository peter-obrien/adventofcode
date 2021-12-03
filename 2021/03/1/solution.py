gamma = ''
epsilon = ''
freq = dict()
with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        val = line.strip()
        counter = 0
        for c in val:
            if counter not in freq:
                freq[counter] = (0, 0)
            freqVal = freq[counter]
            if c == '1':
                freqVal = (freqVal[0] + 1, freqVal[1] )
            else:
                freqVal = (freqVal[0], freqVal[1] + 1)
            freq[counter] = freqVal
            counter += 1
print(freq)
# Gamma = most frequent
for n in range(0, len(freq)):
    if freq[n][0] > freq[n][1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
# Epsilon = least frequent
print(f'Gamma   = {gamma}')
print(f'Gamma int = {int(gamma, 2)}')
print(f'Epsilon = {epsilon}')
print(f'Epsilon int = {int(epsilon, 2)}')
print(f'Gamma x Epsilon = {int(gamma, 2) * int(epsilon, 2)}')