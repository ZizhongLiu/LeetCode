# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://blog.csdn.net/fuxuemingzhu/article/details/101079767
# https://www.cnblogs.com/chruny/p/5477575.html

class SolutionRescursive(object): #递归后序遍历
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

class Solution(object): #迭代后序遍历
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """由于后序遍历把根节点放到了最后，而我们在遍历的过程中，一定先获得到根节点，那么我们可以先倒序，然后再反转。
        后序遍历：左->右->根。我们的做法：根->右->左，然后再反转。
        先把根节点放入栈中，然后把它左孩子、右孩子依次放入，这样我们下次对栈内的元素遍历得到的顺序就是从右向左的，对于栈中弹出的每个节点都是如此。
        得到的顺序是根->右子树(节点全部入栈)->左子树的遍历方式，最后需要加一个翻转即可得到想要的后序遍历。。""" 
        res = []
        if root == None:
            return res
        self.iterative_inorder(root, res)
        res.reverse()
        return res
    def iterative_inorder(self, root, res): 
        stack = [root] #stack是个list
        while stack:
            root = stack.pop() #stack 这个时候相当于一个含有原来完整的树的list，现在把这个树还给了root
            if root:
                res.append(root.val) #此时返回的是树最上层节点的值，并赋给res
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right) #栈先进后出，所以先进左子树节点，再进右子树节点，最后一层一层判断，.pop()的时候，右边的节点才能先出
        return res
