def dataRoute(resource, server, network):
  # Create graph
  flow = {}
  backwards = {}
  N = len(network)
  for i in range(N):
    for j in range(N):
      v = network[i][j]
      if v > 0:
        if i not in flow:
          flow[i] = {}
        if j not in flow[i]:
          flow[i][j] = 0

        if j not in backwards:
          backwards[j] = []
        backwards[j].append(i)
  
  def get_path(flow, backwards, network, start, end):
    forward_res = {}
    backward_res = {}
    for i in flow.keys():
      forward_res[i] = {}
      for j in flow[i].keys():
        cap = network[i][j]
        f = flow[i][j]
        forward_res[i][j] = cap - f
        if j not in backward_res.keys():
          backward_res[j] = {}
        backward_res[j][i] = f
    
    explored = set()
    path = [start]
    values = []
    direction = []
    while len(path) > 0 and path[-1] != end:
      current = path[-1]
      if current in forward_res.keys():
        for possible in forward_res[current].keys():
          t = forward_res[current][possible]
          if t > 0 and (current, possible, 1) not in explored and (possible not in path):
            direction.append(1)
            path.append(possible)
            values.append(t)
            explored.add((current, possible, 1))
            break
      if path[-1] == current and current in backward_res.keys():
        for possible in backward_res[current].keys():
          t = backward_res[current][possible] 
          if t > 0 and (current, possible, -1) not in explored and (possible not in path):
            direction.append(-1)
            path.append(possible)
            values.append(t)
            explored.add((current, possible, -1))
            break
      if current == path[-1]:
        path.pop()
        if len(values) > 0:
          values.pop() 
        if len(direction) > 0:
          direction.pop() 
    if len(path) > 0:
      return path, min(values), direction
    else:
      return [], 0, []

  
  i = 0
  found_path, f, direction = get_path(flow, backwards, network, resource, server)
  while len(found_path) > 0:
    print(i, " : ", found_path, direction )
    prev = resource
    for i, p in enumerate(found_path):
      if i > 0:
        if direction[i-1] == 1:
          flow[prev][p] += f
        else:
          flow[p][prev] -= f


      prev = p
    found_path, f, direction = get_path(flow, backwards, network, resource, server)
  return sum(flow[resource].values()) if resource in flow.keys() else 0


a = [[0,   2, 4, 8, 0,  0],
     [0,   0, 0, 9, 0,  0],
     [0,   0, 0, 0, 0, 10],
     [0,   0, 6, 0, 0, 10],
     [10, 10, 0, 0, 0,  0],
     [0,   0, 0, 0, 0,  0]]
#print(dataRoute(4, 5, a))

def generate(size):
  import random
  result = []
  for i in range(size):
    row = []
    for j in range(size):
      if i==j:
        row.append(0)
      else:
        row.append(random.randint(0, 10**5))
    result.append(row)
  return result

b = generate(15)
print(dataRoute(0, 1, b))
#print(b)
#c = [[0, 50320, 22203, 65612], [33307, 0, 94119, 57351], [38259, 59391, 0, 81350], [21380, 96005, 28131, 0]]
#print(dataRoute(0, 1, c))