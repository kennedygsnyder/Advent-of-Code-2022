sum = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for char in firstpart:
            if char in secondpart:
                num = ord(char)-96
                if num < 0: num+=58
                sum+=num
                break

print(sum)
