def getType(a, b):
  return 0 if a == b else int((a - b)/abs(a - b))

def countBreakage(A):
    if len(A) < 5:
        return 0

    count = 0
    start_streak_point = 0
    streak_type = -2
    for i, a in enumerate(A):
        if i == 0: continue
        new_type = getType(a, A[i-1])
        if i > 1 and new_type != 0 and new_type != streak_type and streak_type != -2:
            start_streak_point = i
            print(i, a, "RESET", streak_type, new_type)
        if i - start_streak_point == 4:
            count += 1
            streak_type = -2
            start_streak_point = i
        if new_type != 0:
            streak_type = new_type
    return count

print("FUCK YEARH: ",countBreakage(list(map(int, "2 2 2 2 3 4 5 6".split()))))   