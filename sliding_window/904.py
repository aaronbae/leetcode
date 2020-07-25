class Solution(object):
  def totalFruit(self, tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    class Window:
      def __init__(self, tree):
        self.count = [0] * (len(tree) + 1)
        self.present = set()
        self.left = 0
        self.right = 0
        self.tree = tree
      
      def add(self):
        val = self.tree[self.right]
        self.right += 1
        self.present.add(val)
        self.count[val] += 1
      
      def remove(self):
        val = self.tree[self.left]
        self.left += 1
        self.count[val] -= 1
        if self.count[val] == 0:
          self.present.remove(val)

      def distinct(self):
        return len(self.present)

      def length(self):
        return self.right - self.left

      def display(self):
        copy = [str(x) for x in self.tree]
        if self.left < len(copy):
          copy[self.left] = "L"
        if self.right < len(copy):
          copy[self.right] = "R"
        print("["+", ".join(copy)+"]")

    window = Window(tree)
    result = 0
    #print(tree)
    #print("===========")
    for _ in tree:
      window.add()
      while window.left <= window.right and window.distinct() > 2:
        window.remove()
      result = max(result, window.length())
      #window.display()
    return result

  
a = Solution()
#print(a.totalFruit([1,2,1])) # 3
print(a.totalFruit([0,1,2,2])) # 3
print(a.totalFruit([1,2,3,2,2])) # 4
print(a.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
