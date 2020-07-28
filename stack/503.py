class Solution(object):
  def nextGreaterElements(self, nums):
    if len(nums) == 0:
      return []
    curr_index = 0
    max_val = nums[0]
    for i, n in enumerate(nums):
      if n > max_val:
        max_val = n
        curr_index = i

    N = len(nums)
    result = [0] * N
    stack = []
    count = 0
    while count < N:
      while stack and nums[curr_index] >= stack[-1]:
        stack.pop()
      result[curr_index] = stack[-1] if stack else -1
      stack.append(nums[curr_index])
      count += 1
      curr_index -= 1
    return result

a = Solution()
print(a.nextGreaterElements([-1, 0]))