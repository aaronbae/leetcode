class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = {}
        self.nums = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val in self.container:
            self.container[val] += 1
            return False
        else:
            self.container[val] = 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.container:
            self.container[val] -= 1
            if self.container[val] == 0:
                del self.container[val]
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.nums[random.randint(0, len(self.nums)-1)]
        