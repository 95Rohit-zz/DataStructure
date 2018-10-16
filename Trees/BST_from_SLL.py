# Balanced Binary Search Tree from Sorted Linked List

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        li = []
        while head != None:
            li.append(head.val)
            head = head.next
        return convertBST(li)

def convertBST(li):
    if len(li) == 1:
        return TreeNode(li[0])
    elif len(li) == 0:
        return None
    else:
        midIndex = int((len(li)-1)/2)
        mid = li[midIndex]
    T = TreeNode(mid)
    T.left = convertBST(li[:midIndex])
    T.right = convertBST(li[midIndex+1:])
    return T