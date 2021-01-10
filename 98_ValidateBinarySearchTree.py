"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
                            5
                        4       6
                            3       7
        :type root: TreeNode
        :rtype: bool
        """

        return self.isValid(root)


    def isValid(self,root, min=-10e9, max=10e9):
        if not root:
            return True

        if root.val <= min or root.val >= max:
            return False

        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)