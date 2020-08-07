class Solution(object):
  def longestConsecutive(self, nums):
    if len(nums) == 0:
      return 0
    results = {}
    for n in nums:
      if n not in results:
        start = n if n - 1 not in results else results[n-1][0]
        end = n if n + 1 not in results else results[n+1][1]
        if start != n:
          results[start] = (start, end)
        if end != n:
          results[end] = (start, end)
        results[n] = (start, end)
    longest = 1
    for k in results.keys():
      v = results[k]
      longest = max(v[1] - v[0] + 1,longest)
    return longest

a = Solution()
print(a.longestConsecutive([ ]))