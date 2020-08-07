class Solution(object):
  def coinChange(self, coins, amount):
    if amount == 0:
      return 0
    if len(coins) == 0 and amount > 0:
      return -1

    result = [0] * (amount + 1)
    for currAmount in range(1, amount + 1):
      val = float('inf')
      for c in coins:
        if currAmount - c >= 0:
          currVal = result[currAmount - c] + 1
          if currVal < val:
            val = currVal
      result[currAmount] = val
    return result[-1] if result[-1] < float('inf') else -1

a = Solution()
print(a.coinChange([1,2,5], 11))
print(a.coinChange([], 0))