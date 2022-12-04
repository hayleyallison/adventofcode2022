letterscore = {chr(i+96):i for i in range(1,27)}
for i in range(1,27):
    letterscore[chr(i+64)] = 26 + i

input_data = 'inputs/input3.txt'

file = open(input_data)

priority = 0
rucksack = []

for fline in file:
    line = fline.split('\n')
    rucksack.append(str(line[0]))

for elf in range(0,int(len(rucksack)/3)):
    bag1 = rucksack[elf*3]
    bag2 = rucksack[(elf*3) + 1]
    bag3 = rucksack[(elf*3) + 2]

    for item in bag1:
        if (item in bag2) and (item in bag3):
            priority += letterscore[item]
            break

print(priority)