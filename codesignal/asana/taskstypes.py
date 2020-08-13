def tasksTypes(deadlines, day):
  result = [0, 0, 0]
  for n in deadlines:
    if n <= day:
      result[0] += 1
    elif n <= day + 7:
      result[1] += 1
    else:
      result[2] += 1
  return result
