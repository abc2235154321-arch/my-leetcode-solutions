from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        x1=head
        x2=head
        ans=0
        while x2 and x2.next:
            x1=x1.next
            x2=x2.next.next
        pre=None
        curr=x1
        while(curr is not None):
            temp=curr.next
            curr.next=pre
            pre=curr
            curr=temp
        a1=head
        a2=pre
        ans=0
        while a2 is not None:
            if (a1.val+a2.val)>ans:
                ans=a1.val+a2.val
            a2=a2.next
            a1=a1.next
        return ans
        