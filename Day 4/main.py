import re
count = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = re.split(',|-', line.strip('\n'))
        line = [int(x) for x in line]

        if line[0] <= line[2] and line[1] >= line[3]:
            count+=1
        elif line[0] >= line[2] and line[1] <= line[3]:
            count +=1
        
print(count)
        