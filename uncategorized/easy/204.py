class Solution(object):
  def countPrimes(self, n):
    result = [True]*(n-2)
    i = 2
    while i * i < n:
      if not result[i - 2]:
        i += 1
        continue
      j = i * i
      while j < n:
        result[j - 2] = False
        j += i
      i += 1
    return sum(result)

a = Solution()
print(a.countPrimes(10000000))

