import re
nodes = {}
first_node_tunnels = []
seconds = 26

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

def move(nodes_list, node, time_left, opened, score, path, benchmark=0):
  if time_left <= 0 or len(opened) == len(nodes):
    return_path = [path, score] if score >= benchmark else []
    return score, path, return_path

  max_score = -1
  max_path = []
  valid_paths = [path, score] if score >= benchmark else []

  #open 
  if node not in opened:
    new_opened = opened[:]
    new_opened.append(node)
    score += time_left * nodes_list[node][0]
    time_left -= 1
    for new_node in nodes_list[node][1]:
      new_path = path + [new_node[0]]
      new_score, new_path, new_valid_paths = move(nodes_list, new_node[0], time_left - new_node[1], new_opened, score, new_path, benchmark)
      valid_paths += new_valid_paths
      valid_paths += [path, score] if score >= benchmark else []
      if new_score >= max_score:
        max_score = new_score
        max_path = new_path

  return max_score, max_path, valid_paths

max_score = 0
max_path = []
for node, dist in starting_nodes:
  results = move(nodes, node, seconds-(dist+1), [], 0, ['AA', node])
  if results[0] > max_score:
    max_score, max_path, valid_paths = results
    max_path = max_path[:-1]

#get best elephant path given best human path
elephant_nodes = {}
for key, value in nodes.items():
  if key not in max_path:
    node_tunnels = [tunnel for tunnel in value[1] if tunnel[0] not in max_path]
    elephant_nodes[key] = [value[0], node_tunnels]

elephant_starting_nodes = [node for node in starting_nodes if node[0] not in max_path]

max_score = 0
for node, dist in elephant_starting_nodes:
  results = move(elephant_nodes, node, seconds-(dist+1), [], 0, ['AA', node])
  if results[0] > max_score:
    max_score, max_path, valid_paths = results
    max_path = max_path[:-1]

benchmark = max_score

#get all paths that beat the best elephant path
max_score = 0
all_valid_paths = []
for node, dist in starting_nodes:
  results = move(nodes, node, seconds-(dist+1), [], 0, ['AA', node], benchmark)
  max_score, max_path, valid_paths = results
  all_valid_paths += valid_paths

max_score = 0
all_valid_path_sets = []
all_valid_path_top_scores = {}
for i in range(0, len(all_valid_paths),2):
  path = all_valid_paths[i]
  score = all_valid_paths[i+1]

  path_set = frozenset(path)
  if path_set not in all_valid_path_sets:
    all_valid_path_sets.append(path_set)
    all_valid_path_top_scores[path_set] = score
  else:
    if score > all_valid_path_top_scores[path_set]:
      all_valid_path_top_scores[path_set] = score
  
for i in range(0,len(all_valid_path_sets)):
  print(f'{i+1}/{len(all_valid_path_sets)}')
  path = list(all_valid_path_sets[i])
  score = all_valid_path_top_scores[all_valid_path_sets[i]]
  elephant_nodes = {}
  for key, value in nodes.items():
    if key not in path:
      node_tunnels = [tunnel for tunnel in value[1] if tunnel[0] not in path]
      elephant_nodes[key] = [value[0], node_tunnels]

  elephant_starting_nodes = [node for node in starting_nodes if node[0] not in path]

  for node, dist in elephant_starting_nodes:
    results = move(elephant_nodes, node, seconds-(dist+1), [], 0, ['AA', node])
    returned_paths = results[2]
    for i in range(0, len(returned_paths),2):
      returned_path = returned_paths[i]
      returned_score = returned_paths[i+1]
      if returned_score + score > max_score:
        max_score = returned_score + score

print(max_score)