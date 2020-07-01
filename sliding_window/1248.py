class Solution(object):
    def numberOfSubarrays(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res
        return atMost(k) - atMost(k - 1)
        

a = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(a.numberOfSubarrays(nums, k))