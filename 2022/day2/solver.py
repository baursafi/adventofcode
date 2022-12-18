import time
with open('input.txt') as file:
    data_in = file.readlines()

# A - rock
# B - paper
# C - scissors
# X - rock
# Y - paper
# Z - scissors
# rock beats scizzors - C X
# paper beats rock - A Y
# scissors beat paper - Z B

data_in = [i.replace('\n', '') for i in data_in]

score = 0
for game in data_in:
    print(game)
    if 'X' in  game:
        score += 1
    elif 'Y' in game:
        score += 2
    elif 'Z' in game:
        score += 3
    else: 
        score += 0
    print(score, 'for your choice')
    if game in ['C X', 'A Y', 'B Z']:
        score += 6
    elif game in ['C Z', 'B Y', 'A X']:
        score += 3
    else:
        score += 0
    print('result of this game', score)
    # time.sleep(5)
print('Task 1', score)

score = 0
for game in data_in:
    if "Y" in game:
        score += 3
        if 'A' in game:
            score += 1
        elif 'B' in game:
            score += 2
        elif 'C' in game:
            score += 3 
    elif 'Z' in game:
        score += 6
        if 'A' in game:
            score += 2
        elif 'B' in game:
            score += 3
        elif 'C' in game:
            score += 1
    elif 'X' in game:
        score += 0
        if 'A' in game:
            score += 3
        elif 'B' in game:
            score += 1
        elif 'C' in game:
            score += 2
    score