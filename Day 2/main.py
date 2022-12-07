score = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if (line[2] == 'X'):
            if(line[0] =='A'):
                score += 3
            elif (line[0] == 'B'):
                score += 1
            elif (line[0] == 'C'):
                score += 2
        
        elif (line[2] == 'Y'):
            score += 3
            if(line[0] =='A'):
                score += 1
            elif (line[0] == 'B'):
                score += 2
            elif (line[0] == 'C'):
                score += 3

        elif (line[2] == 'Z'):
            score += 6
            if(line[0] =='A'):
                score += 2
            elif (line[0] == 'B'):
                score += 3  
            elif (line[0] == 'C'):
                score += 1

print(score)