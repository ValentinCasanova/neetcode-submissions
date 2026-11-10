# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_number(head):
            res = ''
            cur = head
            while cur:
                res += str(cur.val)
                cur = cur.next
            return int(res[::-1])
        
        res = list_to_number(l1) + list_to_number(l2)
        res = str(res)[::-1]
        cur = head = ListNode()
        for i in res:
            cur.next = ListNode(int(i))
            cur = cur.next
        return head.next
