def meanGroups(a):
  temp = {}
  for i, row in enumerate(a):
    mean = 1.0*sum(row)/len(row)
    if mean not in temp:
      temp[mean] = []
    temp[mean].append(i)
  result = []
  print(temp.keys())
  for row in temp.values():
    result.append(sorted(row))
  return sorted(result)

a = [[-2,4,7,-6,2,-5,3], 
 [-1,0,0,0], 
 [2,2,-6,17,9,-22,30,-16,0,-1,-11,6,0,-4], 
 [3,3,-8,-2,3]]
print(meanGroups(a))