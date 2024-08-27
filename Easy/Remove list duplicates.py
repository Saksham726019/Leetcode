# Qno. 83 Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        i = head
        j = head.next

        while j:
            if i.val == j.val:
                j = j.next
            else:
                i.next = j
                i = i.next

        i.next = None

        return head
