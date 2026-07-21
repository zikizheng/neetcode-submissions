# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeHelper(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            
            mid = l + (r - l) // 2
            left = mergeHelper(lists, l, mid)
            right = mergeHelper(lists, mid + 1, r)

            return merge(left, right)
            
        def merge(l1, l2):
            curr = dummy = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        
        if not lists or len(lists) == 0:
            return None
        return mergeHelper(lists, 0, len(lists) - 1)