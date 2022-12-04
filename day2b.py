input_data = 'inputs/input2.txt'
file = open(input_data)

oppon = []
outcome   = []

for fline in file:
    line = fline.split('\n')

    game = line[0].split()
    oppon.append(game[0])
    outcome.append(game[1])

score = 0

symbol_score = {'A': 1, 'B': 2, 'C': 3}
winlist = {'A': 'B', 'B': 'C', 'C': 'A'}
loselist  = {'A': 'C', 'B': 'A', 'C': 'B'}

for i in range(len(oppon)):
    if outcome[i] == 'X':
        # lose
        score += symbol_score[loselist[oppon[i]]]
    elif outcome[i] == 'Z':
        # win
        score += symbol_score[winlist[oppon[i]]]
        score += 6
    else:
        #draw
        score += 3
        score += symbol_score[oppon[i]]
        
print(score)