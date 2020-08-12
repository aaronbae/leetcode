class Solution(object):
  def numDecodings(self, s):
    N = len(s)
    dp = [0]*(N+1)
    dp[-1] = 1
    for i in range(N):
      if s[i] != '0':
        dp[i] += dp[i-1]

      if i > 0:
        twodig = int(s[i-1:i+1])
        if twodig >= 10 and twodig <= 26:
          dp[i] += dp[i-2]

    return dp[-2]


a = Solution()
print(a.numDecodings("220226"))
