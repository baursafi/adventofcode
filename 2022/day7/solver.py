import re
import time
import pandas as pd

with open('input.txt') as file:
    data_in = file.readlines()

data_in = [line.replace('\n', '') for line in data_in]


from anytree import Node, RenderTree, AsciiStyle
from tqdm import tqdm

break_time = 0

root = None
for i in tqdm(data_in):
    if "$ cd" in i and ".." not in i:
        print(i)
        folder_name = i.split(' ')[-1]
        print("move to folder ", folder_name)
        child = Node(name=folder_name, parent=root)
        grandparent = root
        root = folder_name
        time.sleep(break_time)
        continue
    elif "$ ls" in i:
        print(i)
        print('List items')
        continue
    if "dir" in i:
        print(i)
        folder_name = i.split(" ")[-1]
        print('folder', folder_name)
        print('parent', root)
        child = Node(name=folder_name, parent=root)
        time.sleep(break_time)
        continue
    if len(re.findall("\d+",i)) > 0:
        filesize = eval(re.findall("\d+",i)[0])
        folder_name = i.split(" ")[-1]
        child = Node(name=folder_name, parent=root, size = filesize) 
        print('file size', filesize)
        time.sleep(break_time)
    if  i == "$ cd ..":
        print(i)
        print('go up one level')
        root = grandparent




files = pd.DataFrame()
i = 0
while i < len(data_in):
    line = data_in[i]
    if '$ cd' in line and '..' not in line:
        