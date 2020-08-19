class Solution(object):
  def lengthOfLIS(self, nums):
    N = len(nums)
    if N == 0:
      return 0
    results = [0] * N
    results[0] = 1
    result = 0
    for i in range(len(nums)):
      maxval = 0
      for j in range(i):
        if nums[i] > nums[j]:
          maxval = max(maxval, results[j])
      results[i] = maxval + 1
      result = max(result, results[i])
    print(nums)
    print(results)
    return result

a = Solution()
print(a.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
