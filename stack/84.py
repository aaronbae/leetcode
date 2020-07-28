class Solution(object):
  def largestRectangleArea(self, heights):
    if len(heights) == 0:
      return 0
    pre = []
    stack = []
    for i, n in enumerate(heights):
      while stack and n <= heights[stack[-1]]:
        stack.pop()
      pre.append(stack[-1] if stack else -1)
      stack.append(i)
    
    N = len(heights)
    post = []
    stack = []
    for i in range(N-1, -1, -1):
      n = heights[i]
      while stack and n <= heights[stack[-1]]:
        stack.pop()
      post.insert(0, stack[-1] if stack else N)
      stack.append(i)
    
    return max([(post[i] - pre[i] - 1) * heights[i] for i in range(N)])

a = Solution()
print(a.largestRectangleArea([]))