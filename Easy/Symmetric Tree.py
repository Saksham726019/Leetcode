# Qno. 101 Symmetric tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False

        curr_left = root.left
        curr_right = root.right

        stack_left = []
        stack_right = []

        while (curr_left is not None or stack_left) or (curr_right is not None or stack_right):
            while curr_left and curr_right:
                if curr_left.val != curr_right.val:
                    return False

                stack_left.append(curr_left)
                stack_right.append(curr_right)

                curr_left = curr_left.left
                curr_right = curr_right.right

            if (curr_left is None and curr_right is not None) or (curr_left is not None and curr_right is None):
                return False

            curr_left = stack_left.pop()
            curr_left = curr_left.right

            curr_right = stack_right.pop()
            curr_right = curr_right.left

        return True
