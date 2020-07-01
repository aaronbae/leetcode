class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums[:]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original[:]        
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        copy = self.original[:]
        result = []
        while len(copy) > 0:
            val = copy[random.randint(0, len(copy)-1)]
            copy.remove(val)
            result.append(val)
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()