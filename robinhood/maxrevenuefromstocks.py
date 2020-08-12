def maxRevenueFromStocks(prices, algo, k):
  N = len(prices)
  current_sum = 0
  for i in range(N):
    p = prices[i]
    if algo[i] == 1 or i < k:
      current_sum += p
    else:
      current_sum -= p

  max_sum = current_sum
  for i in range(k, N):
    incoming = prices[i]
    outgoing = prices[i-k]
    if algo[i] == 0:
      current_sum += 2 * incoming
    if algo[i-k] == 0:
      current_sum -= 2 * outgoing
    if current_sum > max_sum:
      max_sum = current_sum
  
  return max_sum

a = [2,4,1,5,2,6,7]
b=  [0,1,0,0,1,0,0]
c = 4
print(maxRevenueFromStocks(a,b,c))