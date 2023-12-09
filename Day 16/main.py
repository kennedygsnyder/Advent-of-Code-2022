import re
nodes = {}
first_node_tunnels = []
with open('input.txt') as f:
  lines = f.readlines()
  for line in lines:
    node = line[6:8]
    flow_rate = int(re.search(r'\d+', line).group())
    tunnels = re.findall(r'([A-Z]{2})',line.split(';')[1])
    nodes[node] = [flow_rate,tunnels]

#bfs to get only nonzero nodes 
starting_nodes = []
nonzero_nodes = {}

#initialize all keys 
for start_node_name, start_node_values in nodes.items():
  if nodes[start_node_name][0] != 0:
    nonzero_nodes[start_node_name] = [start_node_values[0],[]]

for start_node_name, start_node_data in nodes.items():
  #if node has nonzero flow rate 
  if start_node_name == 'AA' or nodes[start_node_name][0] != 0:
    #BFS 
    queue = [[start_node_name, -1]]
    visited = []
    #while queue isn't empty
    while queue:
      curr_node_name, curr_distance = queue.pop(0)
      curr_distance += 1
      if curr_node_name not in visited:
        visited.append(curr_node_name)
        
        if curr_node_name != start_node_name and nodes[curr_node_name][0] != 0:
          if start_node_name == 'AA':
            starting_nodes.append([curr_node_name, curr_distance])
          else:
            nonzero_nodes[start_node_name][1].append([curr_node_name, curr_distance])
          
        for adjacent_node in nodes[curr_node_name][1]:
          queue.append([adjacent_node, curr_distance])


nodes = nonzero_nodes

def move(node, time_left, opened, score):
  if time_left <= 0 or len(opened) == len(nodes):
    return score, []
  
  max_score = -1
  max_path = []
  #open 
  if node not in opened:
    new_opened = opened[:]
    new_opened.append(node)
    score += time_left * nodes[node][0]
    time_left -= 1
    for new_node in nodes[node][1]:
      new_score, path = move(new_node[0], time_left - new_node[1], new_opened, score)
      path.insert(0, node)
      if new_score >= max_score:
        max_score = new_score
        max_path = path

  return max_score, max_path

max_score = 0
max_path = []
for node, dist in starting_nodes:
  results = move(node, 30-(dist+1), [], 0)
  if results[0] > max_score:
    max_score, max_path = results
    max_path = '->'.join(max_path)

print(f'{max_score} - {max_path}')