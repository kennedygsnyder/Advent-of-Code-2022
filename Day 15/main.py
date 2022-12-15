import re
with open("input.txt") as f:
    lines = f.readlines()

def manhattan_distance(point_a, point_b):
    ax, ay = point_a
    bx, by = point_b
    return abs(bx - ax) + abs(by - ay)

sensors = []
min_x = 2**32
max_x = -2**32

for line in lines:
    data = [int(i) for i in re.findall(r"-?\d+", line)]
    
    min_x = min(min_x, data[0], data[2])
    max_x = max(max_x, data[0], data[2])

    sensor_position = [data[0], data[1]]
    beacon_position = [data[2], data[3]]
    
    sensor_position.append(manhattan_distance(sensor_position, beacon_position))
    sensors.append(sensor_position)

y = 2000000
count = -1
not_beacon = False

# Part 1
"""for x in range(min_x-1500000, max_x+1500000, 1):
    for sensor in sensors:
        if manhattan_distance([x, y], [sensor[0], sensor[1]]) <= sensor[2]:
            not_beacon = True
            break
    
    if not_beacon:
        count+=1

    not_beacon = False

print(count)"""


# Part 2
#walk around perimeter of every sensor to get all possible points
points = []
count = 1

for sensor in sensors:
    print(str(count) + '/33')
    x, y, dist = sensor

    # starting point on top of diamond
    point_a = [x, y-dist-1]
    #rightmost point of diamond
    point_b = [x + dist + 1, y]
    #bottommost point of diamond
    point_c = [x, y + dist + 1]
    #leftmost point
    point_d = [x - dist - 1, y]

    curr_point = point_a
    # top right edge
    while curr_point[0] < point_b[0] and curr_point[1] < point_b[1]:
        points.append([curr_point[0], curr_point[1]])
        curr_point[0] += 1
        curr_point[1] += 1

    #bottom right edge
    while curr_point[0] > point_c[0] and curr_point[1] < point_c[1]:
        points.append([curr_point[0], curr_point[1]])
        curr_point[0] -= 1
        curr_point[1] += 1

    #bottom left edge
    while curr_point[0] > point_d[0] and curr_point[1] > point_d[1]:
        points.append([curr_point[0], curr_point[1]])
        curr_point[0] -= 1
        curr_point[1] -= 1

    #top left edge
    while curr_point[0] < point_a[0] and curr_point[1] > point_a[1]:
        points.append([curr_point[0], curr_point[1]])
        curr_point[0] += 1
        curr_point[1] -= 1

    points.append([curr_point[0], curr_point[1]])

    count+=1

not_beacon = False
for point in points:
    if point[0] < 4000000 and point[0] > 0 and point[1] < 4000000 and point[1] > 0:
        for sensor in sensors:
            if manhattan_distance([point[0], point[1]], [sensor[0], sensor[1]]) <= sensor[2]:
                not_beacon = True
                break
    
        if not not_beacon:
            print(point[0]*4000000+point[1])
            break

    not_beacon = False

