curr_cals = 0
cals_array = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        if line != '\n':
            curr_cals += int(line)
        else:
            cals_array.append(curr_cals)
            curr_cals = 0

cals_array.sort(reverse=True)
print(cals_array[0]+cals_array[1]+cals_array[2])