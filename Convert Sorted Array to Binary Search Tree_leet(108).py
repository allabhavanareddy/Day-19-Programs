108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(si,li):
            if si<=li:
                mid=(si+li)//2
                root=TreeNode(nums[mid])
                root.left=fun(si,mid-1)
                root.right=fun(mid+1,li)
                return root
        return fun(0,len(nums)-1)


 
