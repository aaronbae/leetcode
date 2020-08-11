def computerNetwork(n, network):
  graph = {}
  for r in network:
    s, e, v = r
    if s not in graph:
      graph[s] = {}
    if e not in graph:
      graph[e] = {}  
    graph[s][e] = v  
    graph[e][s] = v
    
  dead = set()
  distance = [10000 for _ in range(n)]
  distance[0] = 0
  frontier = {1:0}
  while len(frontier.keys()) >  0:
    current_distance, current = sorted([(frontier[k], k) for k in frontier.keys()])[0]
    frontier.pop(current)
    dead.add(current)
    if current in graph:
      for neighbor in graph[current].keys():
        if neighbor not in dead:
          distance[neighbor - 1] = min(distance[neighbor - 1], current_distance + graph[current][neighbor])
          frontier[neighbor] = distance[neighbor - 1]
  return distance[-1]

a = [[1, 4, 200], 
    [1, 2, 5], 
    [1, 3, 10], 
    [2, 3, 4], 
    [2, 4, 150], 
    [3, 4, 100]]
b = [[4,5,9589], 
 [4,1,7217], 
 [4,3,8765], 
 [2,4,247], 
 [2,1,2430], 
 [3,1,10], 
 [3,5,7650],
 [3,3,1]]
#print(computerNetwork(4, a))
#print(computerNetwork(5, b))

def generate(n, edges):
  import random
  MAX_VAL = 10
  result = {}
  all_edges = set()
  prev = 1
  while prev != n:
    if prev not in result:
      result[prev] = {}
    a = random.randint(1, n)
    while a == prev:
      a = random.randint(1, n)
    v = random.randint(1, MAX_VAL)
    result[prev][a] = v
    if a not in result:
      result[a] = {}
    result[a][prev] = v
    
    all_edges.add((min(prev, a), max(prev,a)))
    prev = a
  
  while len(all_edges) < edges:
    a = random.randint(1,n)
    b = random.randint(1,n)
    while a == b or ((min(a, b), max(a,b)) in all_edges):
      a = random.randint(1,n)
      b = random.randint(1, n)
    v = random.randint(1, MAX_VAL)
    if a not in result:
      result[a] = {}
    if b not in result:
      result[b] = {}
    result[a][b] = v
    result[b][a] = v
    all_edges.add((min(a, b), max(a,b)))

  final_result = set()
  for s in result.keys():
    for e in result[s].keys():
      final_result.add((min(s, e), max(s,e), result[s][e]))
  return [[a,b,c] for a,b,c in final_result]

shit = generate(4, 5)
print(shit)
print(computerNetwork(4, shit))