class StockSpanner(object):
  def __init__(self):
    self.history = []
    self.stack = []
  
  def next(self, price):
    index = len(self.history)
    while self.stack and price >= self.history[self.stack[-1]]:
      self.stack.pop()
    result = index - self.stack[-1] if self.stack else index + 1
    self.stack.append(index)
    self.history.append(price)
    return result

a = StockSpanner()
for i in [100, 80, 60, 70, 60, 75, 85]:
  print(a.next(i))