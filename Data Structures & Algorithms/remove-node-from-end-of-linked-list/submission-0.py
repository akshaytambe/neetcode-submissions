# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        sp, fp = dummy, dummy
        for i in range(n):
            fp = fp.next

        while fp.next:
            fp = fp.next
            sp = sp.next

        sp.next = sp.next.next

        return dummy.next