# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        heightMap={}
        def dfs(node):
            nonlocal isBalanced
            if not node:
                return 0

            leftH = dfs(node.left)
            rightH = dfs(node.right)
            print("rigthtH",rightH,node.val)
            if abs(leftH-rightH) >1:
                isBalanced = False
            heightMap[node.val]= 1 + max(leftH,rightH)
            print(heightMap)
            return heightMap[node.val]
        dfs(root)
        return isBalanced


                

        