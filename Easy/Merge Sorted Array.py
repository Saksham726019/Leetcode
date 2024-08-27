# Qno. 88 Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 and m > 0:
            return nums1
        elif m == 0 and n > 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]

        i = m - 1
        j = n - 1
        k = len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

