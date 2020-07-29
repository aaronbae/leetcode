class Solution(object):
  def rotate(self, nums, k):
    n = len(nums)
    result = [0] * n
    for i in range(n):
      result[( i + k) % n] = nums[i]
    nums[:] = result

a = Solution()
shit = [1,2]
a.rotate(shit, 3)
print(shit)