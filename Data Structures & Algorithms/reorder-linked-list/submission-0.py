# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # obtain second half of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half of list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # connect first and second half
        curr_1 = head
        curr_2 = prev
        turn = True
        while curr_1 and curr_2:
            if turn:
                tmp = curr_1.next
                curr_1.next = curr_2
                curr_1 = tmp
                turn = False
            else:
                tmp = curr_2.next
                curr_2.next = curr_1
                curr_2 = tmp
                turn = True
        return
            


