# Qno. 94 Binary tree Inorder Traversal

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


"""Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nums = []
        stack = []
        go_right = False

        current = root

        while current or stack:
            if current.left and not go_right:
                stack.append(current)
                current = current.left
            else:
                nums.append(current.val)
                if current.right:
                    current = current.right
                    go_right = False
                else:
                    if stack:
                        current = stack.pop()
                        go_right = True
                    else:
                        current = None

        return nums
"""