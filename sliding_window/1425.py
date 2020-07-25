class Solution(object):
  def constrainedSubsetSum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    queue = []
    maxcumsum = []
    for j, n in enumerate(nums):
      maxcumsum.append(n + queue[0] if len(queue) > 0 else n)
      while len(queue) > 0 and maxcumsum[j] > queue[-1]:
        queue.pop()
      if maxcumsum[j] > 0:
        queue.append(maxcumsum[j])
      if j >= k and len(queue) > 0 and maxcumsum[j - k] == queue[0]:
        queue.pop(0)
      print(n, queue, maxcumsum)
    return max(maxcumsum)


a = Solution()
nums = [10, -2, -10, -5, 20]
k = 2
nums = [-1, -2, 5, -1, 3, 4, -10, -10, -10, -10, -10, 5, 7, 15, -4, -5, -6]
print(a.constrainedSubsetSum(nums, k))
