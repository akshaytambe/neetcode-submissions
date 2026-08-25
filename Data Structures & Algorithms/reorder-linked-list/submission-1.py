# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp, fp = head, head.next
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        # reverse second half
        second = sp.next
        prev, sp.next = None, None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
