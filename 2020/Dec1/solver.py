with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [eval(x) for x in lines]

# task 1
for indexi, i in enumerate(lines):
    for indexj, j in enumerate(lines[indexi:]):
        if i + j == 2020:
            print(i, j, i * j)

# task 2
for indexi, i in enumerate(lines):
    for indexj, j in enumerate(lines[indexi:]):
        for indexz, z in enumerate(lines[indexj:]):
            if i + j + z == 2020:
                print(i, j, z, i * j * z)
