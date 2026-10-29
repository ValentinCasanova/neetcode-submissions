# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle, hare = head, head
        while hare:
            hare = hare.next.next if hare.next else None
            turtle = turtle.next
            if hare and hare == turtle:
                return True
        return False