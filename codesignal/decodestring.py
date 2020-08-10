def decodeString(s):
  import re
  stack = []
  current = ""
  count = ""
  for c in s:
    if c =="[":
      stack.append((current, int(count)))
      count = ""
      current = ""
    elif c=="]":
      (previous, prevCount) = stack.pop()
      current = previous + ''.join([current]*prevCount)
    elif c.isalpha():
      current += c
    else:
      count += c
  return current

print(decodeString("4[ab]"))
print(decodeString("2[b3[a]]"))
print(decodeString("z1[y]zzz2[abc]"))
