# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []
        sumArr = []

        while l1:
            arr1.insert(0, l1.val)
            l1 = l1.next

        while l2:
            arr2.insert(0, l2.val)
            l2 = l2.next

        number1 = 0
        number2 = 0

        for digit in arr1:
            number1 = number1 * 10 + digit

        for digit in arr2:
            number2 = number2 * 10 + digit

        total = number1 + number2

        if total == 0:
            sumArr.append(0)
        while total > 0:
            sumArr.append(total % 10)
            total = total // 10

        head = ListNode(sumArr[0])
        current = head
        for i in range(1, len(sumArr)):
            current.next = ListNode(sumArr[i])
            current = current.next

        return head
