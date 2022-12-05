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

# stacks = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

# file = ['move 1 from 2 to 1\n', 'move 3 from 1 to 3\n', 'move 2 from 2 to 1\n', 'move 1 from 1 to 2\n']

for line in file:
    if line[0:4] == 'move':
        bits = line.split()
        move = int(bits[1])
        sfrom = int(bits[3])-1
        las = bits[5].split('\n')
        sto = int(las[0])-1

        val = stacks[sfrom][0:move]
        del stacks[sfrom][0:move]
        stacks[sto] = val + stacks[sto]
    else:
        continue

for i in range(len(stacks)):
    print(stacks[i][0])