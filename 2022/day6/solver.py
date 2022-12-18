
with open('input.txt') as file:
    data_in = file.readlines()
data_in = data_in[0]
for index in range(len(data_in)):
    if len(data_in[index:index+4]) == len(set(data_in[index:index+4])):
        print('First marker position is:', index+4)
        break

for index in range(len(data_in)):
    if len(data_in[index:index+14]) == len(set(data_in[index:index+14])):
        print('First marker position is:', index+14)
        break
