# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        c, p = slow.next, None
        slow.next = None

        while c:
            c.next, p, c = p, c, c.next

        f, s = head, p

        while s:
            f.next, s.next, f, s = s, f.next, f.next, s.next
