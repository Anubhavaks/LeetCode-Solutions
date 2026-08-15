# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        slow=headA
        f={}
        fast=headB
        while slow is not None:
            f[slow]=f.get(slow.next,0)+1
            slow=slow.next
        while fast is not None:
            if fast in f:
                return fast
            else:
                fast=fast.next
        return None