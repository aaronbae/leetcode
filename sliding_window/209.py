class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    result = len(nums) + 1
    queue = []
    cumsum = [0]
    for n in nums:
      cumsum.append(cumsum[-1] + n)
    for i, cs in enumerate(cumsum):
      while queue and cs <= cumsum[queue[-1]]:
        queue.pop()
      queue.append(i)
      while queue and cs - cumsum[queue[0]] >= s:
        result = min(result, i-queue.pop(0))
    return result if result != len(nums) + 1 else 0


a = Solution()
# print(a.minSubArrayLen(7, [2,3,1,2F4,3])) # 2
print(a.minSubArrayLen(15, [5, 5, 10, 1, 1, 1, 1, 1, 5, 5, 5]))  # 2
