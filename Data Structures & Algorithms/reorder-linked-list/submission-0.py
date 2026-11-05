# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(head):
            cur = head
            prev = None
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        
        def merge_list(head1, head2):
            dummy = ListNode()
            cur = dummy
            while cur and head1:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
                if head2:
                    cur.next = head2
                    head2 = head2.next
                    cur = cur.next
            return dummy.next
            
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        mid = head
        for i in range((length - 1) // 2):
            mid = mid.next
        tmp = mid.next
        mid.next = None
        mid = tmp
        mid = reverse_list(mid)
        
        head = merge_list(head, mid)