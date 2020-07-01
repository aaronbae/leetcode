class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        flattened = []
        for row in matrix:
            flattened += row
        flattened.sort()
        return flattened[k-1]
            
'''       
matrix = [
   [ 1,  2],
   [ 1,  3],
]
'''
n = 5
matrix = [[i*n + j + 1 for j in range(n)] for i in range(n)]
for i in matrix:
    row = ""
    for j in i:
        row += "{:2d} ".format(j)
    print(row)
print("=============")
k = 10

a = Solution()
print(a.kthSmallest(matrix, k))
            
            