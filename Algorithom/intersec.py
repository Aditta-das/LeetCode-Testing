# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        n1, n2 = headA, headB
        a, b = 0, 0
        while n1:
            a += 1
            n1 = n1.next
        
        while n2:
            b += 1
            n2 = n2.next
        
        if a > b:
            nL = headA
            diff = a - b
            nS = headB
        else:
            nL = headB
            diff = b - a
            nS = headA
        i = 0
        while i < diff:
            i += 1
            nL = nL.next
        
        while nL != nS:
            nL = nL.next
            nS = nS.next
        return nL