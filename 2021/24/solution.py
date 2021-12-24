from __future__ import annotations
from functools import lru_cache
import sys
import time
from collections import deque
from itertools import product

class ALU:
    def __init__(self, instructions: list[tuple]) -> None:
        self.vars = dict()
        self.vars['w'] = 0
        self.vars['x'] = 0
        self.vars['y'] = 0
        self.vars['z'] = 0
        self.instruction_sets = []
        counter = -1
        for i in instructions:
            if 'inp' in i:
                counter += 1
                self.instruction_sets.append([])
            self.instruction_sets[counter].append(i)
        self.next_input: int = None
    
    def __str__(self) -> str:
        return f"w={self.vars['w']} | x={self.vars['x']} | y={self.vars['y']} | z={self.vars['z']}"
    
    def execute(self, input: deque):
        assert 14 == len(self.instruction_sets)
        for iset in self.instruction_sets:
            # print(iset)
            self.vars['z'] = self.process_instruction_set(input.pop(), self.vars['z'], tuple(iset))
            # print(f"{self.vars['z']} ->", end='')
        # print()
    
    # All instruction sets start with an input into 'w' and 'x' and 'y' are cleared to 0 via mul operations so 'z' is the only carry over
    @lru_cache(maxsize=None)
    def process_instruction_set(self, input: int, z: int, instructions: list[tuple]) -> int:
        self.next_input = input
        self.vars['z'] = z # Unnecessary, but wanted to use the variable
        for i in instructions:
            self.process_instruction(i)
        return int(self.vars['z'])

    def process_instruction(self, ins: tuple):
        if ins[0] == 'inp':
            self.vars[ins[1]] = self.next_input
        elif ins[0] == 'add':
            self.vars[ins[1]] += int(ins[2]) if ins[2].lstrip('-').isdigit() else self.vars[ins[2]]
        elif ins[0] == 'mul':
            self.vars[ins[1]] *= int(ins[2]) if ins[2].lstrip('-').isdigit() else self.vars[ins[2]]
        elif ins[0] == 'div':
            self.vars[ins[1]] //= int(ins[2]) if ins[2].lstrip('-').isdigit() else self.vars[ins[2]]
        elif ins[0] == 'mod':
            self.vars[ins[1]] %= int(ins[2]) if ins[2].lstrip('-').isdigit() else self.vars[ins[2]]
        elif ins[0] == 'eql':
            self.vars[ins[1]] = int(self.vars[ins[1]] == (int(ins[2]) if ins[2].lstrip('-').isdigit() else self.vars[ins[2]]))
        else:
            raise Exception(f"'Unknown instruction: {ins[0]}")

if __name__ == '__main__':
    filename = './sample.txt' if '-s' in sys.argv else './input.txt'
    start_time = time.time()

    instructions: list[tuple] = []

    with open(filename) as f:
        instructions = list(map(tuple, [line.split() for line in f.read().splitlines()]))

    max_model_num = 0
    min_model_num = sys.maxsize
    P = ALU(instructions)
    for a,b,c,d,e,f,g,h,i,j,k,l,m,n in product(range(4,5), repeat=14):
        P.execute(deque((a,b,c,d,e,f,g,h,i,j,k,l,m,n)))
        val = int(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}")
        if P.vars['z'] == 0:
            max_model_num = max(max_model_num, val)
            min_model_num = min(min_model_num, val)
            print(f"min is now = {min_model_num} | max is now = {max_model_num}")
        else:
            print(f"Rejected: {val}")

    print(f"Part 1: {max_model_num} (took {(time.time() - start_time)}s)")
    start_time = time.time()

    print(f"Part 2: {min_model_num} (took {(time.time() - start_time)}s)")