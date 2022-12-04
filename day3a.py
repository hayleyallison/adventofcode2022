
letterscore = {chr(i+96):i for i in range(1,27)}
for i in range(1,27):
    letterscore[chr(i+64)] = 26 + i

input_data = 'inputs/input3.txt'

file = open(input_data)

priority = 0

for fline in file:
    line = fline.split('\n')
    rucksack = str(line[0])

    hlaf = int(len(rucksack)/2)
    
    frontr = str(rucksack[0:hlaf])
    backr  = str(rucksack[hlaf:])
    for letter in frontr:
        if letter in backr:
            priority += letterscore[letter]
            break
print(priority)