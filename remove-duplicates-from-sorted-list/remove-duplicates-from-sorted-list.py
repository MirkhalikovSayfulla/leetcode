# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head 
        head_n = head
        
        while head:                 
            if head.next and head.val == head.next.val:
                head.next = head.next.next
                continue    
            head = head.next
            
        return head_n