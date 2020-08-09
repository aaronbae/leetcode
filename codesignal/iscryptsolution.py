def isCryptSolution(crypt, solution):
  def decrypt(s, solution):
    val = ""
    for c in s:
      val += solution[c]
    if len(val) > 1 and val[0] == "0":
      return -1
    else:
      return int(val)

  sol_dict = {}
  for r in solution:
    sol_dict[r[0]] = r[1]
  a = decrypt(crypt[0], sol_dict)
  b = decrypt(crypt[1], sol_dict)
  c = decrypt(crypt[2], sol_dict)
  if a == -1 or b == -1 or c == -1:
    return False
  return a + b == c

a = ["TEN", 'TWO', 'ONE']
b = [["O","1"], 
 ["T","0"], 
 ["W","9"], 
 ["E","5"], 
 ["N","4"]]

print(isCryptSolution(a, b))