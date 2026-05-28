from  typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max=0
        def dfs(node,GOleft,length):
            if not node:
                return 
            self.max=max(self.max,length)
            if GOleft:
                dfs(node.left,False,length+1)
                dfs(node.right,True,1)
            else:
                dfs(node.right,True,length+1)
                dfs(node.left,False,1)
        dfs(root.left,False,1)
        dfs(root.right,True,1)  
        return self.max  