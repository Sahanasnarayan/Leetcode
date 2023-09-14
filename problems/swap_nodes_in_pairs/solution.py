# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, no swapping needed.
        if not head or not head.next:
            return head

        # Swap the current pair of nodes
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        # Return the new head of the swapped pair
        return new_head