class Solution(object):
  def canJump(self, nums):
    N = len(nums)
    lastPos = N - 1
    for i in range(N - 1, -1, -1):
      if i + nums[i] >= lastPos:
        lastPos = i
        print(lastPos)
    return lastPos == 0
      
        
      
a = Solution()
print(a.canJump([10**5,10**1,10**1]*10000))
#print(a.canJump([3]))