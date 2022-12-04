input_data = 'inputs/input4.txt'

file = open(input_data)
fullyContains = 0

for fline in file:
    line = fline.split('\n')
    line = line[0].split(',')
    elf1 = line[0].split('-')
    elf2 = line[1].split('-')
    
    if ((int(elf1[0]) <= int(elf2[0])) and (int(elf1[1]) >= int(elf2[1]))) or ((int(elf2[0]) <= int(elf1[0])) and (int(elf2[1]) >= int(elf1[1]))):
        fullyContains += 1

print(fullyContains)
