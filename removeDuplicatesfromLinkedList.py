# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp = head.val
        previousNode = head
        currentNode = head.next
        while currentNode:
            if temp==currentNode.val:
                if currentNode.next:
                    previousNode.next = currentNode.next
                    currentNode = currentNode.next
                else:
                    previousNode.next = None
                    currentNode=None
            else:
                temp = currentNode.val
                previousNode = currentNode
                if currentNode.next:
                    currentNode = currentNode.next
                else:
                    currentNode = None
                
        return head

# other methods 
#recursive
def deleteDuplicates(self, head):
        if head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head.next = self.deleteDuplicates(head.next)
        return head
# iterative
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy
        