# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        tS1 = 0
        seen = set()
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(len(arr)):
            tS2 = arr[i] + arr[len(arr)-1-i]
            seen.add(tS2)

        return max(seen)
            



