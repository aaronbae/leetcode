class Solution(object):
  def constructArray(self, n, k):
    largest = n
    smallest = 1
    result = []
    for i in range(n):
      if (i < k and i % 2 == 1) or (i >= k and k % 2 == 0):
        result.append(largest)
        largest -= 1
      else:
        result.append(smallest)
        smallest += 1
      

    return result

a = Solution()
print(a.constructArray(5, 3))