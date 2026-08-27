# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        curr=head
        smallDummy=ListNode(0)
        smallDummy.next=head
        prev_tail=smallDummy
        length=0
        while curr :
            length+=1
            curr=curr.next
        curr=head
        sum=0
        while (length)>=k :
            prev=None
            curr_head=curr
            for _ in range (k) :
                new=curr.next
                curr.next=prev
                prev=curr
                curr=new
            prev_tail.next=prev
            curr_head.next=curr

            prev_tail=curr_head
            length-=k
        

        return  smallDummy.next
            



        