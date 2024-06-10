# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        n = TreeNode(preorder[0])
        n.left = self.bstFromPreorder([x for x in preorder if x < preorder[0]])
        n.right = self.bstFromPreorder([x for x in preorder if x > preorder[0]])
        return n