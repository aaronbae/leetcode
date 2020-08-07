class Solution(object):
  def containDuplicate(self, nums):
    results = set()
    for n in nums:
      if n not in results:
        results.add(n)
      else:
        return True
    return False


a = Solution()
print(a.containsDuplicate([]))