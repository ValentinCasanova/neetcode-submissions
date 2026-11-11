# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_res = res_head = ListNode()
        cur1, cur2 = l1, l2
        carry = 0
        while cur1 or cur2 or carry:
            cur1_val = cur1.val if cur1 else 0
            cur2_val = cur2.val if cur2 else 0
            cur_val = cur1_val + cur2_val + carry
            carry = 1 if cur_val >= 10 else 0
            cur_val = cur_val % 10
            cur_res.next = ListNode(cur_val)
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            cur_res = cur_res.next

        return res_head.next
