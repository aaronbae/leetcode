class Solution(object):
  def trap(self, height):
    pre = []
    stack = []
    for i, n in enumerate(height):
      while stack and n >= height[stack[-1]]:
        stack.pop()
      pre.append(stack[-1] if stack else -1)
      stack.append(i)

    N = len(height)
    post = []
    stack = []
    for i in range(N-1, -1, -1):
      n = height[i]
      while stack and n >= height[stack[-1]]:
        stack.pop()
      post.insert(0, stack[-1] if stack else -1)
      stack.append(i)
    
    black_list = set()
    result = 0
    for i in range(N):
      a = pre[i]
      b = post[i]
      if a != -1 and b != -1 and (a,b) not in black_list:
        temp = (b - a - 1) * (min(height[a], height[b]) - height[i])
        result += temp
        black_list.add((a,b))
    return result

a = Solution()
#print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(a.trap([]))