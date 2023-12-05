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
            print(num)
            queue.append(0)
            queue.append(int(num[1]))

print(queue)
for num in queue:
    signal += num
    if cycle % 40 == 20:
        print(f'{cycle} {num} {signal} {cycle*signal}')
        interesting_strengths.append(cycle*signal)
    cycle += 1

print(sum(interesting_strengths))
