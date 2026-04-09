# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverseLL(l,string):
            while l is not None:
                string += str(l.val)
                l = l.next
            return string
        s,t = '',''
        s = traverseLL(l1,s)
        t = traverseLL(l2,t)

        s,t = s[::-1], t[::-1]
        finalS = str(int(t)+int(s))
        finalS = finalS[::-1]
        
        dummy = ListNode()
        cur = dummy
        for ch in finalS:
            cur.next = ListNode(int(ch))
            cur = cur.next

        return dummy.next




