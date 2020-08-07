class Solution(object):
  def maxProfit(self, prices):
    if len(prices) <= 1:
      return 0
    result = 0
    min_val = prices[0]
    for p in prices:
      result = max(p - min_val, result)
      min_val = min(p, min_val)
    return result

a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
print(a.maxProfit([1]))