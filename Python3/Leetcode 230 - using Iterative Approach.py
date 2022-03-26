# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Kth smallest element
In-Order traversal  using Iterative approach.
O(n) - Time and space complexity
like this better than recursive approach since we don't need to mess with global variables and can break out off the stack when we find the value

'''

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        currNode = root
        stack = []
        currCount = 0

        #while (currCount < k):  #this works too
        while (currNode or stack):
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            
            currNode = stack.pop() # no more left nodes so pop the last node
            #print (currNode.val)
            currCount += 1
            if currCount == k:
                return currNode.val
            
            currNode = currNode.right
            
        return 0 #found nothing