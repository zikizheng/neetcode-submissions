# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2
        curr = dummy = ListNode()
        carry = 0
        while l1curr and l2curr:
            s = l1curr.val + l2curr.val + carry
            carry = s // 10
            s %= 10
            curr.next = ListNode(s)
            curr = curr.next
            l1curr = l1curr.next
            l2curr = l2curr.next
        while l1curr:
            s = l1curr.val + carry
            carry = s // 10
            s %= 10
            curr.next = ListNode(s)
            curr = curr.next
            l1curr = l1curr.next
        while l2curr:
            s = l2curr.val + carry
            carry = s // 10
            s %= 10
            curr.next = ListNode(s)
            curr = curr.next
            l2curr = l2curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next