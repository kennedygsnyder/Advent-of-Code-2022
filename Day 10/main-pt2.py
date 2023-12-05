signal = 1
queue = [0]
cycle = 1
interesting_strengths = []
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        if line.strip() == "noop":
            queue.append(0)
        else:
            num = line.split()
            queue.append(0)
            queue.append(int(num[1]))

cur_line = ""
for num in queue:
    signal += num
    
    pixel_pos = cycle % 40 - 1
    if pixel_pos in range(signal-1,signal+2):
        cur_line += "#"
    else:
        cur_line += "."

    if cycle % 40 == 0:
        print(cur_line)
        cur_line = ""
    
    cycle += 1

print(sum(interesting_strengths))
