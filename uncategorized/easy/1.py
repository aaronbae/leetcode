class Solution(object):
  def twoSum(self, nums, target):
    result = {}
    for i, n in enumerate(nums):
      if n not in result:
        result[target - n] = i
      else:
        return [result[n], i]  


a = Solution()
print(a.twoSum([2, 7, 11, 15], 13))