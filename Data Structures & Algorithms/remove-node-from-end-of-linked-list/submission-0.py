# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def find_nth_from_end(head, n):
            cur = head
            length = 0
            while cur:
                cur = cur.next
                length += 1
            return length - n
            
        n = find_nth_from_end(head, n)
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        i = 0
        while i < n:
            cur = cur.next
            i += 1

        # nodes after n
        if cur.next and cur.next.next:
            cur.next = cur.next.next
        else:
            # No nodes after n
            cur.next = None

        return dummy.next
