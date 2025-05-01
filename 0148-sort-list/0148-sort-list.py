class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        
        sortedLeft = self.sortList(left)
        sortedRight = self.sortList(right)
        return self.merge(sortedLeft, sortedRight)
    
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        else:
            tail.next = l2
            
        return dummy.next        