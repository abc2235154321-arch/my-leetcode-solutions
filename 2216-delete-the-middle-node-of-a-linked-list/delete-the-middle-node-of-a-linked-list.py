from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        x1=head.next.next
        x2=head
        while(x1 and x1.next):
            x1=x1.next.next
            x2=x2.next
        x2.next=x2.next.next
        return head