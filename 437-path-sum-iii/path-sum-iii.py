from  typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre=defaultdict(int)
        pre[0]=1
        def dfs(node,current):
            if not node:
                return 0
            current+=node.val
            path_found=pre[current-targetSum]
            pre[current]+=1
            ans=path_found+dfs(node.left,current)+dfs(node.right,current)
            pre[current]-=1
            return ans
        return dfs(root,0)