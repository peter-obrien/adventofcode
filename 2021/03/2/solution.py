oxygen = []
scrubber = []
def getFrequency(binStrings):
    frequencies = dict()
    for binString in binStrings:
        val = binString.strip()
        counter = 0
        for c in val:
            if counter not in frequencies:
                frequencies[counter] = (0, 0)
            freqVal = frequencies[counter]
            if c == '1':
                freqVal = (freqVal[0] + 1, freqVal[1] )
            else:
                freqVal = (freqVal[0], freqVal[1] + 1)
            frequencies[counter] = freqVal
            counter += 1
    return frequencies

with open('./input.txt') as f:
    lines = f.readlines()
    oxygen = lines
    scrubber = lines

counter = 0
while len(oxygen) > 1:
    freq = getFrequency(oxygen)
    newOxygen = []
    freqVal = freq[counter]
    for val in oxygen:
        val = val.strip()
        if freqVal[1] > freqVal[0]:
            if val[counter] == '0':
                newOxygen.append(val)
        else:
            if val[counter] == '1':
                newOxygen.append(val)
    counter += 1
    oxygen = newOxygen
print(oxygen)

counter = 0
while len(scrubber) > 1:
    freq = getFrequency(scrubber)
    newScrubber = []
    freqVal = freq[counter]
    for val in scrubber:
        val = val.strip()
        if freqVal[1] <= freqVal[0]:
            if val[counter] == '0':
                newScrubber.append(val)
        else:
            if val[counter] == '1':
                newScrubber.append(val)
    counter += 1
    scrubber = newScrubber
print(scrubber)
print(f'oxygen   = {oxygen[0]}')
print(f'oxygen int = {int(oxygen[0], 2)}')
print(f'scrubber = {scrubber[0]}')
print(f'scrubber int = {int(scrubber[0], 2)}')
print(f'oxygen x scrubber = {int(oxygen[0], 2) * int(scrubber[0], 2)}')