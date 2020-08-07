class Solution(object):
  def topKFrequent(self, nums, target):
    results = {}
    for n in nums:
      if n not in results:
        results[n] = 0
      results[n] += 1
    final_results = [x for _,x in sorted(zip(results.values(), results.keys()), reverse=True)]
    return final_results[:target]

a = Solution()
print(a.topKFrequent([7, 7, 7, 7,7,7,7,7,1,1,1,2,2,3], 2))