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
page_fault = 0
for index, page in enumerate(page_list):
    curr_mem = []
    # The required page is already in memory
    if page in memory:
        for frame in memory:
            if frame == None:
                curr_mem.append(-1)
                continue
            curr_mem.append(frame)
        memory_status.append(curr_mem)
        continue
    # The required page is missing => swap in
    if len(memory) < num_of_frames:
        memory.append(page)
        page_fault += 1
        for i in range(num_of_frames):
            try:
                curr_mem.append(memory[i])
            except:
                curr_mem.append(-1)
        memory_status.append(curr_mem)
        continue
    # The required page is missing => swap out => swap in
    if True:
        swapping_index = -1
        for i in range(index, 0, -1):
            if page_list[i] in memory:
                swapping_index = memory.index(page_list[i])
                break
        memory[swapping_index] = page
        page_fault += 1
        for frame in memory:
            if frame == None:
                curr_mem.append(-1)
                continue
            curr_mem.append(frame)
        memory_status.append(curr_mem)

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