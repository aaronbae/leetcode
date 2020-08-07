def convert(nums):
  prev = None
  for i in range(len(nums)-1, -1, -1):
    a = ListNode(nums[i], prev)
    prev = a
  return prev

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
  def __repr__(self):
    vals = []
    current = self
    while current:
      vals.append(current.val)
      current = current.next
    return str(vals)
  
  def __str__(self):
    vals = []
    current = self
    while current:
      vals.append(current.val)
      current = current.next
    return str(vals)

  def copy(self):
    start = ListNode(self.val, self.next)
    current = start
    while current and current.next:
      next_copy = ListNode(current.next.val, current.next.next)
      current.next = next_copy
      current = next_copy
    return start

class Solution(object):
  def clean(self, lists):
    result = []
    for l in lists:
      if l:
        result.append(l)
    return result

  def getSmallestNode(self, lists):
    if len(lists) == 0: 
      return None
    index = 0
    result = lists[0]
    # finding smallest
    for i, l in enumerate(lists):
      if l and l.val < result.val:
        result = l
        index = i
    # cleaning
    lists[index] = lists[index].next
    if not lists[index]:
      lists.pop(index)
    return result, lists

  def mergeKLists(self, lists):
    lists = self.clean(lists)
    if len(lists) == 0:
      return None

    start, lists = self.getSmallestNode(lists)
    current_node = start
    while lists:
      next_node, lists = self.getSmallestNode(lists)
      current_node.next = next_node
      current_node = next_node
    return start


a = Solution()
b = convert([x for x in range(5)])
c = convert([x for x in range(5)])
d = convert([x for x in range(5)])
e = convert([x for x in range(5)])
f = a.mergeKLists([b,c]).copy()

print(d)
print(e)
print(f)
print("===================")
print(a.mergeKLists([d, e, f]))