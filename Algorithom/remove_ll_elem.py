# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return head
        itr = head
        while itr and itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
            else: itr = itr.next
        return head if head.val != val else head.next