# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lc = root
        while root:
            if root.val == p :
                lc = root
            if root.val == q:
                lc = root.val
            if p.val > root.val and q.val > root.val:
                root = root.right
                lc = root

            elif p.val < root.val and q.val < root.val:
                root = root.left
                lc = root
            else:
                break

        return lc   


            