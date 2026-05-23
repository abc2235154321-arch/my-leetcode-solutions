from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        if not head.next:
            return head
        x1=head
        x2=head.next
        x2_head=x2
        while x2 and x2.next:
            temp=x1.next.next
            x1.next=temp
            x2.next=temp.next
            x1=x1.next
            x2=x2.next
        x1.next=x2_head
        return head
