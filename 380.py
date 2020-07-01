class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = set()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.container:
            self.container.add(val)
            return True
        else:
            return False 
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.container:
            self.container.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        temp = list(self.container)
        return temp[random.randint(0, len(temp)-1)]
