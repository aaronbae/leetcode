def getRecordBreaking(V):
    if len(V)==0:
        return 0
    best = 0
    count = 0
    for i, v in enumerate(V):
        if v > best and (i == len(V) - 1 or v > V[i+1]):
            count += 1
            print(i, " : ", v)
        best = max(v, best)
    return count
  
V = list(map(int, "11 11 12 11 11 11 12".split()))
print(V)
result = getRecordBreaking(V)
print("FUCK YEARH: ",result)    