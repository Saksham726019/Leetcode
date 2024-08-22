# Qno. 66 Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits))) + 1

        result = list(map(int, str(number)))

        return result