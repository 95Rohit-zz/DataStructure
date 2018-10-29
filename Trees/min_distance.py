# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# Example :

# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.

# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

#           4
#         /   \
#       2      6
#      / \    
#     1   3  

# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:

# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def new(self,root):
        global li
        if root == None:
            return
        else:
            li.append(root.val)
            
        self.new(root.left)
        self.new(root.right)
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global li
        li = []
        self.new(root)
        li = sorted(li)
        mi = li[len(li)-1]
        for i in range(len(li)-1,0,-1):
            mi = min(li[i]-li[i-1],mi)
            
        return mi