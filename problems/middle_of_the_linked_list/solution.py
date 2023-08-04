
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head