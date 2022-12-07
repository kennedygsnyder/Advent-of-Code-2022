max_cals = 0
curr_cals = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        if line != '\n':
            curr_cals += int(line)
        else:
            if curr_cals > max_cals:
                max_cals = curr_cals
            curr_cals = 0

print(max_cals)