import re
import time
import pandas as pd

with open('input.txt') as file:
    data_in = file.readlines()

data_in = [line.replace('\n', '') for line in data_in]

def join_(x):
    return ', '.join(list(x))

path = []
files = {}
df = pd.DataFrame()
counter = 0
for line in data_in:
    if "$ cd" in line and ".." not in line:
        path.append(line.split(" ")[-1])
    if "$ cd .." in line:
        path = path[:-1]
    if "dir" in line or "ls" in line:
        continue
    if len(re.findall("\d+", line)) > 0:
        row = pd.DataFrame([path])
        row['name'] = line.split(" ")[-1]
        row['size'] = eval(re.findall("\d+", line)[0])
        row['counter'] = counter
        counter += 1
        df = pd.concat([df, row],)


folders = pd.DataFrame()
for i in range(9):
    columns = [i for i in range(i+1)]
    gb = df.groupby(columns).agg({'size':'sum', 'name':[join_, 'count']}).reset_index()
    folders = pd.concat([folders,gb[gb[('size', 'sum')] <= 100000]], ignore_index=True)

folders.sort_values(by=[0,1,2,3,4,5,6,7,8], inplace = True)

folders['size'].sum()