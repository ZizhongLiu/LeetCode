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
        def left_traversal(root,stack):
            # print(root.val)
            if root == None:
                return []
            stack = [root]
            res = []
            while stack:
                root = stack.pop()
                if root is not None:
                    res.append(root.val)
                    if root.right is not None:
                        stack.append(root.right)
                    if root.left is not None:
                        stack.append(root.left)
            return res
        
        def right_traversal(root,stack):
            if root == None:
                return []
            stack = [root]
            res = []
            while stack:
                root = stack.pop()
                if root is not None:
                    res.append(root.val)
                    if root.left is not None:
                        stack.append(root.left)
                    if root.right is not None:
                        stack.append(root.right)
            return res        
        
        leftstack = []
        rightstack = []
        
        if root is None:
            return True
        
        left_res = left_traversal(root.left,leftstack)
        right_res = right_traversal(root.right,rightstack)
        
        if left_res == right_res:
            return True
        else:
            return False


        
