def alternatingSort(a):
  prev = -1 * 10**9
  N = len(a)
  for i in range(N):
    val = -1 # temp
    if i % 2 == 0:
      val = a[int(i/2)]
    else:
      val = a[N-int((i+1)/2)]
    if val <= prev:
      return False
    prev = val
  return True
  
print(alternatingSort([1,3,5,6,4,2]))
print(alternatingSort([1,4,5,6,3]))