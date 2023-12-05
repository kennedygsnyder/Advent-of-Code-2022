trees = []
top_score = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        trees.append([int(num) for num in line.strip()])

#for each tree
for i in range(len(trees)):
    for j in range(len(trees[0])):
        distances = []
        blocked = False
        
        #left
        distance = 0
        k = j-1
        while not blocked and k >= 0:
            if trees[i][k] >= trees[i][j]:
                blocked = True
                distance += 1
            else:
                distance += 1
                k -= 1
        
        distances.append(distance)
        blocked = False

        #right
        distance = 0
        k = j+1
        while not blocked and k < len(trees[0]):
            if trees[i][k] >= trees[i][j]:
                blocked = True
                distance += 1
            else:
                distance += 1
                k += 1
        distances.append(distance)
        blocked = False

        #up
        distance = 0
        k = i-1
        while not blocked and k >= 0:
            if trees[k][j] >= trees[i][j]:
                blocked = True
                distance += 1
            else:
                distance += 1
                k -= 1
        
        distances.append(distance)
        blocked = False

        #down
        distance = 0
        k = i+1
        while not blocked and k < len(trees):
            if trees[k][j] >= trees[i][j]:
                blocked = True
                distance += 1
            else:
                distance += 1
                k += 1
        distances.append(distance)

        distance_score = 1  
        for num in distances:
            distance_score *= num
        top_score = max(top_score, distance_score)

print(top_score)