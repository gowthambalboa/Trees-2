#tc : O(n)
#sc: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        
    def sumNumbers(self, root) -> int:
        def helper(root,currNum):
            #base
            if root is None: return
            if root.left is None and root.right is None: # leaf node
                currNum = currNum*10 + root.val
                self.result += currNum
            #logic
            helper(root.left,currNum*10+root.val)
            helper(root.right,currNum*10+root.val)
        
        currNum = 0
        
        helper(root,currNum)
        return self.result
        