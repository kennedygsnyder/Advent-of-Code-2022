directories = {}
curr_directory = ['/']

def get_dir_sum(dir):
    sum = directories[dir]
    for j in directories_list:
        if dir in j and dir != j:
            sum += directories[j]

    return sum

with open('input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if '$ cd' in line:
            if (line[5:-1]) == '..':
                curr_directory.pop()
            elif (line[5:-1]) == '/':
                curr_directory = ['/']
            else:
                curr_directory.append(line[5:-1])

        elif '$ ls' in line:
            string_dir_name = '/'.join(curr_directory)
            directories[string_dir_name] = 0
            i+=1
            while i < len(lines) and '$' not in lines[i]:
                if 'dir' not in lines[i]:
                    line = lines[i].split()
                    directories[string_dir_name] += int(line[0])
                i+=1

    directories_list = directories.keys()
    full_sum = 0
    sum = 0
    for i in directories_list:
        sum = get_dir_sum(i)

        if sum <= 100000:
            full_sum += sum

    print(full_sum)

   # PART TWO
    free_space = 70000000 - get_dir_sum('/')
    
    min_dir_size = 70000000

    for i in directories_list:
        sum = get_dir_sum(i)

        if sum + free_space > 30000000:
            min_dir_size = min(sum, min_dir_size)

    print(min_dir_size)
