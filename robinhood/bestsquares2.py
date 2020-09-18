def bestSquares(m, k):
  def subsetsum(m, a,b,c,d):
    distinct = set()
    total = 0
    for i in range(a, b):
      for j in range(c,d):
        v = m[i][j]
        total += v
        distinct.add(v)
    return total, distinct

  N = len(m)
  M = len(m[0])
  max_sum = 0
  distinct = set()
  for i in range(N-k+1):
    r = range(M-k+1) if i%2 == 0 else range(M-k, -1, -1)
    for j in r:
      current_sum, curr_distinct = subsetsum(m, i,i+k,j, j+k)
      if current_sum > max_sum:
        max_sum = current_sum
        distinct = set()
      if current_sum == max_sum:
        distinct = distinct.union(curr_distinct)
        print(i,j, max_sum, distinct)
  return sum(distinct)

a = [[1, 0, 1, 5, 6],
     [3, 3, 0, 3, 3],
     [2, 9, 2, 1, 2],
     [0, 2, 4, 2, 0]]
print(bestSquares(a, 3))