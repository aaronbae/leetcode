class Solution(object):
  def sumSubarrayMins(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    stack = []
    prev = []
    for i, a in enumerate(A):
      while stack and a <= A[stack[-1]]:
        stack.pop()
      temp = stack[-1] if stack else -1
      prev.append(temp)
      stack.append(i)

    N = len(A)
    stack = []
    post = []
    for i in range(N-1, -1, -1):
      a = A[i]
      while stack and a < A[stack[-1]]:
        stack.pop()
      temp = stack[-1] if stack else N
      post.insert(0, temp) 
      stack.append(i)
    
    result = 0
    for i in range(N):
      result += (prev[i] - i) * (i - post[i]) * A[i]
    return result % (10**9+7)


a = Solution()
print(a.sumSubarrayMins([71,55,82,55]))
