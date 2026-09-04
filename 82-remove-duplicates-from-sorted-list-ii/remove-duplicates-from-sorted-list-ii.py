# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        dummy=ListNode(0)
        ans=dummy
        slow=head
        fast=head.next
        prev=int(-101)
        while slow.next:
            if slow.val!=fast.val and prev!=slow.val:
                ans.next=slow
                ans=ans.next
                slow=slow.next
                fast=fast.next
            else:
                prev=slow.val
                slow=slow.next
                fast=fast.next
        if prev!=slow.val:
            ans.next=slow
        else:
            ans.next = None
        return dummy.next


        