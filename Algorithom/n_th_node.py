# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l, r = head, head
        for _ in range(n):
            r = r.next
        if not r:
            return head.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head