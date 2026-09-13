# Definition for singly-linked list.
#class ListNode:
#def __init__(self, val=0, next=None):
#self.val = val
#self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0 :
            total = carry
            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
        return dummy.next