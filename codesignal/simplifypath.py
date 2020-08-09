def simplifyPath(path):
  stack = []
  for e in path.split("/"):
    if len(e) > 0:
      if e == "..":
        if len(stack) > 0:
          stack.pop()
      elif e == ".":
        continue
      else:
        stack.append(e)
  return "/" + "/".join(stack)

print(simplifyPath("/a/b/c//../././../home"))