file_handler = open('input.txt', 'r')
num_of_frames = -1
page_list = []

try:
    for line in file_handler:
        if line[0] == '#':
            continue
        if num_of_frames == -1:
            num_of_frames = int(line)
            continue
        if len(page_list) == 0:
            page_list = line.split(' ')
            for index, page in enumerate(page_list):
                page_list[index] = int(page)
            break
except:
    print('Invalid input')
    exit()

memory = []
memory_status = []
usage = [0 for x in range(10)]
queue = [] #Secondary factor determining which process to be swapped out
page_fault = 0
for index, page in enumerate(page_list):
    curr_mem = []
    # print(usage)
    if page in memory:
        usage[page] += 1
        for i in range(num_of_frames):
            try:
                curr_mem.append(memory[i])
            except:
                curr_mem.append(-1)
        memory_status.append(curr_mem)
        continue
    if len(memory) < num_of_frames:
        usage[page] += 1
        page_fault += 1
        memory.append(page)
        for i in range(num_of_frames):
            try:
                curr_mem.append(memory[i])
            except:
                curr_mem.append(-1)
        memory_status.append(curr_mem)
        continue
    if True:
        min_frequency = usage[memory[0]]
        for frame in memory:
            if usage[frame] < min_frequency:
                min_frequency = usage[frame]
        for i in range(0, index):
            if page_list[i] in memory and usage[page_list[i]] == min_frequency:
                memory[memory.index(page_list[i])] = page
                break
        usage[page] += 1
        page_fault += 1
        for i in range(num_of_frames):
            try:
                curr_mem.append(memory[i])
            except:
                curr_mem.append(-1)
        memory_status.append(curr_mem)
        continue

output = '{:15s}'.format('Page') + ' |'

for i in page_list:
    output += '{:2d}'.format(i) + ' |'
output += '\n'
for i in range(num_of_frames):
    output += '{:15s}'.format(f'Memory slot {i+1}:') + ' |'
    for j in range(len(page_list)):
        if (memory_status[j][i] != -1):
            output += '{:2d}'.format(memory_status[j][i]) + ' |'
        else:
            output += '{:2s}'.format('') + ' |'
    output += '\n'

print(output)
print(f'Page fault count: {page_fault}')