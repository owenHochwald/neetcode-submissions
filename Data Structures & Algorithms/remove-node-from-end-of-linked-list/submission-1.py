# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        length = 0

        while fast:
            length += 1
            fast = fast.next

        target = length - n

        if target == 0:
            return head.next

        curr = head

        for i in range(length - 1):
            if (i+1) == target:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head








        