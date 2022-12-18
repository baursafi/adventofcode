import re

with open('input.txt') as file:
    data_in = file.readlines()

stack = []
for i in range(8):
    stack.append(data_in[i])

stack = [line.replace('\n',' ') for line in stack]

stack = [[stack[j][i*4+1:i*4+2].replace(' ', '') for i in range(9)] for j in range( 7,-1,-1)]

# convert list of rows into the list of columns
new_stack = []
for i in range(9):
    new_line = []
    for line in stack:
        if line[i] == '':
            break
        else:
            new_line.append(line[i])
    new_stack.append(new_line)


new_stack

actions = [[eval(i) for i in re.findall('\d+', line)] for line in data_in[10:]]
actions[0]

for action in actions:
    count_containers = action[0]
    print(count_containers)
    origin_stack = new_stack[action[1]-1]
    print(origin_stack)
    destination_stack = new_stack[action[2]-1]
    print(destination_stack)
    moving_containers = origin_stack[len(origin_stack) - action[0]:]
    #update origin stack
    new_stack[action[1]-1] = new_stack[action[1]-1][:len(origin_stack) - len(moving_containers)]
    moving_containers.reverse()
    #update destination stack
    new_stack[action[2] - 1].extend(moving_containers)

print('Final top containers are:', 
''.join([stack[-1] for stack in new_stack]))


# part ii 
# all the same but without the revering the moving containers
new_stack = []
for i in range(9):
    new_line = []
    for line in stack:
        if line[i] == '':
            break
        else:
            new_line.append(line[i])
    new_stack.append(new_line)


new_stack

actions = [[eval(i) for i in re.findall('\d+', line)] for line in data_in[10:]]
actions[0]

for action in actions:
    count_containers = action[0]
    print(count_containers)
    origin_stack = new_stack[action[1]-1]
    print(origin_stack)
    destination_stack = new_stack[action[2]-1]
    print(destination_stack)
    moving_containers = origin_stack[len(origin_stack) - action[0]:]
    #update origin stack
    new_stack[action[1]-1] = new_stack[action[1]-1][:len(origin_stack) - len(moving_containers)]
    # moving_containers.reverse()
    #update destination stack
    new_stack[action[2] - 1].extend(moving_containers)

print('Final top containers are:', 
''.join([stack[-1] for stack in new_stack]))

