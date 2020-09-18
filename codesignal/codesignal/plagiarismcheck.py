import re
def plagiarismCheck(code1, code2):
  def repl(matchobj):
    x = matchobj.group(0)
    if x in transform:
      return transform[x]
    return x

  pattern = r'[a-zA-Z_]+[a-zA-Z0-9_]*'
  transform = dict()
  for i in range(len(code1)):
    first = code1[i]
    second = code2[i]
    varSet1 = re.findall(pattern, first)
    varSet2 = re.findall(pattern, second)
    # register variables
    for i in range(len(varSet1)):
      if varSet1[i] not in transform:
        transform[varSet1[i]] = varSet2[i]
      elif transform[varSet1[i]] != varSet2[i]:
        return False
    # transcribe and compare
    new_first = re.sub(pattern, repl, first)
    if new_first != second:
      return False
  return True

a = ["def is_even_sum(a, b):",
         "    return (a + b) % 2 == 0"]
b = ["def is_even_sum(summand_1, summand_2):",
         "    return (summand_1 + summand_2) % 2 == 0"]
print(plagiarismCheck(a,b))

a = ["function is_even_sum(a, b) {",
         "  return (a + b) % 2 === 0;",
         "}"]
b = ["function is_even_sum(a, b) {",
         "  return (a + b) % 2 !== 1;",
         "}"]
print(plagiarismCheck(a,b))

a = ["def foo(a, b):",
         "    return a + a"]
b = ["def foo(b, a):",
         "    return b + b"]
print(plagiarismCheck(a,b))