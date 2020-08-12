def convert(string_input):
  stack = []
  current = ""
  multiplier = ""
  for c in string_input:
    if c == "(":
      stack.append(current)
      current = ""
    elif c == ")":
      continue
    elif c == "{":
      continue
    elif c == "}":
      current = stack.pop() + current * int(multiplier)
      multiplier = ""
    elif c.isnumeric():
      multiplier += c
    elif c.isalpha():
      current += c
  return current

print(convert("(ab){3}(cd){2}"))
print(convert("(ab(c){3}d){2}"))