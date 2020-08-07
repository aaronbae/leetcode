class Solution(object):
  def combinationSum4(self, nums, target):
    result = [0] * (target + 1)
    result[0] = 1
    for goal in range(1, target+1):
      currCount = 0
      for n in nums:
        if goal - n >= 0:
          currCount += result[goal - n]
      result[goal] = currCount
    return result[-1]

a = Solution()
print(a.combinationSum4([2], 11))