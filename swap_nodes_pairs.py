# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        dummy = cur = ListNode()
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            cur.next = tmp
            head = head.next
            cur = tmp.next
        return dummy.next
    
    def swapPairs1(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs1(tmp.next)
            tmp.next = head
            return tmp
        return head

head = [1,2,3,4]
a = Solution()
print(a.swapPairs(head))
