# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentIndex = 0
        # count the nodes
        length=0
        temp=head
        
        while temp!= None:
            length+=1
            temp=temp.next
        
        nodeToRemove = length-n

        if nodeToRemove==0:
            return head.next

        temp=head

        for i in range(nodeToRemove-1):
            temp = temp.next
        
        nextNode = temp.next
        if nextNode and nextNode.next:
            temp.next = nextNode.next
        else:
            temp.next = None

        return head


            
        
        