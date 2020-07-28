class Solution:
  def nextGreaterElement(self, nums1, nums2):
    answers = {}
    stack = []
    for i in range(len(nums2)-1, -1, -1):
      n = nums2[i]
      while stack and n > stack[-1]:
        stack.pop()
      answers[n] = stack[-1] if stack else -1
      stack.append(n)
    return [answers[x] for x in nums1]
    

a = Solution()
print(a.nextGreaterElement([2, 4], [1,2,3,4]))