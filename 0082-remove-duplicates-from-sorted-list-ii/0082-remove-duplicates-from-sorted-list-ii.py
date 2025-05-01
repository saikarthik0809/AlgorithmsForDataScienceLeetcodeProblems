# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head
        values = []

        # Traverse the list and collect values
        while current:
            values.append(current.val)
            current = current.next

        # Keep only values that appear once
        unique_values = [val for val in values if values.count(val) == 1]

        # If no unique values, return None
        if not unique_values:
            return None

        # Build the new linked list
        new_head = ListNode(unique_values[0])
        current = new_head
        for val in unique_values[1:]:
            current.next = ListNode(val)
            current = current.next

        return new_head