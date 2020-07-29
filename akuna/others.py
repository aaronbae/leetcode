def see(val):
  a = (val | (val  + 1)) == val
  b = (val & (val + 1)) == val
  c = (val & (val - 1)) == 0
  d = (val | (val - 1)) == 0
  e = (val >> 1) == (val/2)
  f = ((val >> 1)<< 1) == val
  result = [int(a),int(b),int(c),int(d),int(e),int(f)]
  return result

def asdf(val):
  return int(str(val), 2) 

#for i in range(1,10):
#  print(see(2**i), 2**i)
'''
a = asdf(1010) > asdf(111)
b = asdf(11111111) > asdf(1111111)
c = asdf(11111111) + asdf(11111111) > asdf(1) - asdf(10)
d = asdf(100) * asdf(100) == asdf(10000)
e = asdf(11111010) * asdf(11) == asdf(11101110)
f = asdf(10000000) / asdf(100) == asdf(11100000)
g = asdf(11110000) - asdf(1) == asdf(10001111)
print(a,b,c,d,e,f,g)


def shit(val):
  x = 1
  loop = 1
  while loop < 10:
    x = x*x +1
    loop += 1
    if loop == val:
      break
  return x
print(shit(4))

def shit(a, b):
  print("SHIT")
  if a == b:
    return a
  if a < b:
    return shit(a, b-a)
  else:
    return shit(a-b, b)

shit(15, 21)
'''

def shit( a, l):
  i = 0
  result = 0
  while i < l:
    temp = a[i]
    if temp > result:
      result = temp
    i += 1
  return result

print(shit([1,2,3,43,5,6,7], 7))
