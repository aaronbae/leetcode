def mutateTheArray(n, a):
  b = []
  for i in range(n):
    first = a[i-1] if i > 0 else 0
    last = a[i+1] if i < n-1 else 0
    b.append(first + a[i] + last)
  return b

print(mutateTheArray(5, [4,0,1,-2,3]))