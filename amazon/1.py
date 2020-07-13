# Return type should be a list of tuples
def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    # WRITE YOUR CODE HERE
    import math
    import heapq
    if numDestinations == 0:
        return []
    if numDestinations == numDeliveries:
        return [(t[0], t[1]) for t in allLocations]
    def calculate_distance(t):
        return math.sqrt(t[0]**2+t[1]**2)
    loc_with_d = [(calculate_distance(t), t[0], t[1]) for t in allLocations]
    heapq.heapify(loc_with_d)
    result = []
    for i in range(numDeliveries):
        t = heapq.heappop(loc_with_d)
        result.append((t[1],t[2]))

    return result
n = 1
locs = [[1,2]]
x = 0
print(ClosestXdestinations(n, locs, x))