def bestSquares(m, k):
  def get_subset_sum(m, a, b, c, d):
    result = 0
    if a==b:
      b += 1
    if c==d:
      d += 1
    for i in range(a,b):
      for j in range(c,d):
        result += m[i][j]
    return result

  N = len(m)
  M = len(m[0])

  max_sum = 0
  max_distinct = set()
  for i in range(k):
    for j in range(k):
      v = m[i][j]
      max_distinct.add(v)
      max_sum += v

  current_sum = max_sum
  for i in range(N-k+1):
    horizontal_offset = 0
    for j in range(M-k+1):
      print(i, i+k, j+k)
      incoming = get_subset_sum(m, i, i+k, j+k, j+k) 
      outgoing = get_subset_sum(m, i, i+k, j, j) 
      horizontal_offset += incoming - outgoing
      new_sum = current_sum + horizontal_offset
      if new_sum >= max_sum:
        max_sum = new_sum
        if new_sum > max_sum:
          max_distinct = set()
        for sub_i in range(k):
          for sub_j in range(k):
            max_distinct.add(m[i+sub_i][j+sub_j])
    
    vertical_in = get_subset_sum(m, i+k, i+k, j, j+k) 
    vertical_out = get_subset_sum(m, i, i, j, j+k) 
    current_sum += vertical_in - vertical_out
  return sum(max_distinct)

a = [[1, 0, 1, 5, 6],
     [3, 3, 0, 3, 3],
     [2, 9, 2, 1, 2],
     [0, 2, 4, 2, 0]]
print(bestSquares(a, 3))