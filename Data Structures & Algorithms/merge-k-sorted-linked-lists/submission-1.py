# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            res = curr = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            while l1:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            while l2:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
            return res.next
        
        res = curr = ListNode(-float('inf'))
        for i in range(len(lists)):
            curr = merge(curr, lists[i])
        
        return res.next