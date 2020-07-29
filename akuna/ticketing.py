def process(line: str) -> str:
  try:
    header = line[:2].upper()
    temp = str(int(line[2:], 16))
    tail = 0
    for d in temp:
      tail += int(d)
    tail = hex(tail)[2:].upper()
    #print(header, tail)
    if header == tail:
      return "VALID"
    else:
      return "INVALID"
  except:
    return "INVALID"

print(process("BADF00D5"))
print(process("1CC0FFEE"))