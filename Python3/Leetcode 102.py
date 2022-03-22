'''
Leetcode 102 - Level Order Traversal. Uses BFS to traverse a tree

Time Complexity: O(n*log(n))
Number of rows is height of tree = log(n)
each row, you count nodes = max (n+1)/2


Space Complexity: O(n)
Aux Space: Number of Rows = height of tree (log(n) for a balanced tree)
	per row you need to store Nodes + value. Last row has (n+1)/2
	hence: O(n)
Output Space: O(n)


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:   #edge case. NOTE: DO NOT USE root.val
            return[]
        q = []
        q.append(root)
        result = []
        
        while (len(q) > 0):
            temp_q = []
            temp_out = []
            for i in q:
                temp_out.append(i.val)
                if (i.left is not None):
                    temp_q.append(i.left)
                if (i.right is not None):
                    temp_q.append(i.right)
            q = temp_q
            result.append(temp_out)
        
        return(result)
            