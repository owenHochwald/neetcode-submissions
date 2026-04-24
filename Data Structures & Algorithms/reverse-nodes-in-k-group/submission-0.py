# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = head
        prev = None
        curr = head
        m = 0
        group_prev = None

        while curr:
            print(curr.val)
            # reverse for each k group
            m += 1
            right = curr
            temp = curr
            for _ in range(k):
                if temp:
                    temp = temp.next
                else:
                    return head

            
            for _ in range(k):
                if not curr:
                    return head
                print(curr.val)
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            if m == 1:
                head = prev
            if group_prev:
                group_prev.next = prev
            group_prev = right
            prev = right
            prev.next = curr
        return head
                