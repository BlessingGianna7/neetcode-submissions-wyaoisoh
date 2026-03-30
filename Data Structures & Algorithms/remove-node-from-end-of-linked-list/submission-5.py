class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        front = dummy 
        back = dummy   

        # move front n+1 steps ahead
        for i in range(n + 1):
            front = front.next

        # move both until front hits null
        while front is not None:
            front = front.next
            back = back.next

        # delete the target node
        back.next = back.next.next
        return dummy.next