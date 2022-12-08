sum = 0
with open('input.txt') as f:
    lines = f.readlines()

    for i in range(0,len(lines), 3):
        for char in lines[i]:
            if char in lines[i+1] and char in lines[i+2]:
                num = ord(char)-96
                if num < 0: num+=58
                sum+=num
                break

print(sum)
