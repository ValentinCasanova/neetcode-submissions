# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2

        ptr1 = list1
        ptr2 = list2
        cur = None 
        if ptr1.val <= ptr2.val:
            cur = ptr1
            ptr1 = ptr1.next
        else:
            cur = ptr2
            ptr2 = ptr2.next

        head = cur
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next
        
        cur.next = ptr1 or ptr2
        return head