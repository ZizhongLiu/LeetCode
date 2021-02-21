# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_recursive(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #print(self)
        res = []
        self.recursive_inorder (root, res)
        # print(res)
        return res
    def recursive_inorder(self, root, res):#递归中序遍历
        if root:
            self.recursive_inorder(root.left, res)
            res.append(root.val)
            self.recursive_inorder(root.right, res)
# https://blog.csdn.net/yangjingjing9/article/details/77054899        
        
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''迭代解法需要用到栈。我们先把节点所有的左节点放入栈中，
        然后开始出栈，每次出栈都把栈中的元素放入到结果中，并且把这个结果的右孩子放入栈中。
        因此，这里的遍历顺序先沿着最左方向到达最左下角的孩子，
        然后每次弹出来一个节点，把该节点的值放入结果中，并开始处理该节点的右子树。'''
        # print(root)
        res = []
        self.iterative_inorder(root, res)
        #print(res)
        return res
    def iterative_inorder(self, root, res):#迭代中序遍历
        stack = [] #先建一个空栈
        while root or stack:
            if root: #如果根节点不为空
                stack.append(root) 
                root = root.left #自上而下的先把左侧所有节点放入栈中
            else: #整棵树到底了，然后开始看右侧开始出栈
                root = stack.pop()
                res.append(root.val)
                root = root.right #此时root的值返回到while那一行循环对右侧子树开始相同步骤的判断
        return res
# 这里面有三个数据结构很重要 res(最终的输出)，root（被遍历的树，会不断变化），stack（栈）
# https://blog.csdn.net/yangjingjing9/article/details/77054899        
# https://blog.csdn.net/fuxuemingzhu/article/details/79294461
