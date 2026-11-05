# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        newset= set()
        def dfs(node):

            if not node:
                return 
            
            if node.left:
                left = dfs(node.left)

                newset.add(node.left.val)

            newset.add(node.val)
            if node.right:
                right = dfs(node.right)

                newset.add(node.right.val)

        dfs(root)
        return list(newset)[k-1]



            


        