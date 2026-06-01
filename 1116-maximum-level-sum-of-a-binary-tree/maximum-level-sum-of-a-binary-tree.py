from  typing import Optional
from collections import deque
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue=deque([root])
        curr_level=0
        ans=1
        max_sum=-float('inf')
        while queue:
            curr_level+=1
            level_length=len(queue)
            temp=0
            for i in range(level_length):
                node=queue.popleft()
                temp+=node.val
                if i==level_length-1 and temp>max_sum:
                    max_sum=temp
                    ans=curr_level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans