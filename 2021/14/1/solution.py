import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.prior = None
        self.next = None
    
    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prior = self.tail
            self.tail = n

instructions = dict()
sequence = LinkedList()
iterations = 10

with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            continue
        if '->' in line:
            tokens = line.strip().split(' -> ')
            instructions[tokens[0]] = tokens[1]
        else:
            for l in line.strip():
                sequence.append(l)

for i in range(iterations):
    n = sequence.head
    while n:
        if n.prior:
            reaction = Node(instructions[f"{n.prior.val}{n.val}"])
            n.prior.next = reaction
            reaction.prior = n.prior
            reaction.next = n
            n.prior = reaction
        n = n.next

frequencies = dict()
n = sequence.head
while n:
    if n.val in frequencies:
        frequencies[n.val] += 1
    else:
        frequencies[n.val] = 1
    n = n.next

least = sys.maxsize
most = 0
for k in frequencies:
    v = frequencies[k]
    most = max(most, v)
    least = min(least, v)
print(most - least)
