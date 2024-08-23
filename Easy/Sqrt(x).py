# Qno. 69 Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        left = 0
        right = x
        precision = 0.000001

        while right - left > precision:
            mid = (right + left) / 2
            if mid*mid > x:
                right = mid
            else:
                left = mid

        return int(right)