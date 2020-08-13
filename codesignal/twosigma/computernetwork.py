'''
Could not pass all the tests
'''
def generate(n, edges):
  import random
  MAX_VAL = 10**4
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


def computerNetwork(n, network):
  class Node:
    def __init__(self, index) :
      self.index = index
      self.edges = {}
      self.previous = None
      self.min_distance = 20*10**4
    
    def __repr__(self):
      return str(self.index) + " : " + str(self.min_distance)

    def get_distance(self, node):
      return self.edges[node] if node in self.edges else -1

    def connect(self, node, value):
      self.edges[node] = value

    def is_connected(self, node):
      return node in self.edges

    def update(self, prev_node):
      if prev_node not in self.edges:
        return -1
      possible_dist = prev_node.min_distance + self.edges[prev_node] 
      if possible_dist < self.min_distance:
        self.min_distance = possible_dist
        self.previous = prev_node
    
    def get_neighbors(self):
      return [x for x in self.edges]
    
    def print_path(self):
      current = self
      path = []
      values = []
      while current:
        path.insert(0, current.index)
        values.insert(0, current.min_distance)
        current = current.previous
      print(path)
      print(values)

  # initialize node accessor
  accessor = [Node(i) for i in range(1, n+1)]
  for r in network:
    s, e, v = r
    accessor[s-1].connect(accessor[e-1], v)
    accessor[e-1].connect(accessor[s-1], v)

  dead = set()
  frontier = set()
  start = accessor[0]
  start.min_distance = 0
  frontier.add(start)
  while len(frontier) >  0:
    #print(frontier)
    #print(dead)
    #print("==============")
    current = sorted(list(frontier), key=lambda x: x.min_distance)[0]
    frontier.remove(current)
    dead.add(current)
    for neighbor in current.get_neighbors():
      if neighbor not in dead:
        neighbor.update(current)
        frontier.add(neighbor)


  #accessor[-1].print_path()
  return accessor[-1].min_distance

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
 [3,5,7650]]
c = [[2, 4, 622], 
[3, 4, 7076], 
[6, 9, 6873], 
[1, 4, 8465], 
[3, 6, 4568], 
[3, 5, 3161], 
[6, 8, 7194], 
[8, 9, 7485], 
[1, 3, 4362], 
[2, 5, 2642], 
[1, 6, 8541], 
[4, 9, 5430], 
[2, 10, 1783], 
[5, 6, 4720], 
[3, 8, 8829], 
[4, 10, 6532], 
[6, 10, 3282], 
[8, 10, 5215], 
[3, 7, 159], 
[7, 9, 2328]] 
d = sorted(c)
for r in d:
  print(r)
#print(computerNetwork(4, a))
#print(computerNetwork(5, b))
print(computerNetwork(10, c))

# RANDOM GENERATOR TEST
#GOAL = 10
#shit = generate(GOAL, 20)
#print(shit)
#print(computerNetwork(GOAL, shit))
