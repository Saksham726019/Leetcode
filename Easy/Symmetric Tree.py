# Qno. 101 Symmetric Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # If the tree is empty, it is symmetric
        if not root:
            return True

        # If one subtree is None while the other is not, it is not symmetric
        if (root.left is None) != (root.right is None):
            return False

        left_node = root.left
        right_node = root.right

        left_stack = []  # This stack is responsible for the left half of the tree from the root.
        right_stack = []  # This stack is responsible for the right half of the tree from the root.

        # Traverse both subtrees in mirrored order
        while (left_node or left_stack) or (right_node or right_stack):
            # Traverse both left and right sides
            while left_node and right_node:
                if left_node.val != right_node.val:
                    return False

                left_stack.append(left_node)
                right_stack.append(right_node)

                left_node = left_node.left
                right_node = right_node.right

            # If one subtree has more nodes than the other, it's not symmetric
            if (left_node is None) != (right_node is None):
                return False

            # Process the right child of the left subtree and the left child of the right subtree
            left_node = left_stack.pop().right
            right_node = right_stack.pop().left

        return True

    """Another Approach using paired value in a stack

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # Stack to hold pairs of nodes to be compared
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            # If both nodes are None, continue
            if not left and not right:
                continue

            # If only one is None, or if values don't match, tree is not symmetric
            if not left or not right or left.val != right.val:
                return False

            # Add child pairs to the stack in the mirrored order
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True

        """
