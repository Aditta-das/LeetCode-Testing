# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if len(head) == 0 and not head:
            return None
        while len(head) > 1:
            


head = [1, 2, 3, 4, 5]
k = 2
a = Solution()
print(a.reverseKGroup(head, k))
        