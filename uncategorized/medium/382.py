# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        current = head
        while current.next:
            current = current.next
            self.count += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        current = self.head
        rand = random.randint(0, self.count)
        for _ in range(rand):
            current = current.next
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()