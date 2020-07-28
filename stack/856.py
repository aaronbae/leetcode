class Solution(object):
  def scoreOfParentheses(self, S):
    stack = [0]
    for c in S:
      if c == "(":
        stack.append(0)
      else:
        val = stack.pop()
        stack[-1] += 1 if val == 0 else val * 2
    return stack[0]

a = Solution()
print(a.scoreOfParentheses("((())())"))