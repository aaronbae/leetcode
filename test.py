class Shit:
  def __init__(self, v):
    self.val = v
  
  def __repr__(self):
    return str(self.val)

a = [Shit(1), Shit(10), Shit(5)]

b = set(a)
print(b)