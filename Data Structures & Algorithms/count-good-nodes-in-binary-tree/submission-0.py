# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result=0
        def dfs(node,currMax):
            nonlocal result
            print(currMax)
            if node.val >= currMax:
                currMax = node.val
                result+=1
            if node.left:
                dfs(node.left,currMax)
            if node.right:
                dfs(node.right,currMax)
            
        dfs(root,root.val)
        return result

        