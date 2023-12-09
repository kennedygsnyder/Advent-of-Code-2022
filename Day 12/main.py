#breadth first
grid = []
with open('input.txt') as f:
  lines = f.readlines()

  for line in lines:
    grid_row = []
    for char in line.strip():
      if char == "S":
        grid_row.append(1)
      elif char == "E":
        grid_row.append(27)
      else:
        grid_row.append(ord(char)-96)

    grid.append(grid_row)

start = [20,0]
end = [20,88]
queue = [[start,[start]]]
visited = []
min = 1000

while queue:
  vertex, path = queue.pop(0)
  row = vertex[0]
  col = vertex[1]

  adjacent = []
  #above
  if row > 0 and grid[row-1][col]-grid[row][col] < 2:
    adjacent.append([row-1, col])
  #below
  if row < len(grid)-1 and grid[row+1][col]-grid[row][col] < 2:
    adjacent.append([row+1, col])
  #left
  if col > 0 and grid[row][col-1]-grid[row][col] < 2:
    adjacent.append([row,col-1])
  #right
  if col < len(grid[0])-1 and grid[row][col+1]-grid[row][col] < 2:
    adjacent.append([row,col+1])

  for node in adjacent:
    if grid[row][col] == 27:
      if len(path)-1 < min:
        min = len(path)-1
    else:
      if node not in visited:
        visited.append(node)
        queue.append((node, path + [node]))

print(min)