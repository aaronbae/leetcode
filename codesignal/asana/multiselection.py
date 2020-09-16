def multiSelection(dimensions, tasks, mouseCoordinates):
  _,h,g = dimensions
  y1, y2 = sorted([(y, int(y/(h+g)), y%(h+g)<=h) for _, y in mouseCoordinates])
  if y1[2]:
    return tasks[y1[1]: y2[1]+1]
  else:
    return tasks[y1[1]+1: y2[1]+1]

print(multiSelection([135, 9, 1], ["0" ,"1", "2", "3", "4", "5", "6", "7"], [[132, 42], [35, 13]]))
print(multiSelection([135, 5, 5], ["0" ,"1", "2", "3", "4", "5", "6", "7"], [[132, 4], [35, 4]]))
print(multiSelection([200,4,2], ["0" ,"1", "2", "3", "4", "5", "6"], [[170, 4], [120, 12]]))