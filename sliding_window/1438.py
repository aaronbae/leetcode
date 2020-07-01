class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        i = 0
        max_queue = []
        min_queue = []
        for n in nums:
            while len(max_queue) > 0 and n > max_queue[-1]: max_queue.pop()
            while len(min_queue) > 0 and n < min_queue[-1]: min_queue.pop()
            max_queue.append(n)
            min_queue.append(n)
            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[i]: max_queue.pop(0)
                if min_queue[0] == nums[i]: min_queue.pop(0)
                i += 1
                
        return len(nums)-i


a = Solution()
nums = [1,2,3,100,4,5,6,7,8,90,0,89,1,88]
limit = 5
print(a.longestSubarray(nums, limit))