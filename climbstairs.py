class Solution(object):
  def climbStairs(self, n):
    if n <= 1:
      return 1
    prev = 1
    prevprev = 1
    result = 0
    for _ in range(n-1):
      result = prevprev + prev
      prevprev = prev
      prev = result
    return result


a = Solution()
print(a.climbStairs(3))