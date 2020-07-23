class Solution(object):
  def balancedString(self, s):
    """
    :type s: str
    :rtype: int
    """
    goal = int(len(s)/4)
    count = {"Q": -goal, "W": -goal, "E": -goal, "R": -goal}
    for c in s:
      count[c] += 1
    if count["Q"] <= 0:
      del count["Q"]

    if count["W"] <= 0:
      del count["W"]

    if count["E"] <= 0:
      del count["E"]

    if count["R"] <= 0:
      del count["R"]

    j = 0
    for i, c in enumerate(s):

    print(count)
    return 0


a = Solution()
print(a.balancedString("WWEQERQWQWWRWWERQWEQ"))
print(a.balancedString("WWQQQRQWQWWRWWERQWEQ"))
print(a.balancedString("QQWE"))
print(a.balancedString("QQQW"))
print(a.balancedString("QQQQ"))
