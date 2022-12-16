grid_size = 5000
def chebyshev(a, b):
    return (max(abs(a[0] - b[0]), abs(a[1]-b[1])))

with open('input.txt') as f:
    lines = f.readlines()
    
    grid = [['.']*(grid_size*2+1) for i in range(grid_size*2+1)]

head_pos = [grid_size,grid_size]
tail_pos = [grid_size,grid_size]

def print_grid():
    grid_copy = [row[:] for row in grid]
    grid_copy[head_pos[1]][head_pos[0]] = 'H'
    grid_copy[tail_pos[1]][tail_pos[0]] = 'T'
    grid_copy[grid_size][grid_size] = 's'

    for row in grid_copy:
        for point in row:
            print(point, end="")
        print('')

tail_spot_list = []
spot_str = str(tail_pos[0]) + ',' + str(tail_pos[1])
tail_spot_list.append(spot_str)

for line in lines:
    line = line.split()
    
    for i in range(int(line[1])):
        if (line[0] == 'U'):
            head_pos[1] -= 1
            if(chebyshev(head_pos, tail_pos) > 1):
                tail_pos[1] -= 1 
                if (head_pos[0] > tail_pos[0]):
                    tail_pos[0] += 1
                elif (head_pos[0] < tail_pos[0]):
                    tail_pos[0] -= 1

        if (line[0] == 'R'):
            head_pos[0] += 1
            if(chebyshev(head_pos, tail_pos) > 1): 
                tail_pos[0] += 1
                if (head_pos[1] > tail_pos[1]):
                    tail_pos[1] += 1
                elif (head_pos[1] < tail_pos[1]):
                    tail_pos[1] -= 1

        # DOWN
        if (line[0] == 'D'):
            head_pos[1] += 1
            if(chebyshev(head_pos, tail_pos) > 1): 
                tail_pos[1] += 1
                if (head_pos[0] > tail_pos[0]):
                    tail_pos[0] += 1
                elif (head_pos[0] < tail_pos[0]):
                    tail_pos[0] -= 1

        # LEFT
        if (line[0] == 'L'):
            head_pos[0] -= 1
            if(chebyshev(head_pos, tail_pos) > 1): 
                tail_pos[0] -= 1
                if (head_pos[1] > tail_pos[1]):
                    tail_pos[1] += 1
                elif (head_pos[1] < tail_pos[1]):
                    tail_pos[1] -= 1
        
        grid[tail_pos[1]][tail_pos[0]] = '#'
        spot_str = str(tail_pos[0]) + ',' + str(tail_pos[1])
        tail_spot_list.append(spot_str)

print('here')
print(len(set(tail_spot_list)))

#print_grid()