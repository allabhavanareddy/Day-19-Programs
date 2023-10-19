111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.
Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
             return 0
        if root.right==None:
             return self.minDepth(root.left)+1  
        if root.left==None:
             return self.minDepth(root.right)+1
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        return min(left,right)+1

 