input_data = 'inputs/input2.txt'
file = open(input_data)

oppon = []
you   = []

for fline in file:
    line = fline.split('\n')

    game = line[0].split()
    oppon.append(game[0])
    you.append(game[1])

score = 0

symbol_score = {'X': 1, 'Y': 2, 'Z': 3}
winsymbol = {'X': 'C', 'Y': 'A', 'Z': 'B'}
drawsymbol = {'X': 'A', 'Y': 'B', 'Z': 'C'}


for i in range(len(you)):
    score += symbol_score[you[i]]
    if oppon[i] == drawsymbol[you[i]]:
        # draw
        score += 3
    elif oppon[i] == winsymbol[you[i]]:
        # win
        score += 6

print(score)