# Qno. 108 Convert array to height balanced binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        root = TreeNode(nums[mid])

        stack = [(root, start, end)]

        while stack:
            node, start, end = stack.pop()
            mid = (start + end) // 2

            if start <= mid-1:
                left_mid = (start + (mid - 1)) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, start, mid-1))

            if mid + 1 <= end:
                right_mid = ((mid + 1) + end) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid+1, end))

        return root
