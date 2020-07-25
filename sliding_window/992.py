class Solution(object):
  def subarraysWithKDistinct(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    class Window:
      def __init__(self, A):
        self.A = A
        self.count = [0] * (len(A) + 1) 
        self.present = set()
        self.left = 0
        self.right = 0

      def insert(self, N):
        self.present.add(N)
        self.count[N] += 1
        self.right += 1

      def shorten(self):
        val = self.A[self.left]
        self.count[val] -= 1
        if self.count[val] == 0:
          self.present.remove(val)
        self.left += 1

      def distinct(self):
        return len(self.present)
      
      def display(self):
        copy = [str(x) for x in self.A]
        if self.left < len(copy):
          copy[self.left] = "L"
        if self.right < len(copy):
          copy[self.right] = "R"
        print(" ".join(copy))

    def status_report(tight, loose):
      print("============== "+str(tight.left-loose.left))  
      loose.display()
      tight.display()

    #test = []
    result = 0
    loose = Window(A)
    tight = Window(A)
    for right, val in enumerate(A):
      loose.insert(val)
      tight.insert(val)
      
      while loose.left <= right and loose.distinct() > K:
        loose.shorten()
        
      while tight.left <= right and tight.distinct() >= K:
        tight.shorten()
      
      result += tight.left-loose.left
      #test.append(tight.left-loose.left)
      #status_report(tight, loose)
    #print(A, K)
    #print(test)
    return result


a = Solution()
print(a.subarraysWithKDistinct([1, 2], 1))
#print(a.subarraysWithKDistinct([1, 1, 2, 2, 2, 3, 4], 3))
#print(a.subarraysWithKDistinct([1, 2, 1, 2, 3], 3))
#print(a.subarraysWithKDistinct([1, 2, 1, 3, 4], 1))