input_data = 'inputs/input1.txt'

file = open(input_data)

data = [[]]
i = 0

for fline in file:
    line = fline.split('\n')
    if len(line[0]) > 0:
        data[i].append(int(line[0]))
    else:
        data.append([])
        i += 1

maxC = 0
for j in range(len(data)):
    elfTotal = sum(data[j])
    if elfTotal > maxC:
        maxC = elfTotal

print(maxC)