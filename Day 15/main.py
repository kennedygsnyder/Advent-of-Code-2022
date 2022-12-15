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

y = 10
count = -1
not_beacon = False

for x in range(min_x-1500000, max_x+1500000, 1):
    for sensor in sensors:
        if manhattan_distance([x, y], [sensor[0], sensor[1]]) <= sensor[2]:
            not_beacon = True
            break
    
    if not_beacon:
        count+=1

    not_beacon = False

print(count)


