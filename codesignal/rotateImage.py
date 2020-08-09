def rotateImage(a):
  N = len(a)
  targetVal = 0
  for i in range(N):
    for j in range(i,N-i-1):
      current = (i,j)
      currentVal = a[current[0]][current[1]]
      for _ in range(4):
        target = (current[1],N-current[0]-1)
        targetVal = a[target[0]][ target[1]]
        a[target[0]][ target[1]] = currentVal
        currentVal = targetVal
        current = target
  return a

def display(a):
  for r in a:
    print(" ".join(list(map(lambda x: "{:3d}".format(x), r))))
    
size = 3
a = [[size*y+x for x in range(size)] for y in range(size)]
display(a)
print("===============")
rotateImage(a)
display(a)