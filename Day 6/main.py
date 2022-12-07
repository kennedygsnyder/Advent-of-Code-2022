crates_dict = {}
instructions = []

with open('input.txt') as f:
    lines = f.readlines()
    crates_matrix = []

    for i in range(len(lines)):
        if '[' in lines[i]:
            line = lines[i]
            crates_matrix.append([line[i:i+3] for i in range(0, len(line), 4)])
        
        elif 'from' in lines[i]:
            line = lines[i].split()
            instructions.append([int(line[1]), int(line[3]), int(line[5])])

    for i in range(len(crates_matrix[0])):
        crates_dict[i+1] = []

    for i in range(len(crates_matrix)-1, -1, -1):
        for j in range(0, len(crates_matrix[i])):
            if crates_matrix[i][j] != '   ':
                crates_dict[j+1].append(crates_matrix[i][j][1])

for i in range(len(instructions)):
    num_to_move, from_stack, to_stack = instructions[i]
    crates_dict[to_stack].extend(crates_dict[from_stack][-(num_to_move):])
    crates_dict[from_stack] = crates_dict[from_stack][0:-num_to_move]

for i in range(1, len(crates_matrix)+2):
    print(crates_dict[i])