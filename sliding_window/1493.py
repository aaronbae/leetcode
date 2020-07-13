class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1 # number of instances allowed
        i = 0 # location of the left window
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
            print(nums[j], i, k)
        return len(nums) - i - 1
nums = [0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1]
a = Solution()
print(a.longestSubarray(nums))