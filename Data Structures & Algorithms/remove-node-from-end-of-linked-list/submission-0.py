# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass; get length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # second pass; navigate to n-th node from end
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while length > n:
            tmp = curr
            curr = curr.next
            prev = tmp
            length -= 1
        # remove node from list
        prev.next = curr.next
        return dummy.next
        