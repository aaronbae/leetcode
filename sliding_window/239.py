class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0
        result = []
        queue = []
        for j, n in enumerate(nums):
            while len(queue) > 0 and n > queue[-1]: queue.pop()
            queue.append(n)
            if j + 1 >= k: 
                result.append(queue[0])
                if queue[0] == nums[i]:
                    queue.pop(0)
                i += 1
        return result

a = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
#nums = [1,-1]
#k = 1
print(a.maxSlidingWindow(nums, k))