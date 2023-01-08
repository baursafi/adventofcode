import re
import time
import pandas as pd
import numpy as np

with open('input.txt') as file:
    data_in = file.readlines()

data_in = [line.replace('\n', '') for line in data_in]

df = np.array([[eval(tree) for tree in line] for line in data_in])

counter = 2*df.shape[0] + 2*df.shape[1] - 4
for i in range(1, df.shape[0]-1):
    for j in range(1, df.shape[1]-1): 
        print(i, j)
        if df[i, j] > df[:i, j].max() or df[i, j] > df[i+1:, j].max() or df[i, j] > df[i, :j].max() or df[i, j] > df[i, j+1:].max():
            counter +=1
            print(counter)
