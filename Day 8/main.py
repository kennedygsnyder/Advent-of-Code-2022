trees = []
visible_count = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        trees.append([int(num) for num in line.strip()])

print(trees)
visible_count += 2*len(trees[0]) + 2*(len(trees)-2)

#for each tree
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[0])-1):
        visibilities = []
        
        #left
        visibility = True
        for k in range(j):
            if trees[i][k] >= trees[i][j]:
                visibility = False
        visibilities.append(visibility)

        #right
        visibility = True
        for k in range(j+1,len(trees[0])):
            if trees[i][k] >= trees[i][j]:
                visibility = False
        visibilities.append(visibility)

        #top
        visibility = True
        for k in range(i):
            if trees[k][j] >= trees[i][j]:
                visibility = False
        visibilities.append(visibility)

        #top
        visibility = True
        for k in range(i+1,len(trees)):
            if trees[k][j] >= trees[i][j]:
                visibility = False
        visibilities.append(visibility)

        if any(visibilities):
            visible_count += 1

print(visible_count)