class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(node ,max):
            if not node:
                return 0
            if node.val>=max:
                max=node.val
                good=1
            else:
                good=0
            left_good = DFS(node.left, max)
            right_good = DFS(node.right, max)
            return good+left_good+right_good
        return DFS(root,root.val) 
