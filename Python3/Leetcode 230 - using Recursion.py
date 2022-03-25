'''
LEETCODE 230 - Find Kth smallest element in a BST

With recursion
Time and Space complexity O(n)

Use an in-order traverse

Issue with the code is that we are using non-local variables.
Also, no easy way to break out off the stack when you find a value (because we are using recursion)

Alternative is to use a Iterative Solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0
        currCount = 0
        if root == None:
            return 0
        def dfs(currNode):
            nonlocal result
            nonlocal currCount
            if currNode.left:
                dfs(currNode.left)
            currCount += 1
            if (currCount == k):
                result = currNode.val
            if currNode.right:
                dfs(currNode.right)
        
        dfs(root)
        return result