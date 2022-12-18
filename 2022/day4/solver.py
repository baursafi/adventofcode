import time
import string

with open('input.txt') as file:
    data_in = file.readlines()
data_in = [[i.split("-") for i in (item.replace('\n', '')).split(",")] for item in data_in]

counter = 0
for pair in data_in:
    # print(eval(pair[0][0]))
    # print(eval(pair[0][1]))
    workload1 = range(eval(pair[0][0]),eval(pair[0][1])+1)
    workload2 = range(eval(pair[1][0]),eval(pair[1][1])+1)
    overlap1 = set(workload1).intersection(set(workload2))
    overlap2 = set(workload2).intersection(set(workload1))
    if len(overlap1) == len(workload2) or len(overlap2) == len(workload1):
        counter +=1


counter

# part II

counter = 0
for pair in data_in:
    # print(eval(pair[0][0]))
    # print(eval(pair[0][1]))
    workload1 = range(eval(pair[0][0]),eval(pair[0][1])+1)
    workload2 = range(eval(pair[1][0]),eval(pair[1][1])+1)
    overlap1 = set(workload1).intersection(set(workload2))
    overlap2 = set(workload2).intersection(set(workload1))
    if len(overlap1) > 0 or len(overlap2) > 0:
        counter +=1


counter