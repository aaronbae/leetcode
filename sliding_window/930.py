class Solution(object):
	def numSubarraysWithSum(self, A, S):
		"""
		:type A: List[int]
		:type S: int
		:rtype: int
		"""
		test = []
		result = count = currsum = left = 0
		for right, val in enumerate(A):
			currsum += val
			if val == 1:
				count = 0
			while left <= right and currsum >= S:
				if currsum == S:
					count += 1
				currsum -= A[left]
				left += 1
			test.append(count)
			result += count
		print(A)
		print(test)
		return result

a = Solution()
print(a.numSubarraysWithSum([1,0,1,0,1], 2))
print(a.numSubarraysWithSum([0,0,0,0,0], 0))
