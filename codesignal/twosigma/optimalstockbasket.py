def optimalStockBasket(stocks, riskBudget):
  N = len(stocks)
  dp = [[0 for _ in range(riskBudget + 1)] for _ in range(N+1)]
  for i in range(N+1):
    if i > 0:
      curr_val, curr_risk = stocks[i-1]
      for total_budget in range(riskBudget + 1):
        dont = dp[i - 1][total_budget]
        do = 0
        if total_budget >= curr_risk:
          do = curr_val + dp[i - 1][total_budget - curr_risk]
        dp[i][total_budget] = max(dont, do)
    print(dp[i])
  return dp[N][riskBudget]

a = [[-1, 2], [10, 15], [11, 13], [9, 10]]
b = 30
print(optimalStockBasket(a,b))