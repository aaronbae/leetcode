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

    front = back = 0
    min_length = len(s)
    min_goal = sum(list(count.values()))
    if min_goal == 0 or min_goal == 1:
      return min_goal
    while front < len(s):
      c = s[front]
      if c in count:
        count[c] -= 1
      substring_found = True
      for v in count.values():
        if v > 0:
          substring_found = False
          break
      if substring_found:
        
        back_c = s[back]
        while True:
          if back_c in count:
            if count[back_c] == 0:
              break
            count[back_c] += 1
          if back + 1 <= front:
            back += 1
            back_c = s[back]
          else: 
            break
        
        if front - back + 1 < min_length:
          min_length = front - back + 1
          if min_length == min_goal:
            return min_length 
        back += 1
        count[back_c] += 1
      front += 1
    return min_length


a = Solution()
#print(a.balancedString("WWEQERQWQWWRWWERQWEQ"))
#print(a.balancedString("WWQQQRQWQWWRWWERQWEQ"))
#print(a.balancedString("QQWE"))
#print(a.balancedString("QQQW"))
#print(a.balancedString("QQQQ"))
print(a.balancedString("WQWRQQQW"))
