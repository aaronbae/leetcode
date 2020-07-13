class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff = 0.5 # cannot happen
        window_length = 0
        result = 0
        for j in range(len(A)):
            if j == 0:
                continue
            newdiff = A[j] - A[j - 1]
            if newdiff == diff:
                window_length += 1
            else:
                window_length = 0
            diff = newdiff
            result += window_length
        return result

a = Solution()
nums = [1,2,3,4]
print(a.numberOfArithmeticSlices(nums))