import re
import time
import pandas as pd

with open('input.txt') as file:
    data_in = file.readlines()

data_in = [line.replace('\n', '') for line in data_in]

def join_(x):
    return ', '.join(list(x))

# instantiate path to each file
path = []
# formalize each file into a dataframe with folder names in each column at tier levels
df = pd.DataFrame()
# counter zero to count for the individual files
counter = 0
for line in data_in:
    if "$ cd" in line and ".." not in line:
        path.append(line.split(" ")[-1])
    if "$ cd .." in line:
        path = path[:-1]
    if len(re.findall("\d+", line)) > 0:
        row = pd.DataFrame([path])
        row['name'] = line.split(" ")[-1]
        row['size'] = eval(re.findall("\d+", line)[0])
        row['counter'] = counter
        counter += 1
        df = pd.concat([df, row],)
    if "dir " in line or "$ ls" in line:
        continue

# limit is a shape of the next for-loop
limit = df.shape[1] - 4

# instantiate folder by group by each set of folders that has <= 100,000 units in size
folders = pd.DataFrame()
for i in range(limit,0,-1):
    columns = [i for i in range(i+1)]
    gb = df.groupby(columns).agg({'size':'sum', 'name':[join_, 'count']}).reset_index()
    folders = pd.concat([folders,gb[gb[('size', 'sum')] <= 100000]], ignore_index=True)

print('Size of folders <= 100K units in size: ', folders['size'].sum())


# part II
# find the smallest directory that, if deleted, would free up enough space on the system
# what's the size of such directory
space_to_full = 70000000 - df['size'].sum()
needs_to_free = 30000000 - space_to_full

folders = pd.DataFrame()
for i in range(limit,0,-1):
    columns = [i for i in range(i+1)]
    gb = df.groupby(columns).agg({'size':'sum', 'name':[join_, 'count']}).reset_index()
    folders = pd.concat([folders,gb], ignore_index=True)

# folders.to_csv('folders.cvs')
minimum_folder_size = folders[folders[('size','sum')] > needs_to_free].sort_values(by=('size','sum')).head(1)[('size', 'sum')].values[0]
print('Minimum folder size is:', minimum_folder_size)
