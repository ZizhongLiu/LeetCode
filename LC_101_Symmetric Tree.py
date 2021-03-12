# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Recursive_Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        if root is None:
            return True
        return isMirror(root.left,root.right)
    
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: 
            return True
        
        left_stack = [root.left]
        right_stack = [root.right]
        res = True
        
        while left_stack and right_stack:
            leftnode = left_stack.pop()
            rightnode = right_stack.pop()
            
            if not leftnode and not rightnode:
                res = True
                continue
            if not leftnode or not rightnode:
                res = False
                break
            if leftnode.val != rightnode.val:
                res = False
                break
            else:
                res = True
                left_stack += [leftnode.right,leftnode.left]
                right_stack += [rightnode.left,rightnode.right]
        return res


        
