# Qno. 27 Remove element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[j] == val and nums[i]!=val:
                nums[j] = nums[i]
                j += 1

        return j
