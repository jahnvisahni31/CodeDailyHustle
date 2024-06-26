# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        s = inorder(root)
        def build(values):
            if not values:
                return None
            m = len(values) // 2
            root = TreeNode(values[m])
            root.left = build(values[:m])
            root.right = build(values[m+1:])
            return root
        return build(s)