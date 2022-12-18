import time
with open('input.txt') as file:
    data_in = file.readlines()

type(data_in)

data_in = [i.replace('\n','') for i in data_in]

max_cals = []
elf_cals = 0
elf_counter = 1
for item in data_in:
    if item == '':
        max_cals.append(elf_cals)
        elf_cals = 0
        elf_counter += 1
    else:
        elf_cals += eval(item)
    print('elf #', elf_counter)
    print('item cal', item)
    print('elf_cal', elf_cals)
    print('max_cals', max_cals)
    # time.sleep(.3)

max_cals.append(elf_cals)

print(max_cals)
max(max_cals)
max_cals.sort(reverse=True)
sum(max_cals[:3])