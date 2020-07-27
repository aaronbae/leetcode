class Solution(object):
  def shortestSubarray(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    result = len(A) + 1
    queue = []
    cumsum = [0]
    for a in A:
      cumsum.append(cumsum[-1] + a)
    for i, cs in enumerate(cumsum):
      
      while queue and cs <= cumsum[queue[-1]]: queue.pop()
      while queue and cs - cumsum[queue[0]] >= K:
        result = min(result, i - queue.pop(0))
      queue.append(i)
    return result if result < len(A) + 1 else -1


a = Solution()
print(a.shortestSubarray([84,-37,32,40,95], 167))  # 3
#print(a.shortestSubarray([1], 1))  # 1
#print(a.shortestSubarray([1, 2], 4))  # -1
#print(a.shortestSubarray([2, -1, 2], 3))  # 3
