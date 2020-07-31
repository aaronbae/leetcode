class Solution(object):
  def shortestToChar(self, S, C):
    previous = -1
    results = []
    for i, ch in enumerate(S):
      if ch == C:
        for j in range(previous+1, i+1):
          val = min(j-previous, i-j)
          if previous == -1:
            val = i-j
          results.append(val)
        previous = i
    previous = 1
    while len(results) < len(S):
      results.append(previous)
      previous += 1
    return results

a = Solution()
print(a.shortestToChar("aabaaaa", 'b'))