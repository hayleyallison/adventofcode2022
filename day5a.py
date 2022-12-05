input_data = 'inputs/input5.txt'

file = open(input_data)

stacks =    [['C', 'Q', 'B'], \
            ['Z', 'W', 'Q', 'R'], \
            ['V', 'L', 'R', 'M', 'B'], \
            ['W', 'T', 'V', 'H', 'Z', 'C'], \
            ['G', 'V', 'N', 'B', 'H', 'Z', 'D'], \
            ['Q', 'V', 'F', 'J', 'C', 'P', 'N', 'H'], \
            ['S', 'Z', 'W', 'R', 'T', 'G', 'D'], \
            ['P', 'Z', 'W', 'B', 'N', 'M', 'G', 'C'], \
            ['P', 'F', 'Q', 'W', 'M', 'B', 'J', 'N']]

for line in file:
    if line[0:4] == 'move':
        bits = line.split()
        move = int(bits[1])
        sfrom = int(bits[3])
        las = bits[5].split('\n')
        sto = int(las[0])

        for _ in range(move):
            val = stacks[sfrom-1][0]
            stacks[sfrom-1].remove(val)
            stacks[sto-1].insert(0, val)
    else:
        continue

for i in range(len(stacks)):
    print(stacks[i][0])
        