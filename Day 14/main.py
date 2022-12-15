with open("input.txt") as f:
    lines = f.readlines()

    x_arr = []
    y_arr = []
    map = []
    min_x = 2**12
    min_y = 2**12
    max_x = 0
    max_y = 0

    for line in lines:
        line = line.replace('\n','').split(' -> ')

        # find minmax x, y values
        for i in range(len(line)):
            coord = line[i].split(',')
            coord = [int(i) for i in coord]
            min_x = min(coord[0], min_x)
            min_x = min(coord[0], min_x)
            max_x = max(coord[0], max_x)
            min_y = min(coord[1], min_y)
            max_y = max(coord[1], max_y)

    x_width = max_x-min_x+1
    y_height = max_y-min_y+1

    map = [ ['.']*(x_width+1000) for i in range(max_y+2)]
    map.append(['#']*(x_width+1000))

    # process rock
    for line in lines:
        instructions = []
        instrs = line.replace('\n','').split(' -> ')
        for i in instrs:
            i = i.split(',')
            instructions.append([int(i[0])-min_x+500, int(i[1])])
        
        for i in range(len(instructions)-1):
            curr_x = instructions[i][0]
            curr_y = instructions[i][1]
            next_x = instructions[i+1][0]
            next_y = instructions[i+1][1]

            if (curr_y == next_y):
                increment = 1
                if curr_x > next_x:
                    increment = -1
                for x in range(curr_x, next_x+increment, increment):
                    map[curr_y][x] = '#'
            if (curr_x == next_x):
                increment = 1
                if curr_y > next_y:
                    increment = -1
                for y in range(curr_y, next_y+increment, increment):
                    map[y][curr_x] = '#'
                
    print('\n')
    for m in map:
        for n in m:
            print(n, end="")
        print('\n', end="")

    # Process Sand
    curr_sand_x = 500-min_x+500
    curr_sand_y = 0
    end = False
    num_sand_grains = 0

    while (not end):
        if map[0][500-min_x+500] == 'o':
            end = True
        
        elif (map[curr_sand_y+1][curr_sand_x] not in ['#','o']):
            curr_sand_y += 1
        
        elif ((curr_sand_y + 1 < len(map)) and (curr_sand_x -1 >= 0) and map[curr_sand_y+1][curr_sand_x-1] not in ['#','o']):
            curr_sand_y += 1
            curr_sand_x -= 1
        
        elif ((curr_sand_y + 1 < len(map)) and(curr_sand_x + 1 < len(map[0])) and map[curr_sand_y+1][curr_sand_x+1] not in ['#','o']):
            curr_sand_y += 1
            curr_sand_x += 1
        
        else:
            map[curr_sand_y][curr_sand_x] = 'o'
            curr_sand_x = 500-min_x+500
            curr_sand_y = 0   
            num_sand_grains += 1 

print('\n')
for m in map:
    for n in m:
        print(n, end="")
    print('\n', end="")

print(num_sand_grains)
        