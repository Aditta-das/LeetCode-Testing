# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        if head is None:
            return head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        secondhalf = self.reverse(slow.next)
        firsthalf = head
        while firsthalf != None and secondhalf != None:
            if firsthalf.val != secondhalf.val:
                return False
            secondhalf = secondhalf.next
            firsthalf = firsthalf.next
        return True
    
    def reverse(self, head):
        newHead = None
        while head != None:
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead