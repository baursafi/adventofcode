import time
import string

with open('input.txt') as file:
    data_in = file.readlines()


data_in = [item.replace('\n', '') for item in data_in]


priority = dict((letter, index+1) for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase))
priority

score = 0
for item in data_in:
    overlap = set(item[:len(item)//2]).intersection(set(item[len(item)//2:]))
    score += priority[list(overlap)[0]]


print('Part I score', score)

#part 2
score = 0
sub_list = []
for index, item in enumerate(data_in):
    sub_list.append(item)
    if (index + 1) % 3 == 0:
        overlap = set(sub_list[0]).intersection(sub_list[1]).intersection(sub_list[2])
        print(overlap)
        print('priority of overlap', priority[list(overlap)[0]])
        score += priority[list(overlap)[0]]
        sub_list = []   

print('Part II score', score)