class Solution(object):
  def longestOnes(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    if sum(A) == 0:
      return K
    if len(A) - sum(A) <= K:
      return len(A)
    max_length = count = front = back = 0
    while back <= front and front < len(A):
      if A[front] == 0:
        count += 1
      while count > K and back < front:
        count -= A[back] == 0
        back += 1
      # print("HERE: {} , {}, {} = {}".format(
      #      back, front, count, A[back:front+1]))
      max_length = max(front-back + 1, max_length)
      front += 1
    return max_length


a = Solution()
print(a.longestOnes([0, 0, 0, 0], 0))
print(a.longestOnes([0, 0, 1, 1, 1, 0, 0], 0))
print(a.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

print(a.longestOnes([0, 0, 1, 1, 0, 0, 1, 1,
                     1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
