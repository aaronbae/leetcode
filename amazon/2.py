# Return type should be a list of tuples
def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    # WRITE YOUR CODE HERE
    curr_max = 0
    result = []
    fl = len(foregroundAppList)
    bl = len(backgroundAppList)
    first = sorted(foregroundAppList, key=lambda t:t[1])
    second = sorted(backgroundAppList, key=lambda t:t[1], reverse=True)
    for f in first:
        for s in second:
            total = f[1] + s[1]
            t = (f[0], s[0])
            if total == curr_max:
                result.append(t)
            elif total > curr_max and total <= deviceCapacity:
                result = [t]
                curr_max = total
            elif total < curr_max:
                break
    if len(result) == 0:
        return [()]
    return result



c = 10
#f = [[1,3],[2,5],[3,7],[4,10]]
#g = [[1,2],[2,3],[3,4],[4,5]]

f = [[2,7],[3,14]]
g = [[2,10],[3,14]]
print(optimalUtilization(c,f,g))