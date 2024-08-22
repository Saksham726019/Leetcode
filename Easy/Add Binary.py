# Qno. 67 Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        carry = 0

        for i in range(max_len - 1, -1, -1):
            total = (int(a[i]) + int(b[i]) + carry)

            if total == 0:
                result = "0" + result
                carry = 0
            elif total == 1:
                result = "1" + result
                carry = 0
            elif total == 2:
                result = "0" + result
                carry = 1
            elif total == 3:
                result = "1" + result
                carry = 1

        if carry:
            result = "1" + result

        return result