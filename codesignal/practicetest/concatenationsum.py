def concatenationsSum(a):
  total = 0
  digit_factor = 0
  for n in a:
    total += n
    digit_factor += 10**len(str(n))
  return total * (len(a) + digit_factor)

print(concatenationsSum([10, 2]))
print(concatenationsSum([8]))