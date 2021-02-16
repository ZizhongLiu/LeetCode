# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right # 这个class是用来定义树的概念
        
class Solution(object):
    def preorderTraversal(self, root): # self好像没有用到？
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #print(root)
        if root is None: # 如果节点(或者树)是空的 那就返回一个空值
            return []
        
        stack, output = [root ], [] #root刚进来的时候是完整的一棵树；把root赋给栈，把一个空集赋给output；答案中的[root, ]逗号可以不用
        # print("stack = {}".format(stack))

        while stack: # 或者 len(stack) > 0:       
            root = stack.pop() # stack 这个时候相当于一个含有原来完整的树的list，现在把这个树还给了root
            # print("root = {}".format(root))
            if root is not None:
                output.append(root.val) # 此时返回的是树最上层节点的值，并赋给output
                # print("output = {}".format(output))
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left) #栈先进后出，所以先进右子树节点，再进左子树节点，最后.pop()的时候，左边的节点才能先出
            # print("stack = {}".format(stack))
        
        return output
