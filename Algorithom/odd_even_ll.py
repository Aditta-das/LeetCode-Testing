# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        odd = current = head
        even = evenHead = head.next
        
        i=1

        while current:
            if i > 2 and i % 2 != 0:
                odd.next = current
                odd = odd.next
            elif i > 2 and i % 2 == 0:
                even.next = current
                even = even.next
            current = current.next
            i += 1
            even.next = None
            odd.next = evenHead

        return head