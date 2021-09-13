# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        pt1, pt2 = dummy, dummy
        for i in range(n):
            pt1 = pt1.next

        while pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next
        pt2.next = pt2.next.next
        return head



head = [1,2,3,4,5]
n = 2
a = Solution()
print(a.removeNthFromEnd(head, n))