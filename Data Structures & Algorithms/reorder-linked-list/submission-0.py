# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        f, s = head, prev
        while s.next:
            tempf, temps = f.next, s.next
            f.next = s
            s.next = tempf
            f = tempf
            s = temps