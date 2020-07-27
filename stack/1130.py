class Solution(object):
  def mctFromLeafValues(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    result = 0
    while len(arr) > 1:
      j = 0
      bestProd = max(arr) ** 2
      for i in range(0, len(arr) - 1):
        if arr[i] * arr[i+1] < bestProd:
          bestProd = arr[i] * arr[i+1]
          j = i
      j = j + 1 if arr[j + 1] < arr[j] else j
      arr.pop(j)
      result += bestProd
    return result


a = Solution()
print(a.mctFromLeafValues([2,3,1,4]))
