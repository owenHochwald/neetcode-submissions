# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        # the index positions are 1 indexed
        dummy = ListNode(-1, next=head)
        prev = dummy

        # bring the position to be just before that left start
        # reverse the nodes until we reach the end of the right
        # link up to the normal stuff
        # NOTE: important to keep track of node before the reversal starts
        # NOTE: important to keep track of the node right after the reversal ends

        # get to the position right before the reversal
        for _ in range(left - 1): # -1 because it is one indexed
            prev = prev.next


        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next 
            next_node.next = prev.next
            prev.next = next_node




        return dummy.next 